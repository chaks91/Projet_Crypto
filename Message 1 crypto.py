with open('message1.txt', 'r') as f:
    message = f.read()


def decaler2(caractere, decalage):
    code_caractere=ord(caractere)
    decalage_code_caractere=code_caractere + decalage
    return chr(decalage_code_caractere)
    
    
def chiffrement_cesar(chaine,clé):
    chaine_vide=''
    for c in chaine:
        k = decaler2(c,clé)
        chaine_vide+=k
    return chaine_vide



def lettre_plus_frequente(chaine):
    occurs = {}
    for lettre in chaine.lower():
        occurs[lettre] = chaine.count(lettre)
    return {lettre: occurrences for lettre, occurrences in occurs.items()
                                if occurrences == max(occurs.values())}

def fonction(caractere,chaine):
    number1=ord('a')-ord(caractere)
    number2=ord('e')-ord(caractere)
    number3=ord('i')-ord(caractere)
    number4=ord('o')-ord(caractere)
    number5=ord('u')-ord(caractere)
    text1=chiffrement_cesar(chaine,number1)
    text2=chiffrement_cesar(chaine,number2)
    text3=chiffrement_cesar(chaine,number3)
    text4=chiffrement_cesar(chaine,number4)
    text5=chiffrement_cesar(chaine,number5)    
    return text1, text2, text3, text4, text5

print(fonction(' ',message))


def dechiffrement_cesar(chaine,clé):
    message=''
    for c in chaine:
        k=chiffrement_cesar(c,clé)-(2*clé)
        message+=k
    return message

print(dechiffrement_cesar('a',))
