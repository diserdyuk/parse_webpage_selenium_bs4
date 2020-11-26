
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import csv



def write_csv(d):
    with open('iwilltravel.csv', 'a') as f:
        order = ['title'] #, 'link'] # , 'category', 'locate']
        write = csv.DictWriter(f, fieldnames=order)
        write.writerow(d)


def get_page(data):
    soup = BeautifulSoup(data, 'lxml')

    titles = soup.find_all('h4', class_='activity__title')
    for title in titles:
        try:
            title = title.text
        except:
            title = ''
        # print(type(title))
        data = {'title': title}
        write_csv(data)
 
    for link in titles:    # get links on page
        try:
            link = 'https://iwilltravelagain.com' + link.find('a').get('href')
        except:
            link = ''    
        # print(link)

    location = soup.find_all('span', class_='term')
    cnt = 1
    for i in location:
        if cnt / 2 != 0:
            try:
                category = i.text
                # print(cnt, category)
            except:
                category = ''          
        if cnt / 2 == 0:
            try:
                locate = i.text
                # print(cnt, locate)
            except:
                locate = ''
        cnt += 1    



def main():
    url = 'https://iwilltravelagain.com/usa/?page=1'
    

    driver = webdriver.Chrome()   #executable_path='chromedriver')
    driver.get(url)    # open page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # scroll page from top to down
    time.sleep(6)
    page = driver.page_source    # get html code

    get_page(page)



if __name__ == "__main__":
    main()

