'''
Created on 2023/02/03

@author: class
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

driver = webdriver.Chrome()

driver.get("https://www.yahoo.co.jp/")

search_word = ("ネコ")

path_file = "C:/Users/class/Desktop/ネコ"


el = driver.find_element(By.XPATH,"//*[@id=\"ContentWrapper\"]/header/section[1]/div/ul/li[2]/a/span/span")
el.click()
time.sleep(1)
#↓検索ボックスを指定
search_box = driver.find_element(By.XPATH, "//*[@id=\"ContentWrapper\"]/header/section[1]/div/form/fieldset/span/input")
#↓検索バーに文字を入れる
search_box.send_keys(search_word)

time.sleep(1)
#↓検索ボタンを押す
search_box.submit()
time.sleep(3)

#画面をスクロールする
# driver.execute_script('window.scroll(0,500);')
# time.sleep(3)

#↓ページのHTMLのテキストを取ってくる
soup = BeautifulSoup(driver.page_source,"html.parser")
#↓imgの要素を取ってくる
img = soup.find_all('img')

co=1

for a in img:
    #↓imgのurlを取ってくる
    url=a.attrs['src']
    #↓urlに飛ぶ
    gazo=requests.get(url)
    #↓画像を保存する
    with open(path_file+"/image"+str(co)+".jpg", "wb") as f:
        f.write(gazo.content)
    
    co+=1
    time.sleep(1)

# ブラウザーを終了
driver.quit()

