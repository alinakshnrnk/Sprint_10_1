import allure
from data.test_data import SAME_ADDRESS_ROUTE_TEXT


@allure.feature("Отрисовка блока с выбором маршрута")
class TestRouteSelectionBlockDisplay:

    @allure.title("При вводе двух разных адресов отображается блок выбора маршрута")
    def test_route_block_visible_for_different_addresses(self, route_page_with_two_addresses):
        assert route_page_with_two_addresses.is_route_block_visible()

    @allure.title("При одинаковом адресе блок маршрута показывает 'Авто Бесплатно В пути 0 мин.'")
    def test_route_block_text_for_same_address(self, route_page_with_same_address):
        assert route_page_with_same_address.get_route_summary_text() == SAME_ADDRESS_ROUTE_TEXT
