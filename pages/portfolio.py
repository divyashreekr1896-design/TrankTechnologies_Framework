
class portfolioclass:

    def __init__(self, page):
        self.page = page

        # Portfolio menu
        self.portfolio = page.locator(
            '//a[@href="https://www.tranktechnologies.com/portfolio"]'
        )

        # Portfolio sub links
        self.ics_hw = page.locator(
            '//a[@href="https://www.icshomework.in/"]'
        )

        self.wing_pharma = page.locator(
            '//a[@href="https://www.wingspharma.com/"]'
        )

        self.arena_animation = page.locator(
            '//a[@href="https://www.arenaanimation.com/"]'
        )

        self.home360 = page.locator(
            '//a[@href="https://home360stores.com/"]'
        )

        self.club_meetings = page.locator(
            '//div[@class="cm-content"][5]/a[text()="View More"]'
        )

        self.cords_cables = page.locator(
            '//a[@href="https://cordscable.tranktechnologies.com/"]'
        )

        # List of all portfolio options
        self.portfolio_tabs_list = [
            self.ics_hw,
            self.wing_pharma,
            self.arena_animation,
            self.home360,
            self.club_meetings,
            self.cords_cables
        ]

    # Portfolio tab options
    def portfolio_tabs(self):
        self.portfolio.click()
        self.page.wait_for_load_state("load")

        for i in self.portfolio_tabs_list:
         print("Current page:", self.page.url)
         print("Locator:", i)
         print("Matching elements:", i.count())

        if i.count() > 0:
           print("Visible:", i.first.is_visible())
        else:
            print("Locator not found on the page")


