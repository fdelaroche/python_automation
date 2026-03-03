
from playwright.sync_api import Page
from support.common.menu import Menu

def test_redirect_to_wordpress(page: Page):
    page.goto("https://ufecanada.org/")
    assert page.url == "https://ufecanada.org/wp/"

def test_menu_items(wp_ufe_main_page: Page):
    page = wp_ufe_main_page

    menu = Menu(page)
    menu_items = ["Accueil", "Blog", "Adhésions", "Lettres d’informations", "Postes Utiles", "Livre d’or"]
    
    for item in menu_items:
        assert menu.has_top_level_item(item)
