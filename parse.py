from corenlp import *
from nltk import tokenize
import ast

def parser(filename):
    with codecs.open(filename, encoding='utf-8') as f:
        text = f.read().replace('\n',' ') 
    
    text = text.encode('ascii','ignore')
    sentences = tokenize.sent_tokenize(text)
    
    print "loading the parser... may take a few seconds..."
    corenlp = StanfordCoreNLP()

    keywords = {'violence':('killed', 'killing', 'massacred','massacring','executed','executing'), 
                'target':('men','women','civilians','villagers','people'),
                'months':('January','February','March','April','May','June','July','August',
                'September','October','November','December')}
    list_holder=[]
    print "parsing..."
    for sentence in sentences:
        dep = ast.literal_eval(corenlp.parse(sentence))
        for chunk in dep['sentences'][0]['dependencies']:
            if chunk[0] == 'root' and chunk[2] in keywords['violence']:
                for chunk in dep['sentences'][0]['dependencies']:
                    if chunk[0]=='num' and chunk[1] in keywords['target']:
                        kill_dict = {'killed':chunk[2]}
                        for chunk in dep['sentences'][0]['dependencies']:
                            if chunk[2] in keywords['months']:
                                month_dict = {'month':chunk[2]}
                                kill_dict.update(month_dict)
                                list_holder.append(kill_dict)
                                del kill_dict
                                del month_dict
                            else:
                                pass
                    else:
                        pass
            elif chunk[0] == 'dep' and chunk[2] in keywords['violence']:
                for chunk in dep['sentences'][0]['dependencies']:
                    if chunk[0]=='num' and chunk[1] in keywords['target']:
                        kill_dict = {'killed':chunk[2]}
                        for chunk in dep['sentences'][0]['dependencies']:
                            if chunk[2] in keywords['months']:
                                month_dict = {'month':chunk[2]}
                                kill_dict.update(month_dict)
                                list_holder.append(kill_dict)
                                del kill_dict
                                del month_dict
                            else:
                                pass
                    else:
                        pass
            elif chunk[0] == 'dobj' and chunk[1] in keywords['violence']:
                for chunk in dep['sentences'][0]['dependencies']:
                    if chunk[0]=='num' and chunk[1] in keywords['target']:
                        kill_dict = {'killed':chunk[2]}
                        for chunk in dep['sentences'][0]['dependencies']:
                            if chunk[2] in keywords['months']:
                                month_dict = {'month':chunk[2]}
                                kill_dict.update(month_dict)
                                list_holder.append(kill_dict)
                                del kill_dict
                                del month_dict
                            else:
                                pass
                    else:
                        pass
            else:
                pass
    return list_holder

