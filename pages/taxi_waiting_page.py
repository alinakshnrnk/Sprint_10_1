from locators import taxi_waiting_page_locators as loc
from pages.base_page import BasePage
from pages.taxi_completed_page import TaxiCompletedPage


class TaxiWaitingPage(BasePage):
    def get_title_text(self) -> str:
        return self.get_text(loc.TITLE)

    def is_countdown_timer_visible(self) -> bool:
        return self.is_visible(loc.COUNTDOWN_TIMER)

    def click_details(self) -> None:
        self.click(loc.order_button("Детали"))

    def click_cancel(self) -> None:
        self.click(loc.order_button("Отменить"))

    def get_details_pickup_address(self) -> str:
        return self.get_text(loc.details_row_value("Адрес подачи"))

    def get_details_destination_address(self) -> str:
        return self.get_text(loc.details_row_value("Адрес назначения"))

    def get_details_payment_method(self) -> str:
        return self.get_text(loc.details_row_value("Способ оплаты"))

    def get_details_price_text(self) -> str:
        return self.get_text(loc.PRICE_ROW_VALUE)

    def wait_for_completed_order(self, timeout: int = 60) -> TaxiCompletedPage:
        completed_page = TaxiCompletedPage(self.driver)
        completed_page.wait_until_loaded(timeout=timeout)
        return completed_page