
def writeFile(fileName, input):
    import os
    if os.path.exists(fileName):
        os.remove(fileName)
        print("//Trashed old file!//")
        print("//Generating new file!//\n")
    else:
        print("//Generating new file!//\n")
    f = open(fileName, "w")
    f.write(input)
    f.close

def readFile(fileName, emptyList):
    source = open(fileName, "r")
    for x in source:
        if x.strip("\n") != "":
            emptyList.append(x.strip("\n"))
    source.close()
    emptyList.pop(1)
    return(emptyList)


