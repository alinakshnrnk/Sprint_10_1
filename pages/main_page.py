from locators import main_page_locators as loc
from pages.base_page import BasePage
from pages.route_page import RoutePage


class MainPage(BasePage):
    def enter_address_from(self, address: str) -> None:
        self.type_text(loc.ADDRESS_FROM_INPUT, address)

    def enter_address_to(self, address: str) -> None:
        self.type_text(loc.ADDRESS_TO_INPUT, address)

    def get_route_points_count(self) -> int:
        return len(self.find_all(loc.MAP_ROUTE_POINTS))

    def is_map_visible(self) -> bool:
        return self.is_visible(loc.MAP_CONTAINER)

    def to_route_page(self) -> RoutePage:
        return RoutePage(self.driver)
