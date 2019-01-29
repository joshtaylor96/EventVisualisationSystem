from dateparser.search import search_dates

def getDatesFromText(text):
    dateList = search_dates(text, settings={'PREFER_DAY_OF_MONTH': 'first', 'PREFER_DATES_FROM': 'past'})
    #dateDict = dict(dateList)

    return dateList

#print(getDatesFromText("Iran has no plans to cut oil output amid U.S. sanctions pressure on buyers to stop dealing with the country, the energy ministry news service Shana reported, citing Ali Kardor, CEO of state crude producer National Iranian Oil Co. The NIOC is providing full insurance coverage for shipments of its crude."))


#testSentence = """Brent climbed above $80/bbl to its highest level since November 2014 after OPEC and its allies signaled less urgency to boost output, despite U.S. pressure to temper prices.
#Futures in London rose as much as 2.7%. Bank of America Merrill Lynch joined JPMorgan Chase in anticipating higher prices down the line -- the former expects crude to reach $95/bbl in 1H19."""
#print(getDatesFromText(testSentence))
