import time, os
from tkinter import BROWSE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

day = 3
Xpath1 = '//*[@id="upload-icon"]'
Xpath2 = '//*[@id="content"]/input'
Xpath3 = '//*[@id="next-button"]'
Xpath4 = '//*[@id="schedule-radio-button"]'
Xpath5 = '//*[@id="datepicker-trigger"]'
Xpath6 = '//*[@id="input-2"]/input'

options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--log-level=3")
options.add_argument("user-data-dir=C:\\Users\\Alperen\\AppData\\Local\\Google\\Chrome\\User Data\\")
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
print("\033[1;31;40m IMPORTANT: Put one or more videos in the *videos* folder in the bot directory. Please make sure to name the video files like this --> Ex: vid1.mp4 vid2.mp4 vid3.mp4 etc..")
time.sleep(6)
answer = input("\033[1;32;40m Press 1 if you want to spam same video or Press 2 if you want to upload multiple videos: ")

if(int(answer) == 1):
    nameofvid = input("\033[1;33;40m Put the name of the video you want to upload (Ex: vid.mp4 or myshort.mp4 etc..) ---> ")
    howmany = input("\033[1;33;40m How many times you want to upload this video ---> ")

    for i in range(int(howmany)):
        bot = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)

        bot.get("https://studio.youtube.com")
        wait = WebDriverWait(bot, 30)
        element = wait.until(EC.presence_of_element_located((By.XPATH, Xpath1)))
        time.sleep(3)
        upload_button = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
        upload_button.click()
        #element = wait.until(EC.presence_of_element_located((By.XPATH, Xpath2)))
        time.sleep(1)

        file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
        simp_path = 'videos/{}'.format(str(nameofvid))
        abs_path = os.path.abspath(simp_path)
        file_input.send_keys(abs_path)

        time.sleep(7)

        element = wait.until(EC.presence_of_element_located((By.XPATH, Xpath3)))

        next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
        for i in range(3):
            next_button.click()
        
        element = wait.until(EC.presence_of_element_located((By.XPATH, Xpath4)))
        done_button = bot.find_element(By.XPATH, '//*[@id="schedule-radio-button"]')
        done_button.click()
        time.sleep(5)

        element = wait.until(EC.presence_of_element_located((By.XPATH, Xpath5)))
        done_button = bot.find_element(By.XPATH, '//*[@id="datepicker-trigger"]')
        done_button.click()
        time.sleep(5)

        element = wait.until(EC.presence_of_element_located((By.XPATH, Xpath6)))
        input_element = bot.find_element(By.XPATH, '//*[@id="input-2"]/input')
        input_element.clear()
        input_element.send_keys('29 Mart 2024')
        input_element.send_keys(Keys.ESCAPE)

        done_button = bot.find_element(By.CSS_SELECTOR, "#done-button > div")
        done_button.click()
        time.sleep(5)
# until wait



elif(int(answer) == 2):
    bot = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
    print("\033[1;31;40m IMPORTANT: Please make sure the name of the videos are like this: vid1.mp4, vid2.mp4, vid3.2mp4 ...  etc")
    dir_path = '.\\videos'
    count = 0

    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print("   ", count, " Videos found in the videos folder, ready to upload...")
    time.sleep(6)

    dayCounter = 0



    for i in range(count):
        
        bot.get("https://studio.youtube.com")
        wait = WebDriverWait(bot, 30)
        element = wait.until(EC.presence_of_element_located((By.XPATH, Xpath1)))

        upload_button = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
        upload_button.click()
        #element = wait.until(EC.presence_of_element_located((By.XPATH, Xpath2)))
        time.sleep(1)

        file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
        simp_path = 'videos/Reels ({}).mp4'.format(str(i+1))
        abs_path = os.path.abspath(simp_path)
        
        file_input.send_keys(abs_path)

        time.sleep(7)

        element = wait.until(EC.presence_of_element_located((By.XPATH, Xpath3)))

        next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
        for i in range(3):
            next_button.click()
            
        element = wait.until(EC.presence_of_element_located((By.XPATH, Xpath4)))
        done_button = bot.find_element(By.XPATH, '//*[@id="schedule-radio-button"]')
        done_button.click()
        
        element = wait.until(EC.presence_of_element_located((By.XPATH, Xpath5)))
        done_button = bot.find_element(By.XPATH, '//*[@id="datepicker-trigger"]')
        done_button.click()
        
        element = wait.until(EC.presence_of_element_located((By.XPATH, Xpath6)))
        input_element = bot.find_element(By.XPATH, '//*[@id="input-2"]/input')
        input_element.clear()
        input_element.send_keys('{} Haz 2023'.format(str(day)))
        dayCounter += 1
        if dayCounter == 3:
            day += 1
            dayCounter = 0
        input_element.send_keys(Keys.ESCAPE)

        done_button = bot.find_element(By.CSS_SELECTOR, "#done-button > div")
        done_button.click()
        time.sleep(5)
        




