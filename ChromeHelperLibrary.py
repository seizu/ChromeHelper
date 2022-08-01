from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from SeleniumLibrary.base import keyword, LibraryComponent
from SeleniumLibrary.locators import WindowManager
from SeleniumLibrary.keywords.webdrivertools import WebDriverCreator

__version__ = '0.0.1'

class ChromeHelperLibrary(LibraryComponent):
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self._window_manager = WindowManager(ctx)
        self._webdriver_creator = WebDriverCreator(self.log_dir)

    @keyword
    def attach_chrome(self, chrome_driver, debugger_address="127.0.0.1:9222", log_path=None):
        service = Service(executable_path=chrome_driver, log_path=log_path)
        options = webdriver.ChromeOptions()
        setattr(options, "debugger_address", debugger_address)
        #options.debugger_address = debugger_address
        driver = webdriver.Chrome(service=service, options=options)
        driver = self._wrap_event_firing_webdriver(driver)
        return self.ctx.register_driver(driver, None)

    def _wrap_event_firing_webdriver(self, driver):
        if not self.ctx.event_firing_webdriver:
            return driver
        self.debug("Wrapping driver to event_firing_webdriver.")
        return EventFiringWebDriver(driver, self.ctx.event_firing_webdriver())
