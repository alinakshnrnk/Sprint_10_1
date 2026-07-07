from selenium.webdriver.common.by import By
from pages.base_page import BasePage

ACTIVE_TARIFF_CLASS = "active"


class TaxiOrderPage(BasePage):
    def _tariff_card_locator(self, tariff_name: str):
        return (
            By.XPATH,
            f".//div[contains(@class,'tcard')][.//div[contains(@class,'tcard-title')][text()='{tariff_name}']]",
        )

    def _tariff_info_icon_locator(self, tariff_name: str):
        return (
            By.XPATH,
            f".//div[contains(@class,'tcard')][.//div[contains(@class,'tcard-title')][text()='{tariff_name}']]"
            "//button[contains(@class,'tcard-i')]",
        )

    def _tariff_price_locator(self, tariff_name: str):
        return (
            By.XPATH,
            f".//div[contains(@class,'tcard')][.//div[contains(@class,'tcard-title')][text()='{tariff_name}']]"
            "//div[contains(@class,'tcard-price')]",
        )

    PHONE_FIELD = (By.CSS_SELECTOR, ".np-button")
    PAYMENT_METHOD_FIELD = (By.CSS_SELECTOR, ".pp-button")
    DRIVER_COMMENT_FIELD = (By.ID, "comment")
    ORDER_REQUIREMENTS_BLOCK = (By.CSS_SELECTOR, ".reqs")
    REQUIREMENT_CHECKBOX = lambda self, name: (
        By.XPATH,
        f".//div[contains(@class,'r-sw-container')][.//div[contains(@class,'r-sw-label')][text()='{name}']]"
        "//input[@type='checkbox']",
    )
    SUBMIT_ORDER_BUTTON = (By.CSS_SELECTOR, ".smart-button-wrapper button.smart-button")

    def is_tariff_visible(self, tariff_name: str) -> bool:
        return self.is_visible(self._tariff_card_locator(tariff_name))

    def is_tariff_active(self, tariff_name: str) -> bool:
        return self.has_class(self._tariff_card_locator(tariff_name), ACTIVE_TARIFF_CLASS)

    def select_tariff(self, tariff_name: str) -> None:
        self.click(self._tariff_card_locator(tariff_name))

    def get_tariff_price_text(self, tariff_name: str) -> str:
        return self.get_text(self._tariff_price_locator(tariff_name))

    def hover_tariff_info_icon(self, tariff_name: str) -> None:
        self.hover_js(self._tariff_info_icon_locator(tariff_name))

    def get_tariff_tooltip_text(self, tariff_name: str) -> str:
        icon = self.find(self._tariff_info_icon_locator(tariff_name))
        tooltip_id = icon.get_attribute("data-for")
        tooltip_description_locator = (By.CSS_SELECTOR, f"#{tooltip_id} .i-dPrefix")
        return self.get_text_content(tooltip_description_locator)

    def is_order_form_fields_visible(self) -> bool:
        return all(
            [
                self.is_visible(self.PHONE_FIELD),
                self.is_visible(self.PAYMENT_METHOD_FIELD),
                self.is_visible(self.DRIVER_COMMENT_FIELD),
                self.is_visible(self.ORDER_REQUIREMENTS_BLOCK),
            ]
        )

    def check_requirement(self, requirement_name: str) -> None:
        self.click_js(self.REQUIREMENT_CHECKBOX(requirement_name))

    def click_submit_order(self) -> "TaxiWaitingPage":
        from pages.taxi_waiting_page import TaxiWaitingPage

        self.click_js(self.SUBMIT_ORDER_BUTTON)
        return TaxiWaitingPage(self.driver)
