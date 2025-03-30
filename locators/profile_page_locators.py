from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Локатор для кнопки "История заказов" на странице профиля
    order_history_button = (By.XPATH, "//a[contains(@href, '/account/order-history') and contains(@class, 'Account_link')]")

    order_history_list = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList__374GU')]//li")
    last_order_number = (By.XPATH,
                         "//ul[contains(@class, 'OrderHistory_profileList__374GU')]//li[last()]//p[contains(@class, 'text_type_digits-default')]")

    # Локатор для кнопки "Выход" на странице профиля
    logout_button = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']")
