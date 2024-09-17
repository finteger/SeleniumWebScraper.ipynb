from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service 
import csv

driver = webdriver.Chrome()

#Sample page for practice
page_url = 'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401'

#Wait for the table to load
driver.get(page_url)

# Get page source code after JavaScript execution
driver.implicitly_wait(20)

page_source = driver.page_source

#specify html parser
soup = BeautifulSoup(page_source, 'html.parser')

#find table by id
table = soup.find('table', class_='pub-table')

if table:
    #get the column headers
    headers = [th.get_text().strip() for th in table.find_all('th')]
    
    #extract the rows
    rows = []
    for tr in table.find_all('tr'):
        row = [td.get_text().strip() for td in tr.find_all('td')]
        if row: 
            rows.append(row)
    
    #Print out column headers
    print("Columns:")
    print(headers)
    
    #Print out rows
    print("Rows:")
    print(rows)
    
    
    headers_tuple = {
        'All-items',
        'Food5',
        'Shelter6',
        'Household operations,furnishings and equipment',
        'Clothing and footwear',
        'Transportation',
        'Gasoline', 
        'Health and personal care',
        'Recreation,education and reading', 
        'Alcoholic beverages,tobacco products and recreational cannabis',
        'All-items excluding food and energy7',
        'All-items excluding energy7',
        'Energy7',
        'Goods8', 
        'Services9'
    }

    






