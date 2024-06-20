from conftest import *
from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage


def test_6(driver):
    MainPage(driver).click(MainPage.macbook_link)
    MainPage(driver).click(ProductPage.add_to_favorites_button)


def test_7(driver):
    MainPage(driver).click(MainPage.macbook_link)
    MainPage(driver).click(ProductPage.add_to_cart_button)


def test_8(driver):
    MainPage(driver).click(MainPage.tablets_dropdown)
    MainPage(driver).click(MainPage.samsung_galaxy_tab_link)
    MainPage(driver).click(ProductPage.add_to_cart_button)


def test_9(driver):
    MainPage(driver).click(MainPage.phones_dropdown)
    MainPage(driver).click(MainPage.iphone_link)
    MainPage(driver).click(ProductPage.add_to_cart_button)


def test_10(driver):
    MainPage(driver).click(MainPage.macbook_link)
    ProductPage(driver).click(ProductPage.review_tab)
    ProductPage(driver).input(ProductPage.review_name_input, "NAME")
    ProductPage(driver).input(ProductPage.review_text_input, "TESTTESTTESTTESTTESTTESTTESTTESTTESTTEST")
    ProductPage(driver).click(ProductPage.review_rating_input)
    ProductPage(driver).click(ProductPage.submit_review_button)

