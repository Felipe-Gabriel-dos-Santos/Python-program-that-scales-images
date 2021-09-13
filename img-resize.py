from selenium import webdriver
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

prefs = {"download.default_directory" : "C:\\Users\\vdoss\\Pictures\\Imagens com escala mudada"}
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path='./ChromeDriver/chromedriver', options=options)
wait = WebDriverWait(driver,50).until
i = 0

driver.get('https://www.img2go.com/pt/redimensionar-imagem')

for file in os.listdir('C:\\Users\\vdoss\\Pictures\\Imagens para mudar escala'):

    wait(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
    driver.find_element_by_xpath('//input[@type="file"]').send_keys('C:\\Users\\vdoss\\Pictures\\Imagens para mudar escala\\' + str(file))
    driver.find_element_by_xpath('/html/body/div[4]/div[6]/div[2]/div/form/div[1]/div[3]/div/div[1]/div/input').click()
    driver.find_element_by_xpath('/html/body/div[4]/div[6]/div[2]/div/form/div[1]/div[3]/div/div[1]/div/input').send_keys('1200')
    driver.find_element_by_xpath('/html/body/div[4]/div[6]/div[2]/div/form/div[1]/div[3]/div/div[2]/div/input').click()
    driver.find_element_by_xpath('/html/body/div[4]/div[6]/div[2]/div/form/div[1]/div[3]/div/div[2]/div/input').send_keys('1200')
    driver.find_element_by_xpath('/html/body/div[4]/div[6]/div[2]/div/form/div[2]/button').click()
    wait(EC.element_to_be_clickable((By.XPATH, '//a[@class="btn btn-large btn-download"]'))).click()
    while True:
        if (len(os.listdir('C:\\Users\\vdoss\\Pictures\\Imagens com escala mudada')) == i and str(file).endswith('.crdownload')):
            time.sleep(1)
        else:
            break

    i = i + 1

    wait(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div/div[1]/div[6]/div[1]/div/div/div[4]/div[2]/a[3]'))).click()


driver.close()