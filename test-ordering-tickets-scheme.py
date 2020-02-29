# Тестируем заказ билетов со схем. Из событий с главной страницы.
import sys

sys.path.append("page_classes/page_order/")
from ordering_class import *

# Точка входа в тест. Вызов методов базового класса из папки page_classes/page_order/. Работа со страницами сайта.
if __name__ == '__main__':
    start = time.time()
    page = DriverHandlingPage(driver=my_driver)
    # Открываем наш сайт указанный в __init__, в DriverHandlingPage.
    page.open()
    # Выбираем случайное тестовое событие с главной страницы, добавленное через Xpath в переменную join_link.
    time.sleep(3)
    page.random_event()
    # На странице выбранного события, нажимаем кнопку "Выбрать билеты". Если она там есть, иначе будет ошибка в тесте.
    time.sleep(3)
    page.link_is_present()
    # Выбираем 2 билета со схемы. Скроллим страницу вниз, чтобы схема была лучше видна.
    time.sleep(3)
    my_driver.execute_script("window.scrollTo(0, window.scrollY + 250)")
    page.click_active()
    time.sleep(3)
    page.click_active()
    # Выбираем 3 билета со схемы, end.
    time.sleep(3)
    # Показываем тултип, с добавленными билетами, внизу страницы.
    page.hovered_cart()
    time.sleep(5)
    # Переходим на страницу корзины.
    page.cart_link.click()
    # Удаляем 3 добавленных билета из корзины.
    time.sleep(5)
    page.click_cart()
    time.sleep(3)
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
