import csv

resultArray = []
masterDoc = open('master.csv') # this is main doc.
resultDoc = open('results.csv', 'w') # this is where the results will go
playerDoc = open('players.csv', 'w') # this is just a raw list of all entities
masterDoc = csv.reader(masterDoc)
csvWriter = csv.writer(resultDoc)
playercsvWriter = csv.writer(playerDoc)


class ent(object):
    def __init__(self, name, deps, label, publisher, rroName, level1, level2, level3):
        self.name = name
        self.deps = deps
        self.deprep = []
        self.label = label
        self.deprep2 = []
        self.publisher = publisher
        self.rroName = rroName
        self.level1 = level1
        self.level2 = level2
        self.level3 = level3

    def gendepRep(self):
        for x in self.deps:
            if x != '':
                self.deprep.append(str(self.label + ", " + x))


        evencount = 0
        for x in self.deprep:
            self.deprep2.append([self.deprep[(evencount)]])
            evencount +=1


        return self.deprep2


def entCreator(primaryDoc):  # TODO: extend entcreator to fill out ent deets.

    entcreatorCounter = 0
    entContainer = []
    for line in masterDoc:
        deps =line[7]

        deparray = deps.split(',')




        entContainer.append(ent(entcreatorCounter, deparray, line[2], line[0]))
        entcreatorCounter +=1
    for x in entContainer:
       print(x.gendepRep())



entCreator(masterDoc)






