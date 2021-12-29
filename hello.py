from selenium import webdriver as wb
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import requests as req

driver = wb.Chrome()
url = 'https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&BestType=SteadySeller'
driver.get(url)
soup = bs(driver.page_source, 'lxml')

title_steady = soup.select('.bo3')
title_list_steady = []
rank_list_steady = []
for i in range(len(title_steady)):
    title_list_steady.append(title_steady[i].text)
    rank_list_steady.append(i+1)
dic = {'번호':rank_list_steady,'책제목':title_list_steady}
df = pd.DataFrame(dic)
df.set_index('번호', inplace=True)
df
