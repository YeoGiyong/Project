#-*- coding: utf-8 -*-

import requests
import time
import codecs
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select


data = []
# 광고모델 호감도 순위
# https://www.adic.or.kr/stat/mrp/getStats.do?className=Admrp
URL = 'https://www.adic.or.kr/stat/mrp/getStats.do?className=Modelmrp'

#firefox를 띄워 브라우져에 나타난 소스를 스크래핑함
driver = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver.get(URL)

# 년도 선택
year = Select( driver.find_element_by_id('year') )
year.select_by_visible_text('2015년')

# 월 선택
month = Select(driver.find_element_by_id('month'))
month.select_by_visible_text('1월')

# 검색하기 클릭
btn = driver.find_element_by_id('srchBtn')
btn.click()

# 시간지연 주기
time.sleep(3)

#웹 페이지 xpath 정의
alink=driver.find_element_by_xpath('//div["id=modelsearch"]/a')

#마우스,단축키 이벤트 처리를 위해 ActionChains 초기화
mouse = webdriver.ActionChains(driver)
mouse.move_to_element(alink).click().perform()

#source_code = requests.get(URL)
source_code = driver.page_source    #firefox로 가져온 소스를 source_code 변수에 저장

#soup = BeautifulSoup(plain_text,'html.parser')  #html 파서
soup = BeautifulSoup(source_code,'lxml')         #xml 파서

# 데이터 추출

findkey = 'td'
for mrp in soup.select(findkey):
    # print(mrp.text.strip())
    data.append(mrp.text.strip())

#테스트를 위해 띄운 브라우져 닫기
driver.close()

# 데이터 저장
f = codecs.open('advModel_rank_201501.csv', 'w','utf-8')    #파일을 쓰기모드로 open
cnt = 1
tmp = []
for str in data:
    tmp.append(str)
    print(tmp)
    if cnt % 5 == 0:
        fmt = '%s,%s,%s,%s,%s\n'
        rank = fmt % (tmp[0], tmp[1], tmp[2], tmp[3], tmp[4])
        f.write(rank)
        tmp = []
        cnt = 0
    cnt = cnt + 1

f.close()