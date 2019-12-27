from primeNums import liste
import random

#choose a prime num diffrent than other
def nbPremierDiff(src) :
  dest = liste[r.randrange(len(liste))]
  while src == dest:
    dest = liste[r.randrange(len(liste))]
  return dest

def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b

def euclide_etendu(e, phi_n) :
  d = 1 
  temp = (e*d)%phi_n
  while(temp != 1):
    d = d+1
    temp = (e*d)%phi_n
  return d

def chiffrer(message, e, n):
  i=0
  message_chiffre = ""
  while i != len(message):
    bloc = str(pow(ord(message[i]), e)%n)

    while (len(bloc) != 6):
      bloc = "0" + bloc
    message_chiffre = message_chiffre + bloc
    i = i + 1
  return message_chiffre
# Dechiffrement du message  
def dechiffrer(message_chiffre, d, n):
  i=0
  bloc=""
  message_dechiffre = ""
  while i != len(message):
    bloc = bloc + message[i]
    if (len(bloc)==6):
      #print bloc
      bloc = pow(int(bloc), d)%n
      message_dechiffre = message_dechiffre + chr(bloc)
      bloc = ""
    i = i + 1
  return message_dechiffre
#Menu
choix = input(' \na.Chiffrer\nb.Dechiffrer\nchoisir une operation : ')
while choix != "a" and choix != "b" :
  choix = input('\noperation non valide , entrez soit 1 ou 2 : ')
# Chiffrement
if choix=="a":
  message = input('\n entrez le message à chiffrer : ')
  print ("\n...\n")
  # Generation de p et q
  r = random.SystemRandom()
  p =liste[r.randrange(len(liste))]
  q = nbPremierDiff(p)
  n = p * q
  phi_n = (p-1)*(q-1)
  #Choix d'un exposant e et calcul de son inverse d
  e = r.choice(liste)
  d = euclide_etendu(e, phi_n)
  print ("Cle publique :", e, "\nModulo :", n,"\nCle prive :", d)
  # n et e = cle publique, d = cle prive
  print ("\nMessage apres le chiffrement:\n", chiffrer(message, e, n))
 #Dechiffrement
else:
  message = input('\n entrez  le message à dechiffrer : ')
  d = input('entrez cle prive : ')
  n = input('entrez le modulo : ')
  message = dechiffrer(message, int(d), int(n))
  print ("\nMessage apres le dechiffrement:\n", message)