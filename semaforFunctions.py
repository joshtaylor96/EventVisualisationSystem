import requests

#text = """Brent climbed above $80/bbl to its highest level since November 2014 after OPEC and its allies signaled less urgency to boost output, despite U.S. pressure to temper prices.
#Futures in London rose as much as 2.7%.
#Bank of America Merrill Lynch joined JPMorgan Chase in anticipating higher prices down the line -- the former expects crude to reach $95/bbl in 1H19.
#"""


url = 'http://localhost:8090/parse-frames'
#response = requests.post(url, data=text)
#print(response.json())

def parseFrames(text):
    parsedFrames = requests.post(url, data=text)

    return parsedFrames.json()