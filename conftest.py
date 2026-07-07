import pytest
from selenium import webdriver
from urls import BASE_URL
from data.test_data import ADDRESS_KHAMOVNICHESKY, ADDRESS_ZUBOVSKY
from data.test_data import ROUTE_TYPE_FAST
from pages.main_page import MainPage
from pages.route_page import RoutePage
from pages.taxi_order_page import TaxiOrderPage


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(0)  # явные ожидания реализованы в BasePage
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open(BASE_URL)
    return page


@pytest.fixture
def route_page_with_two_addresses(main_page):
    main_page.enter_address_from(ADDRESS_KHAMOVNICHESKY)
    main_page.enter_address_to(ADDRESS_ZUBOVSKY)
    return RoutePage(main_page.driver)


@pytest.fixture
def route_page_with_same_address(main_page):
    main_page.enter_address_from(ADDRESS_KHAMOVNICHESKY)
    main_page.enter_address_to(ADDRESS_KHAMOVNICHESKY)
    return RoutePage(main_page.driver)


@pytest.fixture
def taxi_order_page(route_page_with_two_addresses):
    route_page_with_two_addresses.select_route_tab(ROUTE_TYPE_FAST)
    route_page_with_two_addresses.click_call_taxi()
    return TaxiOrderPage(route_page_with_two_addresses.driver)
