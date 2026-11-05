
from config import BASE_URL


class vertical:

    def __init__(self, page):
        self.page = page

        # Main menu locators
        self.verticals = page.locator('(//li[@class="drop_down"])[1]')

        self.trading = page.locator('//li[@data-id="trading"]')
        self.Retail_Ecommerce = page.locator('//li[@data-id="retailEcommerce"]')
        self.Healthcare = page.locator('//li[@data-id="healthcare"]')
        self.Fintech = page.locator('//li[@data-id="fintech"]')
        self.customApp = page.locator('//li[@data-id="customApp"]')

        # Trading submenu locators
        self.p0 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.p1 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.p2 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.p3 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.p4 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.p5 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.p6 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')

        self.trading_option_list = [
            self.p0, self.p1, self.p2, self.p3,
            self.p4, self.p5, self.p6
        ]

        # Healthcare submenu locators
        self.p7 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.p8 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        self.healthcare_option_list = [
            self.p7, self.p8
        ]

        # Fintech submenu locators
        self.p9 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.p09 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        self.Fintech_option_list = [
            self.p9, self.p09
        ]

        # Custom App submenu locators
        self.p10 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.p11 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.p12 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.p13 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.p14 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.p15 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.p16 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.p17 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.p18 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')

        self.customer_option_list = [
            self.p10, self.p11, self.p12, self.p13,
            self.p14, self.p15, self.p16, self.p17, self.p18
        ]

        # Retail and Ecommerce submenu locators
        self.p19 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.p20 = page.locator('(//li/a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

        self.Retail_Ecommerce_option_list = [
            self.p19, self.p20
        ]

    def _click_visible_option(self, option):
        href = option.get_attribute("href")
        visible_option = self.page.locator(f'li a[href="{href}"]:visible').first
        visible_option.wait_for(state="visible", timeout=10000)
        visible_option.scroll_into_view_if_needed()
        visible_option.click(timeout=15000, force=True)

    # Trading menu
    def trading_options_clicking(self):
        for i in self.trading_option_list:
            self.verticals.hover(force=True)
            self.trading.wait_for(state="visible", timeout=10000)
            self.trading.hover(force=True)

            self._click_visible_option(i)

            self.page.wait_for_load_state("load")
            self.page.goto(BASE_URL, wait_until="load")

    # Healthcare menu
    def Healthcare_options_clicking(self):
        for i in self.healthcare_option_list:
            self.verticals.hover()
            self.Healthcare.hover()
            self.page.wait_for_timeout(3000)

            i.scroll_into_view_if_needed()
            i.click(timeout=15000)

            self.page.wait_for_load_state("domcontentloaded")
            self.page.go_back()
            self.page.wait_for_load_state("domcontentloaded")
            self.page.wait_for_timeout(1000)

    # Fintech menu
    def Fintech_options_clicking(self):
        for option in self.Fintech_option_list:
         self.verticals.hover(force=True)

         self.Fintech.wait_for(state="visible", timeout=15000)
         self.Fintech.hover()

         self._click_visible_option(option)
         self.page.wait_for_load_state("load")
         self.page.goto("https://www.tranktechnologies.com/", wait_until="load")


    # Custom App menu
    def customApp_options_clicking(self):
        for i in self.customer_option_list:
            self.verticals.hover(force=True)
            self.customApp.wait_for(state="visible", timeout=10000)
            self.customApp.hover(force=True)

            self._click_visible_option(i)

            self.page.wait_for_load_state("load")
            self.page.goto(BASE_URL, wait_until="load")

    # Retail and Ecommerce menu
    def Retail_Ecommerce_options_clicking(self):
        for i in self.Retail_Ecommerce_option_list:
            self.verticals.hover()
            self.Retail_Ecommerce.hover()
            self.page.wait_for_timeout(3000)

            i.scroll_into_view_if_needed()
            i.click(timeout=15000)

            self.page.wait_for_load_state("domcontentloaded")
            self.page.go_back()
            self.page.wait_for_load_state("domcontentloaded")
            self.page.wait_for_timeout(1000)
