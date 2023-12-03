from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import chromedriver_autoinstaller
#credits to
# https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de for guidance on
#copy chromedriver to /usr/local/bin
#cd to /usr/local/bin
# xattr -d com.apple.quarantine chromedriver

#chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://www.epa.gov/greenpower/green-power-partnership-national-top-100")
players = driver.find_elements_by_xpath('//td[@class="tablebord"]')
players_list = []
for p in range(len(players)):
    players_list.append(players[p].text)
print(len(players_list))
#assert "Python" in driver.title

# driver = webdriver.Chrome('./chromedriver')
# driver.get('https://hoopshype.com/salaries/players/')