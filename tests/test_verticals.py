import pytest
from pages.verticals import vertical

@pytest.mark.smoke
def test_trading(page):
    trading_obj=vertical(page)
    trading_obj.trading_options_clicking()


@pytest.mark.smoke
def test_Fintech(page):
    trading_obj=vertical(page)
    trading_obj.Fintech_options_clicking()


@pytest.mark.smoke
def test_Healthcare(page):
    trading_obj=vertical(page)
    trading_obj.Healthcare_options_clicking()

@pytest.mark.smoke
def test_customApp(page):
    trading_obj=vertical(page)
    trading_obj.customApp_options_clicking()


@pytest.mark.smoke
def test_Retail_Ecommerce(page):
    trading_obj=vertical(page)
    trading_obj.Retail_Ecommerce_options_clicking()