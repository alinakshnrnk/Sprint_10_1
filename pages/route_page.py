from locators import route_page_locators as loc
from pages.base_page import BasePage
from pages.taxi_order_page import TaxiOrderPage

ACTIVE_CLASS = "active"
DISABLED_CLASS = "disabled"


class RoutePage(BasePage):
    def is_route_block_visible(self) -> bool:
        return self.is_visible(loc.ROUTE_BLOCK)

    def get_route_summary_text(self) -> str:
        return f"{self.get_text(loc.PRICE_TEXT)} {self.get_text(loc.TIME_TEXT)}"

    def select_route_tab(self, tab_name: str) -> None:
        self.click(loc.route_tab(tab_name))

    def is_route_tab_active(self, tab_name: str) -> bool:
        return self.has_class(loc.route_tab(tab_name), ACTIVE_CLASS)

    def select_transport_type(self, transport_name: str) -> None:
        self.click(loc.transport_type(transport_name))

    def is_transport_type_active(self, transport_name: str) -> bool:
        return self.has_class(loc.transport_type(transport_name), ACTIVE_CLASS)

    def is_transport_type_enabled(self, transport_name: str) -> bool:
        return not self.has_class(loc.transport_type(transport_name), DISABLED_CLASS)

    def get_price_text(self) -> str:
        return self.get_text(loc.PRICE_TEXT)

    def get_time_text(self) -> str:
        return self.get_text(loc.TIME_TEXT)

    def is_call_taxi_button_active(self) -> bool:
        return self.find(loc.ORDER_ACTION_BUTTON).is_enabled()

    def click_call_taxi(self) -> TaxiOrderPage:
        self.click(loc.ORDER_ACTION_BUTTON)
        return TaxiOrderPage(self.driver)

    def is_book_drive_button_active(self) -> bool:
        return self.find(loc.ORDER_ACTION_BUTTON).is_enabled()

    def click_book_drive(self) -> None:
        self.click(loc.ORDER_ACTION_BUTTON)
