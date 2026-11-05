
class contactustab:

    def __init__(self, page):
        self.page = page

        # Contact Us main menu
        self.contactus_menu = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]'
        )

        # Contact Us form
        self.name = page.locator('(//input[@placeholder="Your Name"])[2]')
        self.email = page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.send_otp = page.locator('//button[@class="send-otp-btn"]')
        self.otp = page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.company = page.locator('(//input[@placeholder="Your Company"])[2]')
        self.service = page.locator('(//select[@name="service"])[2]')
        self.phone = page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.message = page.locator('(//textarea[@placeholder="Message"])[2]')
        self.submit = page.locator('(//input[@type="submit"])[2]')

        # Web Development links
        self.webdevelopment = page.locator(
            '//a[@href="https://www.tranktechnologies.com/web-development-company"]'
        )

        self.cmswebsitedevelopment = page.locator(
            '//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]'
        )

        self.ecommerecedevelopment = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]'
        )

        self.customwebportaldevelopment = page.locator(
            '//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]'
        )

        self.ui_uxdesign = page.locator(
            '//a[@href="https://www.tranktechnologies.com/ui-ux-design-company"]'
        )

        self.mobileapp = page.locator(
            '//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]'
        )

        self.responsiveweb = page.locator(
            '//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]'
        )

        self.brandidentity = page.locator(
            '//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]'
        )

        # App Development links
        self.appdevelopment = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/app-development-company"])[1]'
        )

        self.iosapp = page.locator(
            '//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]'
        )

        self.androidapp = page.locator(
            '//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]'
        )

        self.hybrid = page.locator(
            '//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]'
        )

        self.crossplatform = page.locator(
            '//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]'
        )

        self.progressive = page.locator(
            '//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]'
        )

        # Graphic Design links
        self.graphicdesign = page.locator(
            '//a[@href="https://www.tranktechnologies.com/graphic-design-company"]'
        )

        self.logodesign = page.locator(
            '//a[@href="https://www.tranktechnologies.com/logo-design-company"]'
        )

        self.bannerdesign = page.locator(
            '//a[@href="https://www.tranktechnologies.com/banner-design-company"]'
        )

        self.packagdesign = page.locator(
            '//a[@href="https://www.tranktechnologies.com/packaging-design-company"]'
        )

        self.businesscarddesign = page.locator(
            '//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]'
        )

        # List of all Contact Us service links
        self.contacts_list = [
            self.webdevelopment,
            self.cmswebsitedevelopment,
            self.ecommerecedevelopment,
            self.customwebportaldevelopment,
            self.ui_uxdesign,
            self.mobileapp,
            self.responsiveweb,
            self.brandidentity,
            self.appdevelopment,
            self.iosapp,
            self.androidapp,
            self.hybrid,
            self.crossplatform,
            self.progressive,
            self.graphicdesign,
            self.logodesign,
            self.bannerdesign,
            self.packagdesign,
            self.businesscarddesign
        ]

        # Follow Us social media
        self.facebook = page.locator('//img[@alt="Facebook"]')
        self.linkedin = page.locator('//img[@alt="LinkedIn"]')
        self.insta = page.locator('(//img[@alt="Instagram"])[1]')
        self.printerest = page.locator('(//img[@alt="Pinterest"])[1]')
        self.twitter = page.locator('(//img[@alt="Twitter"])[1]')
        self.youtube = page.locator('(//img[@alt="Youtube"])[1]')
        self.quaro = page.locator('(//img[@alt="Quaro"])[1]')

        self.follow_us = [
            self.facebook,
            self.linkedin,
            self.insta,
            self.printerest,
            self.twitter,
            self.youtube,
            self.quaro
        ]

    # Contact Us form
    def contactus_form_options(self):
        self.contactus_menu.click()

        self.name.fill("Divya")
        self.email.fill("divyashree.kr96@gmail.com")
        self.send_otp.click()

        # OTP must be obtained from the actual verification flow.
        # Do not use a fixed dummy OTP.
        # Complete OTP verification before submitting the form.

    # Contact Us service links
    def contactus_menu_options(self):
        self.contactus_menu.click()
        self.page.wait_for_load_state("load")

        for i in self.contacts_list:
            i.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
            self.page.wait_for_load_state("load")

    # Follow Us links: check presence
    
    def follow_us_options(self):
        self.contactus_menu.click()
        self.page.wait_for_load_state("load")

        for i in self.follow_us:
            print("Checking locator:", i)

            if i.count() > 0:
             print("Icon found:", i)
            else:
             print("Icon not found:", i)

