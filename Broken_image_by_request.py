from selenium import webdriver
import requests
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
baseurl = "https://staging.deligram.com/"
driver.get(baseurl)
image_tag = driver.find_elements_by_tag_name('img')
correct_images = []
broken_images =[]
empty_or_None_Links = []
not_image_link = []
for link in image_tag:
    url = link.get_attribute('src')
    try:
        if (url == None or url == ''):
            empty_or_None_Links.append(url)
        else:
            request_code =(requests.get(url).status_code)
            if (request_code == 200):
                correct_images.append(url)
            else:
                broken_images.append(url)
    except :
        not_image_link.append(url)


print('Total images Link' + ' ' + str(len(correct_images + broken_images + empty_or_None_Links + not_image_link)))
print('Total empty or None images Link' + ' ' + str(len(empty_or_None_Links)))
print('Total Correct Images Link'+ ' ' + str(len(correct_images)))
print('Total Broken Images link' + ' ' + str(len(broken_images)))
print('Invalid Formmat Image link:' + ' ' + str(len(not_image_link)))
print('Broken Images Link Are Here:' + ' ' +str(broken_images))