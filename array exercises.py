seqlength = 0
lastinput = 0

# get user input to start
thisinput = input("Enter a sequence of non-decreasing numbers")

# def check
def check(thisinput):
    if float(thisinput) >= float(lastinput):
        True
    else:
        False

# check if less than last
while check(thisinput) is False:
    lastinput = thisinput
    thisinput = input("Enter a sequence of non-decreasing numbers")
    
    
# end
print("Thanks for playing")
print ("Sequence length: ",seqlength)
    

        