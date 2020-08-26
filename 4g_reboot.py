from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    driver = webdriver.Chrome()
    driver.get('http://192.168.0.1/');
    input_login = driver.find_element_by_id('pc-login-password')
    input_login.send_keys('2BD')

    btn_login  = driver.find_element_by_id('pc-login-btn')
    btn_login.click()

    # Check si user déjà connecté pour bypasser la popup
    id_confirmer = driver.find_element_by_id('confirm-yes')
   
    if id_confirmer is not None:
       id_confirmer.click()

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'topReboot'))
    )

    btn_reboot = driver.find_element_by_id('topReboot')
    btn_reboot.click()

    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="alert-container"]/div/div[4]/div/div[2]/div/div[2]/button'))
    )

    # Confirmation du reboot
    btn_confirmer_reboot = driver.find_element_by_xpath('//*[@id="alert-container"]/div/div[4]/div/div[2]/div/div[2]/button')
    btn_confirmer_reboot.click()
except Exception as e:
    print("Erreur : {0}".format(e))
