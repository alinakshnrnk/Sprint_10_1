from locators import taxi_order_page_locators as loc
from pages.base_page import BasePage
from pages.taxi_waiting_page import TaxiWaitingPage

ACTIVE_TARIFF_CLASS = "active"


class TaxiOrderPage(BasePage):
    def is_tariff_visible(self, tariff_name: str) -> bool:
        return self.is_visible(loc.tariff_card(tariff_name))

    def is_tariff_active(self, tariff_name: str) -> bool:
        return self.has_class(loc.tariff_card(tariff_name), ACTIVE_TARIFF_CLASS)

    def select_tariff(self, tariff_name: str) -> None:
        self.click(loc.tariff_card(tariff_name))

    def get_tariff_price_text(self, tariff_name: str) -> str:
        return self.get_text(loc.tariff_price(tariff_name))

    def hover_tariff_info_icon(self, tariff_name: str) -> None:
        self.hover_js(loc.tariff_info_icon(tariff_name))

    def get_tariff_tooltip_text(self, tariff_name: str) -> str:
        icon = self.find(loc.tariff_info_icon(tariff_name))
        tooltip_id = icon.get_attribute("data-for")
        return self.get_text_content(loc.tooltip_description(tooltip_id))

    def is_order_form_fields_visible(self) -> bool:
        return all(
            [
                self.is_visible(loc.PHONE_FIELD),
                self.is_visible(loc.PAYMENT_METHOD_FIELD),
                self.is_visible(loc.DRIVER_COMMENT_FIELD),
                self.is_visible(loc.ORDER_REQUIREMENTS_BLOCK),
            ]
        )

    def check_requirement(self, requirement_name: str) -> None:
        self.click_js(loc.requirement_checkbox(requirement_name))

    def click_submit_order(self) -> TaxiWaitingPage:
        self.click_js(loc.SUBMIT_ORDER_BUTTON)
        return TaxiWaitingPage(self.driver)
