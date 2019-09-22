text = "Nowadays solar energy is widely used as an alternative form of power. Solar panels transform the energy from the sun into electricity. The first plane that does not need fuel was constructed in France, in 2015. It uses only the sun's energy. The panels are placed on the huge wings of the plane. It doesn’t fly very fast. Solar energy can make the plane move at only 140 miles an hour. However, the plane is able to travel round the world. It is safe and can successfully cross areas of bad weather. In the future, engineers hope to construct a model that people can fly in. Our dream of environmentally friendly transport may come true very soon. Would you like to take a flight on the solar plane?"
dict1 = {}

def calculate_frequences(text):
    text = text.lower()
    alf = 'abcdefghijklmnopqrstuvwxyz '
    for sym in text:
        if sym not in alf: 
            text = text.replace (sym, "")
    text = text.split (' ')
    for word in text:
        if word not in dict1:
            dict1 [word] = 1
        else:
            dict1 [word] = dict1 [word] +1 


stop_words = ('an', 'a', 'the')
frequencies = {}

def filter_stop_words (frequencies, stop_words):
    for elm in dict1:
        if elm not in stop_words:
            frequencies [elm] = dict1 [elm]
           


top_n = 9
toplist = []
def get_top_n(frequencies, top_n):
    toplist = list(frequencies.items())
    toplist.sort(key = lambda i: i[1])
    toplist.reverse()
    toplist1 = []
    for elm in toplist:
        toplist1 += elm
        top_n -= 1
        if top_n == 0:
            break
    for elm in toplist1:
        if type(elm) is int:
            toplist1.remove(elm)
    toplist1 = tuple(toplist1)
    print (toplist1)
  
    


calculate_frequences(text)
filter_stop_words (frequencies, stop_words)
get_top_n (frequencies, top_n)
