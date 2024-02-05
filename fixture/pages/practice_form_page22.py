from time import sleep

from selenium.webdriver.common.by import By


class PracticeFormPage:
    _FIRST_NAME = (By.ID, 'firstName')
    _FIRST_LAST = (By.ID, 'lastName')
    _EMAIL = (By.ID, 'userEmail')
    _GENDER_MALE = (By.CSS_SELECTOR, '.custom-radio:nth-child(1) > .custom-control-label')
    _GENDER_FEMALE = (By.CSS_SELECTOR, '.custom-radio:nth-child(2) > .custom-control-label')
    _GENDER_OTHER = (By.CSS_SELECTOR, '.custom-radio:nth-child(3) > .custom-control-label')
    _MOBILE = (By.ID, 'userNumber')
    _DATE_OF_BIRTH_FIELD = (By.ID, 'dateOfBirthInput')
    _DATE_OF_BIRTH_MONTH_SELECT = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    _DATE_OF_BIRTH_YEAR_SELECT = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    _DATE_OF_BIRTH_DAY = (By.CSS_SELECTOR, ".react-datepicker__day--026")
    _SUBJECTS = (By.CSS_SELECTOR, '.subjects-auto-complete__value-container')
    _PICTURE_BTN = (By.ID, 'uploadPicture')
    _CURRENT_ADDRES = (By.ID, 'currentAddress')
    _STATE = (By.ID, 'react-select-3-option-1')  #вот тут не просто так как это выпадающий список
    _PICTURE_CITY = (By.CSS_SELECTOR, '.css-1pahdxg-control > .css-1hwfws3') # та же ебала, надо изучить
    _SUBNIT_BTN = (By.XPATH, '//div/button')
    _THANK_FOR_SUBMITING_TXT = (By.XPATH, '//div/button')
   #  _TABLE_VALUE = (By.XPATH, f'//tr[{n}]/td[2]')  #разобраться попозжа

    def __init__(self, app):
        self.wd = app.wd
        self.app = app

    def open_site(self):
        self.wd.maximize_window()

    def fill_and_submit_form(self, first_name, last_name, email, gender, mobile, date_of_birth, subjects, picture_path,
                             current_address, state, city):
        wd = self.app.wd
        # Заполнение полей формы
        self.enter_text(self._FIRST_NAME, first_name)
        self.enter_text(self._FIRST_LAST, last_name)
        self.enter_text(self._EMAIL, email)
        self.select_gender(gender)
        self.enter_text(self._MOBILE, mobile)
        self.select_date_of_birth(date_of_birth)
        # Ввод предметов (если нужно)
        subject_input = wd.find_element(*self._SUBJECTS)
        subject_input.clear()
        sleep(10)
        subject_input.send_keys(subjects)

        # Загрузка изображения
     #   wd.find_element(*self._PICTURE_BTN).send_keys(picture_path)

        self.enter_text(self._CURRENT_ADDRES, current_address)

        # Выбор штата (если нужно)
    #    if state:
 #            wd.find_element(*self._STATE).click()
 #           wd.find_element(*self._STATE).send_keys(state)

        # Ввод города (если нужно)
 #       if city:
 #           city_input = wd.find_element(*self._PICTURE_CITY)
 #           city_input.clear()
  #          city_input.send_keys(city)

        # Нажатие кнопки отправки формы
        wd.find_element(*self._SUBNIT_BTN).click()
        sleep(20)

    def select_date_of_birth(self, date_of_birth):
        wd = self.app.wd
        wd.find_element(*self._DATE_OF_BIRTH_FIELD).click()
        # Нажатие на выпадающее меню выбора месяца
        wd.find_element(*self._DATE_OF_BIRTH_MONTH_SELECT).click()
        # Выбор нужного месяца
        month_option = wd.find_element(By.XPATH, f"//option[. = '{date_of_birth.split()[1]}']")
        month_option.click()
        # Нажатие на выпадающее меню выбора года
        wd.find_element(*self._DATE_OF_BIRTH_YEAR_SELECT).click()
        # Выбор нужного года
        year_option = wd.find_element(By.XPATH, f"//option[. = '{date_of_birth.split()[2]}']")
        year_option.click()
        # Выбор нужного числа
        day_option = wd.find_element(By.XPATH,
                                     f"//div[contains(@class, 'react-datepicker__day') and "
                                     f"text() = '{date_of_birth.split()[0]}']")
        day_option.click()

    def select_gender(self, gender):
        if gender == "Male":
            self.wd.find_element(*self._GENDER_MALE).click()
        elif gender == "Female":
            self.wd.find_element(*self._GENDER_FEMALE).click()
        else:
            self.wd.find_element(*self._GENDER_OTHER).click()

    def enter_text(self, locator, text):
        element = self.wd.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def get_inner_text(self, locator):
        return self.wd.find_element(*locator).get_attribute('innerText')

    def get_table(self):
        return self.get("/device/metainfo")

    def check_version(self, selector):
        self.wd.refresh()
        return str(self.get_innerText(selector))
