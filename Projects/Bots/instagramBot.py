from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'C:\\geckodriver\\geckodriver.exe')


# // a[@href='/accounts/emailsignup/']
# //input[@name='username']
# //input[@name='password']

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(2)
        #login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']") 
        #login_button.click()
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.like_pictures('ltl_engschool')

    def like_pictures(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/' + hashtag + '/' )
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' pictures: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            if 'whatsapp' in pic_href:
                continue
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_elements_by_class_name('//button[@class="wpO6b"]').click()
                time.sleep(19)
            except Exception as e:
                time.sleep(5)






crisBot = InstagramBot('ti_tests','letscreateabot')
crisBot.login()