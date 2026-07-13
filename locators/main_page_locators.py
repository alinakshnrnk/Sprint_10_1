from selenium.webdriver.common.by import By

ADDRESS_FROM_INPUT = (By.ID, "from")
ADDRESS_TO_INPUT = (By.ID, "to")
MAP_CONTAINER = (By.ID, "map")
MAP_ROUTE_POINTS = (By.CSS_SELECTOR, "#map [class*='placemark-overlay']")
