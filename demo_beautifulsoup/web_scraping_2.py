from bs4 import BeautifulSoup
import re

with open('index2.html') as fp:
    doc = BeautifulSoup(fp,'html.parser')

tag = doc.find('option')
# If you want to change the value of the attributes of the selected tag , we do something like this
tag['value'] = 'new value'
tag['selected'] = 'false'
tag['color'] = 'blue'
print(tag)

# You can also find multiple tags within the first go.
print('\n')
tags = doc.find_all(['p','div','li'])
print(tags)

#You can also do something like this
print('\n')
tags_1 = doc.find_all(['option'] , text = "Undergraduate", value = 'undergraduate')
print(tags_1)

# Let's understand retrieving content from different class names.
print('\n')
tags_2 = doc.find_all(class_='btn-item')
print(tags_2)

# Understanding how we can use regular expressions + fetching all the prices based on the dollar sign.
print('\n')
tags_2 = doc.find_all(text=re.compile("\$.*"))
for t in tags_2 :
    print(t.strip())
# print(tags_2)

# Understanding how to save changes in the actual HTMl files.
tags_3 = doc.find_all("input", type='text')
for tag in tags_3: 
    tag['placeholder'] = 'I changed you !'

# Below code allows us to write the changes in a newly created html file.
with open('changed.html', 'w') as file : 
    file.write(str(doc))