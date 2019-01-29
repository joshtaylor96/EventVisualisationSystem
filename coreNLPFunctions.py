from stanfordcorenlp import StanfordCoreNLP

def nlpServerTest(sentence):
    nlp = StanfordCoreNLP('http://localhost', port=9000)

    print('Tokenize:', nlp.word_tokenize(sentence))
    print('Part of Speech:', nlp.pos_tag(sentence))
    print('Named Entities:', nlp.ner(sentence))
    print('Constituency Parsing:', nlp.parse(sentence))
    print('Dependency Parsing:', nlp.dependency_parse(sentence))

    nlp.close()

#Named Entity Recognition

def ner(sentence):
    nlp = StanfordCoreNLP('http://localhost', port=9000)
    taggedSentence = nlp.ner(sentence)
    nlp.close()

    entityDict = {}
    for taggedWord in taggedSentence:
        if taggedWord[1] != 'O':
            tag = taggedWord[1].lower()
            if tag not in entityDict:
                entityDict[tag] = [taggedWord[0]]
            else:
                entityDict[tag].append(taggedWord[0])

    return entityDict




#testSentence = "Brent climbed above $80/bbl to its highest level since November 2014 after OPEC and its allies signaled less urgency to boost output, despite U.S. pressure to temper prices."
#nlpServerTest(testSentence)
#print(ner(testSentence))