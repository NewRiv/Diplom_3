from selenium.webdriver.common.by import By

class MainPageLocators:
    # Локатор для кнопки "Личный кабинет" на главной странице
    account_button = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and @href='/account']")

    # Локатор для кнопки “Конструктор” на странице авторизации
    constructor_button = (
    By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and .//p[text()='Конструктор']]")

    # Проверка на наличие заголовка "Соберите бургер"
    burger_title = (By.XPATH, "//h1[text()='Соберите бургер']")

    # Локатор для заголовка “Соберите бургер” на странице конструктора
    build_burger_header = (
    By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients__1N8v2')]//h1[text()='Соберите бургер']")

    # Локатор для кнопки “Лента заказов” на главной странице
    feed_button = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and .//p[text()='Лента Заказов']]")

    # Локатор для ингредиента “Флюоресцентная булка R2-D3”
    ingredient_item = (By.XPATH,
                       "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6') and .//p[text()='Флюоресцентная булка R2-D3']]")

    # Локатор для модального окна “Детали ингредиента”
    modal_ingredient = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")

    # Локатор для кнопки закрытия (крестик) в модальном окне ингредиента
    modal_close_ingredient_button = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")

    #Локатор для зоны «Выбранные ингредиенты»
    droppable_area = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")

    # Локатор для счетчика ингредиента
    ingredient_counter = (
    By.XPATH, "//div[contains(@class, 'counter_counter__ZNLkj')]//p[@class='counter_counter__num__3nue1']")

    # Локатор для кнопки “Оформить заказ”
    order_button = (By.XPATH,
                    "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_large__G21Vg')]")

    # Локатор для модального окна “Индикатор заказа”
    order_indicator_modal = (By.XPATH,
                             "//div[contains(@class, 'Modal_modal__container__')]")

    # Локатор для кнопки закрытия (крестик) в модальном окне заказа
    modal_close_order_button = (By.XPATH,
    "//button[contains(@class, 'Modal_modal__close') and @type='button']")


    order_number_modal = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') and contains(@class, 'text_type_digits-large')]"
    )

    # Локатор для кнопки “Войти в аккаунт”
    login_button = (By.XPATH,
                    "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_large__G21Vg')]")
    