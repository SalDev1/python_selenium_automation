from bs4 import BeautifulSoup


# For Parsing the HTML document , pass it into the Beautiful constructor.
# You can pass it in a string or an open filehandle. 

# 1) The document is firstly converted to Unicode and HTML entities are converted to Unicode characters.
# 2) Then it parses the document using the best available parser , mentioned html.parser 
# fp --> file path
with open("index.html") as fp :
    soup = BeautifulSoup(fp , 'html.parser')

# print(soup)

# to beautify your html document which is parsed by beautifulSoup , you can do something like this. 
# print(soup.prettify())

# Finding things with the tag name, head , center , body tag.
tag = soup.title
print(tag)   #It returns the first child of the tag.
print(tag.string)  #It returns the string of the tag.
print("\n")

tag.string = 'hello'  #This allows you to modify the content existing inside of the tag.
print(soup)

# To find all the anchor tags , we do something like this. 
tags_a = soup.find_all("a")  #Returns the array of anchor tags.
print(tags_a)

# to find all the p tags , we do something like this. 
print('\n')
tags_p = soup.find_all('p')
print(tags_p[0].find_all('b'))  #To access nested elements , we do something like this.