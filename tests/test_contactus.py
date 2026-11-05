
import pytest
from pages.contactus import contactustab


@pytest.mark.smoke
def test_contactus_menu_options(page):
    contactus_obj = contactustab(page)
    contactus_obj.contactus_menu_options()


@pytest.mark.contactus
def test_follow_us_options(page):
    contactus_obj = contactustab(page)
    contactus_obj.follow_us_options()
