#C:\utils\Python\Python27\python.exe insertMat.py nuevos\out.dat nuevos\insert.dat

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
    arRow = (bfMatFile.replace(';', '')).split(',')
    bfTmp = 'INSERT INTO `matriculados`(`matricula`, `nombre`, `apellido`, `fantasia`, `direccion`, `cpostal`, `barrio`) VALUES '
    bfTmp += '(' + arRow[0] + ',\'' + arRow[3] + '\',\'' + arRow[2] + '\',\'' + arRow[1] + '\',\'' + arRow[5] + '\',\'\', \'\');'
    lsOutTmp.append(bfTmp)

bufferTmp = '\n'
bufferTmp = bufferTmp.join(lsOutTmp)
fo= open(fileNameOu, 'w')
fo.write(bufferTmp)
fo.close()

