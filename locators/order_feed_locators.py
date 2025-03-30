from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    order_feed_list = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list__OLh59')]//p[contains(@class, 'text_type_digits-default')]")

    first_order_block = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_list')]/li[contains(@class, 'OrderHistory_listItem')][1]//a[contains(@class, 'OrderHistory_link')]"
    )

    modal_window_order = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]/div[contains(@class, 'Modal_modal__container')]"
    )

    order_number_in_feed = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default') and contains(text(), '{}')]")


    order_completed_total = (By.XPATH, "//p[contains(@class, 'text_type_digits-large')]")

    order_completed_today = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )

    orders_in_progress = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li[contains(@class, 'text_type_digits-default')]"
    )
    