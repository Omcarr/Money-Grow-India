from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Secure import Url, login_id, pass_word, download_loc

class Features():
    def __init__(self):
        self.url = Url
        self.login_id = login_id
        self.pass_word = pass_word

        # download location to be changed from here
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('prefs', {
            "download.default_directory": download_loc,
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True})
        self.driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()), options=self.options)

    # fill the login form
    def login(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(40)

        username = self.driver.find_element(
            By.XPATH, '/html/body/div/div[1]/div/div[1]/form/fieldset/div[1]/div/input')
        username.send_keys(login_id)

        password = self.driver.find_element(
            By.XPATH, '/html/body/div/div[1]/div/div[1]/form/fieldset/div[2]/div/input')
        password.send_keys(pass_word)

        login_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[1]/div/div[1]/form/fieldset/div[3]/input')))
        login_btn.click()


  # CSV download
    def CSVdownloader(self):
        # back office queries click
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="boQueryLeftMenu"]/a')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="queryFile"]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="queryFile"]/option[2]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="output"]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="output"]/option[1]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="myTabContent"]/div/div[7]/div/button')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr/td[3]/a')))
        cursor.click()

    #Can't be custom dated
    def FactSheet(self, client_id,end_date):
        # click on reports
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[1]/div/ul/li[3]/a')))
        cursor.click()

        # Report Factsheet is by default selected

        #as on date option here
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="toDateUI"]')))
        cursor.clear()
        cursor.send_keys(Keys.ENTER)
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="toDateUI"]')))
        cursor.send_keys(end_date)

        # click on scope dropdown list
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="myTabContent"]/div/div[5]/div/div[1]')))
        cursor.click()
        # choose account from the dropdown
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[1]/select/option[5]')))
        cursor.click()
        # scope selector
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[2]/div/a/span[1]')))
        cursor.click()
        # enters the account id
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/input')))
        cursor.send_keys(client_id)
        # final selection tap
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/ul/li/div')))
        cursor.click()
        # user id passed to generate the pdf
        cursor = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="myTabContent"]/div/div[10]/div/div[1]/button')))
        cursor.click()
        # to handle no data error
        try:
            cursor = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/a/i')))
            cursor.click()
        except:
            pass
   
    def CurrentPortfolio(self, client_id,end_date):
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[1]/div/ul/li[3]/a')))
        cursor.click()
        report = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div/div')))
        report.click()
        # report dropdown

        report = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div/div/div/ul/li[3]')))
        report.click()

        #clear the date
        report = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="toDateUI"]')))
        report.clear()
        report.send_keys(Keys.ENTER)

        report = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="toDateUI"]')))
        report.send_keys(end_date)

        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="myTabContent"]/div/div[5]/div/div[1]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[1]/select/option[5]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[2]/div/a/span[1]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/input')))
        cursor.send_keys(client_id)
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/ul/li/div')))
        cursor.click()

        # Execute
        cursor = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[15]/div/div[1]/button')))
        cursor.click()
        try:
            cursor = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/a/i')))
            cursor.click()
        except:
            pass

    def TransactionStatement(self, client_id, start_date, end_date, CustomDate):
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[1]/div/ul/li[3]/a')))
        cursor.click()
        report = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div/div')))
        report.click()
        # report dropdown
        report = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div/div/div/ul/li[4]')))
        report.click()
     
        if CustomDate==True:
        # DATE setter
            cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div/div[1]/input')))
            cursor.clear()
            cursor.send_keys(start_date)
            cursor.send_keys(Keys.ENTER)

            cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div/div[2]/input')))
            cursor.clear()
            cursor.send_keys(end_date)
            cursor.send_keys(Keys.ENTER)
            # date setting ends

        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="myTabContent"]/div/div[5]/div/div[1]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[1]/select/option[5]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[2]/div/a/span[1]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/input')))
        cursor.send_keys(client_id)
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/ul/li/div')))
        cursor.click()

        # Execute
        cursor = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[16]/div/div[1]/button')))
        cursor.click()
        try:
            cursor = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/a/i')))
            cursor.click()
        except:
            pass

    def BankBook(self, client_id, start_date, end_date,CustomDate):
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[1]/div/ul/li[3]/a')))
        cursor.click()
        report = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div/div')))
        report.click()
        # report dropdown
        report = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div/div/div/ul/li[5]')))
        report.click()
        
        if CustomDate==True:
            # DATE setter
            cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div/div[1]/input')))
            cursor.clear()
            cursor.send_keys(start_date)
            cursor.send_keys(Keys.ENTER)

            cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div/div[2]/input')))
            cursor.clear()
            cursor.send_keys(end_date)
            cursor.send_keys(Keys.ENTER)
            # date setting ends
       
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="myTabContent"]/div/div[5]/div/div[1]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[1]/select/option[5]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[2]/div/a/span[1]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/input')))
        cursor.send_keys(client_id)
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/ul/li/div')))
        cursor.click()
        # Execute

        cursor = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[10]/div/div[1]/button')))
        cursor.click()
        try:
            cursor = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/a/i')))
            cursor.click()
        except:
            pass


    def StatementOfDividend(self, client_id, start_date, end_date,CustomDate):
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[1]/div/ul/li[3]/a')))
        cursor.click()
        report = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div/div')))
        report.click()
        # report dropdown
        report = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div/div/div/ul/li[6]')))
        report.click()
        
        if CustomDate==True:
            # DATE setter
            cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div/div[1]/input')))
            cursor.clear()
            cursor.send_keys(start_date)
            cursor.send_keys(Keys.ENTER)

            cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div/div[2]/input')))
            cursor.clear()
            cursor.send_keys(end_date)
            cursor.send_keys(Keys.ENTER)
            # date setting ends

        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="myTabContent"]/div/div[5]/div/div[1]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[1]/select/option[5]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[2]/div/a/span[1]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/input')))
        cursor.send_keys(client_id)
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/ul/li/div')))
        cursor.click()

        # Execute
        cursor = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[15]/div/div[1]/button')))
        cursor.click()
        try:
            cursor = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/a/i')))
            cursor.click()
        except:
            pass

    def StatementOfExpense(self, client_id, start_date, end_date,CustomDate):
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[1]/div/ul/li[3]/a')))
        cursor.click()
        report = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div/div')))
        report.click()
        # report dropdown
        report = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div/div/div/ul/li[7]')))
        report.click()
        
        if CustomDate==True:
            # DATE setter
            cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div/div[1]/input')))
            cursor.clear()
            cursor.send_keys(start_date)
            cursor.send_keys(Keys.ENTER)

            cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div/div[2]/input')))
            cursor.clear()
            cursor.send_keys(end_date)
            cursor.send_keys(Keys.ENTER)
            # date setting ends

        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="myTabContent"]/div/div[5]/div/div[1]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[1]/select/option[5]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[2]/div/a/span[1]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/input')))
        cursor.send_keys(client_id)
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/ul/li/div')))
        cursor.click()

        # Execute button
        cursor = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[10]/div/div[1]/button')))
        cursor.click()
        try:
            cursor = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/a/i')))
            cursor.click()
        except:
            pass

    def CaptialGainLoss(self, client_id, start_date, end_date,CustomDate):
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[1]/div/ul/li[3]/a')))
        cursor.click()
        # report empty spot
        report = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div/div')))
        report.click()
        # report dropdown
        report = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div/div/div/ul/li[8]')))
        report.click()

        if CustomDate==True:
            # DATE setter
            cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div/div[1]/input')))
            cursor.clear()
            cursor.send_keys(start_date)
            cursor.send_keys(Keys.ENTER)

            cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div/div[2]/input')))
            cursor.clear()
            cursor.send_keys(end_date)
            cursor.send_keys(Keys.ENTER)
            # date setting ends
        
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="myTabContent"]/div/div[5]/div/div[1]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[1]/select/option[5]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[5]/div/div[2]/div/a/span[1]')))
        cursor.click()
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/input')))
        cursor.send_keys(client_id)
        cursor = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/ul/li/div')))
        cursor.click()
        
        # Exceute button
        cursor = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[14]/div/div[1]/button')))
        cursor.click()
        try:
            cursor = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/a/i')))
            cursor.click()
        except:
            pass

    def EndTask(self):
        self.driver.quit()
