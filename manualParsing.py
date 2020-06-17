from urllib.request import Request, urlopen
import re,csv

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def To_the_bottom(driver, times_scroled):
    i = 0
    while i<=times_scroled:
        try:
            driver.find_element_by_xpath('//*[@id="www_pages_reaction_see_more_unitwww_pages_home"]/div/a/i')
            last_height = driver.execute_script("return document.body.scrollHeight")
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            last_height = new_height
        except: break
    i += 1
    

def get_url_List(driver,html):
    driver.get(html)
    #To_the_bottom(driver, 200)
    adress = []
    user_adress = []
    for adr in driver.find_elements_by_class_name('_3dlf'):
        adress.append(adr.get_attribute('href'))
    print(adress)
    for mark_list in adress:
        driver.get(mark_list)
        i = 0
        while i<50:
            try:
                print('+')
                driver.find_element_by_link_text('Ещё').click()
                time.sleep(6)
            except:
                print('-')
            i+=1
            
        for url in driver.find_elements_by_xpath('//*[@id="reaction_profile_browser1"]/li/div/a'):
            if user_adress.count(url) == 0:
                user_adress.append(url.get_attribute('href'))
        print(user_adress)
    return adress




def get_person_urls(driver,urls):
    
    return url_list
    

def login(driver,mail,password):
    driver.get('https://www.facebook.com/')
    inputElement = driver.find_element_by_id("email")
    inputElement.send_keys(mail)
    inputElement = driver.find_element_by_id("pass")
    inputElement.send_keys(password)
    driver.find_element_by_id('loginbutton').click()
    

def main():
    driver = webdriver.Chrome()
    S_url = 'https://www.facebook.com/pg/gmsummit.me/posts/'                   #LOB19
  # S_url = 'https://www.facebook.com/pg/olerom.ua/posts/'                     #OLEROM
  # S_url = 'https://www.facebook.com/pg/isaac.pintosevich.systems/posts/'     #Isaac Pintosevich Systems
    login(driver,'egorpl1205@gmail.com','rjk,fcrf12051999')
    all_mark_urls = get_url_List(driver,S_url)



    
if __name__ == '__main__':
    main()


