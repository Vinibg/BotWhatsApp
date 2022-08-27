from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Firefox()

navegador.get("https://ri.magazineluiza.com.br/")

navegador.find_element(By.XPATH,'/html/body/form/header/div/div/div/div[2]/ul/li[3]/a').click()

time.sleep(1)

navegador.find_element(By.XPATH,'/html/body/form/div[9]/div/div/div/div/ul[3]/li[2]/a').click()

time.sleep(2)

navegador.find_element(By.XPATH, '//*[@id="/yn8cix7XmBHQ2FgNBrtCg=="]').click()