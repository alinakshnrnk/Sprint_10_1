from selenium.webdriver.common.by import By

ROUTE_BLOCK = (By.CSS_SELECTOR, ".workflow-subcontainer")
PRICE_TEXT = (By.CSS_SELECTOR, ".results-text .text")
TIME_TEXT = (By.CSS_SELECTOR, ".results-text .duration")
ORDER_ACTION_BUTTON = (By.CSS_SELECTOR, ".results-text button.button.round")

TRANSPORT_ICON_KEYWORDS = {
    "Машина": "car",
    "Пешком": "walk",
    "Такси": "taxi",
    "Велосипед": "bike",
    "Самокат": "scooter",
    "Драйв": "drive",
}


def route_tab(tab_name: str):
    return (By.XPATH, f".//div[contains(@class,'mode') and text()='{tab_name}']")


def transport_type(transport_name: str):
    keyword = TRANSPORT_ICON_KEYWORDS[transport_name]
    return (By.XPATH, f".//div[contains(@class,'type')][.//img[contains(@src,'{keyword}')]]")
