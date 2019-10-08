#urlify - turn URLs into HTML links
import re

text = 'Check the web site, http://www.oreilly.com/catalog/regexppr.'

pattern = r'''
        \b # start at word boundary
        (                           # capture to \1
        (https?|telnet|gopher|file|wais|ftp) :
                                    # resource and colon
        [\w/#~:.?+=&%@!\-] +?       # one or more valid chars
                                    # take little as possible
)
        (?=                         # lookahead
        [.:?\-] *                   #  for possible punc
        (?: [^\w/#~:.?+=&%@!\-]     #  invalid character
        | $ )                       #  or end of string
        )'''
        
regex = re.compile(pattern,  re.IGNORECASE + re.VERBOSE)
result = regex.sub(r'<a href="\1">\1</a>', text)
print(result)