from playwright.sync_api import Locator, Page

# TODO
# - Add support for sub-menu items
# - Add support for mobile menu (hamburger menu)

class Menu:
    def __init__(self, page: Page):
        self.page = page

# -- Selectors 
    def _top_level_menu_items_selector(self, text: str) -> Locator:
        return self.page.locator(".site-header-below-section-center").locator(".menu-item").filter(has_text=text)

# -- Methods
    def has_top_level_item(self, text: str) -> bool:
        return self._top_level_menu_items_selector(text).is_visible()
    
    def click_top_level_item(self, text: str) -> None:
        self._top_level_menu_items_selector(text).click()

    def hover_top_level_item(self, text: str) -> None:
        self._top_level_menu_items_selector(text).hover()

