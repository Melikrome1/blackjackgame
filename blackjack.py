#function
#rules of game
#dealer
#player
#deck of cards
#cards in deck
# win or loser
#breaks
#if statements
#game loop
#get variables

#import
import random
playerIn = True
dealerIn = True

#deck of cards
deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
        'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A']
playerHand = []
dealerHand = []

#create function1/deal cards
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

#create funtion2/total of each hand
def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 1
        else:
            if total > 11: #greater than 11
                total += 1
            else:
                total += 11 #ace
    return total   

#for winner     
def revealDealerHand ():
    if len(dealerHand) == 2:
        return dealerHand [0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]
    
#create for loop so the game can keep moving
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

while playerIn or dealerIn:
    print(f"Dealer has {revealDealerHand()} and X")
    print(f"You have {playerHand} for a total of {total(playerHand)}")
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealerHand) > 16:
        dealerIn = False
    else:
       dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn = False
    else:
       dealCard(playerHand)
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break
#Determine winner and then print out
    if total(playerHand) == 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack!!! You're a winner!")
    elif total(dealerHand) == 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack!You're a bust! Dealer Wins!")
    elif total(playerHand) > 21:
         print(f"\nYou have {playerHand} for a total of {total(playerHand)} the dealer has {dealerHand} for a total of {total(dealerHand)}")
         print("You bust! Dealer wins!")
    elif total(dealerHand) > 21:
         print(f"\nYou have {playerHand} for a total of {total(playerHand)} the dealer has {dealerHand} for a total of {total(dealerHand)}")
         print("Yay! Dealer busts! You win! Don't forget to tip ;) ")
    #who is closer than 21?
    elif 21 - total(dealerHand) < 21 - total(playerHand):
         print(f"\nYou have {playerHand} for a total of {total(playerHand)} the dealer has {dealerHand} for a total of {total(dealerHand)}")
         print("Dealer wins!")
    elif 21 - total(dealerHand) > 21 - total(playerHand):
         print(f"\nYou have {playerHand} for a total of {total(playerHand)} the dealer has {dealerHand} for a total of {total(dealerHand)}")
