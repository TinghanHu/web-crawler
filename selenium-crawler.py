from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 設定 Chrome 選項（可以不用加東西，預設即可）
options = Options()

# 指定 chromedriver 的完整路徑
service = Service(executable_path="/Users/a123/Desktop/爬蟲/chromedriver")

# 建立 driver 實例
driver = webdriver.Chrome(service=service, options=options)

# 開啟 Google 頁面
driver.get("https://www.google.com")

# 關閉瀏覽器
driver.close()
