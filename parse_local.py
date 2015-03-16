from corenlp import *
from nltk import tokenize
from datetime import datetime
import os,sys
import ast
import codecs
import pandas as pd
import multiprocessing as mp


def parser(files):
    starttime = datetime.now()
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print "loading the parser... may take a few seconds..."
    corenlp = StanfordCoreNLP()
    keywords = {'violence':('killed', 'killing', 'massacred','massacring','executed','executing','attacked'), 
                'target':('men','women','civilians','villagers','people'),
                'months':('January','February','March','April','May','June','July','August',
                'September','October','November','December')}
    list_holder=[]
    for filename in files:
        with codecs.open(filename, encoding='utf-8') as f:
            text = f.read().replace('\r\n',' ') 
        
        text = text.replace("\'","'")
        text = text.replace('Q','')
        text = text.replace('(','')
        text = text.replace(')','')
        #text = text.encode('ascii','ignore')
        text = text.replace('"','')
        text = text.replace('[','')
        text = text.replace(']','')
        text = text.replace(';',',')
        sentences = tokenize.sent_tokenize(text)

        print('parsing %s' % filename[75:])
        try:
            for sentence in sentences:
                sentence_holder = []
                try:
                    dep = ast.literal_eval(corenlp.parse(sentence))
                    try:
                        for chunk in dep['sentences'][0]['dependencies']:
                            if chunk[0] == 'root' and chunk[2] in keywords['violence']:
                                for chunk in dep['sentences'][0]['dependencies']:
                                    if chunk[0]=='num' and chunk[1] in keywords['target']:
                                        kill_dict = {'killed':chunk[2]}
                                        for chunk in dep['sentences'][0]['dependencies']:
                                            if chunk[2] in keywords['months']:
                                                dict_holder = {'country':filename[80:-4], 'year':filename[75:79]}
                                                month_dict = {'month':chunk[2]}
                                                try:
                                                    kill_dict.update(month_dict) #here1
                                                except NameError:
                                                    kill_dict = {'killed':'0','month':'NA'}
                                                kill_dict.update(month_dict)
                                                dict_holder.update(kill_dict)
                                                list_holder.append(dict_holder)
                                                del kill_dict
                                                del month_dict
                                                del dict_holder
                                                sentence_holder.append(sentence)
                                            else:
                                                pass
                                    else:
                                        pass
                            elif sentence not in sentence_holder and chunk[0] == 'root' and chunk[2] in keywords['target']:
                                for chunk in dep['sentences'][0]['dependencies']:
                                    if chunk[0] == 'num' and chunk[1] in keywords['target']:
                                        kill_dict = {'killed':chunk[2]}
                                        for chunk in dep['sentences'][0]['dependencies']:
                                            if chunk[2] in keywords['months']:
                                                dict_holder = {'country':filename[80:-4], 'year':filename[75:79]}
                                                month_dict = {'month':chunk[2]}
                                                try:
                                                    kill_dict.update(month_dict) #here1
                                                except NameError:
                                                    kill_dict = {'killed':'0','month':'NA'}
                                                kill_dict.update(month_dict)
                                                dict_holder.update(kill_dict)
                                                list_holder.append(dict_holder)
                                                del kill_dict
                                                del month_dict
                                                del dict_holder
                                                sentence_holder.append(sentence)
                                            else:
                                                pass
                                    else:
                                        pass
                            elif sentence not in sentence_holder and chunk[0] == 'dep' and chunk[2] in keywords['violence']:
                                for chunk in dep['sentences'][0]['dependencies']:
                                    if chunk[0]=='num' and chunk[1] in keywords['target']:
                                        kill_dict = {'killed':chunk[2]}
                                        for chunk in dep['sentences'][0]['dependencies']:
                                            if chunk[2] in keywords['months']:
                                                dict_holder = {'country':filename[80:-4], 'year':filename[75:79]}
                                                month_dict = {'month':chunk[2]}
                                                try:
                                                    kill_dict.update(month_dict) #here1
                                                except NameError:
                                                    kill_dict = {'killed':'0','month':'NA'}
                                                kill_dict.update(month_dict)
                                                dict_holder.update(kill_dict)
                                                list_holder.append(dict_holder)
                                                del kill_dict
                                                del month_dict
                                                del dict_holder
                                                sentence_holder.append(sentence)
                                            else:
                                                pass
                                    else:
                                        pass
                            elif sentence not in sentence_holder and chunk[0] == 'dobj' and chunk[1] in keywords['violence']:
                                for chunk in dep['sentences'][0]['dependencies']:
                                    if chunk[0]=='num' and chunk[1] in keywords['target']:
                                        kill_dict = {'killed':chunk[2]}
                                        for chunk in dep['sentences'][0]['dependencies']:
                                            if chunk[2] in keywords['months']:
                                                dict_holder = {'country':filename[80:-4], 'year':filename[75:79]}
                                                month_dict = {'month':chunk[2]}
                                                try:
                                                    kill_dict.update(month_dict) #here1
                                                except NameError:
                                                    kill_dict = {'killed':'0','month':'NA'} #here3
                                                dict_holder.update(kill_dict)
                                                list_holder.append(dict_holder)
                                                del kill_dict
                                                del month_dict
                                                del dict_holder
                                                sentence_holder.append(sentence)
                                            else:
                                                pass
                                    else:
                                        pass
                            elif sentence not in sentence_holder and chunk[0] == 'nsubjpass' and chunk[1] in keywords['violence'] and chunk[2] in keywords['target']:
                                for chunk in dep['sentences'][0]['dependencies']:
                                    if chunk[0]=='num' and chunk[1] in keywords['target']:
                                        kill_dict = {'killed':chunk[2]}
                                        for chunk in dep['sentences'][0]['dependencies']:
                                            if chunk[2] in keywords['months']:
                                                dict_holder = {'country':filename[80:-4], 'year':filename[75:79]}
                                                month_dict = {'month':chunk[2]}
                                                try:
                                                    kill_dict.update(month_dict) #here1
                                                except NameError:
                                                    kill_dict = {'killed':'0','month':'NA'} #here3
                                                kill_dict.update(month_dict)
                                                dict_holder.update(kill_dict)
                                                list_holder.append(dict_holder)
                                                del kill_dict
                                                del month_dict
                                                del dict_holder
                                                sentence_holder.append(sentence)
                                            else:
                                                pass
                                    else:
                                        pass
                            elif sentence not in sentence_holder and chunk[0] == 'root' and chunk[2] == 'reported':
                                for chunk in dep['sentences'][0]['dependencies']:
                                    if chunk[0] == 'nsubj' and chunk[1] in keywords['violence']:
                                        for chunk in dep['sentences'][0]['dependencies']:
                                            if chunk[0] == 'num' and chunk[1] in keywords['target']:
                                                kill_dict = {'killed':chunk[2]}
                                                for chunk in dep['sentences'][0]['dependencies']:
                                                    if chunk[2] in keywords['months']:
                                                        dict_holder = {'country':filename[80:-4], 'year':filename[75:79]}
                                                        month_dict = {'month':chunk[2]}
                                                        try:
                                                            kill_dict.update(month_dict) #here1
                                                        except NameError:
                                                            kill_dict = {'killed':'0','month':'NA'} #here3
                                                        kill_dict.update(month_dict)
                                                        dict_holder.update(kill_dict)
                                                        list_holder.append(dict_holder)
                                                        del kill_dict
                                                        del month_dict
                                                        del dict_holder
                                                        sentence_holder.append(sentence)
                                                    else:
                                                        pass
                                            else:
                                                pass
                                    else:
                                        pass

                            else:
                                pass
                    except (IndexError, KeyError):
                        pass
                except (IndexError, KeyError):
                    pass
        except (IndexError, KeyError):
            pass
    df=pd.DataFrame(list_holder)
    df.to_csv('deaths.csv', index=False)
    print(datetime.now()-starttime)
    return list_holder

