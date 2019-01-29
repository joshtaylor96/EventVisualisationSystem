import coreNLPFunctions
import openNLPFunctions
import semaforFunctions
import timeNormalisation
import json

#testSentence = "Petroleum is a naturally occurring, yellow-to-black liquid found in geological formations beneath the Earth's surface, discovered in 1996. It is commonly refined into various types of fuels. Components of petroleum are separated using a technique called fractional distillation, i.e. separation of a liquid mixture into fractions differing in boiling point by means of distillation, typically using a fractionating column."

data = {}
data["coreNLP"] = {}
data["openNLP"] = {}
data["semafor"] = {}
data["normalisedDates"] = {}

def constructJson(sentence):
    data["coreNLP"]["ner"] = coreNLPFunctions.ner(sentence)
    data["openNLP"]["ner"] = openNLPFunctions.ner(sentence)
    data["semafor"] = semaforFunctions.parseFrames(sentence)
    data["normalisedDates"] = timeNormalisation.getDatesFromText(sentence)

    return(data)


headlines = open("headlines.txt")
eventifiedHeadlines = open("eventifiedHeadlines.txt", "a")
try:
    for line in headlines:
        print(line)
        json.dump(constructJson(line), eventifiedHeadlines, default=str, indent=1)
finally:
    headlines.close()
    eventifiedHeadlines.close()

#jsonData = json.dumps(data, indent=1, default=str)
#print(jsonData)
