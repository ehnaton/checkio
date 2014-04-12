import re
from collections import Counter
 
def checkio(text):
    #lower() method didn't work at the time	
    words = re.findall(ur'\b[A-Z][A-Z]*?\b', text.upper())
    s = ''.join([letter for word in words for letter in word])
 
    if len(s) > 1:
        return Counter(s).most_common()[0][0].lower()
    return s.lower()
 
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
