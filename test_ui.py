import allure
import pytest
from selenium import webdriver
from main_page import MainPage


@allure.title("Поиск на кириллице")
@allure.description("Тест проверяет поиск книги на русском языке")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_rus_search(chrome_browser):
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):

        main_page = MainPage(chrome_browser)
        text = main_page.rus_search('Капитанская дочка')
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:52] == "Показываем результаты по запросу «капитанская дочка»"

@allure.title("Поиск на латинице")
@allure.description("Тест проверяет поиск книги на английском языке")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_eng_search(chrome_browser):
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):

         main_page = MainPage(chrome_browser)
         text = main_page.eng_search('Harry Potter and the philosophers stone')
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:74] == "Показываем результаты по запросу «harry potter and the philosophers stone»"

@allure.title("Пустой поиск")
@allure.description("Тест проверяет выполнение пустого поиска")
@allure.feature("READ")
@allure.severity("trivial")
@pytest.mark.negative_test
def test_empty_search(chrome_browser):
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
         main_page = MainPage(chrome_browser)
         main_page.empty_search("")
    with allure.step("Отсутствие действия на сайте"):
         url = chrome_browser.current_url
    assert url == "https://www.chitai-gorod.ru/"

@allure.title("Поиск по двум книгам")
@allure.description("Тест проверяет корректное выполнение поиска сразу по нескольким книгам")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_books_search(chrome_browser):
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):

        main_page = MainPage(chrome_browser)
        text = main_page.books_search('Бесприданница, Золушка')
    with allure.step("Проверка текста с результатами поиска на странице "):
        assert text[0:56] == "Показываем результаты по запросу «бесприданница золушка»"

@allure.title("Поиск по категории")
@allure.description("Тест проверяет корректное выполнение поиска по категории книг")
@allure.feature("READ")
@allure.severity("critical")
@pytest.mark.positive_test
def test_series_search(chrome_browser):
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        main_page = MainPage(chrome_browser)
        text = main_page.series_search('Книги для детей')
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert text[0:50] == "Показываем результаты по запросу «книги для детей»"
