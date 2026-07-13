import allure

from data.test_data import ADDRESS_KHAMOVNICHESKY, ADDRESS_ZUBOVSKY


@allure.feature("Отрисовка маршрута")
class TestRouteDrawing:

    @allure.title("При вводе двух разных адресов на карте отображаются точки начала и конца маршрута")
    def test_two_points_displayed_on_map_for_different_addresses(self, main_page):
        main_page.enter_address_from(ADDRESS_KHAMOVNICHESKY)
        main_page.enter_address_to(ADDRESS_ZUBOVSKY)

        assert main_page.get_route_points_count() == 2
