import os
from spacy.en import English
from datetime import datetime

def atrocities_parser(directory):
    nlp = English()
    
    starttime = datetime.now()

    keywords = {'violence':('killed', 'killing', 'massacred','massacring','executed','executing'), 
                'target':('men','women','civilians','villagers','people'),
                'months':('January','February','March','April','May','June','July','August',
                'September','October','November','December'),
                'numbers':('one','two','three','four','five','six','seven','eight','nine','ten')}
    catch_words = ['anniversary','domestic','sentenced','condemned','trial','partner','partners','questioned',
                    'court','sentencing','sentences','sentence','charges','charged','charge','stalking']
    years = range(1950,2015,1)
    file_list = []
    for path, subdirs, files in os.walk(directory):
        for name in files:
            if name.endswith((".txt")):
                file_list.append(os.path.join(path,name))

    list_holder = []
    for filename in file_list:
        ## get year and country name from filename ##
        path_split = filename.rsplit('/')[1:] 
        year = path_split[-1][3:7]
        country = path_split[-1][8:-4]

        print('parsing %s %s...' % (country, year))
        
        ## read in file and do some cleanup ##
        with open(filename, encoding='utf-8') as f:
            text = f.read().replace('\n',' ')

        ## parse sentence by sentence ##
        doc = nlp(text)
        sentences = []
        for span in doc.sents:
            sent = ''.join(doc[i].string for i in range(span.start,span.end)).strip()
            sentences.append(sent)
        for sentence in sentences:
            tokens = nlp(sentence)
            check = 0
            viol_check = 0
            num_check = 0
            tar_check = 0
            month_check = 0
            dict_holder = {}
            dict_holder = {'sentence':sentence, 'country':country, 'year':int(year)-1}
            for token in tokens:
                if token.orth_.isdigit():
                    if int(token.orth_) in years and int(token.orth_) != (int(year)-1):
                        check += 5
                if token.orth_ in catch_words:
                    check += 5
                if (token.orth_ in keywords['violence']) and check==0:
                    viol_check += 1
                    for token in tokens:
                        if token.orth_ in keywords['months'] and month_check==0:
                            month_dict = {'month':token.orth_}
                            month_check += 1
                            for token in tokens:
                                if token.orth_ in keywords['target'] and tar_check==0:
                                    chunk = token.subtree
                                    tar_check += 1
                                    ls = []
                                    for item in chunk:
                                        ls.append(item.orth_)
                                    for word in ls:
                                        if (word.isdigit() or word in keywords['numbers']) and num_check==0:
                                            kill_dict = {'fatalities':word}
                                            tar_check += 1
                                            num_check += 1
                                            month_dict.update(kill_dict)
                                            dict_holder.update(month_dict)
                                            list_holder.append(dict_holder)
    print(datetime.now()-starttime)
    return list_holder

