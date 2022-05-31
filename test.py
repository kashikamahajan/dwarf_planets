from pyparsing import col
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
import requests
import os

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(start_url)

#print(page)
headers=[ "V Mag. (mV)","Proper name",	"Bayer designation",	"Distance (ly)",	"Spectral class",	"Mass (M☉)"	,"Radius (R☉)", "Luminosity (L☉)"]
star_data=[]
name=[]
dist=[]
mass=[]
rad=[]
temp_list=[]

def scrap():
    soup=BeautifulSoup(page.text, "html.parser")
    star_table=soup.find('table')
    for tbdody in star_table.find_all("tr"):
            td=tbdody.find_all("td")
            row=[]
            for i in td:
                row.append(i.text.rstrip())
            
            temp_list.append(row)



scrap()

for i in range(1,len(temp_list)):
    name.append(temp_list[i][1])
    dist.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    rad.append(temp_list[i][6])

df2=pd.DataFrame(list(zip(name,dist,mass, rad)),columns=["Proper name","Distance (ly)","Mass (M☉)"	,"Radius (R☉)"])

print(df2)

df2.to_csv('Users/Kashika/OneDrive/Desktop/whiteHat/python/p126/brightest_star.csv')
    




