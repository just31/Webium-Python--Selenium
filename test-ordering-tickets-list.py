# Тестируем заказ билетов из списков. Из событий с главной страницы.
import sys

sys.path.append("page_classes/page_order/")
from ordering_class import *

# Точка входа в тест. Вызов методов базового класса из папки page_classes/page_order/. Работа со страницами сайта.
if __name__ == '__main__':
    start = time.time()
    page = DriverHandlingPage(driver=my_driver)
    # Открываем наш dev-сайт https://i-vasiliev.com/, указанный в __init__, в DriverHandlingPage.
    page.open()
    # Выбираем случайное тестовое событие с главной страницы, добавленное через Xpath в переменную join_link.
    time.sleep(3)
    page.random_event()
    # На странице выбранного события, нажимаем кнопку "Выбрать билеты". Если она там есть, иначе будет ошибка в тесте.
    time.sleep(3)
    page.link_is_present()
    # Переключаемся со схемы на список.
    time.sleep(3)
    page.switch_list()
    # Показываем билеты в первом аккордеоне списка.
    time.sleep(3)
    page.button_show_tickets()
    # Нажимаем на кнопку "Показать места", в первом аккордеоне списка.
    time.sleep(3)
    page.show_locations()
    # Пробуем отметить 1 чекбокс, в выпадающем списке выбранного аккордеона.
    time.sleep(3)
    page.check_tickets()
    # Показываем тултип, с добавленными билетами, внизу страницы.
    time.sleep(3)
    page.hovered_cart()
    # Переходим на страницу корзины.
    time.sleep(5)
    page.cart_link.click()
    # Удаляем 1 добавленный билет из корзины.
    time.sleep(5)
    page.click_cart()
    # Удаляем 2 добавленных билета из корзины, end.
    time.sleep(3)
    # Переходим на главную страницу.
    page.main_link.click()
    time.sleep(3)
    # Выключаем тестовый браузер.
    my_driver.quit()
    # Посчитаем сколько времени занял наш тест.
    finish = time.time()
    result = finish - start
    print("Тест занял: " + str(math.floor(result)) + " секунд(ы).")