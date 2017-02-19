import csv

# Imports and setting up work
resultArray = []
masterDoc = open('master.csv') # this is main doc.
resultDoc = open('results.csv', 'w') # this is where the results will go
playerDoc = open('players.csv', 'w') # this is just a raw list of all entities
masterDoc = csv.reader(masterDoc)
csvWriter = csv.writer(resultDoc)
playercsvWriter = csv.writer(playerDoc)



class ent(object):
    def __init__(self):
        self.name = ''
        self.deps =  ''
        self.deprep = []

    def gendepRep(self):
        for x in self.deps:
            self.deprep.append(self.label+ ", "+ x)
        return self.deprep





def entCreator(primaryDoc):
    entContainer = [ent() for x in range(len(primaryDoc))]
    entcreatorCounter = 0
    for line in masterDoc:
        


















def initialDataParse(masterDoc): # Initial Readout of the data
    for line in masterDoc:

        playercsvWriter.writerow([line[2]])
        dependencyArray = []
        dependencyArray.append(line[7])
        resultArray.append(line[2])
        resultArray.append(dependencyArray)
    return resultArray


def edgeListWriter(resultArray):
    sourceTartget = []
    for x in resultArray:


        if resultArray.index(x) % 2 != 0:
            for dependency in x:
                sourceTartget.append(resultArray[(resultArray.index(x)-1)])
                sourceTartget.append(dependency)
    return sourceTartget


def edgeCSVwriter(sourceTarget, csvWriter):
    csvWriter.writerow(['Source','Target'])
    for x in sourceTarget:
        if x != '' and (sourceTarget.index(x) % 2 == 0):
            lars = sourceTarget[sourceTarget.index(x) + 1]
            if lars != '':
              larsArray = lars.split(',')
              for dan in larsArray:
                 csvWriter.writerow([x, dan])


def playerCSV(masterDoc2, playercsvWriter):
    playerMaster = open('master.csv')
    playerMaster = csv.reader(playerMaster)

    for line in playerMaster:
        print(line[4])
        print(line[2])
        print('i am a pretty boy')
        playercsvWriter.writerow(line[2])

def getFileName():
    tli_name = input("What is the name of the file you would like to work with? ")
    return tli_name




def sequence(masterDoc, resultDoc, playerDoc, csvWriter, playercsvWriter):
    fileName = getFileName()
    #TODO: move all file assignment stuff here


    masterDoc2 = masterDoc
    resultArray = initialDataParse(masterDoc)
    sourceTarget = edgeListWriter(resultArray)
    edgeCSVwriter(sourceTarget, csvWriter)
    playerCSV(masterDoc2, playercsvWriter)

sequence(masterDoc, resultDoc, playerDoc, csvWriter, playercsvWriter)


