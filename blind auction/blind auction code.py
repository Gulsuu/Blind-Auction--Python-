#from replit import clear bu modül replitte var burda yok
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("WELCOME TO THE BLIND AUCTION!")

others="yes"
dic={}
while others=="yes":
  name=input("What's your name?")
  price=input("What's the bid price?")
  dic[name]=price
  #print(dic)
  others=input("Is there another person who wants to bid?Press yes or no.").lower()
  #if others=="yes":
    #clear() modül replitte var

if others=="no":
  maxx=0
  winner=""
  for key in dic:
    if int(dic[key])>int(maxx):
      maxx=dic[key]
      winner=key
  print(f"The winner of the auction is {winner} with the amount of {maxx}$.")
