import requests
import dateparser
from dateparser.search import search_dates

text = """Brent climbed above $80/bbl to its highest level since November 2014 after OPEC and its allies signaled less urgency to boost output, despite U.S. pressure to temper prices. 
Futures in London rose as much as 2.7%. 
Bank of America Merrill Lynch joined JPMorgan Chase in anticipating higher prices down the line -- the former expects crude to reach $95/bbl in 1H19.
"""

#coreference
url = 'http://localhost:8080'
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
response = requests.post(url+'/coreference/text', json={"text": text}, headers=headers)
#print(response.status_code)
print(response.json()['substitutedText'])

#discourseSimplification
response = requests.post(url+'/discourseSimplification/text',
                         json={"text": text, "doCoreference": "true", "isolateSentences": "false", "format": "DEFAULT"},
                         headers=headers)
print(response.json())

#openRelationExtraction
response = requests.post(url+'/relationExtraction/text',
                         json={"text": text, "doCoreference": "true", "isolateSentences": "false", "format": "DEFAULT"},
                         headers=headers)
print(response.json())

#dates = search_dates(text)
#print(dates)