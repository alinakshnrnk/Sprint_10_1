import allure


@allure.feature("Отрисовка маршрута")
class TestRouteDrawing:

    @allure.title("При вводе двух разных адресов на карте отображаются точки начала и конца маршрута")
    def test_two_points_displayed_on_map_for_different_addresses(self, route_page_with_two_addresses, main_page):
        assert main_page.get_route_points_count() == 2
