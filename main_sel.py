
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import csv
import itertools



def get_page(data):
    soup = BeautifulSoup(data, 'lxml')

    title_l = [ ]
    link_l = [ ]
    titles = soup.find_all('h4', class_='activity__title')
    for title in titles:
        try:
            title = title.text
            title_l.append(title)
        except:
            title = ''
    # print(title_l)
 
    for link in titles:    # get links on page
        try:
            link = 'https://iwilltravelagain.com' + link.find('a').get('href')
            link_l.append(link)
        except:
            link = ''    
    # print(link_l)

    category_l = [ ]
    locate_l = [ ]
    location = soup.find_all('span', class_='term')
    cnt = 1
    for i in location:
        if cnt % 2 != 0:
            try:
                category = i.text
                category_l.append(category)
                # print(cnt, category)
            except:
                category = ''          
        if cnt % 2 == 0:
            try:
                locate = i.text
                locate_l.append(locate)
                # print(cnt, locate)
            except:
                locate = ''
        cnt += 1
    # print(c)
    # print(lt)
     
    for k, l, m, n in zip(title_l, link_l, category_l, locate_l): 
        data = (k, l, m, n)
        
        with open("iwilltravl7.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)



def main():
    url = 'https://iwilltravelagain.com/usa/?page=1'
    
    driver = webdriver.Chrome()   #executable_path='chromedriver')
    time.sleep(8)
    driver.get(url)    # open page
    time.sleep(40)

    cnt = 1
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # scroll page from top to down
        time.sleep(40)

        page = driver.page_source    # get html code
        get_page(page)
        time.sleep(6)

        driver.find_element_by_xpath('/html/body/main/section[3]/div[2]/div[4]/button[8]').click()
        time.sleep(300)
        cnt += 1
        if cnt == 294:
            break



if __name__ == "__main__":
    main()

