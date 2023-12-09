import logging
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options

gecko_driver_path = 'C:\\Users\\Jesus\\Desktop\\projetoA\\valoresApartamentosRegiao\\firefoxdriver-win64\\geckodriver.exe'
firefox_options = Options()
#options.add_argument("--headless")  # Ativa o modo headless
firefox_service = FirefoxService(executable_path=gecko_driver_path)
driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
driver.get('google.com')