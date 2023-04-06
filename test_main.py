# libreria importadas
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pytest import mark
import time

# Abrir navegardor
driver = webdriver.Chrome()

# maximizar pantalla
driver.maximize_window()
#Pagina Para Abrir
driver.get('https://do.linkedin.com')

driver.save_screenshot("results/introPage.png") # Capturo imagen

#Prueba HU01
@mark.ui
def test_prueba1():
    # Acciones
    driver.find_element(By.CSS_SELECTOR, 'body > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis').click()

    
    driver.save_screenshot("results/intrologin.png") # Capturo imagen
    assert True

#Prueba HU02
@mark.ui
def test_prueba2():
    #loggear
    element_email = driver.find_element(By.CSS_SELECTOR, '#username')
    element_email.send_keys('descargaxmx@gmail.com')

    element_password = driver.find_element(By.CSS_SELECTOR, '#password')
    element_password.send_keys('prueba123')
    
    driver.save_screenshot("results/filledlogin.png") # Capturo imagen
    #loggear click
    driver.find_element(By.CSS_SELECTOR, '#organic-div > form > div.login__form_action_container > button').click()
    
    driver.save_screenshot("results/loginComplete.png") # Capturo imagen
    assert True
    
#Prueba HU03
@mark.ui
def test_prueba3():
    # nav search-typeahead
    driver.find_element(By.CSS_SELECTOR, '#global-nav-search > div').click()

    element_buscar = driver.find_element(By.CSS_SELECTOR, '#global-nav-typeahead > input')
    element_buscar.send_keys('ITLA' + Keys.ENTER)
    driver.save_screenshot("results/buscarR.png") # Capturo imagen
    time.sleep(3)

    assert True

#Prueba HU05
@mark.ui
def test_prueba4():

    driver.find_element(By.CSS_SELECTOR, '#global-nav > div > nav > ul > li:nth-child(1) > a > div > div > li-icon > svg > path').click() #nav Inicio
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#global-nav > div > nav > ul > li:nth-child(2) > a > span').click() # nav Mi red
    driver.save_screenshot("results/navarIcon1.png") # Capturo imagen
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#global-nav > div > nav > ul > li:nth-child(3) > a > div > div > li-icon > svg').click() # nav Empleos
    driver.save_screenshot("results/navarIcon2.png") # Capturo imagen
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#global-nav > div > nav > ul > li:nth-child(4) > a').click() # nav Mensajes
    driver.save_screenshot("results/navarIcon3.png") # Capturo imagen
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#global-nav > div > nav > ul > li:nth-child(5) > a > div > div > li-icon > svg > path').click() # nav Notificaciones
    driver.save_screenshot("results/navarIcon4.png") # Capturo imagen
    time.sleep(2)

    assert True

#Prueba HU05
@mark.ui
def test_prueba5():

    driver.find_element(By.CSS_SELECTOR, '#global-nav > div > nav > ul > li:nth-child(1) > a > div > div > li-icon > svg > path').click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[6]/div/button/span").click()
    time.sleep(2)
    driver.get('https://www.linkedin.com/m/logout/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3Bm9xcCV9OR12BHIky3vlxTQ%3D%3D')
    driver.save_screenshot("results/SingOut.png") # Capturo imagen
    assert True


@mark.ui
def test_pruebafinal():
    time.sleep(4)
    driver.quit()
    assert True