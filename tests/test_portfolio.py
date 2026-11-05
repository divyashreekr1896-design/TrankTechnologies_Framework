import pytest
from pages.portfolio import portfolioclass


@pytest.mark.smoke
def test_portfolio_tabs(page):
    portfolio_obj = portfolioclass(page)
    portfolio_obj.portfolio_tabs()
