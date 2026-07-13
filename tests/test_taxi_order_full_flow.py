import allure

from data.test_data import ADDRESS_KHAMOVNICHESKY, ADDRESS_ZUBOVSKY, ROUTE_TYPE_FAST
from helpers.wait_utils import parse_price_from_text


@allure.feature("Заказ тарифа Такси")
@allure.story("Полный флоу заказа")
class TestTaxiOrderFullFlow:

    @allure.title("После отправки заказа появляется окно поиска машины")
    def test_submitting_order_shows_waiting_screen(self, main_page):
        main_page.enter_address_from(ADDRESS_KHAMOVNICHESKY)
        main_page.enter_address_to(ADDRESS_ZUBOVSKY)
        route_page = main_page.to_route_page()
        route_page.select_route_tab(ROUTE_TYPE_FAST)
        taxi_order_page = route_page.click_call_taxi()
        taxi_order_page.select_tariff("Рабочий")
        taxi_order_page.check_requirement("Столик для ноутбука")
        waiting_page = taxi_order_page.click_submit_order()

        assert waiting_page.get_title_text() == "Поиск машины"
        assert waiting_page.is_countdown_timer_visible()

    @allure.title("В окне совершённого заказа отображаются данные водителя")
    def test_completed_order_shows_driver_info(self, main_page):
        main_page.enter_address_from(ADDRESS_KHAMOVNICHESKY)
        main_page.enter_address_to(ADDRESS_ZUBOVSKY)
        route_page = main_page.to_route_page()
        route_page.select_route_tab(ROUTE_TYPE_FAST)
        taxi_order_page = route_page.click_call_taxi()
        taxi_order_page.select_tariff("Рабочий")
        taxi_order_page.check_requirement("Столик для ноутбука")
        waiting_page = taxi_order_page.click_submit_order()
        completed_page = waiting_page.wait_for_completed_order(timeout=60)

        assert completed_page.get_driver_name(timeout=60), "Имя водителя не найдено или пусто"
        assert completed_page.get_driver_photo_src(timeout=60), "У фото водителя пустой/отсутствующий src"
        assert completed_page.get_driver_rating(timeout=60), "Рейтинг водителя не найден или пуст"

    @allure.title("В блоке 'Детали' указана стоимость выбранного тарифа")
    def test_completed_order_details_price_matches_selected_tariff(self, main_page):
        main_page.enter_address_from(ADDRESS_KHAMOVNICHESKY)
        main_page.enter_address_to(ADDRESS_ZUBOVSKY)
        route_page = main_page.to_route_page()
        route_page.select_route_tab(ROUTE_TYPE_FAST)
        taxi_order_page = route_page.click_call_taxi()
        taxi_order_page.select_tariff("Рабочий")
        selected_price_text = taxi_order_page.get_tariff_price_text("Рабочий")
        taxi_order_page.check_requirement("Столик для ноутбука")
        waiting_page = taxi_order_page.click_submit_order()
        completed_page = waiting_page.wait_for_completed_order(timeout=60)
        completed_page.click_details()

        assert parse_price_from_text(completed_page.get_details_price_text()) == parse_price_from_text(selected_price_text)

    @allure.title("Кнопка 'Отменить' закрывает окно совершённого заказа")
    def test_completed_order_cancel_closes_window(self, main_page):
        main_page.enter_address_from(ADDRESS_KHAMOVNICHESKY)
        main_page.enter_address_to(ADDRESS_ZUBOVSKY)
        route_page = main_page.to_route_page()
        route_page.select_route_tab(ROUTE_TYPE_FAST)
        taxi_order_page = route_page.click_call_taxi()
        taxi_order_page.select_tariff("Рабочий")
        taxi_order_page.check_requirement("Столик для ноутбука")
        waiting_page = taxi_order_page.click_submit_order()
        completed_page = waiting_page.wait_for_completed_order(timeout=60)
        completed_page.click_cancel()

        assert not completed_page.is_title_visible(timeout=3)
