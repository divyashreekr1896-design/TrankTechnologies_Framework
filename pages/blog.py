
class blogtab:

    def __init__(self, page):
        self.page = page

        # ================= Header: BLOGS menu =================

        self.blog_tab_option_menu = page.locator(
            '(//a[@href="https://www.tranktechnologies.com/blog/"])[1]'
        )

        # Sub links

        self.app_development = page.locator(
            '//a[@href="/blog/category/app-development/"]'
        )

        self.web_development = page.locator(
            '//a[@href="/blog/category/web-development/"]'
        )

        self.software_development = page.locator(
            '//a[@href="/blog/category/software-development/"]'
        )

        self.digital_marketing = page.locator(
            '//a[@href="/blog/category/digital-marketing/"]'
        )

        self.email_marketing = page.locator(
            '//a[@href="/blog/category/email-marketing/"]'
        )

        self.artificial_intelligence = page.locator(
            '//a[@href="/blog/category/artificial-intelligence/"]'
        )

        self.ui_ux_design = page.locator(
            '//a[@href="/blog/category/ui-ux-design/"]'
        )

        # List of all submenu options

        self.blogs_option_list = [
            self.app_development,
            self.web_development,
            self.software_development,
            self.digital_marketing,
            self.email_marketing,
            self.artificial_intelligence,
            self.ui_ux_design
        ]

    # Blog tab menu options

    def blog_tab_options(self):
        for i in self.blogs_option_list:
            self.blog_tab_option_menu.hover()
            self.blog_tab_option_menu.click()
            self.page.wait_for_timeout(3000)
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
