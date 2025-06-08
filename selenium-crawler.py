from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 設定 Chrome 選項（可以不用加東西，預設即可）
options = Options()

# 指定 chromedriver 的完整路徑
service = Service(executable_path="/Users/a123/Desktop/爬蟲/chromedriver")

# 建立 driver 實例
driver = webdriver.Chrome(service=service, options=options)

# 開啟 ptt 股票版 頁面
driver.get("https://www.ptt.cc/bbs/stock/index.html")
# ＃print(driver.page_source)#取得網頁原始碼
tags = driver.find_elements(By.CLASS_NAME, "title")#搜尋屬性是title的路徑
for tag in tags:
    print(tag.text)

#取得上一頁＃取得上一頁的文章標題    
link = driver.find_element(By.LINK_TEXT, "‹ 上頁")
link.click()#模仿使用者點擊
tags = driver.find_elements(By.CLASS_NAME, "title")#搜尋屬性是title的路徑
for tag in tags:
    print(tag.text)

# 關閉瀏覽器
driver.close()
