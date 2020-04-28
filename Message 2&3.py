# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:06:09 2020

@author: chaks
"""
 

with open('message3.txt', 'r', encoding="utf8") as f:
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

def dechiffrement_cesar(caractere,chaine):
    number1=ord(' ')-ord(caractere)
    text1=chiffrement_cesar(chaine,number1)
    return text1



print(dechiffrement_cesar(caractere_le_plus_frequent,message))


