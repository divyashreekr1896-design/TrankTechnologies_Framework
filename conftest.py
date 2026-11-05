from pathlib import Path
import hashlib
import os
import re
import uuid

import pytest
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright
import pytest_html

from config import BASE_URL


@pytest.fixture(scope="function")
def page(request, recordings_dir):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        test_id = hashlib.sha1(request.node.nodeid.encode("utf-8")).hexdigest()[:10]
        test_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", request.node.name)
        video_dir = recordings_dir / f"{test_name}-{test_id}"
        video_dir.mkdir(parents=True, exist_ok=True)
        context = browser.new_context(record_video_dir=str(video_dir))

        page = context.new_page()

        try:
            for attempt in range(2):
                page.goto(BASE_URL, wait_until="load")
                try:
                    page.locator("li.drop_down").first.wait_for(
                        state="visible", timeout=15000
                    )
                    break
                except PlaywrightTimeoutError:
                    if attempt == 1:
                        raise

            yield page
        finally:
            video = page.video
            context.close()
            browser.close()
            if video:
                request.node._execution_video = Path(video.path()).resolve()


@pytest.fixture(scope="session")
def recordings_dir():
    directory = Path("videos") / f"run-{uuid.uuid4().hex}"
    directory.mkdir(parents=True, exist_ok=True)
    return directory.resolve()

@pytest.hookimpl(hookwrapper=True)    #helps to create or attach the hook
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extras", [])

    if report.when == "teardown":
        video_path = getattr(item, "_execution_video", None)
        if video_path and video_path.exists():
            html_path = item.config.getoption("htmlpath", default=None)
            report_dir = Path(html_path).resolve().parent if html_path else Path.cwd()
            relative_path = Path(os.path.relpath(video_path, report_dir)).as_posix()
            extra.append(pytest_html.extras.url(relative_path, name="Execution recording"))
            report.extras = extra

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")    #it call only anything is failed
            screenshots_dir.mkdir(exist_ok=True)

            file_name = screenshots_dir / f"{item.name}.png"

            page.screenshot(path=str(file_name))

            extra.append(pytest_html.extras.image(str(file_name)))

        report.extras = extra