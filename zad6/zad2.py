#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import time
import os
import requests
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.pap.pl/')
# a
cookies = driver.find_element_by_xpath('//div[@id="cookie"]/div/div/div/div/div[1]')
cookies.click()
# b
driver.maximize_window() # zwiekszamy wielkosc okna
time.sleep(1)
# c
driver.find_element_by_link_text('| En').click()
# d
driver.find_element_by_link_text('Business').click()
# e
titles = driver.find_elements_by_class_name('title')
titles = [title.find_elements_by_tag_name('a')[0].text for title in titles]
print(titles)
# f
images = driver.find_elements_by_class_name('imageWrapper')
images = [image.find_element_by_tag_name('a').find_element_by_tag_name('img').get_attribute('src') for image in images]

os.makedirs('images', exist_ok=True)
for i, image in enumerate(images):
    with open(f'images/{i}.jpg', 'wb') as handle:
        response = requests.get(image, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
# g
element = driver.find_element_by_partial_link_text('Ostatnia')
driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'start', inline: 'start'});", element)
# trzeba zescrollowac do gory zeby moc kliknac na element
driver.execute_script("window.scrollBy(0, -50);")
element.click()
# h
print(driver.find_element_by_xpath("//a[@title='Current page']").text)
