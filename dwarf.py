from pyparsing import col
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
import requests
import os

start_url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(start_url)

print(page)
headers=[ "V Mag. (mV)","Proper name",	"Bayer designation",	"Distance (ly)",	"Spectral class",	"Mass (M☉)"	,"Radius (R☉)", "Luminosity (L☉)"]
star_data=[]
name=[]
dist=[]
mass=[]
rad=[]
temp_list=[]

def scrap():
    soup=BeautifulSoup(page.text, "html.parser") 
    star_table = soup.find_all('table')
    table_rows = star_table[5].find_all('tr')
   # print(star_table[7])

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)
    
scrap()

for i in range(1,len(temp_list)):
    name.append(temp_list[i][0])
    dist.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    rad.append(temp_list[i][8])

df3=pd.DataFrame(list(zip(name,dist,mass, rad)),columns=["star name","Distance (ly)","Mass (M☉)","Radius (R☉)"])

print(df3)

df3.to_csv('dwarf_data.csv')
