import allure
import pytest

from data.test_data import ADDRESS_KHAMOVNICHESKY, ADDRESS_ZUBOVSKY, ROUTE_TYPE_FAST, TAXI_TARIFFS


def _open_taxi_order_page(main_page):
    main_page.enter_address_from(ADDRESS_KHAMOVNICHESKY)
    main_page.enter_address_to(ADDRESS_ZUBOVSKY)
    route_page = main_page.to_route_page()
    route_page.select_route_tab(ROUTE_TYPE_FAST)
    return route_page.click_call_taxi()


@allure.feature("Заказ тарифа Такси")
@allure.story("Выбор тарифа и форма заказа")
class TestTaxiTariffSelection:

    @allure.title("Форма заказа открывается со всеми 6 тарифами")
    def test_all_tariffs_displayed(self, main_page):
        taxi_order_page = _open_taxi_order_page(main_page)

        for tariff_name in TAXI_TARIFFS:
            assert taxi_order_page.is_tariff_visible(tariff_name), f"Тариф '{tariff_name}' не отображается"

    @allure.title("Ровно один тариф отмечен активным по умолчанию")
    def test_exactly_one_tariff_is_active(self, main_page):
        taxi_order_page = _open_taxi_order_page(main_page)

        active_tariffs = [name for name in TAXI_TARIFFS if taxi_order_page.is_tariff_active(name)]

        assert len(active_tariffs) == 1

    @allure.title("Тултип тарифа 'Рабочий' соответствует ТЗ")
    def test_tariff_tooltip_description_rabochiy(self, main_page):
        taxi_order_page = _open_taxi_order_page(main_page)
        taxi_order_page.hover_tariff_info_icon("Рабочий")

        assert taxi_order_page.get_tariff_tooltip_text("Рабочий") == TAXI_TARIFFS["Рабочий"]

    @allure.title("Тултип тарифа 'Отпускной' соответствует ТЗ")
    def test_tariff_tooltip_description_otpusknoy(self, main_page):
        taxi_order_page = _open_taxi_order_page(main_page)
        taxi_order_page.hover_tariff_info_icon("Отпускной")

        assert taxi_order_page.get_tariff_tooltip_text("Отпускной") == TAXI_TARIFFS["Отпускной"]

    @allure.title("Тултип тарифа 'Утешительный' соответствует ТЗ")
    def test_tariff_tooltip_description_uteshitelniy(self, main_page):
        taxi_order_page = _open_taxi_order_page(main_page)
        taxi_order_page.hover_tariff_info_icon("Утешительный")

        assert taxi_order_page.get_tariff_tooltip_text("Утешительный") == TAXI_TARIFFS["Утешительный"]

    @allure.title("Тултип тарифа 'Глянцевый' соответствует ТЗ")
    def test_tariff_tooltip_description_glyantsevy(self, main_page):
        taxi_order_page = _open_taxi_order_page(main_page)
        taxi_order_page.hover_tariff_info_icon("Глянцевый")

        assert taxi_order_page.get_tariff_tooltip_text("Глянцевый") == TAXI_TARIFFS["Глянцевый"]

    @allure.title("Тултип тарифа 'Сонный' соответствует ТЗ")
    @pytest.mark.xfail(reason="Баг: у тарифа 'Сонный' в тултипе показано описание тарифа 'Разговорчивый'")
    def test_tariff_tooltip_description_sonny(self, main_page):
        taxi_order_page = _open_taxi_order_page(main_page)
        taxi_order_page.hover_tariff_info_icon("Сонный")

        assert taxi_order_page.get_tariff_tooltip_text("Сонный") == TAXI_TARIFFS["Сонный"]

    @allure.title("Тултип тарифа 'Разговорчивый' соответствует ТЗ")
    @pytest.mark.xfail(reason="Баг: у тарифа 'Разговорчивый' в тултипе показано описание тарифа 'Сонный'")
    def test_tariff_tooltip_description_razgovorchivy(self, main_page):
        taxi_order_page = _open_taxi_order_page(main_page)
        taxi_order_page.hover_tariff_info_icon("Разговорчивый")

        assert taxi_order_page.get_tariff_tooltip_text("Разговорчивый") == TAXI_TARIFFS["Разговорчивый"]

    @allure.title("Под тарифами отображается блок с полями Телефон/Способ оплаты/Комментарий/Требования")
    def test_order_form_fields_displayed(self, main_page):
        taxi_order_page = _open_taxi_order_page(main_page)

        assert taxi_order_page.is_order_form_fields_visible()
