from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from urllib.request import urlretrieve
import ddddocr
ocr = ddddocr.DdddOcr()
options=Options()
options.chrome_executable_path="C:/Users/steff/Desktop/project_2/chromedriver.exe"
driver=webdriver.Chrome(options=options)
url = "https://www.etax.nat.gov.tw/etwmain/etw113w1/ban/query"
driver.get(url)

username = "16313302"
screenImg = "C:/Users/steff/Desktop/project_2/image.png"

driver.implicitly_wait(1)

#輸入統一編號
driver.find_element(By.ID,"ban").send_keys(username)
driver.implicitly_wait(10)
#找到驗證碼做OCR並輸入
src=driver.find_element(By.CSS_SELECTOR,"img.mr-2").get_attribute('src')
urlretrieve(src, "image.png")
with open(screenImg, 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)
driver.find_element(By.ID,"captchaText").send_keys(res)
#確認
driver.find_element(By.CSS_SELECTOR,".btn.btn-lg.btn-block.btn-primary").click()
#進入頁面後抓下資料
result=driver.find_element(By.CSS_SELECTOR,".etw-list-data.mb-0").text
with open("result.txt",'w',encoding='utf-8') as f:
    f.write(result)
#driver.implicitly_wait(10)
driver.close()