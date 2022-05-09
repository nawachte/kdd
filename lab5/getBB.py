#Beautiful Soup demo in Python3
#Foaad Khosmood / Spring 2017

import os, sys, random, requests
from bs4 import BeautifulSoup

#obtain the content of the URL in HTML
#url = "https://www.gopoly.com/sports/mbkb/2018-19/schedule"
url = "http://frank.ored.calpoly.edu/BB/www.gopoly.com/sports/mbkb/2018-19/schedule"
myRequest = requests.get(url)

#Create a soup object that parses the HTML
soup = BeautifulSoup(myRequest.text,"html.parser")

#Print the HTML Title
print("Page Title: ",soup.head.title.get_text())
print()

#step through the tag hierarchy
for eventRow in soup.find_all('div', attrs={'class':'event-row'}):
   dateHTML = eventRow.find('div', attrs={'class':'date'})
   date = dateHTML['title'] #the full date is actually a title attribute
   #get the score
   scoreHTML = eventRow.find('div',attrs={'class':'result'})
   if scoreHTML.string is not None and len(scoreHTML.string) > 2:
      score = scoreHTML.string.strip()
   else:
      score = "not availble"
   #get the status
   statusHTML = eventRow.find('div', attrs={'class':'status'})
   status = statusHTML.string.strip() # text between the open/close tags
   #now get the opponent
   opponentHTML = eventRow.find('div', attrs={'class':'opponent'})
   opponent = opponentHTML.span.string.strip() #this is any text decorated by the tag
   #print the summary for this row
   print("On",date,"Cal Poly played against",opponent,"with the result:",score,"("+status+")")
