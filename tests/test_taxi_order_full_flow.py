import allure
from helpers.wait_utils import parse_price_from_text


@allure.feature("Заказ тарифа Такси")
@allure.story("Полный флоу заказа")
class TestTaxiOrderFullFlow:

    @allure.title("Полный флоу: выбор тарифа → ожидание → совершённый заказ → детали → отмена")
    def test_full_taxi_order_flow(self, taxi_order_page):
        taxi_order_page.select_tariff("Рабочий")
        selected_price_text = taxi_order_page.get_tariff_price_text("Рабочий")
        taxi_order_page.check_requirement("Столик для ноутбука")
        waiting_page = taxi_order_page.click_submit_order()

        assert waiting_page.get_title_text() == "Поиск машины"
        assert waiting_page.is_countdown_timer_visible()

        # Явное ожидание перехода в окно совершённого заказа после окончания таймера поиска
        completed_page = waiting_page.wait_for_completed_order(timeout=60)
        assert completed_page.get_driver_name(timeout=60), "Имя водителя не найдено или пусто"
        assert completed_page.get_driver_photo_src(timeout=60), "У фото водителя пустой/отсутствующий src"
        assert completed_page.get_driver_rating(timeout=60), "Рейтинг водителя не найден или пуст"

        completed_page.click_details()
        details_price = parse_price_from_text(completed_page.get_details_price_text())
        expected_price = parse_price_from_text(selected_price_text)
        assert details_price == expected_price

        completed_page.click_cancel()
        assert not completed_page.is_visible(completed_page.TITLE, timeout=3)
