import allure
from locators.main_page_locators import MainPageLocators
from data.urls_site_data import UrlsSiteData
from selenium.common.exceptions import ElementClickInterceptedException
from page_objects.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_url(UrlsSiteData.main_url)

    @allure.step("Ожидание загрузки главной страницы")
    def wait_main_page(self):
        self.wait_for_url(UrlsSiteData.main_url)

    @allure.step("Проверка перехода на главную страницу")
    def is_on_main_page(self):
        return self.is_current_url(UrlsSiteData.main_url)

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_account_button(self):
        self.click(MainPageLocators.account_button)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.constructor_button)

    @allure.step("Проверка отображения блока 'Соберите бургер'")
    def is_burger_header_displayed(self):
        return self.is_element_displayed(MainPageLocators.burger_title)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_order_feed(self):
        self.click(MainPageLocators.feed_button)

    @allure.step("Клик по ингредиенту 'Флюоресцентная булка R2-D3'")
    def open_ingredient_modal(self):
        self.click(MainPageLocators.ingredient_item)

    @allure.step("Проверка открытие модального окна ингредиента")
    def is_modal_ingredient_displayed(self):
        return self.is_element_displayed(MainPageLocators.modal_ingredient)

    @allure.step("Проверка закрытия модального окна ингредиента")
    def is_modal_ingredient_closed(self):
        return self.is_element_not_displayed(MainPageLocators.modal_ingredient)

    @allure.step("Закрытие модального окна ингредиента")
    def close_modal_ingredient(self):
        self.click(MainPageLocators.modal_close_ingredient_button)

    @allure.step("Перетаскиваем ингредиент в зону 'Выбранные ингредиенты'")
    def add_ingredient_to_order(self):
        self.drag_and_drop(MainPageLocators.ingredient_item, MainPageLocators.droppable_area)

    @allure.step("Получение количества добавленных ингредиентов")
    def get_ingredient_count(self):
        return int(self.get_text(MainPageLocators.ingredient_counter))

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_order_button(self):
        self.click(MainPageLocators.order_button)

    @allure.step("Проверка отображения модального окна 'Индикатор заказа'")
    def is_modal_order_displayed(self):
        return self.is_element_displayed(MainPageLocators.order_indicator_modal)

    @allure.step("Закрытие модального окна заказа")
    def close_modal_order(self):
        self.wait_until_visible(MainPageLocators.modal_close_order_button)

        # Проверяем, что кнопка закрытия не перекрыта и доступна для клика
        is_clicked = False
        while not is_clicked:
            try:
                # Пробуем кликнуть на кнопку
                self.click(MainPageLocators.modal_close_order_button)
                is_clicked = True  # Если клик успешен, устанавливаем флаг
#                break
            except ElementClickInterceptedException:
                # Если элемент все еще перекрыт, ждем перед повторной попыткой
                self.wait_until_visible(MainPageLocators.modal_close_order_button)

    @allure.step("Проверка отсутствия модального окна заказа")
    def is_modal_order_not_displayed(self):
        return self.is_element_not_displayed(MainPageLocators.order_indicator_modal)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        # Ожидание появления номера заказа в модальном окне
        self.wait_until_visible(MainPageLocators.order_number_modal)

        # Ожидание, пока номер заказа изменится с заглушки "9999" на другой номер
        order_number_element = self.find_element(MainPageLocators.order_number_modal)
        self.wait_for_condition(lambda driver: order_number_element.text != "9999")

        return order_number_element.text

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_button(self):
        self.click(MainPageLocators.login_button)
