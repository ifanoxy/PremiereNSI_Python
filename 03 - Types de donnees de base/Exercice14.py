# Écrivez un script qui recopie une chaîne (dans une nouvelle variable)
# en insérant des astérisques entre les caractères.
# Ainsi par exemple, « frénétique » devra devenir « f*r*é*n*é*t*i*q*u*e » .

phrase = input('Entre une phrase')
newPhrase = ""

for lettre in phrase:
    newPhrase += lettre
    if(lettre != " "):
        newPhrase +=  "*"

print(newPhrase)
