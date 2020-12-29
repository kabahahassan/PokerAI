# Hassan Kabha 318242914
# Aishy Awawdy 316065200
import numpy as np
import numpy
numpy.set_printoptions(threshold = 100000)
from treys import Card
from treys import Deck
from treys import Evaluator
import random


# create a state list to save all the states we have
# every state have 2 cards and if sb and if the 2 card the same suits
# state[0] and state[1] and two card state[2] if same suit and state[3] if sb
statelist =[]
deck = Deck()
counter=0
for i in range(2,15):
    for j in range(2,15):
        state = [i,j,0,0]
        statelist.append(state)


for i in range(2,15):
    for j in range(2,15):
        state = [i,j,1,0]
        statelist.append(state)

for i in range(2,15):
    for j in range(2,15):
        state = [i,j,0,1]
        statelist.append(state)

for i in range(2,15):
    for j in range(2,15):
        state = [i,j,1,1]
        statelist.append(state)

# init the Qtable with zeros
Qtable = np.zeros((len(statelist),2))

np.save('Qtable.npy', Qtable)
# list with all cards
cardslist =[]
card=Card.new('2d')
cardslist.append(card)
card=Card.new('3d')
cardslist.append(card)
card=Card.new('4d')
cardslist.append(card)
card=Card.new('5d')
cardslist.append(card)
card=Card.new('6d')
cardslist.append(card)
card=Card.new('7d')
cardslist.append(card)
card=Card.new('8d')
cardslist.append(card)
card=Card.new('9d')
cardslist.append(card)
card=Card.new('Td')
cardslist.append(card)
card=Card.new('Jd')
cardslist.append(card)
card=Card.new('Qd')
cardslist.append(card)
card=Card.new('Kd')
cardslist.append(card)
card=Card.new('Ad')
cardslist.append(card)

###

card=Card.new('2s')
cardslist.append(card)
card=Card.new('3s')
cardslist.append(card)
card=Card.new('4s')
cardslist.append(card)
card=Card.new('5s')
cardslist.append(card)
card=Card.new('6s')
cardslist.append(card)
card=Card.new('7s')
cardslist.append(card)
card=Card.new('8s')
cardslist.append(card)
card=Card.new('9s')
cardslist.append(card)
card=Card.new('Ts')
cardslist.append(card)
card=Card.new('Js')
cardslist.append(card)
card=Card.new('Qs')
cardslist.append(card)
card=Card.new('Ks')
cardslist.append(card)
card=Card.new('As')
cardslist.append(card)

###

card=Card.new('2h')
cardslist.append(card)
card=Card.new('3h')
cardslist.append(card)
card=Card.new('4h')
cardslist.append(card)
card=Card.new('5h')
cardslist.append(card)
card=Card.new('6h')
cardslist.append(card)
card=Card.new('7h')
cardslist.append(card)
card=Card.new('8h')
cardslist.append(card)
card=Card.new('9h')
cardslist.append(card)
card=Card.new('Th')
cardslist.append(card)
card=Card.new('Jh')
cardslist.append(card)
card=Card.new('Qh')
cardslist.append(card)
card=Card.new('Kh')
cardslist.append(card)
card=Card.new('Ah')
cardslist.append(card)

###

card=Card.new('2c')
cardslist.append(card)
card=Card.new('3c')
cardslist.append(card)
card=Card.new('4c')
cardslist.append(card)
card=Card.new('5c')
cardslist.append(card)
card=Card.new('6c')
cardslist.append(card)
card=Card.new('7c')
cardslist.append(card)
card=Card.new('8c')
cardslist.append(card)
card=Card.new('9c')
cardslist.append(card)
card=Card.new('Tc')
cardslist.append(card)
card=Card.new('Jc')
cardslist.append(card)
card=Card.new('Qc')
cardslist.append(card)
card=Card.new('Kc')
cardslist.append(card)
card=Card.new('Ac')
cardslist.append(card)

# search in the cards list for the unique number for the card
def checkCardsList(num):
    index =0
    for i in range(0,len(cardslist)):
        if num == cardslist[i]:
            index = i
    return index

