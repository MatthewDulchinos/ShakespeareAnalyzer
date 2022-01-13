#Shakespeare analyzer
#By Matthew Dulchinos
#Credit to shakespeare.mit.edu for the scripts

#Global Variables
playFile = 'RandJEntire.txt' #Change this line to whatever play you want to analyze
play = open(playFile,'r')
lineByLine = play.readlines()
playLists = []
name = ""
recordingName=False
speaking=False
statsIndex=[]
peopleTalking = []

def StartOfSceneOrAct(line):
    if len(line) >= 6:
        for letter in line[0:5]:
            if letter != ' ':
                return False
        #print("New Act:",line)
        return True

def StageDirection(line):
    if len(line) >= 5:
        if line[4] == '/':
            #print("Stage Direction:",line)
            return True
        else:
            return False
"""
returns true if the name already exists in the statsIndex
"""
def hasActor(name):
    if len(statsIndex) != 0:
        for actor in statsIndex:
            if actor[0] == name:
                return True
    return False
    
def createActor(name):
    return [name,0,0]
    #[name,words,lines]

def getPos(name):
    pos = 0
    for i in statsIndex:
        if i[0] == name:
            return pos
        pos+=1
    return -1

#Adds a line to the character, using number rep of character
def addLinePos(pos):
    statsIndex[pos][2]+=1

def addWordPos(pos):
    statsIndex[pos][1]+=1
    


#print (lineByLine)
for line in lineByLine:
    if line[0]=='*':
        #print("Starting a new person")
        
        peopleTalking=[]
        for letter in line:
            if recordingName:
                name += letter
                if letter == '*':
                    recordingName=False
                    if not hasActor(name):
                        statsIndex.append(createActor(name))
                    nPos = getPos(name)
                    peopleTalking.append(nPos)
                    addLinePos(nPos)
                    name = ""
                    #print(name)
                    #name = ""
                    #activate recording software
            else:
                if letter == '*':
                    name += letter
                    recordingName=True
    elif (not StartOfSceneOrAct(line)) and (not StageDirection(line)):
        words=line.split()
        for word in words:
            for x in peopleTalking:
                addWordPos(x)
            #print(word)
        #print("!!!!!!!!!!!!!!!!!!!!!!")
        #print(line)
        

print (statsIndex)
for actor in statsIndex:
    print(str(actor[0])+" Words:"+str(actor[1])+" Lines:"+str(actor[2])+" Avg:"+str(actor[1]/actor[2]))
