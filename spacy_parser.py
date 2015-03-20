from __future__ import unicode_literals
import codecs
import os, sys
import pandas as pd
from spacy.en import English
from nltk import tokenize
from datetime import datetime

def atrocities_parser(directory):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    nlp = English()
    
    starttime = datetime.now()

    keywords = {'violence':('killed', 'killing', 'massacred','massacring','executed','executing'), 
                'target':('men','women','civilians','villagers','people'),
                'months':('January','February','March','April','May','June','July','August',
                'September','October','November','December'),
                'numbers':('one','two','three','four','five','six','seven','eight','nine','ten')}

    file_list = []
    for path, subdirs, files in os.walk(directory):
        for name in files:
            if name.endswith((".txt")):
                file_list.append(os.path.join(path,name))

    list_holder = []
    for filename in file_list:
        ## get year and country name from filename ##
        path_split = filename.rsplit('/')[1:] 
        year = path_split[-1][10:14]
        country = path_split[-1][15:-4]

        print 'parsing %s %s...' % (country, year)
        
        ## read in file and do some cleanup ##
        with codecs.open(filename, encoding='utf-8') as f:
            text = f.read().replace('\r\n',' ')
        text = text.replace("\'","'")
        text = text.replace('Q','')
        text = text.replace(';','.')

        ## parse sentence by sentence ##
        sentences = tokenize.sent_tokenize(text)
        for sentence in sentences:
            tokens = nlp(sentence)
            check = 0
            check2 = 0
            check3 = 0
            check4 = 0
            metacheck = 0
            for token in tokens: # begin by checking that the sentence has a month, attack verb, target, and number of dead
                if (token.orth_ in keywords['violence']) and check==0:
                    check+=1
                    metacheck+=1
                    for token in tokens:
                        if token.orth_ in keywords['months'] and check3==0:
                            #print token.orth_
                            check3 += 1
                            metacheck += 1
                        if token.orth_ in keywords['target'] and check2==0:
                            chunk = token.subtree
                            ls=[]
                            metacheck += 1
                            for item in chunk:
                                ls.append(item.orth_)
                            for word in ls:
                                if (word.isdigit() or word in keywords['numbers']) and check4==0:
                                    check2 += 1
                                    metacheck += 1
                                    check4 += 1
                                else:
                                    pass
                        else:
                            pass
                else:
                    pass

            if metacheck==4: # if the sentence has all 4 criteria, parse it
                check = 0
                check2 = 0
                check3 = 0
                check4 = 0
                dict_holder = {}
                dict_holder = {'sentence':sentence, 'country':country, 'year':year}
                for token in tokens:
                    if (token.orth_ in keywords['violence']) and check==0:
                        check+=1
                        for token in tokens:
                            if token.orth_ in keywords['months'] and check3==0:
                                month_dict = {'month':token.orth_}
                                check3 += 1
                                for token in tokens:
                                    if token.orth_ in keywords['target'] and check2==0:
                                        chunk = token.subtree
                                        metacheck += 1
                                        for item in chunk:
                                            ls.append(item.orth_)
                                        for word in ls:
                                            if (word.isdigit() or word in keywords['numbers']) and check4==0:
                                                kill_dict = {'fatalities':word}
                                                check2 += 1
                                                check4 += 1
                                                month_dict.update(kill_dict)
                                                dict_holder.update(month_dict)
                                                list_holder.append(dict_holder)
                                            else:
                                                pass
                                    else:
                                        pass
                            else:
                                pass
                    else:
                        pass
    print(datetime.now()-starttime)
    return list_holder
