from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    # Buttons
    main_images_product = (By.CSS_SELECTOR, 'a.thumbnail')
    add_to_cart_button = (By.CSS_SELECTOR, "#button-cart")
    add_to_favorites_button = (By.CSS_SELECTOR, "div.btn-group:nth-child(1) > button.btn.btn-default:nth-child(1)")

    # Review section
    review_tab = (By.PARTIAL_LINK_TEXT, "Отзывов (")
    review_name_input = (By.CSS_SELECTOR, "#input-name")
    review_text_input = (By.CSS_SELECTOR, "#input-review")
    review_rating_input = (By.CSS_SELECTOR, "input:nth-child(5)")
    submit_review_button = (By.CSS_SELECTOR, "#button-review")

