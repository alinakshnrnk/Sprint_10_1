from locators import taxi_completed_page_locators as loc
from pages.base_page import BasePage, DEFAULT_TIMEOUT


class TaxiCompletedPage(BasePage):
    def wait_until_loaded(self, timeout: int = 60) -> None:
        self.find(loc.TITLE, timeout)

    def is_title_visible(self, timeout: int = DEFAULT_TIMEOUT) -> bool:
        return self.is_visible(loc.TITLE, timeout)

    def get_title_text(self) -> str:
        return self.get_text(loc.TITLE)

    def get_car_number(self) -> str:
        return self.get_text(loc.CAR_NUMBER)

    def get_driver_name(self, timeout: int = DEFAULT_TIMEOUT) -> str:
        return self.get_text_content(loc.DRIVER_NAME, timeout)

    def get_driver_rating(self, timeout: int = DEFAULT_TIMEOUT) -> str:
        return self.get_text_content(loc.DRIVER_RATING, timeout)

    def get_driver_photo_src(self, timeout: int = DEFAULT_TIMEOUT) -> str:
        return self.find(loc.DRIVER_PHOTO, timeout).get_attribute("src") or ""

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