# create a state with the hand we have and if sb
def createState(hand, sb):
  #arr = Card.print_pretty_cards(hand)
  same=0
  index1 = checkCardsList(hand[0])
  index2 = checkCardsList(hand[1])
  a1= (index1)/13
  a2= (index2)/13

  if  a1< 1 and a2<1:
      same=1

  if  (a1>=1 and a1<2) and (a2<2 and a2>=1):
      same=1


  if  (a1>=2 and a1<3) and (a2<3 and a2>=2):
      same=1

  if  (a1>=3 and a1<4) and (a2<4 and a2>=3):
      same=1


  index1=index1%13
  index2=index2%13
  num1 = index1+2
  num2 = index2+2
 # s1 = arr[3]
  #s2 = arr[8]
  state = []
  state.append("")
  state.append("")
  state.append("")
  state.append("")
  if num1=="T":
      num1=10
  if num1=="J":
      num1=11
  if num1=="Q":
      num1=12
  if num1=="K":
      num1=13
  if num1=="A":
      num1=14

  if num2 == "T":
      num2  = 10
  if num2 == "J":
      num2 = 11
  if num2 == "Q":
      num2 = 12
  if num2 == "K":
      num2 = 13
  if num2 == "A":
      num2 = 14

  state[0]= int(num1)
  state[1]= int(num2)
  state[2]= same #(s1 == s2)
  if sb == "A":
      state[3]= 1
  else :
      state[3]=0
  return state

# get the index of the state in the statelist
def getIndex(myState):
 index =(myState[0]-2)*13 + (myState[1]-2)
 if myState[2] == 0 and myState[3] == 0:
     index=index
 if myState[2] == 1 and myState[3] == 0:
     index=index+169
 if myState[2] == 0 and myState[3] == 1:
     index=index+2*169
 if myState[2] == 1 and myState[3] == 1:
     index=index+3*169
 return index

# play one round in the game
def onePly(balanceA, balanceB,board, player1_hand, player2_hand, sb , actionA,actionB,evaluator):

    reward = 0
    rndA = random.uniform(0, 1)
    rndB = random.uniform(0, 1)
    if sb == "A":
        balanceA = balanceA - 0.5
        if balanceB < 1:
            reward = 0.5 + balanceB
            balanceB = 0
        else:
            balanceB = balanceB - 1
            reward = 1.5

    if sb == "B":
        balanceB = balanceB - 0.5
        if balanceA < 1:
            reward = 0.5 + balanceA
            balanceA = 0
        else:
            balanceA = balanceA - 1
            reward = 1.5

    # evaluate the hand with the board
    p1_score = evaluator.evaluate(board, player1_hand)
    p2_score = evaluator.evaluate(board, player2_hand)

    if sb == "A" and actionA == "fold":
        balanceB = balanceB + reward

    if sb == "B" and actionB == "fold":
        balanceA = balanceA + reward

    if sb == "A" and actionA == "call" and actionB == "fold":
        balanceA = balanceA + reward
    if sb == "B" and actionB == "call" and actionA == "fold":
        balanceB = balanceB + reward
    if sb == "A" and actionA == "call" and actionB == "call":
        reward = reward + balanceA + balanceB
        balanceB = 0
        balanceA = 0
        if p1_score < p2_score:
            balanceA = balanceA + reward
        if p1_score > p2_score:
            balanceB = balanceB + reward
        if p1_score == p2_score:
            balanceB = balanceB + reward / 2
            balanceA = balanceA + reward / 2
    if sb == "B" and actionA == "call" and actionB == "call":
        reward = reward + balanceA + balanceB
        balanceB = 0
        balanceA = 0
        if p1_score < p2_score:
            balanceA = balanceA + reward
        if p1_score > p2_score:
            balanceB = balanceB + reward
        if p1_score == p2_score:
            balanceB = balanceB + reward / 2
            balanceA = balanceA + reward / 2

    if sb == "A":
        sb = "B"
    else:
        sb = "A"
    return balanceA, balanceB, sb


