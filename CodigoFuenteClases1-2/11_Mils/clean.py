#C:\utils\Python\Python27\python.exe incompletosClean.py incompletos\inc.dat incompletos\out.dat

import sys
import os
import os.path

bfTmp = ''
lsOutTmp = []
InFileName = []
lsHTMLName = []

fileNameIn= sys.argv[1]
fileNameOu= sys.argv[2]

fo = open(fileNameIn)
InFileName += [x.replace('\n', '') for x in fo.readlines()]
fo.close()

for bfMatFile in InFileName:
   if os.path.isfile(bfMatFile):
      lsHTMLName = []
      fo = open(bfMatFile)
      lsHTMLName += [x.replace('\n', '') for x in fo.readlines()]
      fo.close()

      bfRow = ''
      for rowHTML in lsHTMLName:
          iPosic = rowHTML.find('<td><p>')
          if iPosic > 0:
             bfRowPart = rowHTML[iPosic + len('<td><p>'):]
             bfRow += ((bfRowPart[:bfRowPart.index('</p></td>')] + ',').replace('&nbsp;', ',')).strip()

      if bfRow != '':
          lsOutTmp.append(bfRow[:len(bfRow)-1] + ';')

bufferTmp = '\n'
bufferTmp = bufferTmp.join(lsOutTmp)
fo= open(fileNameOu, 'w')
fo.write(bufferTmp)
fo.close()

