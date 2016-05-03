import os
import time
import folium
import pandas as pd
from selenium import webdriver


state_geo = r'data/shandong.json'
state_unemployment = r'data/shandong_user.csv'

state_data = pd.read_csv(state_unemployment)

#Let Folium determine the scale
fn='shandong.html'
map = folium.Map(location=[36, 119], zoom_start=7)
map.geo_json(geo_path=state_geo, data=state_data,
             columns=['City', 'User'],
             key_on='feature.id',
             fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
             legend_name='Users')
map.save(outfile=fn)

delay=5
tmpurl='file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=fn)

chromedriver = "/Users/jihongfei/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get(tmpurl)
#Give the map tiles some time to load
time.sleep(delay)
browser.save_screenshot('map3.png')
browser.quit()
