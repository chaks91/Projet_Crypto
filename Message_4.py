

with open('message4.txt', 'r', encoding="utf8") as f:
    message = f.read()


def lettre_plus_frequente2(chaine):
    piles = {}
    for c in chaine:
        if c in piles:
            piles[c] += 1
        else :
            piles[c] = 1
    valeur_max = 0
    indice_max=''
    for c in piles:
        if piles[c] > valeur_max :
            valeur_max = piles[c]
            indice_max = c
    return indice_max

caractere_le_plus_frequent = lettre_plus_frequente2(message)
#print(caractere_le_plus_frequent)


def decaler2(caractere, decalage):
    decalage_code_caractere=ord(caractere) + decalage
    return chr(decalage_code_caractere)


def chiffrement_cesar(chaine,clé):
    chaine_vide=''
    for c in chaine:
        k = decaler2(c,clé)
        chaine_vide+=k
    return chaine_vide

def dechiffrement_cesar(chaine):
    caractere=lettre_plus_frequente2(chaine)
    number1=ord(' ')-ord(caractere)
    text1=chiffrement_cesar(chaine,number1)
    return text1



#print(dechiffrement_cesar(message))
    



def separation(chaine):
    chaine_vide1=''
    chaine_vide2=''
    chaine_dechiffrer_final=''
    for i in range (len(chaine)):
        if i%2==0:
            chaine_vide1+=chaine[i]
        else:
            chaine_vide2+=chaine[i]
    #On a deux chaine, avec une clé pour chaque chaîne
    chaine1_dechiffré = dechiffrement_cesar(chaine_vide1)
    chaine2_dechiffré = dechiffrement_cesar(chaine_vide2)
    for i in range(len(chaine1_dechiffré)):
        chaine_dechiffrer_final+=chaine1_dechiffré[i] + chaine2_dechiffré[i]        
    return chaine_dechiffrer_final

           
    

print(separation(message))
