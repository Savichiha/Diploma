import allure
from selenium.webdriver.common.by import By


class MainPage:
      def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.chitai-gorod.ru/")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    
      with allure.step("Поиск книги на кириллице"):
           def rus_search(self,term):
               self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
               self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
               txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
               return txt

      with allure.step("Поиск книги на латинице"):
          def eng_search(self,term):
              self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
              self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
              txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
              return txt
    
      with allure.step("Пустой поиск"):
          def empty_search(self,term):
              self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
              self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
       
      with allure.step("Поиск сразу нескольких книг"):
            def books_search(self,term):
                self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
                self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
                txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
                return txt
      
      with allure.step("Поиск по категории"):
          def series_search(self,term):
              self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term)
              self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
              txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
              return txt
                  
      
      with allure.step("Закрытие веб-браузера"):
            def close_driver(self):
                self._driver.quit()