# training the agent
def train(evaluator):
 print("Please wait 3 min until the agent finish training")
 # Hyperparameters
 alpha = 0.01
 gamma = 0.3
 epsilon = 0.2
 print("Trainig :")
 print("Number iterations in training : 100000")
 Qtable = np.load('Qtable.npy')
 penalty=0
 for i in range(1, 100000):


  balanceA=10
  balanceB=10

  rnd = random.uniform(0, 1)

  if rnd > 0.5:
   sb = "A"
  else:
   sb = "B"

  # calculate the state
  done = False
  deck = Deck()
  board = deck.draw(5)
  player1_hand = deck.draw(2)
  player2_hand = deck.draw(2)
  stateA = createState(player1_hand, sb)
  stateB = createState(player2_hand, sb)
  stateIndexA = getIndex(stateA)
  stateIndexB = getIndex(stateB)

  while not done:


         if random.uniform(0, 1) < epsilon:   # Explore action space
             if random.uniform(0, 1) < 0.5:
              action1 = 0   # fold
             else:
              action1 =1    # all in
         else:

             action1 = np.argmax(Qtable[stateIndexA])  # Exploit learned values

         if random.uniform(0, 1) < epsilon:  # Explore action space
             if random.uniform(0, 1) < 0.5:
                 action2 = 0  # fold
             else:
                 action2 = 1  # all in
         else:

             action2 = np.argmax(Qtable[stateIndexB])  # Exploit learned values

         if action1 == 1:
             actionA= "fold"
         else:
             actionA="call"

         if action2 == 1:
             actionB= "fold"
         else:
             actionB="call"
         oldBalanceA = balanceA
         oldBalanceB = balanceB
         #########################################################
         balanceA, balanceB, sb = onePly(balanceA,balanceB,board,player1_hand,player2_hand,sb,actionA,actionB,evaluator)

         ########################################################
         if balanceB == 0 or balanceA == 0:
             done = 1
         old_valueA = Qtable[stateIndexA, action1] # get the old value
         old_valueB = Qtable[stateIndexB, action2]
         deck=Deck()
         cardsNewRoundPlayer1 = deck.draw(2) # two hands for the next round
         cardsNewRoundPlayer2 = deck.draw(2)
         next_stateA= createState(cardsNewRoundPlayer1,sb) # calculate the next round
         next_stateB = createState(cardsNewRoundPlayer2, sb)
         next_indexStateA = getIndex(next_stateA) # get the index of the state for the next round
         next_indexStateB =getIndex(next_stateB)
         next_maxA = np.max(Qtable[next_indexStateA]) # best action for the next state
         next_maxB = np.max(Qtable[next_indexStateB])
         rewardA = balanceA - oldBalanceA # calculate the reward
         rewardB = balanceB - oldBalanceB
         if rewardA < 0 :
             penalty = penalty+1
         new_valueA = (1 - alpha) * old_valueA + alpha * (rewardA+ gamma * next_maxA) # calculate new value by the q learning eqution
         new_valueB = (1 - alpha) * old_valueB + alpha * (rewardB + gamma * next_maxB)
         Qtable[stateIndexA, action1] = new_valueA # update the Qtable with the new value
         Qtable[stateIndexB, action2] = new_valueB

        # update the state with the next state
         stateA = next_stateA
         stateB = next_stateB
         player1_hand=cardsNewRoundPlayer1
         player2_hand=cardsNewRoundPlayer2
         board = deck.draw(5)
         stateIndexA=next_indexStateA
         stateIndexB=next_indexStateB
 np.save('Qtable.npy', Qtable)
 print("Trainig finished ")
 print("the penalty average: ",penalty/100000)



 ######################################################################################
# playing
def main():
 evaluator = Evaluator()
