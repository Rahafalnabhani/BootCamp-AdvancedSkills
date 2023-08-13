#Use Filter/lambda to find a list of words including substring ‘cat’
#Example a = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]
#Result = ['cat', 'wildcat', 'thundercat']
#Hint use: re.compile(pattern, flags=0) , you need to import re
# Search and match

import re
List= ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]
re = re.compile(r'cat')

#using filters:
s = list(filter(lambda n : re.search(n) , (List)))
print ("Filters : ",s)