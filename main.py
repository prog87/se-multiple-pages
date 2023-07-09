from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

web = 'https://www.audible.com/adblbestsellers?ref=a_ep_audiob_c3_adblp13nmpxxp13n-mpl-dt-c_showmore&pf_rd_p=0069ccfe-15f4-4b99-afae-173004d327be&pf_rd_r=F0GXT11A2M7ZP66EG7QN&pageLoadId=yF910hF53sSDFWv0&creativeId=0ed480d5-7a13-4150-b3aa-2c96f2fc9ae9'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get(web)
driver.maximize_window()

container = driver.find_element(By.XPATH, '//*[@id="product-list-a11y-skiplink-target"]/span/ul/li[1]/div/div[1]/div/div[2]/div/div/span/ul/li[1]/h3')


books_title = []
for product in container.find_elements(By.XPATH, '//li'):
    title = [item.text for item in product.find_elements(By.XPATH, './/h3[contains(@class, "bc-heading")]')]
    books_title.append(title)
    print(*title)

# all_years = [item.text for item in populations.find_elements(By.XPATH, './/td[1]')]
#     year.append(all_years)
#     print(*all_years)
