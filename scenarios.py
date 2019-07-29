import components
from time import sleep


def set_up(driver):
    components.sign_in(driver)
    driver.implicitly_wait(5)
    components.select_adaptive(driver)
