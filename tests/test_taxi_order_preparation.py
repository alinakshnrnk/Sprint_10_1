import allure
from data.test_data import (
    ROUTE_TYPE_OPTIMAL,
    ROUTE_TYPE_FAST,
    ROUTE_TYPE_CUSTOM,
    TRANSPORT_TYPES,
)


@allure.feature("Подготовка к заказу такси")
class TestTaxiOrderPreparation:

    @allure.title("Переключение между Оптимальный/Быстрый меняет активный таб и пересчитывает время/стоимость")
    def test_switching_optimal_fast_updates_active_tab_and_price(self, route_page_with_two_addresses):
        page = route_page_with_two_addresses
        page.select_route_tab(ROUTE_TYPE_OPTIMAL)
        optimal_price = page.get_price_text()
        optimal_time = page.get_time_text()

        page.select_route_tab(ROUTE_TYPE_FAST)

        assert page.is_route_tab_active(ROUTE_TYPE_FAST)
        assert not page.is_route_tab_active(ROUTE_TYPE_OPTIMAL)
        assert (page.get_price_text(), page.get_time_text()) != (optimal_price, optimal_time)

    @allure.title("При выборе вида маршрута 'Свой' становятся активны все типы передвижения")
    def test_custom_route_enables_all_transport_types(self, route_page_with_two_addresses):
        page = route_page_with_two_addresses
        page.select_route_tab(ROUTE_TYPE_CUSTOM)

        assert page.is_route_tab_active(ROUTE_TYPE_CUSTOM)
        for transport_type in TRANSPORT_TYPES:
            assert page.is_transport_type_enabled(transport_type), f"Тип передвижения '{transport_type}' не активен"

    @allure.title("При выборе вида маршрута 'Быстрый' активна кнопка 'Вызвать такси'")
    def test_fast_route_enables_call_taxi_button(self, route_page_with_two_addresses):
        page = route_page_with_two_addresses
        page.select_route_tab(ROUTE_TYPE_FAST)

        assert page.is_call_taxi_button_active()

    @allure.title("При выборе маршрута 'Свой' и типа 'Драйв' активна кнопка 'Забронировать'")
    def test_custom_route_drive_enables_book_button(self, route_page_with_two_addresses):
        page = route_page_with_two_addresses
        page.select_route_tab(ROUTE_TYPE_CUSTOM)
        page.select_transport_type("Драйв")

        assert page.is_book_drive_button_active()
