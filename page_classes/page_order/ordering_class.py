# Создаем базовый класс страниц, для проверки работы заказов билетов.

# Импортируем необходимые пакеты, для нашего тестирования.
import math
import random
import time

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
from selenium.common.exceptions import WebDriverException

# Создаем тестовые браузеры, с помощью Selenium Web Driver. Можете выбрать проверку или в FF Mozilla или в Google
# Chrome. По умолчанию установлен Google Chrome(v.75). Другие релизы для Chrome, можно посмотреть здесь -
# https://sites.google.com/a/chromium.org/chromedriver/downloads.

# 1. Тестовый браузер FF Mozilla.
# my_driver = Firefox()
# 2. Тестовый браузер Google Chrome.
# my_driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
my_driver = webdriver.Chrome()

# Открываем браузер во весь экран.
my_driver.maximize_window()

'''
# Тестирование мобильной версии сайта. Создаем тестовое мобильное устройство.

from selenium.webdriver.chrome.options import Options

mobile_emulation = {

    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, "
                 "like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

chrome_options = Options()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

my_driver = webdriver.Chrome(chrome_options = chrome_options)
'''

# Создаем базовый класс, с необходимыми свойствами и методами. Для тестирования, на тестовом сайте.

class DriverHandlingPage(BasePage):
    # Метод инициализирующий dev-сайт.
    def __init__(self, *args, **kwargs):
        super(DriverHandlingPage, self).__init__(url='https://testsite.com/', *args, **kwargs)

    # Находим необходимые для работы переходов между страницами, ссылки.
    cart_link = Find(by=By.XPATH, value="//a[@class='cart-bottom__order inline-top']")
    main_link = Find(by=By.XPATH, value="//a[@href='/']")

    # Выбираем случайно какое-либо событие на главной странице сайта. В диапазоне 20 событий. Запуская несколько раз
    # данный тест, можно потестировать, случайные события на главной.
    def random_event(self):
        random_number = random.randint(1, 20)
        join_link = Find(by=By.XPATH, value="//div[@class='afishaList complete']//div[@class='date__content'][" + str(
            random_number) + "]//div["
                             "@class='date__text inline-top']/a", context=self)
        join_link.click()

    # Находим кнопку "Выбрать билеты", на странице события, если она там есть. Если кнопки нет, то возвращаемся
    # обратно на главную и ищем другое событие.
    def link_is_present(self):
        try:
            ticket_link = Find(by=By.XPATH, value="//div[@class='performance__ticket']/a", context=self)
            ticket_link.click()
        except:
            print("Возможная причина прерывания теста, из-за того, что к данному событию нет билетов, а есть "
                  "кнопка 'Оставить "
                  "заявку.")

    # Метод находящий через XPATH, активные элементы на странице схемы, в том числе и в событиях с вложенными
    # секторами. И выбирающий их. Если экран перекрывает окно "Танцевальный партер", закрываем его.
    def click_active(self):
        try:
            active_xpath_nesting = my_driver.find_element_by_xpath("//svg:g[@class='active']")
            time.sleep(2)
            ActionChains(my_driver).move_to_element(active_xpath_nesting).perform()
            time.sleep(5)
            active_xpath_nesting.click()

            time.sleep(3)
            active_xpath = "//*[name()='svg']//*[name()='path' and @class='active' or name()='circle' and " \
                           "@class='active'] "
            active = Find(by=By.XPATH, value=active_xpath, context=self)
            active.click()
        except:
            try:
                active_xpath = "//*[name()='svg']//*[name()='path' and @class='active' or name()='circle' and " \
                               "@class='active'] "
                active = Find(by=By.XPATH, value=active_xpath, context=self)
                active.click()
            except:
                url = my_driver.current_url
                print("Возможная причина прерывания теста в событии: " + str(
                    url) + "из-за того, что на схеме нет билетов "
                           "или они перекрываются другими "
                           "элементами.")
                try:
                    my_driver.execute_script("alert('Возможные причины прерывания теста в данном событии: 1. В событии "
                                             "нет схемы с билетами, а есть только список. 2. На схеме нет "
                                             "билетов. 3. Схема перекрывается другими элементами(например: popup и т.д.) "
                                             "4. Событие отменено. Запустите тест еще раз.');").accept()
                except WebDriverException:
                    pass

    # Метод показывающий тултип, с добавленными билетами, внизу страницы.
    def hovered_cart(self):
        ticket_hovered = my_driver.find_element_by_xpath("//div[@class='cart_bot__counter']/span")
        ActionChains(my_driver).move_to_element(ticket_hovered).perform()

    # Метод переключающий со схемы на список
    def switch_list(self):
        ticket_hovered = my_driver.find_element_by_xpath("//div[@data-test='list-scenario']")
        ticket_hovered.click()

    # Метод показывающий билеты в первом аккордеоне списка.
    def button_show_tickets(self):
        button_show = my_driver.find_element_by_xpath("//div[@class='inline-top map__show-more']")
        button_show.click()

    # Метод нажимающий на кнопку "Показать места", в первом аккордеоне списка.
    def show_locations(self):
        href_locations = my_driver.find_element_by_xpath(
            "//div[@class='inline-top row__show']/span[@data-test='list-row']")
        href_locations.click()

    # Метод отмечающий 2 чекбокса, в выпадающем списке выбранного аккордеона.
    def check_tickets(self):
        try:
            check_ticket = my_driver.find_element_by_xpath(
                "//div[@data-test='list-seat']/input[@type='checkbox' and not(@class)]/following-sibling::label")
            check_ticket.click()
        except:
            my_driver.execute_script("alert('В указанном списке больше нет чекбоксов для выбора');").accept()

    # Метод находящий через XPATH, значок удалить на странице Корзины и нажимающий на него.
    def click_cart(self):
        cart_xpath = "//div[@class='delete_from_cart cart__close inline-top']/*[name()='svg']"
        cart = Find(by=By.XPATH, value=cart_xpath, context=self)
        cart.click()
