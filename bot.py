import flask
import os
import time
import urllib2
from bs4 import BeautifulSoup
import json


from flask import Flask, jsonify



app = Flask(__name__)

urlBase = "http://www.bowdoin.edu/atreus/views?unit="
mealMarker="&meal="
diningHalls = ["48","49"]
meals =["Breakfast","Lunch","Dinner"]

def menuItems(hall,meal):
    url = urlBase+hall+mealMarker+meal
    webpage= urllib2.urlopen(url)
    html = webpage.read()
    soup = BeautifulSoup(html, 'html.parser')
    necessaryTags = soup(["h3", "span"])
    necessaryTagsAsStrings = []
    for i in necessaryTags:
        necessaryTagsAsStrings.append(str(i))
##    necessaryTagsPure = []
##    for j in necessaryTagsAsStrings:
##        if j[0:6] =="<span>":
##            necessaryTagsPure.append(j)
##        if j[0:4] =="<h3>":
##            necessaryTagsPure.append(j)
##    necessaryTagsDoublePure = []
    necessaryTagsAsStringsPure=[]
    for j in necessaryTagsAsStrings:
        if j[0:6] =="<span>":

            try:
                textToAppend = j[6:-7]
                necessaryTagsAsStringsPure.append(textToAppend)

            except:
                pass
        if j[0:4] =="<h3>":

            try:
                textToAppend = j[4:-5]+"*"
                necessaryTagsAsStringsPure.append(textToAppend)

            except:
                pass            

    necessaryTagsAsStringsPure.append(hall)
    return necessaryTagsAsStringsPure

def createMenu(menuItems):
    diningHall = ""
    if menuItems[-1] == "48":
        diningHall = "Moulton"
    if menuItems[-1] == "49":
        diningHall = "Thorne"
    del menuItems[-1]
    string = ""
    lastWasTitle = False
    for i in range(len(menuItems)):
        if menuItems[i][-1]=="*":
            stringToAppend = menuItems[i][0:-1].upper()+"\n"
            string = string+stringToAppend
            
            continue
        string = string + menuItems[i]+ "\n"
        if i != len(menuItems)-1:
            if menuItems[i+1][-1]=="*":
                string = string + "\n"
    string = string.replace("&amp;","and")
    if string == "":
    	return "No menus available"
    return string




@app.route('/moulton',methods=['GET','POST'])
def moulton():
    x = {'menu': None}
    currenttime= int(time.ctime()[11:19][0:2]) -3
    if currenttime>= 5 and currenttime < 10:
        return createMenu(menuItems("48","Breakfast"))
    elif currenttime>= 10 and currenttime < 14:
		return createMenu(menuItems("48","Lunch"))
    else:
		return createMenu(menuItems("48","Dinner"))


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', '5000'))

    app.run(
        host="0.0.0.0",
        port=PORT
    )
