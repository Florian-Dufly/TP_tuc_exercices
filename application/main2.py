import time
import random
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.wikiroulette.co/")
driver.set_window_size(1920, 1080)
wikiurl = "https://www.wikiroulette.co/"


def gettitre(url):
    driver.get(url)
    str_title = driver.title
    print(str_title)


def titrewikiroulette(url):
    driver.get(url)
    titre_article = driver.find_elements(
        by=By.CLASS_NAME, value="mw-page-title-main")
    print("le titre de l'article de wikiroulette est : " + titre_article[0])


# xpath = //h1[@id = 'firstHeading']/span

gettitre(wikiurl)
titrewikiroulette(wikiurl)
