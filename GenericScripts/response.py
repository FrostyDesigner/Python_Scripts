#get response from url and parse it
import requests

resp = requests.get("https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html")
#print first 500 characters - compare with webpage > right-click > view page source
#print(resp.text[0:500])
#print(resp.content)
#print(resp.json)

#use beautifulsoup to parse data
#may need to install beautifulsoup
#to do so type: "pip install beautifulsoup4" in python shell
from bs4 import BeautifulSoup
soup = BeautifulSoup(resp.text, 'html.parser')

#collect all the records
#<span class="short-desc"><strong>Jan. 21 </strong>“I wasn't a fan of Iraq. I didn't want to go into Iraq.” <span class="short-truth"><a href="https://www.buzzfeed.com/andrewkaczynski/in-2002-donald-trump-said-he-supported-invading-iraq-on-the" target="_blank">(He was for an invasion before he was against it.)</a></span></span>
#<span class="short-desc"><strong> DATE </strong> LIE <span class="short-truth"><a href= "LINK" target="_blank"> DESCRIPTION </a></span></span>
#this finds all span tags with "short-desc" as the value for the class attribute.
results = soup.find_all('span', attrs={'class':'short-desc'})

#print(len(results))
#print(results[0:3])
#last result
#print(results[-1])

#extract the date
#we prefect the first row first and then apply to all oter objects
first_result = results[0]
#print(first_result)
#print(first_result.find('strong'))
print(first_result.find('strong').text)
#print(first_result.find('strong').text[0:-1])

#extract the lie
#print(first_result.contents)
#first child of contents
#print(first_result.contents[0])
#second child of contents
print(first_result.contents[1])
#remove first character (") and the last 2 characters (" and the space)
#print(first_result.contents[1] [1][1:-2])

#extract the explanation
#print(first_result.find('a'))
#select the text part fo the explanation
#print(first_result.find('a').text)
#remove the first and last characters (the parenthesis marks)
print(first_result.find('a').text[1:-1])

#extract the url
print(first_result.find('a')['href'])

records = []
for result in results:
    date = result.find('strong').text[0:-1] + ', 2017'
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date, lie, explanation, url))

print(len(records))
print(records[0:3])

#RLH to do:
#https://www.youtube.com/watch?v=Zh2fkZ-uzBU