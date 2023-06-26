from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumDataMining:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_data_mining(self):
        self.driver.get("https://www.amazon.com.br/")

        wait = WebDriverWait(self.driver, 10)
        search = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".nav-input.nav-progressive-attribute")
            )
        )
        search.send_keys("Mineração de dados")
        search.submit()
        time.sleep(3)

        title_element = self.driver.find_elements(
            By.CSS_SELECTOR, ".a-size-base-plus.a-color-base.a-text-normal"
        )
        title = [element.text for element in title_element]
        time.sleep(10)

        self.driver.quit()

        return title
