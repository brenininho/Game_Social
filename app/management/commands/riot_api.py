from django.core.management import BaseCommand
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from app.models import Account


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        path = "/home/breno/Área de Trabalho/Python Projects/GameAnalytics/chromedriver"
        page = 'https://developer.riotgames.com/apis#account-v1'
        chrome_option = Options()
        # chrome_option.add_argument("--headless")
        # chrome_option.add_argument("--no-sadbox")
        # chrome_option.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(path, options=chrome_option)
        driver.get(page)
        name = driver.find_element(By.CLASS_NAME, "navbar-brand-text")
        print(f"Welcome {name.text}")
        login_button = driver.find_element(By.CLASS_NAME, "navbar-avatar")
        login_button.click()
        sleep(3)
        username_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/input")
        username_input.send_keys("eoroico")
        username_input.get_attribute("value")
        password_input = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/input")
        password_input.send_keys("0b17h3k2yb14")
        sleep(5)
        submit_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/button")
        submit_button.click()
        WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.XPATH, '//*[@id="_getByRiotId"]/div[1]/span[2]/a')))
        account_by_game_name_api = driver.find_element(By.XPATH, '//*[@id="_getByRiotId"]/div[1]/span[2]/a')
        account_by_game_name_api.click()
        WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.NAME, "tagLine")))
        sleep(5)
        tag_line = driver.find_element(By.NAME, 'tagLine')
        tag_line.send_keys("BR1")
        game_name = driver.find_element(By.NAME, 'gameName')
        game_name.send_keys("brenininho2")
        WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.NAME, "tagLine")))
        import ipdb;
        ipdb.set_trace()
        execute_request = driver.find_element(By.ID, 'execute_account-v1_GET_getByRiotId')
        execute_request.click()






