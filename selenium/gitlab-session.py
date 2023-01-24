# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
driver.get("https://newgitlab.great.ufc.br/")

login_box = driver.find_element("name", "user[login]")
password_box = driver.find_element("name", "user[password]")

login_box.send_keys('marciogomes')
password_box.send_keys('#sirius084')

login_box.submit()
password_box.submit()

# -


