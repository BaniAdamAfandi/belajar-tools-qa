import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class TestLogin(unittest.TestCase): 

    def setUp(self):
        # Jika ada error CHROMEDRIVERMANAGER, cara install nya di CMD : pip install webdriver_manager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys("barru.kurniawan@gmail.com") #ini email
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("sman60jakarta")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)

        response_status = driver.find_element_by_id("swal2-title").text #pop up tulisan atas
        response_message = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]").text #pop up tulisan bawah
        
        self.assertEqual(response_status, "Welcome Barru Kurniawan")
        self.assertEqual(response_message, "Anda Berhasil Login")

    def test_failed_login_with_empty_all_fields(self): 
        self.assertEqual("aa","aa")
        driver = self.driver
        driver.maximize_window()
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)

        response_status = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/h2").text
        response_message = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]").text
        
        self.assertEqual(response_status, "Email tidak valid")
        self.assertEqual(response_message, "Cek kembali email anda")

    ######################################################################
    ########### BUAT LAH 5 TEST CASE LOGIN DIBAWAH INI ###################
    ############### CONTOH SEPERTI 2 FUNCTION DEF DIATAS #################

    def test_failed_login_with_wrong_email(self):
        self.assertEqual("aa","aa")

    def test_failed_login_with_wrong_password(self):
        self.assertEqual("aa","aa")

    def test_failed_login_with_wrong_password(self):
        self.assertEqual("aa","aa")
        
    def test_failed_login_with_invalid_email_by_phonenumber(self):
        self.assertEqual("aa","aa")

    def test_failed_login_with_invalid_email_by_username(self):
        self.assertEqual("aa","aa")

    def test_failed_login_with_invalid_email_by_sqli(self):
        self.assertEqual("aa","aa")

    def test_failed_login_with_invalid_email_by_symbol(self):
        self.assertEqual("aa","aa")

    def test_failed_login_with_empty_password(self):
        self.assertEqual("aa","aa")

    def test_failed_login_with_empty_email(self):
        self.assertEqual("aa","aa")

    def tearDown(self): 
        self.driver.close() 
  
# execute the script 
if __name__ == "__main__": 
    unittest.main() 
