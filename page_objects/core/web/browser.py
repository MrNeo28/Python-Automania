"""
contains browser specific objects
"""
from selenium.webdriver.remote.webdriver import WebDriver


class Browser:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate_url(self, url: str):
        self.driver.get(url)

    def maximize_window(self):
        self.driver.maximize_window()

    @property
    def get_title(self) -> str:
        return self.driver.title
    
    @property
    def get_current_url(self) -> str:
        return self.driver.current_url

    @property
    def get_nums_tabs(self) -> int:
        return len(self.driver.window_handles)
    
    def go_forward(self):
        self.driver.forward()
    
    def go_backward(self):
        self.driver.back()

    def refresh_page(self):
        self.driver.refresh()

    def close_window(self):
        self.driver.close()
    
    def quit_session(self):
        self.driver.quit()

    def maximize_window(self):
        self.driver.maximize_window()

    def minimize_window(self):
        self.driver.minimize_window()

    def set_fullscreen_window(self):
        self.driver.fullscreen_window()