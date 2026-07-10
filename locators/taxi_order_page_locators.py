from selenium.webdriver.common.by import By

PHONE_FIELD = (By.CSS_SELECTOR, ".np-button")
PAYMENT_METHOD_FIELD = (By.CSS_SELECTOR, ".pp-button")
DRIVER_COMMENT_FIELD = (By.ID, "comment")
ORDER_REQUIREMENTS_BLOCK = (By.CSS_SELECTOR, ".reqs")
SUBMIT_ORDER_BUTTON = (By.CSS_SELECTOR, ".smart-button-wrapper button.smart-button")


def tariff_card(tariff_name: str):
    return (
        By.XPATH,
        f".//div[contains(@class,'tcard')][.//div[contains(@class,'tcard-title')][text()='{tariff_name}']]",
    )


def tariff_info_icon(tariff_name: str):
    return (
        By.XPATH,
        f".//div[contains(@class,'tcard')][.//div[contains(@class,'tcard-title')][text()='{tariff_name}']]"
        "//button[contains(@class,'tcard-i')]",
    )


def tariff_price(tariff_name: str):
    return (
        By.XPATH,
        f".//div[contains(@class,'tcard')][.//div[contains(@class,'tcard-title')][text()='{tariff_name}']]"
        "//div[contains(@class,'tcard-price')]",
    )


def tooltip_description(tooltip_id: str):
    return (By.CSS_SELECTOR, f"#{tooltip_id} .i-dPrefix")


def requirement_checkbox(requirement_name: str):
    return (
        By.XPATH,
        f".//div[contains(@class,'r-sw-container')][.//div[contains(@class,'r-sw-label')][text()='{requirement_name}']]"
        "//input[@type='checkbox']",
    )
