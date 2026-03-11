from playwright.sync_api import Locator, Page

# TODO
# - Add support for mobile menu (hamburger menu)

class Menu:
    def __init__(self, page: Page):
        self.page = page

# -- Selectors 
    def _menu_item_selector(self) -> Locator:
        return self.page.locator(".main-header-menu > [id^='menu-item']")
    
    def _sub_menu_item_selector(self, parent_text: str) -> Locator:
        parent_locator = self._menu_item_selector().filter(has=self.page.get_by_role("button", name=parent_text))
        return parent_locator.locator("ul li")

# -- Methods
    def has_item(self, text: str) -> bool:
        return self._menu_item_selector().get_by_text(text, exact=True).is_visible()
    
    def menu_items(self) -> list[str]:
        return self._menu_item_selector().all_inner_texts()

    def click_menu_item(self, text: str) -> None:
        self._menu_item_selector().get_by_text(text, exact=True).click()

    def hover_menu_item(self, text: str) -> None:
        menu_item_locator = self._menu_item_selector().get_by_text(text, exact=True)
        menu_item_locator.hover()
        # Wait for the sub-menu to appear after hovering.
        self._sub_menu_item_selector(text).first.wait_for(state='visible')

    def sub_menu_items(self, parent_text: str) -> list[str]:
        return self._sub_menu_item_selector(parent_text).all_inner_texts()
