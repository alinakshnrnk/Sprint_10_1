from selenium.webdriver.common.by import By
from pages.base_page import BasePage, DEFAULT_TIMEOUT


class TaxiCompletedPage(BasePage):

    TITLE = (By.CSS_SELECTOR, ".order-header-title")
    CAR_NUMBER = (By.CSS_SELECTOR, ".order-number .number")
    TARIFF_IMAGE = (By.CSS_SELECTOR, ".order-number img")

    # Блок водителя — единственная group в .order-buttons с рейтингом внутри.
    # CSS :has()/:not() вместо XPath div[last()] — надёжнее, не зависит от позиции узлов
    _DRIVER_GROUP_CSS = ".order-btn-group:has(.order-btn-rating)"
    DRIVER_NAME = (By.CSS_SELECTOR, f"{_DRIVER_GROUP_CSS} > div:not(.order-button)")
    DRIVER_RATING = (By.CSS_SELECTOR, f"{_DRIVER_GROUP_CSS} .order-btn-rating")
    DRIVER_PHOTO = (By.CSS_SELECTOR, f"{_DRIVER_GROUP_CSS} img")

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

    def get_driver_name(self, timeout: int = DEFAULT_TIMEOUT) -> str:
        return self.get_text_content(self.DRIVER_NAME, timeout)

    def get_driver_rating(self, timeout: int = DEFAULT_TIMEOUT) -> str:
        return self.get_text_content(self.DRIVER_RATING, timeout)

    def get_driver_photo_src(self, timeout: int = DEFAULT_TIMEOUT) -> str:
        return self.find(self.DRIVER_PHOTO, timeout).get_attribute("src") or ""

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
