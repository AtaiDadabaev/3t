from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    # Search field
    search_field = (By.CSS_SELECTOR, "#search")

    # Product links
    macbook_link = (By.LINK_TEXT, "MacBook")
    iphone_link = (By.LINK_TEXT, "iPhone")
    samsung_galaxy_tab_link = (By.LINK_TEXT, "Samsung Galaxy Tab 10.1")

    # Dropdown categories
    tablets_dropdown = (By.LINK_TEXT, "Планшеты")
    phones_dropdown = (By.LINK_TEXT, "Телефоны")
