import pytest
from pages.blog import blogtab


@pytest.mark.smoke
def test_blog_tab_options(page):
    blog_obj = blogtab(page)
    blog_obj.blog_tab_options()