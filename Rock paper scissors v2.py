import random
rps = ["rock", "paper", "scissors"]
ready = ["go","yes"]
restartoptions = ["yes", "no"]
your_score = []
computer_score = []
restart = "yes"

## start the game
start_message = input("Are you ready to start? Type GO and hit RETURN to being the game")
start_message = start_message.lower()
while start_message not in ready:
  start_message = input("I didn't quite get that, could you try again please?")
  start_message = start_message.lower()

## restart message if applicable

while restart == "yes":

  ## validated data input to and convert to int
  choice = input("are you going to choose rock, paper or scissors?")
  choice = choice.lower()
  while choice not in rps:
    choice = input("I didn't get that... try typing rock, paper or scissors?")
    choice = choice.lower()
    print ("you chose", choice)

  ## get choices as ints
  choice = rps.index(choice,0,3) 
  computer_play = random.randrange(0,3)

  ## evaluate winner
  scorediff = choice - computer_play
  modscore = scorediff%3
  outcome = ["draw", "win", "lose"]
  result = outcome[modscore]

  choice = rps[computer_play]
  computer_play = rps[computer_play]
  print ("The computer chose", computer_play)
  print ("so you", result, "this round")

  ## tally score
  if result == "win":
    your_score.append(1)
  elif result == "lose":
    computer_score.append(1)
  sumyourscore = sum(your_score)
  sumcompscore = sum(computer_score)
  print ("The score is",sumyourscore, "to you and",sumcompscore, "to the computer")

  ## go again?
  restart = input("Do you want to go again?")
  str(restart)
  while restart not in restartoptions:
    restart = input ("I didn't get that. Type Yes or No")
    restart = restart.lower()
  if restart == "no":
    print ("Hope you enjoyed the game, bye")  





