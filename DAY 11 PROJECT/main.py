############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.



### Program
### Trying to do the game without any hints :--)


### Score calculator
def calculate_scores(list = []):
    suma = 0  
    is_ace = 0
    for i in range(0, len(list)):
        if list[i] == 11:
            is_ace = 1
        suma += list[i]

    if suma > 21 and is_ace == 1:
        suma -= 10
      
    return suma

### Decide the result of the game
def winner_decider(a, b):
    ## a is user
    ## b is comp
    user = 'User'
    comp = 'Computer'
  
    if a > 21 and b > 21:
        print (user, ' and ', comp, ' both lost.')
    elif a > 21 and b <= 21:
        print (f'The winner is {comp}')
    elif a <= 21 and b > 21:
        print (f'The winner is {user}')
    elif a > b:
        print (f'The winner is {user}')
    elif b > a:
        print (f'The winner is {comp}')
    else:
        print('Not defined winner.')
      

import random 

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   
print(logo)

computer_cards= []
user_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
loop_stopper = False
computer_ended = False

st_card = cards[random.randint(0, len(cards) - 1)]
nd_card = cards[random.randint(0, len(cards) - 1)]
rd_card = cards[random.randint(0, len(cards) - 1)]
th_card = cards[random.randint(0, len(cards) - 1)]

user_cards.append(st_card)
user_cards.append(nd_card)
computer_cards.append(rd_card)

while loop_stopper is not True:

    print("Your cards:", user_cards)
    print("Computer cards:", rd_card)
    do_continue = input("Type 'y' to get another card, type 'n' to pass.")

    if do_continue == 'y':
      
      user_cards.append(cards[random.randint(0, len(cards) - 1)])
      print("Your current cards:", user_cards)
      
    elif do_continue == 'n':
      
      user_result = calculate_scores(user_cards)
      computer_result = calculate_scores(computer_cards)

      if user_result > 21:
          winner_decider(user_result, computer_result)
      else:
          while computer_result <= user_result:
              computer_cards.append(cards[random.randint(0, len(cards) - 1)])
              computer_result = calculate_scores(computer_cards)


      print(f"User cards: {user_cards}")
      print(f"Computer cards: {computer_cards}")
      print("-----------------------------")
      print(f"User result: {user_result}")
      print(f"Computer result: {computer_result}")

      winner_decider(user_result, computer_result)
      loop_stopper = True
      
    else:
      
        print('Something went wrong. Try again.')    


  