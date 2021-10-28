from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
baseurl = "https://staging.deligram.com/"
driver.get(baseurl)
time.sleep(4)
image_tag = driver.find_elements_by_tag_name('img')
image_links = []
for link in image_tag:
    image_links.append(link.get_attribute("src"))

empty_or_None_Links = []
correct_images = []
broken_images =[]
total_link = len(image_links)
for link in range (total_link):
    if (image_links[link] == '' or image_links[link] == None):
        empty_or_None_Links.append(image_links[link])

    else:
        url = str(image_links[link])
        driver.get(url)
        time.sleep(2)
        title = driver.title
        if ("Error" in title):   #this "error" will be change as per as title
            broken_images.append(url)
        else:
            correct_images.append(url)


print('Total Images Link' + ' ' + str(total_link))
print('Total empty or None Images Links' + ' ' + str(len(empty_or_None_Links)))
print('Total Correct Images Link' + ' ' + str(len(correct_images)))
print('Total Broken Images Link' + ' ' + str(len(broken_images)))
print('Broken images Link are here:' + ' ' + str(broken_images))
