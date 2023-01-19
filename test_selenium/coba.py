import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class Amazon(unittest.TestCase): 

    
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://www.amazon.in/")
        cls.driver.maximize_window()
        
    def test_amazon(self):

        # In the search box, enter ' data catalog' and search'
        self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("data catalog")
        self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").submit()
        self.driver.implicitly_wait(5)                               
        print("done")
        
        first_book_title = "The Condensed Chemical Dictionary; A Reference Volume for All Requiring Quick Access to a Large Amount of Essential Data Regarding Chemicals, and ... Used in Manufacturing and Laboratory Work"

        #check for title
        title = self.driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[1]/a/h2').text.strip()
        self.assertEqual(first_book_title,title)
    
        # check for author
        author = self.driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[2]/span[2]').text
        self.assertEqual(author,"Inc Chemical Catalog Company")
       
        # check for paperback price 
        paperback = self.driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[2]/div[1]/div[2]/a/span').text.strip()
        self.assertEqual(paperback,"1,499")
        
        # check for hardcover price
        hardcover = self.driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[2]/div[1]/div[7]/a/span').text.strip()
        self.assertEqual(hardcover,"3,115.91")

        print("Title = ", title)
        print("Author = ", author)
        print("Paperback Price = " , paperback)
        print("Hard Cover Price = " , hardcover)
        
      
    def tearDown(cls):
        #Close the browser
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()    