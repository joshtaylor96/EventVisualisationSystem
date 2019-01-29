from nltk_opennlp.taggers import OpenNLPTagger
from nltk_opennlp.chunkers import OpenNERChunkerMulti
import os
from nltk.tree import ParentedTree

#testSentence = "Pierre Vinken , 61 years old , born in America , will join the board as a nonexecutive director Nov. 29 ."
openNLPDir = '/Users/Josh/apache-opennlp/opennlp-tools'
language = 'en'

models = ['person', 'date', 'location', 'time', 'organization', 'percentage', 'money']

tagger = OpenNLPTagger(language=language, path_to_bin=os.path.join(openNLPDir, 'bin'),
                       path_to_model=os.path.join('/Users/Josh/apache-opennlp/opennlp-tools', 'en-pos-maxent.bin'))

chunker = OpenNERChunkerMulti(
                             path_to_bin=os.path.join(openNLPDir, 'bin'),
                             path_to_chunker=os.path.join(openNLPDir, '{}-chunker.bin'.format(language)),use_punc_tag=True,
                             ner_models=[
                                 os.path.join(openNLPDir, '{}-ner-person.bin'.format(language)),
                                 os.path.join(openNLPDir, '{}-ner-date.bin'.format(language)),
                                 os.path.join(openNLPDir, '{}-ner-location.bin'.format(language)),
                                 os.path.join(openNLPDir, '{}-ner-time.bin'.format(language)),
                                 os.path.join(openNLPDir, '{}-ner-organization.bin'.format(language)),
                                 os.path.join(openNLPDir, '{}-ner-percentage.bin'.format(language)),
                                 os.path.join(openNLPDir, '{}-ner-money.bin'.format(language))])


def tagSentence(sentence):
    #startingDir = os.getcwd()
    os.chdir(openNLPDir)

    taggedSentence = tagger.tag(sentence)
    #os.chdir(startingDir)

    return taggedSentence

def ner(sentence):
    #startingDir = os.getcwd()
    os.chdir(openNLPDir)
    taggedSentence = tagger.tag(sentence)
    chunkedSentence = chunker.parse(taggedSentence)

    entityDict = {}

    for chunk in chunkedSentence:
        if type(chunk) == ParentedTree and chunk.label().lower() in models:
            tag = chunk.label().lower()
            chunkItems = []
            for leaf in chunk.leaves():
                chunkItems.append(leaf[0])
            if tag not in entityDict:
                entityDict[tag] = [chunkItems]
            else:
                entityDict[tag].append(chunkItems)


    #os.chdir(startingDir)
    return entityDict



