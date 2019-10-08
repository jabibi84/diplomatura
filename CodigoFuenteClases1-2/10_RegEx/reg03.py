#Convert <br> to <br /> for XHTML compliance
import re

text  = 'Hello world. <br>'
regex = re.compile(r'<br>', re.IGNORECASE);
repl  = r'<br />'
result = regex.sub(repl,text)
print(result)