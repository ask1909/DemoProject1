from selenium.webdriver import Chrome
import json


class BDriver(Chrome):
    with open('../Resources/DriverConfig.json', 'r') as fp:
        data = json.load(fp)

    exe_path = data['exe_path']

    def __init__(self, url):
        Chrome.__init__(self, executable_path=BDriver.exe_path)
        self.url = url
        self.maximize_window()
        self.get(self.url)

    def driver_close(self):
        self.close()
