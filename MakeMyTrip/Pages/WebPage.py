from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class WebPage:
    """
    This is a parent class for all web-page classes created in this project.
    This class provides the basic common functionality required for web-page.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def check_page_load_success(self):
        if 'This site can’t be reached' in self.driver.page_source:
            print('Page not found')
            return False
        return True

    def check_element_accessible(self, element, expected_text):
        iter_count = 0
        elem_found = False
        while not elem_found:
            try:
                elem_found = self.wait.until(ec.text_to_be_present_in_element((By.XPATH, element), expected_text))
            except Exception as e:
                print(e)
                iter_count = iter_count + 1
                if iter_count > 5:
                    break
        return elem_found

    def element_tobe_clickable(self, by, element_id):
        try:
            found_element = self.wait.until(ec.element_to_be_clickable((by, element_id)))
            return found_element
        except TimeoutException as e:
            print(e)
            return False

    def visibility_of_element_located(self, by, element_id):
        try:
            found_element = self.wait.until(ec.visibility_of_element_located((by, element_id)))
            return found_element
        except TimeoutException as e:
            print('Login pop up did not appear.', e)

    def presence_of_required_element(self, by, element_id):
        try:
            found_element = self.wait.until(ec.presence_of_element_located((by, element_id)))
            return found_element
        except TimeoutException as e:
            print(e)

    def element_clickable(self, by, element_id):
        element_found = self.wait.until(ec.element_to_be_clickable((by, element_id)))
        if not element_found:
            raise TimeoutException
        else:
            return element_found

    def element_visible_loc(self, by, element_id):
        element_found = self.wait.until(ec.visibility_of_element_located((by, element_id)))
        if not element_found:
            return False
        else:
            return element_found
