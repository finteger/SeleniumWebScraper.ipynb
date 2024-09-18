from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import csv

driver = webdriver.Chrome()

#specify the url
page_url = 'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401'

driver.get(page_url)

#Wait for the table to load
driver.implicitly_wait(10)

#Get the page source after the JavaScript execution
page_source = driver.page_source

#Parsing the HTML document
soup = BeautifulSoup(page_source, 'html.parser')

#Find the table element
table = soup.find('table', class_='pub-table')

if table:
    #Extract the column headers using list comprehension
    headers = [th.get_text().strip() for th in table.find_all('th')]
    
    #Extract the row data
    rows = []
    for tr in table.find_all('tr'):
        row = [td.get_text().strip() for td in tr.find_all('td')]
        if row: 
            rows.append(row)
            
            
    #Print column headers
    print("Column headers:")
    print(headers)
    
    #Print column headers
    print("\nRow Data:")
    print(rows)
    
    #new set of headers inside a tuple
    headers_tuple = (   
        'All-items',
        'Food5',
        'Shelter6', 
        'Household operations,furnishings and equipment',
        'Clothing and footwear', 
        'Transportation',
        'Gasoline', 
        'Health and personal care', 
        'Recreation, education and reading',
        'Alcoholic beverages, tobacco products and recreational cannabis',
        'All-items excluding food and energy7',
        'All-items excluding energy7',
        'Energy7',
        'Goods8', 
        'Services9'
    )
    
    #write the data to CSV file
    with open('table_data.csv', 'w', newline="") as csvfile:
        writer = csv.writer(csvfile)
        
        #Insert the new column as the first column in each row
        for i, row in enumerate(rows):
            rows[i] = [headers_tuple[i]] + row
            
        #Write headers
        writer.writerow(headers[2:8])
        
        #Write rows
        writer.writerows(rows)
        
    print('Data has been successfully saved to table_data.csv!')
else:
    print('Table not found')
        
        
#Close the WebDriver
driver.quit()
        
        
        
    
    
    
