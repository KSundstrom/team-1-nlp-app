from urllib import request    
import re

url = "https://www.gutenberg.org/cache/epub/1041/pg1041.txt"
html = request.urlopen(url).read().decode('utf8')

newlines_removed = html.replace("\r\n", "#")

pattern = '((?#*)[IVXLC]+#+)'
sonnets = re.split(pattern, newlines_removed)

previous_line = ""
with_title = []
for poem in sonnets:
    without_title = poem.replace("#", "")
    if previous_line:
        poem_with_title = previous_line.append(without_title)
        previous_line = ""
        with_title.append(poem_with_title)
                              
    
print(with_title) 

