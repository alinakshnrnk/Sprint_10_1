from selenium.webdriver.common.by import By
from pages.base_page import BasePage

ACTIVE_CLASS = "active"
DISABLED_CLASS = "disabled"

# Типы передвижения не имеют текста/alt — определяются по имени файла иконки.
# "taxi" совпадает и с taxi.svg, и с taxi-active.svg — этого достаточно, т.к.
# активность проверяется отдельно через класс "active", а не через файл иконки.
TRANSPORT_ICON_KEYWORDS = {
    "Машина": "car",
    "Пешком": "walk",
    "Такси": "taxi",
    "Велосипед": "bike",
    "Самокат": "scooter",
    "Драйв": "drive",
}


class RoutePage(BasePage):
    ROUTE_BLOCK = (By.CSS_SELECTOR, ".workflow-subcontainer")
    ROUTE_TAB = lambda self, name: (By.XPATH, f".//div[contains(@class,'mode') and text()='{name}']")

    def _transport_type_locator(self, transport_name: str):
        keyword = TRANSPORT_ICON_KEYWORDS[transport_name]
        return (By.XPATH, f".//div[contains(@class,'type')][.//img[contains(@src,'{keyword}')]]")

    PRICE_TEXT = (By.CSS_SELECTOR, ".results-text .text")
    TIME_TEXT = (By.CSS_SELECTOR, ".results-text .duration")
    # Это одна и та же кнопка: "Вызвать такси" для типа Такси, "Забронировать" для типа Драйв
    ORDER_ACTION_BUTTON = (By.CSS_SELECTOR, ".results-text button.button.round")

    def is_route_block_visible(self) -> bool:
        return self.is_visible(self.ROUTE_BLOCK)

    def get_route_summary_text(self) -> str:
        return f"{self.get_text(self.PRICE_TEXT)} {self.get_text(self.TIME_TEXT)}"

    def select_route_tab(self, tab_name: str) -> None:
        self.click(self.ROUTE_TAB(tab_name))

    def is_route_tab_active(self, tab_name: str) -> bool:
        return self.has_class(self.ROUTE_TAB(tab_name), ACTIVE_CLASS)

    def select_transport_type(self, transport_name: str) -> None:
        self.click(self._transport_type_locator(transport_name))

    def is_transport_type_active(self, transport_name: str) -> bool:
        return self.has_class(self._transport_type_locator(transport_name), ACTIVE_CLASS)

    def is_transport_type_enabled(self, transport_name: str) -> bool:
        return not self.has_class(self._transport_type_locator(transport_name), DISABLED_CLASS)

    def get_price_text(self) -> str:
        return self.get_text(self.PRICE_TEXT)

    def get_time_text(self) -> str:
        return self.get_text(self.TIME_TEXT)

    def is_call_taxi_button_active(self) -> bool:
        return self.find(self.ORDER_ACTION_BUTTON).is_enabled()

    def click_call_taxi(self) -> None:
        self.click(self.ORDER_ACTION_BUTTON)

    def is_book_drive_button_active(self) -> bool:
        return self.find(self.ORDER_ACTION_BUTTON).is_enabled()

    def click_book_drive(self) -> None:
        self.click(self.ORDER_ACTION_BUTTON)
