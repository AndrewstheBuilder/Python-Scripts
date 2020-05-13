#! /usr/bin/python3
#webscrapper.py - this webscrapper gathers phone numbers and email addresses from any website

import requests, bs4, re

#Create Regex
phoneRegex = re.compile( r'''(
    (\d{3}|\(\d{3}\))?              #area code
    (\s|-|\.)?                      #separator
    (\d{3})                         #first three digits
    (\s|-|\.)?                      #separator
    (\d{4})                         #last four digits
    )''', re.VERBOSE)


emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      #username
    @                      #@ symbol
    [a-zA-Z0-9.-]+         #domain name
    (\.[a-zA-Z]{2,3})      #dot-something
    )''', re.VERBOSE)

#Get URL
webpage = input("Enter url: ")
webdata = requests.get(webpage)
try:
webdata.raise_for_status()
except Exception as exc:
print("There was a problem: %s" %(exc))

#Find email and phone number matches from webdata
numbers = []
emails = []
for elem in phoneRegex.findall(webdata.text):
phoneNum = '-'.join([elem[1], elem[3], elem[5]])
numbers.append(phoneNum)
for elem in emailRegex.findall(webdata.text):
emails.append(elem)

#Write result to websiteinfo.txt
webpageInfoFile = open('webpageinfo.txt', 'w')
webpageInfoFile.write('Phone Numbers from link: ' + webpage)
if(len(numbers)<1):
print('No phone numbers found!\n')
webpageInfoFile.write('No phone numbers found!\n')
else:
for elem in numbers:
webpageInfoFile.write(elem)
webpageInfoFile.write('\n')
webpageInfoFile.write('Email addresses from link: ' + webpage)
if(len(emails)<1):
print('No email addresses found!\n')
webpageInfoFile.write('No email addresses found!\n')
else:
for elem in emails:
webpageInfoFile.write(elem[0])
webpageInfoFile.write('\n')
print('Data saved to webpageinfo.txt\n')
