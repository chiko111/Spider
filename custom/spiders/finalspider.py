                    ##############-----------------Tsvetan Valchev--------------------------####################

#Imports

from decimal import Decimal
import scrapy
import json
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from csv import unregister_dialect
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ..items import CustomItem
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from decimal import Decimal



class FinalspiderSpider(scrapy.Spider):
    
        #Spider start url and cookies
        
    name = 'finalspider'
    allowed_domains = ['shop.mango.com']
    def start_requests(self):
        url = "https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99"
        yield scrapy.Request(url=url, cookies={'bg':'1000'})
       
        #Selenium WebDriver with url 
        
    def parse(self,response):
        driver = webdriver.Chrome()
        driver.get("https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99")
        driver.implicitly_wait(1000)
        driver.find_element_by_id("onetrust-accept-btn-handler").click()
        driver.implicitly_wait(10)
        
        #Scraped links to attributes
        
        name = driver.find_element_by_xpath('//*[@id="app"]/main/div/div[3]/div[1]/div[1]/h1').text
        price = [elem.get_attribute("content") 
                   for elem in driver.find_elements_by_xpath('//*[@id="app"]/main/div/div[3]/div[1]/div[2]/meta[2]')]
        colour = [elem.get_attribute("alt") 
                   for elem in driver.find_elements_by_xpath('//*[@id="08"]/img[1]')]
        colour2 = [elem.get_attribute("alt") 
                   for elem in driver.find_elements_by_xpath('//*[@id="99"]/img[1]')]
        size = [elem.get_attribute("data-size") 
                   for elem in driver.find_elements_by_xpath('//*[@id="sizeSelector"]/div/span[1]')]
        size2 = [elem.get_attribute("data-size") 
                   for elem in driver.find_elements_by_xpath('//*[@id="sizeSelector"]/div/span[2]')]
        size3 = [elem.get_attribute("data-size") 
                   for elem in driver.find_elements_by_xpath('//*[@id="sizeSelector"]/div/span[3]')]
        size4 = [elem.get_attribute("data-size") 
                   for elem in driver.find_elements_by_xpath('//*[@id="sizeSelector"]/div/span[4]')]
        size5 = [elem.get_attribute("data-size") 
                   for elem in driver.find_elements_by_xpath('//*[@id="sizeSelector"]/div/span[5]')]
        
        sizelist = [size,size2,size3,size4,size5]
        listofsizes = sizelist
        p = price
        
        #Exporting to JSON
        
        dictionary = {"name" : name, "price": p, "colours": [colour,colour2], "size": [listofsizes] }
        json_dump = json.dumps(dictionary)
        with open('/Users/cw/custom/custom/listofattributes.json', 'w', encoding='utf8') as f:
            f.write(json_dump)

        
        driver(quit);
