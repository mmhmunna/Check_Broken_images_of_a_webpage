from selenium import webdriver
import time
import requests

driver = webdriver.Chrome("driver/chromedriver")
driver.maximize_window()
baseurl = "https://www.munna.cyou/"
driver.get(baseurl)
time.sleep(6)
image_tag = driver.find_elements_by_tag_name('img')
correct_images = []
broken_images =[]
empty_or_None_Links = []
for link in image_tag:
    url = link.get_attribute('src')
    if (url == None or url == ''):
        empty_or_None_Links.append(url)
    else:
        request_code =(requests.head(url).status_code)
        if (request_code == 200):
            correct_images.append(url)
        else:
            broken_images.append(url)

print('Total Images' + ' ' + str(len(correct_images + broken_images + empty_or_None_Links)))
print('Total empty or None Links' + ' ' + str(len(empty_or_None_Links)))
print('Total Correct Images'+ ' ' + str(len(correct_images)))
print('Total Broken Images' + ' ' + str(len(broken_images)))
print('Broken images Link are here:')
print(broken_images)

    