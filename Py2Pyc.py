import os
import re
import py_compile

def eachFile(filepath, suffix):
    pathDir =  os.listdir(filepath)
    filesName = []
    for allDir in pathDir:
        if re.compile('.+\.%s$'%suffix).match(allDir):
            filesName.append(allDir.decode('gbk'))
    return filesName

if __name__ == '__main__':
    compilePath = r'C:\Users\sunrise\Desktop\AnyLibrary\Package'
    pycFiles = eachFile(compilePath, 'pyc')
    for fileName in pycFiles:
        os.remove(fileName)
    pyFiles = eachFile(compilePath, 'py')
    for fileName in pyFiles:
        if 'Py2Pyc.py' == fileName:
            continue
        py_compile.compile(fileName)
        os.remove(fileName)
