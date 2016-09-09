atrocities-parser
=================

The file spacy\_parser.py contains the function 'atrocities\_parser', which extracts
the date and number of deaths from sentences in Amnesty International reports that mention attacks on civilians.
It takes as its input the filepath of the directory which contains the AI reports
that you want to parse and returns the information in a list formate (which can then
be converted to a pandas dataframe or something similar).

Example

```python
from spacy_parser import atrocities_parser

dir = '/path/to/amnestyreports'

atrocities_parser(dir)
```
