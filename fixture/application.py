
from selenium import webdriver
from fixture.pages.practice_form_page import PracticeFormPage


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)
        self.base_url = 'https://demoqa.com/automation-practice-form'
        self.practice_form_page = None

    def open_practice_form_page(self):
        self.wd.get(self.base_url)
        if not self.practice_form_page:
            self.practice_form_page = PracticeFormPage(self)
        return self.practice_form_page

    def destroy(self):
        self.wd.quit()
