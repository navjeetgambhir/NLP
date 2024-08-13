from re import Pattern
from urllib import request
from nltk import re
from bs4 import BeautifulSoup

'''part 1 of 1st question'''
'''accesing Url'''
url = 'https://www.bbc.co.uk/news/business-41779341'
# url='https://en.wikipedia.org/wiki/Renminbi'
# url='https://en.wikipedia.org/wiki/Indian_rupee'

response = request.urlopen(url)
'''reading the html from url'''
raw = response.read().decode('utf8')
'''converting text from html'''
text=BeautifulSoup(raw, 'html.parser').get_text()
'''regular expression to find out the currency values'''
regex = re.compile(r'(?:[£$₹¥]\d+(?:\.|,\d+)?(?:[pm]|bn)?|\d+(?:\.\d+)?(?:[pm]|bn)(?: euros?)?)')

print(re.findall(regex,text)) 
# reference(https://stackoverflow.com/questions/65008802/how-to-write-a-regex-pattern-to-match-string-with-currency-sybol-at-end-or-start)



'''part 2 of 1st question'''

phonenumbers=["555.123.4565","+1-(800)-545-2468","2-(800)-545-2468","3-800-545-2468","555-123-3456","555 222 3342",
              "(234) 234 2442","(243)-234-2342","1234567890","123.456.7890","123.4567","123-4567","1234567900","12345678900"]
print("Phone number list: \n",phonenumbers)

'''regex to find the matching phone numbers'''
phonenumbersregex=re.compile(r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}|[\^+]|\d{1}[-\(\d*)]|[\^(\d{3}]')
matchedresults=[]
for phonenumber in phonenumbers:
    if re.match(phonenumbersregex,phonenumber):
        matchedresults.append(phonenumber)
print("Matched Phone Numbers \n " ,matchedresults)
if (len(phonenumbers)==len(matchedresults)):
  print("All the Phonenumbers matched with Regex")