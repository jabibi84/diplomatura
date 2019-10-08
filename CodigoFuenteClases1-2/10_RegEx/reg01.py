#Find Spider-Man, Spiderman, SPIDER-MAN, etc.
import re

dailybugle = 'Spider-Man Menaces City!'
pattern    = r'spider[- ]?man.'

if re.match(pattern, dailybugle, re.IGNORECASE):
    print(dailybugle)


