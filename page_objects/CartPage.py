from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    # Product actions
    update_button = (By.XPATH, "//tbody/tr[1]/td[4]/div[1]/span[1]/button[1]")
    delete_button = (By.XPATH, "//tbody/tr[1]/td[4]/div[1]/span[1]/button[2]")
    product_link = (By.LINK_TEXT, "MacBook")
    product_quantity_input = (By.XPATH, "//tbody/tr[1]/td[4]/div[1]/input[1]")

    # Navigation buttons
    continue_shopping_button = (By.LINK_TEXT, "Продолжить покупки")
    proceed_to_checkout_button = (By.LINK_TEXT, "Оформление заказа")

    # Coupon elements
    open_coupon_button = (By.PARTIAL_LINK_TEXT, "Использовать куп")
    confirm_coupon_button = (By.CSS_SELECTOR, "#button-coupon")
    coupon_input = (By.CSS_SELECTOR, "#input-coupon")

    # Voucher elements
    open_voucher_button = (By.PARTIAL_LINK_TEXT, "Использовать Подароч")
    confirm_voucher_button = (By.CSS_SELECTOR, "#button-voucher")
    voucher_input = (By.CSS_SELECTOR, "#input-voucher")
