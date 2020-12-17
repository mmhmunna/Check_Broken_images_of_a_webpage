from selenium import webdriver
import time

driver = webdriver.Chrome("driver/chromedriver")
driver.maximize_window()
baseurl = "https://www.munna.cyou/"
driver.get(baseurl)
time.sleep(6)
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
        if ("error" in title):
            broken_images.append(url)
        else:
            correct_images.append(url)


print('Total Images' + ' ' + str(len(image_links)))
print('Total empty or None Links' + ' ' + str(len(empty_or_None_Links)))
print('Total Correct Images'+ ' ' + str(len(correct_images)))
print('Total Broken Images' + ' ' + str(len(broken_images)))
print('Broken images Link are here:')
print(broken_images)
