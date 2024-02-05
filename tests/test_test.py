# Задаем данные для заполнения формы
data = {
    'Student Name': "Aleksandr Alekseev",
    'Student Email': "fireostendere@gmail.com",
    'Gender': "Male",
    'Mobile': "8904119618",
    'Date of Birth': "12 January,2024",  # Обратите внимание на формат даты
    'Subjects': "Maths, Biology",
    'Hobbies': '',
    'Picture': "SimbirSoft.png",
    'Address': "Улица Пушкина, дом 83, квартира 89",
    'State and City': "Haryana Panipat"
  }

def test_fill_form_and_check_confirmation(app):
    # Открываем страницу с формой
    practice_form_page = app.open_practice_form_page()

    # Заполняем форму данными
    practice_form_page.fill_and_submit_form(data)
    actual_data = practice_form_page.get_table()
    assert practice_form_page.get_inner_text() == 'Thanks for submitting the form'
    assert actual_data == data, f"Actual data {actual_data} does not match expected data"
