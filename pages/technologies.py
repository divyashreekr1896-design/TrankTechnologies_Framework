
from config import BASE_URL


class technologiestab:

    def __init__(self, page):
        self.page = page

        # Header: Technologies menu
        self.technologies_menu_tab = page.locator("li.drop_down").nth(1)

        # eCommerce Development submenu
        self.ecommerce_technologies_menu = page.locator(
            '//li[@data-id="ecomm"]'
        )

        # eCommerce Development links
        self.magento_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]'
        )

        self.opencart_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]'
        )

        self.codeigniter_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]'
        )

        self.wordpress_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]'
        )

        self.bigcommerce_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]'
        )

        self.shopify_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]'
        )

        self.cs_cart_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]'
        )

        self.node_js_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]'
        )

        self.nopcommerce_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]'
        )

        self.woocommerce_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]'
        )

        self.laravel_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]'
        )

        self.prestashop_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]'
        )

        self.drupal_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]'
        )

        self.wix_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]'
        )

        self.joomla_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]'
        )

        self.react_js_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]'
        )

        self.express_js_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]'
        )

        # List of all eCommerce submenu options
        self.ecommerce_technology_option_list = [
            self.magento_development,
            self.opencart_development,
            self.codeigniter_development,
            self.wordpress_development,
            self.bigcommerce_development,
            self.shopify_development,
            self.cs_cart_development,
            self.node_js_development,
            self.nopcommerce_development,
            self.woocommerce_development,
            self.laravel_development,
            self.prestashop_development,
            self.drupal_development,
            self.wix_development,
            self.joomla_development,
            self.react_js_development,
            self.express_js_development
        ]

        # Mobile App Development submenu
        self.mobile_app_technologies_menu = page.locator(
            '//li[@data-id="mobileApp"]'
        )

        # Mobile App Development links
        self.react_native_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]'
        )

        self.enterprise_mobile_app_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]'
        )

        self.xamarin_mobile_app_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]'
        )

        self.kotlin_mobile_app_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]'
        )

        self.flutter_mobile_app_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]'
        )

        self.ionic_mobile_app_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]'
        )

        self.swift_mobile_app_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]'
        )

        self.appointment_booking_development = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]'
        )

        # List of all Mobile App submenu options
        self.mobile_app_development_option_list = [
            self.react_native_development,
            self.enterprise_mobile_app_development,
            self.xamarin_mobile_app_development,
            self.kotlin_mobile_app_development,
            self.flutter_mobile_app_development,
            self.ionic_mobile_app_development,
            self.swift_mobile_app_development,
            self.appointment_booking_development
        ]

        # Artificial Intelligence submenu
        self.artificial_intelligence_menu = page.locator(
            '//li[@data-id="aipage"]'
        )

        # Keep empty until the actual AI submenu links are identified
        self.ai_option_list = []

    # eCommerce Development menu options
    
    # eCommerce Development menu options
    def ecommerce_technologies_menu_options(self):
        for i in self.ecommerce_technology_option_list:
            self.technologies_menu_tab.wait_for(state="visible", timeout=15000)
            self.technologies_menu_tab.hover()
            self.ecommerce_technologies_menu.wait_for(state="visible", timeout=10000)
            self.ecommerce_technologies_menu.hover(force=True)

            href = i.get_attribute("href")
            visible_option = self.page.locator(f'a[href="{href}"]:visible').first
            visible_option.click(timeout=15000, force=True)
            self.page.wait_for_load_state("load")
            self.page.goto(BASE_URL, wait_until="load")


    # Mobile App Development menu options
    
    # Mobile App Development menu options
    
    # Mobile App Development menu options
    def mobile_app_menu_options(self):
        for i in self.mobile_app_development_option_list:
            self.technologies_menu_tab.wait_for(state="visible", timeout=15000)
            self.technologies_menu_tab.hover()
            self.mobile_app_technologies_menu.wait_for(state="visible", timeout=10000)
            self.mobile_app_technologies_menu.hover(force=True)

            href = i.get_attribute("href")
            visible_option = self.page.locator(f'a[href="{href}"]:visible').first
            visible_option.click(timeout=15000, force=True)
            self.page.wait_for_load_state("load")
            self.page.goto(BASE_URL, wait_until="load")



    # Artificial Intelligence menu options
    def ai_menu_options(self):
        for i in self.ai_option_list:
            self.technologies_menu_tab.hover()
            self.artificial_intelligence_menu.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

