import urllib
from bs4 import BeautifulSoup

myfile = open('/home/harish/Desktop/clarityctf2017-master/community/dump.html')
mytxt = myfile.read()
soup = BeautifulSoup(mytxt, "html.parser")
day = {}
time = {}

count = 0
for eventlist in soup.findAll('div', {"class": "list-card__body"}):
    # strng = str(eventlist.text.encode('utf-8'))
    # text =  "".join(strng.split('\n'))
    text = eventlist.text.split("\n")
    text = filter(None, text)  # This is to remove the empty elements
    text = [" ".join(c.split()) for c in text]  # To remove the extra whitespaces
    text = filter(lambda name: name.strip(), text)  # Remove strings containing only white spaces from list

    # print "breank"
    # for i in text:


    tempCount = 0
    for i in text:
        if tempCount % 3 == 0:
            day[i.split(',')[0]] = day.get(i.split(',')[0], 0) + 1
            time[i.replace(',', ' ').split()[3]] = time.get(i.replace(',', ' ').split()[3],0)+1
        tempCount = tempCount + 1

    count = count + 1
print "Most active day and Least Active day"
print max(day,key=day.get)# Getting key wiht maximum value
print min(day,key=day.get)

print "Greater active time and lesser active time "
print max(time,key=time.get)# Getting key wiht maximum value
print min(time,key=time.get)
myfile.close()