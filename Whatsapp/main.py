from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import urllib
import time 


def findSide():
    try:
        navegador.find_element(By.ID, 'side')
        print("ok")
        return True

    except NoSuchElementException:
        print("Elemento não foi encontrado")
        return False



navegador = webdriver.Firefox()

navegador.get("https://web.whatsapp.com/")

mensagem="Teste Diana"

telefone = "5519994653091"

while  findSide() == False:
    time.sleep(1)


print("achado")

texto = urllib.parse.quote(mensagem)
link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"
navegador.get(link)

while  findSide() == False:
    time.sleep(1)

time.sleep(5)

navegador.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
