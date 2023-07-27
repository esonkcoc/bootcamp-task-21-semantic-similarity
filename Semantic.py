import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''Cat and Monkey have a strong similarity because they are both animals. Banana and Monkey have a fair but weak similarity because Monkeys eat Bananas, while Cat and Banana show a weak similarity.'''

word1 = nlp("Football")
word2 = nlp("Cricket")
word3 = nlp("Tiger")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''Football and Cricket have a high similarty as they are both sports, both of their similarity to Tiger is low.'''

'''Running example1.py via en_core_web_sm returns a very low degree of text similarity whereas running it via en_core_web_md returns a much stronger degree of similarity.'''