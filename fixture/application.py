from time import sleep

import allure
from selenium import webdriver
from fixture.pages.practice_form_page import PracticeFormPage


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)
        self.base_url = 'https://demoqa.com/automation-practice-form'
        self.practice_form_page = None

    @allure.step("Open form page")
    def open_practice_form_page(self):
        self.wd.get(self.base_url)
        if not self.practice_form_page:
            self.practice_form_page = PracticeFormPage(self)
        return self.practice_form_page

    def destroy(self):
        self.wd.quit()

    @allure.step("Take a screenshot")
    def take_screenshot(self, name):
        if hasattr(allure, 'attach'):
            sleep(1)
            screenshot_name = f"{name}.png"  # Генерация имени скриншота
            allure.attach(self.wd.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
