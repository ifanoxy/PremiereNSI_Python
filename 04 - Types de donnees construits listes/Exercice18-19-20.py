fichier = open("prenom.txt", "r", encoding='utf-8').read()

class Tri: 
    def ordreAlphabetique(str):
        spaceTable = []
        for name in str.split():
            spaceTable.append(name)
        
        for i in range(len(spaceTable)):
            dejaTrier = True
            for j in range(len(spaceTable) - i - 1):
                if spaceTable[j] > spaceTable[j+1]:
                    spaceTable[j], spaceTable[j+1] = spaceTable[j+1], spaceTable[j]
                    dejaTrier = False
            if dejaTrier:
                break

        return " ".join(spaceTable)
    def ordreAlphabetiqueInverse(str):
        spaceTable = []
        for name in str.split():
            spaceTable.append(name)
        
        for i in range(len(spaceTable)):
            dejaTrier = True
            for j in range(len(spaceTable) - i - 1):
                if spaceTable[j] < spaceTable[j+1]:
                    spaceTable[j], spaceTable[j+1] = spaceTable[j+1], spaceTable[j]
                    dejaTrier = False
            if dejaTrier:
                break

        return " ".join(spaceTable)
    def NombreCaracteres(str):
        spaceTable = []
        for name in str.split():
            spaceTable.append(name)
        
        for i in range(len(spaceTable)):
            dejaTrier = True
            for j in range(len(spaceTable) - i - 1):
                if len(spaceTable[j]) > len(spaceTable[j+1]):
                    spaceTable[j], spaceTable[j+1] = spaceTable[j+1], spaceTable[j]
                    dejaTrier = False
            if dejaTrier:
                break

        return " ".join(spaceTable)
    
    def NombreCaracteresInverse(str):
        spaceTable = []
        for name in str.split():
            spaceTable.append(name)
        
        for i in range(len(spaceTable)):
            dejaTrier = True
            for j in range(len(spaceTable) - i - 1):
                if len(spaceTable[j]) < len(spaceTable[j+1]):
                    spaceTable[j], spaceTable[j+1] = spaceTable[j+1], spaceTable[j]
                    dejaTrier = False
            if dejaTrier:
                break

        return " ".join(spaceTable)

open('prenomTrié.txt', "w", encoding='utf-8').write(Tri.ordreAlphabetique(fichier))
