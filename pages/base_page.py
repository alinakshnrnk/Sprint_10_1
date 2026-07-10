from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

DEFAULT_TIMEOUT = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str) -> None:
        self.driver.get(url)

    def _wait(self, timeout: int = DEFAULT_TIMEOUT) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout)

    def find(self, locator, timeout: int = DEFAULT_TIMEOUT):
        return self._wait(timeout).until(EC.presence_of_element_located(locator))

    def find_all(self, locator, timeout: int = DEFAULT_TIMEOUT):
        return self._wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def is_visible(self, locator, timeout: int = DEFAULT_TIMEOUT) -> bool:
        try:
            self._wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def click(self, locator, timeout: int = DEFAULT_TIMEOUT) -> None:
        self._wait(timeout).until(EC.element_to_be_clickable(locator)).click()

    def click_js(self, locator, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Клик через JS — обходит перекрытие элемента оверлеем."""
        element = self.find(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        element = self._wait(timeout).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout: int = DEFAULT_TIMEOUT) -> str:
        return self.find(locator, timeout).text

    def get_text_content(self, locator, timeout: int = DEFAULT_TIMEOUT) -> str:
        """
        textContent через JS вместо .text — не зависит от того, считает ли Selenium
        элемент видимым (.text возвращает '' для невидимых/переходных по CSS элементов).
        """
        element = self.find(locator, timeout)
        return (self.driver.execute_script("return arguments[0].textContent;", element) or "").strip()

    def hover(self, locator, timeout: int = DEFAULT_TIMEOUT) -> None:
        element = self.find(locator, timeout)
        ActionChains(self.driver).move_to_element(element).perform()

    def hover_js(self, locator, timeout: int = DEFAULT_TIMEOUT) -> None:
        element = self.find(locator, timeout)
        self.driver.execute_script(
            "arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));"
            "arguments[0].dispatchEvent(new MouseEvent('mouseenter', {bubbles: true}));",
            element,
        )

    def is_element_active(self, locator, active_class: str, timeout: int = DEFAULT_TIMEOUT) -> bool:
        element = self.find(locator, timeout)
        return active_class in element.get_attribute("class")

    def has_class(self, locator, class_name: str, timeout: int = DEFAULT_TIMEOUT) -> bool:
        element = self.find(locator, timeout)
        classes = (element.get_attribute("class") or "").split()
        return class_name in classes
