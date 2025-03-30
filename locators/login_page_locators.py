from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Локатор для кнопки "Восстановить пароль" на странице авторизации
    restore_password_button = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")

    # Локатор для поля ввода email на странице восстановления пароля
    email_input = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='text']")

    # Локатор для поля пароля на странице сброса пароля
    password_input = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='password']")

    # Локатор для кнопки "Войти" на странице авторизации
    login_button = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']")

    # Локатор для кнопки "Восстановить" на странице восстановления пароля
    restore_button = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Восстановить']")

    # Локатор для значка "Показать/Скрыть пароль" на странице сброса пароля
    toggle_password_visibility = (By.XPATH, "//div[contains(@class, 'input__icon') and contains(@class, 'input__icon-action')]")

    password_field = (By.CLASS_NAME, "input")

    toggle_password_visibility_button = (By.CLASS_NAME, "input__icon-action")
