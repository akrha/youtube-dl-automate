from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dja%26next%3D%252Fplaylist%253Flist%253DWL&hl=ja')
login = ""
password = ""

driver.find_element_by_name("identifier").send_keys(login)
driver.find_element_by_name("identifier").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("password").send_keys(Keys.ENTER)
print("Authenticating...")
while ("- YouTube" not in driver.title):
    continue

# 表示されている後で見るリストのURLの値を取得する
videolist = []
for video in driver.find_elements_by_css_selector("a.yt-simple-endpoint.style-scope.ytd-playlist-video-renderer"):
    videolist.append(str(video.get_attribute("href")))

for video in videolist:
    print("Downloading: "+video)
    driver.get('https://www.onlinevideoconverter.com/youtube-converter')
    driver.find_element_by_id("texturl").send_keys(video)
    driver.find_element_by_id("texturl").send_keys(Keys.ENTER)
    while ("Your conversion is completed - OnlineVideoConverter.com" not in driver.title):
        continue
    driver.find_element_by_id("downloadq").click()
    driver.find_element_by_id()