import sys

bfTmp = ''
lsOutTmp = []
InFileName = []
lsFileName = []

fileNameIn= sys.argv[1]
fileNameLs= sys.argv[2]
fileNameOu= sys.argv[3]

fo = open(fileNameIn)
InFileName += [x.replace('\n', '').replace('\t', ',') for x in fo.readlines()]
fo.close()

fo = open(fileNameLs)
lsFileName += [x.replace('\n', '') for x in fo.readlines()]
fo.close()

for bfMatName in InFileName:
   blExist = False
   for bfFileName in lsFileName:
      if bfMatName.count(bfFileName)> 0:
         blExist = True
         break

   if blExist == False:
      bfMatName = bfMatName.replace(',Cesante', '')
      arName = bfMatName.split(',')
      lsOutTmp.append('INSERT INTO `matriculados` ( `matricula` , `nombre` , `apellido` , `fantasia` , `direccion` , `cpostal` , `barrio` ) VALUES (' + arName[2] + ', \'' + arName[0] + '\', \'' + arName[1] + '\', \'' + arName[3]+ '\', \'\', \'\', \'\' )')

bufferTmp = '\n'
bufferTmp = bufferTmp.join(lsOutTmp)
fo= open(fileNameOu, 'w')
fo.write(bufferTmp)
fo.close()

