from selenium import webdriver
from time import sleep
  
url = 'https://www.redfin.com/city/30756/GA/Atlanta'
# Create object page
# Create webdriver object
driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver_win32\chromedriver.exe")
  
# Get the website
driver.get(url)
  
# Make Python sleep for some time
sleep(2)
  
# Obtain the number of rows in body
rows = 1+len(driver.find_elements_by_xpath("/html/body/div[1]/div[8]/div[2]/div[2]/div[3]/div/div/div[1]/div[3]/table/tbody/tr"))



# Obtain the number of columns in table
cols = len(driver.find_elements_by_xpath("/html/body/div[1]/div[8]/div[2]/div[2]/div[3]/div/div/div[1]/div[3]/table/tbody/tr[1]/td"))
  
# Print rows and columns
print(rows)
print(cols)
  
f = open('../input/newset/sample.csv', 'w', encoding='UTF8')
writer = csv.writer(f)


# Printing the data of the table
for r in range(2, rows+1):
    data =[]
    for p in range(1, cols+1):
        
        # obtaining the text from each column of the table
        value = driver.find_element_by_xpath("/html/body/div[1]/div[8]/div[2]/div[2]/div[3]/div/div/div[1]/div[3]/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
        data.append(value)
    writer.writerow(data)

f.close()
    
    

