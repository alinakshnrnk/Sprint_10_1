from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    ADDRESS_FROM_INPUT = (By.ID, "from")
    ADDRESS_TO_INPUT = (By.ID, "to")
    MAP_CONTAINER = (By.ID, "map")
    # Частичное совпадение класса: у ymaps в названии класса зашита версия API (например,
    # 'ymaps-2-1-79-placemark-overlay'), и она может измениться при обновлении версии карт
    MAP_ROUTE_POINTS = (By.CSS_SELECTOR, "#map [class*='placemark-overlay']")

    def enter_address_from(self, address: str) -> None:
        self.type_text(self.ADDRESS_FROM_INPUT, address)

    def enter_address_to(self, address: str) -> None:
        self.type_text(self.ADDRESS_TO_INPUT, address)

    def get_route_points_count(self) -> int:
        return len(self.find_all(self.MAP_ROUTE_POINTS))

    def is_map_visible(self) -> bool:
        return self.is_visible(self.MAP_CONTAINER)
