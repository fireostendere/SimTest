import json
import sys
import allure

'''Берём данные для формы'''
with open(f"{sys.path[0]}/data/dataform.json", 'r') as file:
    data = json.load(file)


@allure.feature('Form page')
@allure.story('Validation')
@allure.title('Validation of title and table ellements')
def test_fill_form_and_check_confirmation(app):
    # Открываем страницу с формой
    practice_form_page = app.open_practice_form_page()
    # Заполняем форму данными
    practice_form_page.fill_and_submit_form(data)
    app.take_screenshot("form_screenshot")
    assert practice_form_page.get_inner_text() == 'Thanks for submitting the form'
    actual_data = practice_form_page.get_table_and_close_table()
    assert actual_data == data, f"Actual data {actual_data} does not match expected data"
