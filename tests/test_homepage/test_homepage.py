
from playwright.sync_api import Page
from support.common.menu import Menu

def test_redirect_to_wordpress(page: Page):
    page.goto("https://ufecanada.org/")
    assert page.url == "https://ufecanada.org/wp/"

def test_menu_items(wp_ufe_main_page: Page):
    page = wp_ufe_main_page

    menu = Menu(page)
    assert(menu.menu_items() == ["Accueil", "Blog", "Adhésions", "À propos", "Lettres d’informations", "Postes Utiles", "Livre d’or"])

def test_a_propos_sub_menu_items(wp_ufe_main_page: Page):
    page = wp_ufe_main_page

    menu = Menu(page)
    print(f"menu items are {menu.menu_items()}")

    menu.hover_menu_item("À propos")
    sub_menu_items =  [ "Conseil d’administration", "Partenaires", "Page Youtube", "Nous contacter par e-mail", "Ancien site web (archivé)" ]

    assert(menu.sub_menu_items("À propos") == sub_menu_items)
        
def test_lettres_d_information_sub_menu_items(wp_ufe_main_page: Page):
    page = wp_ufe_main_page
    menu = Menu(page)

    menu.hover_menu_item("Lettres d’informations")
    sub_menu_items =  [ "Dernières lettres", "S’inscrire" ]

    assert (menu.sub_menu_items("Lettres d’informations") == sub_menu_items)

def test_postes_utiles_sub_menu_items(wp_ufe_main_page: Page):
    page = wp_ufe_main_page

    menu = Menu(page)
    menu.hover_menu_item("Postes Utiles")
    sub_menu_items =  [ "Liens utiles", "Certificats de vie", "Index des recettes", "Quelques bonnes adresses de nos membres" ]

    assert(menu.sub_menu_items("Postes Utiles") == sub_menu_items) 
