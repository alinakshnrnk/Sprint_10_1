import allure

from data.test_data import ADDRESS_KHAMOVNICHESKY, ADDRESS_ZUBOVSKY, SAME_ADDRESS_ROUTE_TEXT


@allure.feature("Отрисовка блока с выбором маршрута")
class TestRouteSelectionBlockDisplay:

    @allure.title("При вводе двух разных адресов отображается блок выбора маршрута")
    def test_route_block_visible_for_different_addresses(self, main_page):
        main_page.enter_address_from(ADDRESS_KHAMOVNICHESKY)
        main_page.enter_address_to(ADDRESS_ZUBOVSKY)
        route_page = main_page.to_route_page()

        assert route_page.is_route_block_visible()

    @allure.title("При одинаковом адресе блок маршрута показывает 'Авто Бесплатно В пути 0 мин.'")
    def test_route_block_text_for_same_address(self, main_page):
        main_page.enter_address_from(ADDRESS_KHAMOVNICHESKY)
        main_page.enter_address_to(ADDRESS_KHAMOVNICHESKY)
        route_page = main_page.to_route_page()

        assert route_page.get_route_summary_text() == SAME_ADDRESS_ROUTE_TEXT
