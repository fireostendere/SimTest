import sys
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class PracticeFormPage:
    # Локаторы элементов страницы
    _FIRST_NAME = (By.ID, 'firstName')
    _LAST_NAME = (By.ID, 'lastName')
    _EMAIL = (By.ID, 'userEmail')
    _GENDER_MALE = (By.CSS_SELECTOR, '.custom-radio:nth-child(1) > .custom-control-label')
    _GENDER_FEMALE = (By.CSS_SELECTOR, '.custom-radio:nth-child(2) > .custom-control-label')
    _GENDER_OTHER = (By.CSS_SELECTOR, '.custom-radio:nth-child(3) > .custom-control-label')
    _MOBILE = (By.ID, 'userNumber')
    _DATE_OF_BIRTH_FIELD = (By.ID, 'dateOfBirthInput')
    _DATE_OF_BIRTH_MONTH_SELECT = (By.CSS_SELECTOR, '.react-datepicker__month-select')
    _DATE_OF_BIRTH_YEAR_SELECT = (By.CSS_SELECTOR, '.react-datepicker__year-select')
    _DATE_OF_BIRTH_DAY = (By.CSS_SELECTOR, '.react-datepicker__day--026')
    _SUBJECTS_FIELD = (By.CSS_SELECTOR, '.subjects-auto-complete__value-container')
    _SUBJECTS_INPUTS = (By.ID, 'subjectsInput')
    _PICTURE_BTN = (By.ID, 'uploadPicture')
    _CURRENT_ADDRES = (By.ID, 'currentAddress')
    _DROPDOWN_STATE = (By.XPATH, "//div[@id='state']/div/div")
    _DROPDOWN_CITY = (By.XPATH, '//*[@id="city"]/div/div[1]')
    _SUBNIT_BTN = (By.XPATH, '//div/button')
    _THANK_FOR_SUBMITING_TXT = (By.ID, 'example-modal-sizes-title-lg')
    _TABLE = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div/table')
    _TABLE_CLOSE_BTN = (By.ID, 'closeLargeModal')
    _ROWS = (By.CSS_SELECTOR, 'tr')
    _CELLS = (By.CSS_SELECTOR, 'td')

    def __init__(self, app):
        self.wd = app.wd
        self.app = app

    def open_site(self):
        self.wd.maximize_window()

    @allure.step("Заполнение и отправление формы")
    def fill_and_submit_form(self, data):
        """Заполняет форму данными и отправляет ее."""
        f_name, l_name = data['Student Name'].split()
        wd = self.app.wd
        self.enter_text(self._FIRST_NAME, f_name)
        self.enter_text(self._LAST_NAME, l_name)
        self.enter_text(self._EMAIL, data['Student Email'])
        self.select_gender(data['Gender'])
        self.enter_text(self._MOBILE, data['Mobile'])
        self.select_date_of_birth(data['Date of Birth'])
        self.enter_subjects(data['Subjects'])
        wd.find_element(*self._PICTURE_BTN).send_keys(f"{sys.path[0]}/data/{data['Picture']}")
        self.enter_text(self._CURRENT_ADDRES, data['Address'])
        self.select_state_city(data['State and City'])
        wd.find_element(*self._SUBNIT_BTN).click()

    @allure.step("Заполнение даты рождения")
    def select_date_of_birth(self, date_of_birth):
        """Выбирает дату рождения из календаря."""
        date_of_birth = date_of_birth.replace(',', ' ').split()
        wd = self.app.wd
        wd.find_element(*self._DATE_OF_BIRTH_FIELD).click()
        wd.find_element(*self._DATE_OF_BIRTH_MONTH_SELECT).click()
        month_option = wd.find_element(By.XPATH, f"//option[. = '{date_of_birth[1]}']")
        month_option.click()
        wd.find_element(*self._DATE_OF_BIRTH_YEAR_SELECT).click()
        year_option = wd.find_element(By.XPATH, f"//option[. = '{date_of_birth[2]}']")
        year_option.click()
        day_option = wd.find_element(By.XPATH,
                                     f"//div[contains(@class, 'react-datepicker__day') and "
                                     f"text() = '{date_of_birth[0]}']")
        day_option.click()

    @allure.step("Выбор пола")
    def select_gender(self, gender):
        """Выбирает пол студента."""
        wd = self.app.wd
        if gender == 'Male':
            wd.find_element(*self._GENDER_MALE).click()
        elif gender == 'Female':
            wd.find_element(*self._GENDER_FEMALE).click()
        else:
            wd.find_element(*self._GENDER_OTHER).click()

    @allure.step("Выбор штата и города")
    def select_state_city(self, state_and_city):
        """Выбирает штат и город проживания студента."""
        wd = self.app.wd
        state_and_city = state_and_city.split()
        wd.find_element(*self._DROPDOWN_STATE).click()
        wd.find_element(By.XPATH, f"//*[contains(text(), '{state_and_city[0]}')]").click()
        wd.find_element(*self._DROPDOWN_CITY).click()
        wd.find_element(By.XPATH, f"//*[contains(text(), '{state_and_city[1]}')]").click()

    @allure.step("Выбор предметов")
    def enter_subjects(self, subjects):
        """Выбирает предметы, которые изучает студент."""
        wd = self.app.wd
        subjects = subjects.replace(',', '').split()
        subject = wd.find_element(*self._SUBJECTS_FIELD)
        subject_input = wd.find_element(*self._SUBJECTS_INPUTS)
        subject.click()
        for i in range(len(subjects)):
            subject_input.send_keys(subjects[i])
            subject_input.send_keys(Keys.ENTER)

    @allure.step("Ввод текста")
    def enter_text(self, locator, text):
        """Вводит текст в указанное поле."""
        wd = self.app.wd
        element = wd.find_element(*locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_inner_text(self):
        """Возвращает текст элемента благодарности после отправки формы."""
        wd = self.app.wd
        element = wd.find_element(*self._THANK_FOR_SUBMITING_TXT)
        return element.text

    @allure.step("Полчение данных из таблицы")
    def get_table_and_close_table(self):
        """Возвращает данные из таблицы на странице."""
        wd = self.app.wd
        table_data = {}
        rows = wd.find_elements(*self._ROWS)
        for row in rows:
            cells = row.find_elements(*self._CELLS)
            if len(cells) == 2:
                key = cells[0].text.strip()
                value = cells[1].text.strip()
                table_data[key] = value
                if key == "State and City":
                    break
        allure.attach(str(table_data), name="Table", attachment_type=allure.attachment_type.TEXT)
        wd.find_element(*self._TABLE_CLOSE_BTN).click()
        return table_data
