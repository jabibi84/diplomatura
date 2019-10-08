# Match dates formatted like MM/DD/YYYY, MM-DD-YY,...
import re

date = '12/30/1969'
regex = re.compile(r'^(\d\d)[-/](\d\d)[-/](\d\d(?:\d\d)?)$')
match = regex.match(date)
if match:
    month = match.group(1)
    day = match.group(2)
    year = match.group(3)

    print(year)