# the training
 train(evaluator)
 Qtable = np.load('Qtable.npy') # Qtable to save the values
 p=1
 while(p):
  answer = input("Do you want to play (if NO the agent will play against random player)? (y/n)")
  if answer != "y" and answer != "n":
      print("Wrong input !!")
  else:
      p=0


 if answer=="n":
  print("The agent will play vs random player")

  c = 0
  numRound =0
  evaluator = Evaluator()
  print("Playing: ")
  for j in range(1,100000):
     if j% 10000 == 0:
         print("Game Number ",j)
     # the balance of the 2 players
     balanceA = 10
     balanceB = 10
     reward = 0
     # random value
     rnd = random.uniform(0, 1)

     deck = Deck()

     if rnd > 0.5:
         sb = "A"
     else:
         sb = "B"
     # until the game did not finished
     while balanceA > 0 and balanceB > 0:
         numRound = numRound+1
         deck = Deck()
         reward = 0
         rndA = random.uniform(0, 1)
         rndB = random.uniform(0, 1)
         board = deck.draw(5)
         player1_hand = deck.draw(2)
         player2_hand = deck.draw(2)
         if sb == "A":
             balanceA = balanceA - 0.5
             if balanceB < 1:
                 reward = 0.5 + balanceB
                 balanceB = 0
             else:
                 balanceB = balanceB - 1
                 reward = 1.5

         if sb == "B":
             balanceB = balanceB - 0.5
             if balanceA < 1:
                 reward = 0.5 + balanceA
                 balanceA = 0
             else:
                 balanceA = balanceA - 1
                 reward = 1.5


         state = createState(player1_hand,sb)
         stateIndex = getIndex(state)
         action = np.argmax(Qtable[stateIndex])
         if action == 1:
             actionA="fold"
         else:
             actionA="call"



         if rndB > 0.5:
             actionB = "fold"
         else:
             actionB = "call"
         # evaluate the 2 hands
         p1_score = evaluator.evaluate(board, player1_hand)
         p2_score = evaluator.evaluate(board, player2_hand)

         if sb == "A" and actionA == "fold":
             balanceB = balanceB + reward

         if sb == "B" and actionB == "fold":
             balanceA = balanceA + reward

         if sb == "A" and actionA == "call" and actionB == "fold":
             balanceA = balanceA + reward
         if sb == "B" and actionB == "call" and actionA == "fold":
             balanceB = balanceB + reward
         if sb == "A" and actionA == "call" and actionB == "call":
             reward = reward + balanceA + balanceB
             balanceB = 0
             balanceA = 0
             if p1_score < p2_score:
                 balanceA = balanceA + reward
             if p1_score > p2_score:
                 balanceB = balanceB + reward
             if p1_score == p2_score:
                 balanceB = balanceB + reward / 2
                 balanceA = balanceA + reward / 2
         if sb == "B" and actionA == "call" and actionB == "call":
             reward = reward + balanceA + balanceB
             balanceB = 0
             balanceA = 0
             if p1_score < p2_score:
                 balanceA = balanceA + reward
             if p1_score > p2_score:
                 balanceB = balanceB + reward
             if p1_score == p2_score:
                 balanceB = balanceB + reward / 2
                 balanceA = balanceA + reward / 2

         if sb == "A":
          sb = "B"
         else:
          sb = "A"


     if balanceA == 20:
         c = c + 1
  print("number games our agent win in 100,000 games: ", c)
  print("number rounds each game on average", numRound / 100000)
  q = input("Please press any key to exit")

 else:
     d=0
     again=1
     done=0
     Qtable = np.load('Qtable.npy')
     p=1

     while again:
         p=1
         while(p):
          answer = input("against AI player(a) or random player(r): (a/r)")
          if answer != "a" and answer != "r":
              print("Wrong input !!")
          else:
              p = 0

         balanceA =10
         balanceB = 10
         rnd = random.uniform(0, 1)
         done=0
         deck = Deck()
         evaluator = Evaluator()
         if rnd > 0.5:
             sb = "A"
         else:
             sb = "B"
         if sb == "A":
             print("You start first ")
         else:
             print("Your opponinte start first ")
         while not done:
             print(" ")
             print("*** New Round ***")
             deck = Deck()
             reward = 0
             actionB=0
             actionA=0
             rndB = random.uniform(0, 1)
             rndA = random.uniform(0, 1)
             board = deck.draw(5)
             player1_hand = deck.draw(2)
             player2_hand = deck.draw(2)
             p1_score = evaluator.evaluate(board, player1_hand)
             p2_score = evaluator.evaluate(board, player2_hand)
             p1_class = evaluator.get_rank_class(p1_score)
             p2_class = evaluator.get_rank_class(p2_score)


             if answer == "a":
                 state = createState(player2_hand, sb)
                 stateIndex = getIndex(state)
                 action = np.argmax(Qtable[stateIndex])
                 if action == 1:
                     actionB = "fold"
                 else:
                     actionB = "call"
             else:
              if rndB > 0.5:
                  actionB = "fold"
              else:
                 actionB = "call"


             if sb == "A":
                 print("Your turn, Your balance is : ", balanceA)
                 print("Your hand :")
                 print(Card.print_pretty_cards(player1_hand))
                 p=1
                 while(p):
                  actionA = input("please select action : (fold/call)")
                  if actionA != "fold" and actionA != "call":
                      print("Wrong input !!")
                  else:
                      p = 0
                 if actionA =="call":
                  print("Your opponinte turn, balance : ", balanceB)
                  print("Your opponinte action is : ", actionB)


             if sb == "B":
                 print("Your opponinte turn, balance : ", balanceB)
                 print("Your opponinte action is : ", actionB)
                 print("You turn, Your balance is : ", balanceA)
                 if actionB == "call":

                  print("Your hand :")
                  print(Card.print_pretty_cards(player1_hand))
                  p=1
                  while(p):
                   actionA = input("please select action : (fold/call)")
                   if actionA != "fold" and actionA != "call":
                       print("Wrong input !!")
                   else:
                       p = 0

             if actionB == "call" and actionA == "call":
                 print("The board cards: ")
                 print(Card.print_pretty_cards(board))
                 print("Your opponinte hand: ")
                 print(Card.print_pretty_cards(player2_hand))
                 print("Your Hand = ",evaluator.class_to_string(p1_class))
                 print("Your Opponinte Hand = ", evaluator.class_to_string(p2_class))
             balanceA, balanceB, sb = onePly(balanceA, balanceB, board, player1_hand, player2_hand, sb, actionA,
                                             actionB,evaluator)
             if balanceB == 0:
                 print("You Win")
                 done=1
                 p=1
                 while(p):
                  answer = input("do you want to play again? (y/n)")
                  if answer != "y" and answer != "n":
                      print("Wrong input !!")
                  else:
                      p = 0
                 if answer == "y":
                     again = 1
                 else:
                     again = 0

             if balanceA == 0:
                 print("You Lose")
                 done=1
                 p=1
                 while(p):
                  answer = input("do you want to play again? (y/n)")
                  if answer != "y" and answer != "n":
                      print("Wrong input !!")
                  else:
                      p = 0
                 if answer == "y":
                     again = 1
                 else:
                     again = 0
     q = input("Please press any key to exit")

# print(Qtable)



main()





