import allure
import pytest
from data.test_data import TAXI_TARIFFS


@allure.feature("Заказ тарифа Такси")
@allure.story("Выбор тарифа и форма заказа")
class TestTaxiTariffSelection:

    @allure.title("Форма заказа открывается со всеми 6 тарифами, один из них активен")
    def test_all_tariffs_displayed_with_one_active(self, taxi_order_page):
        for tariff_name in TAXI_TARIFFS:
            assert taxi_order_page.is_tariff_visible(tariff_name), f"Тариф '{tariff_name}' не отображается"

        active_tariffs = [name for name in TAXI_TARIFFS if taxi_order_page.is_tariff_active(name)]
        assert len(active_tariffs) == 1, f"Ожидался ровно 1 активный тариф, получено: {active_tariffs}"

    @allure.title("Тултип с описанием тарифа соответствует ТЗ")
    @pytest.mark.parametrize(
        "tariff_name, expected_description",
        [
            pytest.param(
                name,
                description,
                marks=pytest.mark.xfail(
                    reason="Баг: у тарифов 'Сонный' и 'Разговорчивый' в тултипах перепутаны описания"
                ),
            )
            if name in ("Сонный", "Разговорчивый")
            else (name, description)
            for name, description in TAXI_TARIFFS.items()
        ],
    )
    def test_tariff_tooltip_description(self, taxi_order_page, tariff_name, expected_description):
        taxi_order_page.hover_tariff_info_icon(tariff_name)

        assert taxi_order_page.get_tariff_tooltip_text(tariff_name) == expected_description

    @allure.title("Под тарифами отображается блок с полями Телефон/Способ оплаты/Комментарий/Требования")
    def test_order_form_fields_displayed(self, taxi_order_page):
        assert taxi_order_page.is_order_form_fields_visible()
