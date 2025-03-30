class UrlsSiteData:
    BASE_URL = "https://stellarburgers.nomoreparties.site" # Она же и страница с конструктором заказа

    main_url = f"{BASE_URL}/" # Главная страница
    order_feed_url = f"{BASE_URL}/feed"
    login_url = f"{BASE_URL}/login"
    forgot_password_url = f"{BASE_URL}/forgot-password"
    reset_password_url = f"{BASE_URL}/reset-password"
    profile_url = f"{BASE_URL}/account/profile"
    order_history_url = f"{BASE_URL}/account/order-history"