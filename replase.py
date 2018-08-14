import os, sys, shutil

inputDir = "."

findStr = r"""/*
    sdfwofgjkwaerfg
    wsef[ksef[p
    wefwpefkw[ef
    we[fpkwef[pkwef
    werfwkef[pwekf
    werfl,wef][,lw
    w'e;flwe][fl
*/"""
repStr = r"""/****************************************
    Hi all!
    flnfvsdogjposj pgopog gpogdfg
    gldfgp;dfgjpodfg
    fgldfg'dpfogk
    w;lfsf;ksd
/****************************************"""
filePath = '../for_test_replase'


def replaceStringInFile(findStr, repStr, filePath):
    "replaces all findStr by repStr in file filePath"
    tempName = filePath + '~~'
    backupName = filePath + '~'
    with open(os.path.join(filePath, 'output.cpp')) as inputFile, open(os.path.join(filePath, 'output.cpp_temp'), 'w') as outputFile:
        inputFile = inputFile.read()

        for thisLine in inputFile:
            outputFile.write(thisLine.replace(findStr, repStr))

    shutil.copy2(filePath, backupName)
    os.rename(tempName, filePath)
    print("file processed: {}".format(filePath))

replaceStringInFile(findStr, repStr, filePath)
