from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TaxiWaitingPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".order-header-title")
    COUNTDOWN_TIMER = (By.CSS_SELECTOR, ".order-header-time")

    def _order_button_locator(self, button_label: str):
        return (
            By.XPATH,
            f".//div[contains(@class,'order-btn-group')][.//div[text()='{button_label}']]//button",
        )

    def _details_row_value_locator(self, row_label: str):
        return (
            By.XPATH,
            f".//div[contains(@class,'order-details-row')]"
            f"[.//div[contains(@class,'o-d-sh')][text()='{row_label}']]"
            "//div[contains(@class,'o-d-h')]",
        )

    def get_title_text(self) -> str:
        return self.get_text(self.TITLE)

    def is_countdown_timer_visible(self) -> bool:
        return self.is_visible(self.COUNTDOWN_TIMER)

    def wait_for_completed_order(self, timeout: int = 60) -> "TaxiCompletedPage":
        from pages.taxi_completed_page import TaxiCompletedPage

        completed_page = TaxiCompletedPage(self.driver)
        title_appeared = completed_page.is_visible(completed_page.TITLE, timeout=timeout)
        assert title_appeared, f"Окно совершённого заказа не появилось за {timeout} секунд"
        return completed_page

    def click_details(self) -> None:
        self.click(self._order_button_locator("Детали"))

    def click_cancel(self) -> None:
        self.click(self._order_button_locator("Отменить"))

    def get_details_pickup_address(self) -> str:
        return self.get_text(self._details_row_value_locator("Адрес подачи"))

    def get_details_destination_address(self) -> str:
        return self.get_text(self._details_row_value_locator("Адрес назначения"))

    def get_details_payment_method(self) -> str:
        return self.get_text(self._details_row_value_locator("Способ оплаты"))

    def get_details_price_text(self) -> str:
        row_locator = (
            By.XPATH,
            ".//div[contains(@class,'order-details-row')]"
            "[.//div[contains(@class,'o-d-h')][text()='Еще про поездку']]"
            "//div[contains(@class,'o-d-sh')]",
        )
        return self.get_text(row_locator)
