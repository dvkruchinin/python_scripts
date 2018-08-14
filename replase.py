import os, sys, shutil

inputDir = r'D:/python/for_test_replase'

findStr = \
"""
/*
    sdfwofgjkwaerfg
    wsef[ksef[p
    wefwpefkw[ef
    we[fpkwef[pkwef
    werfwkef[pwekf
    werfl,wef][,lw
    w'e;flwe][fl
*/
"""
repStr = \
"""
//****************************************
// Hi all!
// flnfvsdogjposj pgopog gpogdfg
// gldfgp;dfgjpodfg
// fgldfg'dpfogk
// w;lfsf;ksd
//****************************************
"""

def replaceStringInFile(findStr, repStr, inputDir):
    "replaces all findStr by repStr in file filePath"
    for root, dirs, files in os.walk(inputDir):
        for file_name in files:
            if file_name.endswith('.cpp'):
                shutil.copy2(os.path.join(root, file_name), os.path.join(root, file_name + '.bak'))
                #os.rename(os.path.join(root, file_name), os.path.join(root, file_name + '.orig'))

                with open(os.path.join(root, file_name)) as inputFile, open(os.path.join(root, file_name), 'r+') as outputFile:
                    inputFile_read = inputFile.read()

                    for line in inputFile_read:
                        outputFile.write(line.replace(findStr, repStr))

                print("file processed: {}".format(root + r'/' + file_name))

replaceStringInFile(findStr, repStr, inputDir)