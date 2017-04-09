import urllib
from bs4 import BeautifulSoup

myfile = open('/home/harish/Desktop/clarityctf2017-master/community/dump.html')
mytxt = myfile.read()
soup = BeautifulSoup(mytxt, "html.parser")
time = {}
name = {}
location = {}

count = 0
for eventlist in soup.findAll('div', {"class": "list-card__body"}):
    text = eventlist.text.split("\n")
    text = filter(None, text)  # This is to remove the empty elements
    text = [" ".join(c.split()) for c in text]  # To remove the extra whitespaces
    text = filter(lambda name: name.strip(), text)  # Remove strings containing only white spaces from list



    tempCount = 0
    for i in text:
        if tempCount % 3 == 0:
            time[count] = i
        elif tempCount % 3 == 1:
            name[count] = i
        else:
            location[count] = i
        tempCount = tempCount + 1

    count = count + 1

for i in range(0, count):
    print str(i + 1) + "Event Time:" + str(time[i].encode('utf-8'))
    print str(i + 1) + "Event Name:" + str(name[i].encode('utf-8'))
    print str(i + 1) + "Event Location:" + str(name[i].encode('utf-8'))

myfile.close()