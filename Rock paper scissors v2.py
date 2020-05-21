import random
rps = ["rock", "paper", "scissors"]
ready = ["go","yes"]
restartoptions = ["yes", "no"]
your_score = []
computer_score = []
restart = "yes"

## method to clean inputs with retry ##
def validate(userinput):


## start the game
start_message = input("Are you ready to start? Type GO and hit RETURN to being the game")
lower.start_message
trim.start_message
while start_message not in ready:
      start_message = input("I didn't get that - type GO to start")
      lower.start_message
      trim.start_message
      
while restart == "yes":
  choice = input("are you going to choose rock, paper or scissors?")
  lower.choice
  trim.choice
  while choice not in rps:
      choice = input("I didn't get that - rock, paper or scissors")
      lower.choice
      trim.choice
  
  print ("you chose", choice)

  ## get choices as ints
  choice = rps.index(choice,0,3) 
  computer_play = random.randrange(0,3)

  ## evaluate winner
  scorediff = choice - computer_play
  modscore = scorediff%3
  outcome = ["draw", "win", "lose"]
  result = outcome[modscore]

  ## print results
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

  # restart
  restart = input("Do you want to go again?")
  lower.restart
  trim.restart
  while restart not in restartoptions:
      restart = input("I didn't get that - YES or NO?")
      lower.restart
      trim.restart

  str(restart)
  if restart == "no":
    print ("Hope you enjoyed the game, bye")  

