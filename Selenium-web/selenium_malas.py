#OWNER johan

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
import time
import random
import multiprocessing

url = "https://enrichment.apps.binus.ac.id/Login"

first_name = "johan"
last_name = "tandy"
email = ""
telephone = ""
identity_id = ""
ticket_name = "CAT 2B"
dob_day = "18"
dob_month = "11"
dob_year = "1996"

class loket_bot(multiprocessing.Process):
    
    def __init__(
        self,
        url: str,
        name
    ):
        multiprocessing.Process.__init__(self)
        self.url = url
        print("Browser",name,"Started")
    
    def load_webdriver(self):
        self.driver = webdriver.Chrome()

    def load_page(self):
        self.driver.get(self.url) 

    def retry_mechanism(self):
        self.driver.delete_all_cookies()
        self.load_page()

    def run(self):
        self.load_webdriver()
        self.load_page()
        while True:

            try:
                public_sale_button = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//span[text()="BUY TICKETS"]'))
                )
                
            except NoSuchElementException as e :
                print(e)
                self.retry_mechanism()
                continue
            except TimeoutException as e:
                print(e)
                self.retry_mechanism()
                continue
            
            # rando = random.choices([0,1], weights=(2, 98), k=1)
            # print(rando)
            # if rando[0] == 1:
            try:
                public_sale_button.click()
            except ElementClickInterceptedException as e:
                print(e)
                time.sleep(random.uniform(0.4, 1.2))
                self.load_page()
                continue
            # else :
            #     self.driver.get("file:///Users/johan.tandy/Downloads/loket/Loket.com.html")

            try:
                join_button = WebDriverWait(self.driver, 86400).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR,'#join-btn'))
                        )
                join_button.click()
                print("join queue clicked !!")
            except Exception as e :
                print(e)

            try:
                select_element =  WebDriverWait(self.driver, 86400).until(
                                        EC.presence_of_element_located((By.CSS_SELECTOR, f'div[ticket-name="{ticket_name}"] select.ticket-types')))
                self.driver.execute_script("arguments[0].scrollIntoView();", select_element)
                time.sleep(0.2)
                select = Select(select_element)
                select.select_by_value('2')

                time.sleep(0.1)
                WebDriverWait(self.driver, 10).until(
                                        EC.presence_of_element_located((By.ID, 'buy_ticket'))).click()

                WebDriverWait(self.driver, 10).until(
                                        EC.presence_of_element_located((By.ID, 'btn-agree-tnc'))).click()

                WebDriverWait(self.driver, 10).until(
                                        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="firstname"]'))).click()

                self.driver.find_element(By.CSS_SELECTOR, 'input[name="firstname"]').send_keys(first_name)
                self.driver.find_element(By.CSS_SELECTOR, 'input[name="lastname"]').send_keys(last_name)
                self.driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys(email)
                self.driver.find_element(By.CSS_SELECTOR, 'input[name="telephone"]').send_keys(telephone)
                self.driver.find_element(By.CSS_SELECTOR, 'input[name="identity_id"]').send_keys(identity_id)

                self.driver.find_element(By.NAME, 'dob_day').send_keys('1')
                Select(self.driver.find_element(By.NAME, 'dob_day')).select_by_value(dob_day)
                Select(self.driver.find_element(By.NAME, 'dob_month')).select_by_value(dob_month)
                Select(self.driver.find_element(By.NAME, 'dob_year')).select_by_value(dob_year)

                gender_radio = self.driver.find_element(By.NAME, 'gender')
                self.driver.execute_script("arguments[0].scrollIntoView();", gender_radio)
                time.sleep(0.2)
                gender_radio.click()

                btn_register = self.driver.find_element(By.ID, 'btn-register')
                self.driver.execute_script("arguments[0].scrollIntoView();", btn_register)
                time.sleep(0.2)
                # btn_register.click()

                # WebDriverWait(self.driver, 10).until(
                #                         EC.presence_of_element_located((By.XPATH, '//h5[text()=" Virtual Account "]'))).click()
                # WebDriverWait(self.driver, 10).until(
                #                         EC.presence_of_element_located((By.XPATH, '//h6[text()=" Virtual Account BCA "]'))).click()

                # lanjut_button = self.driver.find_element(By.XPATH, '//button[text()=" Lanjut "]')
                # self.driver.execute_script("arguments[0].scrollIntoView();", lanjut_button)
                # time.sleep(0.2)
                # lanjut_button.click()

                # WebDriverWait(self.driver, 10).until(
                #                         EC.presence_of_element_located((By.XPATH, '//button[text()=" OK "]'))).click()

                # bayar_sekarang = WebDriverWait(self.driver, 10).until(
                #                         EC.presence_of_element_located((By.XPATH, '//button[text()="Bayar Sekarang"]')))

                # self.driver.execute_script("arguments[0].scrollIntoView();", bayar_sekarang)
                # time.sleep(0.2)
                # bayar_sekarang.click()
                
            except Exception as e:
                print(e)

            
            break

if __name__ == '__main__':
    browsers = []
    for i in range(1):
        browsers.append(loket_bot(url=url,name=i))

    for browser in browsers:
        browser.start()