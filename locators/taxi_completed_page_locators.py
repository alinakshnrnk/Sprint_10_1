from selenium.webdriver.common.by import By

TITLE = (By.CSS_SELECTOR, ".order-header-title")
CAR_NUMBER = (By.CSS_SELECTOR, ".order-number .number")
TARIFF_IMAGE = (By.CSS_SELECTOR, ".order-number img")

_DRIVER_GROUP_CSS = ".order-btn-group:has(.order-btn-rating)"
DRIVER_NAME = (By.CSS_SELECTOR, f"{_DRIVER_GROUP_CSS} > div:not(.order-button)")
DRIVER_RATING = (By.CSS_SELECTOR, f"{_DRIVER_GROUP_CSS} .order-btn-rating")
DRIVER_PHOTO = (By.CSS_SELECTOR, f"{_DRIVER_GROUP_CSS} img")

PRICE_ROW_VALUE = (
    By.XPATH,
    ".//div[contains(@class,'order-details-row')]"
    "[.//div[contains(@class,'o-d-h')][text()='Еще про поездку']]"
    "//div[contains(@class,'o-d-sh')]",
)


def order_button(button_label: str):
    """Кнопки 'Отменить'/'Детали' — одна разметка (button.order-button + подпись рядом)."""
    return (
        By.XPATH,
        f".//div[contains(@class,'order-btn-group')][.//div[text()='{button_label}']]//button",
    )


def details_row_value(row_label: str):
    return (
        By.XPATH,
        f".//div[contains(@class,'order-details-row')]"
        f"[.//div[contains(@class,'o-d-sh')][text()='{row_label}']]"
        "//div[contains(@class,'o-d-h')]",
    )
