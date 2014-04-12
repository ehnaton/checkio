import re
 
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
 
vowels = re.compile(u'[%s]{2,}' % VOWELS)
consonants = re.compile(u'[%s]{2,}' % CONSONANTS)
 
def checkio(text):
    words = re.findall(ur'\b[A-Z][A-Z]+\b', text.upper())
    count = 0
    for word in words:
        if vowels.search(word) or consonants.search(word):
            continue
        count += 1
    return count
 
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
