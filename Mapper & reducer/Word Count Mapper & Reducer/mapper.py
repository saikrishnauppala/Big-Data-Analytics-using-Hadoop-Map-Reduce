#!/usr/bin/env python
"""mapper.py"""

import sys

import re

from stemming.porter2 import stem

stopwords = ['a', 'an', 'the', 'and', 'is', 'are', 'was', 'were', 'what', 'them', 'had', 'some', 'ca',

             'why', 'when', 'where', 'who', 'whose', 'which', 'that', 'off', 'ever', 'many', 've',

             'those', 'this', 'those', 'but', 'so', 'thus', 'again', 'therefore', 'its', 'both',

             'like', 'in', 'on', 'up', 'down', 'under', 'over', 'i', 'we', 'they', 'while', 'okay',

             'he', 'them', 'their', 'there', 'us', 'of', 'you', 'your', 'us', 'our', 'mine', 'mr',

             'such', 'am', 'to', 'too', 'for', 'from', 'since', 'until', 'between', 'she', 'own',

             'my', 'not', 'if', 'as', 'well', 'youre', 'hadnt', 'havent', 'wont', 'q', 'se', 'ok',

             'very', 'have', 'it', 'be', 'been', 'has', 'having', 'his', 'her', 'never', 'above',

             'should', 'would', 'could', 'just', 'about', 'do', 'doing', 'does', 'did', 'la', 'ha'

             'go', 'going', 'goes', 'being', 'with', 'yes', 'no', 'how', 'before', 'than', 'd',

             'after', 'any', 'here', 'out', 'now', 'then', 'got', 'into', 'all', 'cant', 'or', 'ya',

             'despite', 'beyond', 'further', 'wanna', 'want', 'gonna', 'isnt', 'at', 'also', 'lo',

             'because', 'due', 'heres', 'try', 'said', 'says', 'will', 'shall', 'link', 'asked',

             'more', 'less', 'often', 'lol', 'maybe', 'perhaps', 'quite', 'even', 'him', 'by', 'n',

             'among', 'can', 'may', 'most', 'took', 'during', 'me', 'told', 'might', 'hi', 'es', 'l',

             'theyll', 'use', 'u', 'whats', 'couldnt', 'wouldnt', 'see', 'im', 'dont', 'x', 'de',

             'doesnt', 'shouldnt', 'hes', 'thats', 'let', 'lets', 'get', 'gets', 'en', 'co', 'k',

             'whats', 's', 'say', 'via', 'youll', 'wed', 'theyd', 'youd', 'w', 'm', 'hey', 'hello',

             'youve', 'theyve', 'weve', 'theyd', 'youd', 'ive', 'were', 'ill', 'yet', 'b', 'rt',

             'id', 'o', 'r', 'z', 'um', 'em', 'seen', 'didnt', 'r', 'e', 't', 'c', 'y', 'only', 'v',

             'arent', 'werent', 'hasnt', 'mostly', 'much', 'ago', 'wasnt', 'aint', 'nope', 'p',

             'll', 'ja', 'al', 'el', 'gt', 'cs', 'si', 'didn', 're', 'f', 'fo', 'j', 'ni', 'tr', 'il',"rt","http","https","it","one","two","im","three"]



# input comes from STDIN (standard input)

for line in sys.stdin:

    # remove leading and trailing whitespace

    line = line.strip()

    re.sub(r'[^\w]', ' ', line)

    l1 = [";", ":", "/", "'", "[", "]", "*", "!", "@", "#", "$",

          "%", ",", "^", "&", "*", "(", ")", "_", "-", ".", "+", "?"]

    # split the line into words

    wl = line.split()

    rx = r"[;:\)]+.,*"

    wl = [x.lower() for x in wl]

    wl = [x for x in wl if not any(c.isdigit() for c in x)]

    wl = [i for i in wl if len(i) > 1]

    bl = ['advertise']

    B = re.compile('|'.join([re.escape(word) for word in bl]))

    wl = [word for word in wl if not B.search(word)]

    wl = [x.replace('_', '').replace("", '') for x in wl]

    wl = [x.replace(' ', '').replace("", '') for x in wl]

    wl = [re.sub(rx, "", x) for x in wl]

# increase counters

    for word in wl:

        if word in stopwords:

            continue



    # write the results to STDOUT (standard output);

    # what we output here will be the input for the

    # Reduce step, i.e. the input for reducer.py

    #

    # tab-delimited; the trivial word count is 1

        for i in l1:

            word = word.strip(i)

            word=filter(str.isalnum, word)

        word = stem(word)

        if (len(word.strip())==0):

            continue



        print("%s\t%s" % (word, 1))
        
