with open('message3.txt', 'r') as f:
    message = f.read()

"""

def separation(chaine):
    chaine_vide1=''
    chaine_vide2=''
    #chaine_vide_final=''
    for i in range (len(chaine)):
        if i%2==0:
            chaine_vide1+=chaine[i]
        else:
            chaine_vide2+=chaine[i]
    
    return dechiffrement_cesar(,chaine_vide1), dechiffrement_cesar(,chaine_vide2)
    """
#print(separation(message))


def decaler2(caractere, decalage):
    code_caractere=ord(caractere)
    decalage_code_caractere=max(code_caractere + decalage,ord(' '))
    return chr(decalage_code_caractere)
    
    
def chiffrement_cesar(chaine,clé):
    chaine_vide=''
    for c in chaine:
        k = decaler2(c,clé)
        chaine_vide+=k
    return chaine_vide

def lettre_plus_frequente2(chaine):
    piles = {}
    for c in chaine:
        if c in piles:
            piles[c] += 1
        else :
            piles[c] = 1
    valeur_max = 0
    indice_max = ''
    for c in piles:
        if piles[c] > valeur_max :
            valeur_max = piles[c]
            indice_max = c
    return indice_max


print(lettre_plus_frequente2(message))


"""
def lettre_plus_frequente(chaine):
    occurs = {}
    for lettre in chaine.lower():
        occurs[lettre] = chaine.count(lettre)
    return {lettre: occurrences for lettre, occurrences in occurs.items()
                                if occurrences == max(occurs.values())
"""


def dechiffrement_cesar(caractere,chaine):
    number1=ord(' ')-ord(caractere)
    """number2=ord('e')-ord(caractere)
    number3=ord('i')-ord(caractere)
    number4=ord('o')-ord(caractere)
    number5=ord('u')-ord(caractere)"""
    text1=chiffrement_cesar(chaine,number1)
    """text2=chiffrement_cesar(chaine,number2)
    text3=chiffrement_cesar(chaine,number3)
    text4=chiffrement_cesar(chaine,number4)
    text5=chiffrement_cesar(chaine,number5)  """  
    return text1#, text2, text3, text4, text5

print(fonction('ħ',message))

"""
def dechiffrement_cesar2(chaine,clé):
    message=''
    for c in chaine:
        k=chiffrement_cesar(c,clé)-(2*clé)
        message+=k
    return message

#print(dechiffrement_cesar('a',))
