atrocities-parser
=================

The file spacy\_parser.py contains the function 'atrocities\_parser', which extracts
the date and number of deaths from sentences in Amnesty International reports that mention attacks on civilians.
It takes as its input the filepath of the directory which contains the AI reports
that you want to parse and returns a list with the information that you can then 
convert to a pandas dataframe (my attempts to do this within the function were met
with many angry ascii unicode errors). I used the spaCy NLP library in Python to
write this. 
