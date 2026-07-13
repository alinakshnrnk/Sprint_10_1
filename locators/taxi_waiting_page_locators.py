from selenium.webdriver.common.by import By

TITLE = (By.CSS_SELECTOR, ".order-header-title")
COUNTDOWN_TIMER = (By.CSS_SELECTOR, ".order-header-time")

PRICE_ROW_VALUE = (
    By.XPATH,
    ".//div[contains(@class,'order-details-row')]"
    "[.//div[contains(@class,'o-d-h')][text()='Еще про поездку']]"
    "//div[contains(@class,'o-d-sh')]",
)


def order_button(button_label: str):
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
