from random import shuffle
from ball import *
from Game import *
NUM_DIGITS=4
print("Welcome to Mastermind Game!!")
for i in range(10):
	game=Game()
	code=game.getCode()
	c=['b','c','d','e','f','g']
	#shuffle(c)
	p=Ball(c[0],0)
	q=Ball(c[0],1)
	r=Ball(c[0],2)
	s=Ball(c[0],3)
	arr=[Ball for _ in range(4)]
	arr[0]=p
	arr[1]=q
	arr[2]=r
	arr[3]=s
#Initialize the initial gues to 0000
	user_input=arr[0].getcolor()+arr[0].getcolor()+arr[0].getcolor()+arr[0].getcolor()
	print(user_input)
	black,white=game.play(arr)
	#user_input=arr[0].getcolor()+arr[0].getcolor()+arr[0].getcolor()+arr[0].getcolor()
	if(black!=NUM_DIGITS):
	  while True:
	    p=c.index(arr[0].getcolor())
	    q=c.index(arr[1].getcolor())
	    r=c.index(arr[2].getcolor())
	    s=c.index(arr[3].getcolor())
	    #if white is there shuffle till white becomes zero.
	    while(white!=0):
	      temp=list(user_input)
	     # print('Before',temp)
	      shuffle(temp)
	      #print('After',temp)
	      user_input=temp[0]+temp[1]+temp[2]+temp[3]
	      #print('Shuffle due to white',user_input)
	      black,white=game.check(user_input)
	#if no guess is correct chnage to next color of all balls
	    if(black==0):
	      user_input=c[p+1]+c[q+1]+c[r+1]+c[s+1]
	      print('0');
	#if 1 guess is correct keep the first one as const and increment next color to all balls.
	    elif(black==1):
	      user_input=c[p]+c[q+1]+c[r+1]+c[s+1]
	      print('1'); 
	    elif(black==2):
	      user_input=c[p]+c[q]+c[r+1]+c[s+1]
	      print('2');
	    elif(black==3):
	      user_input=c[p]+c[q]+c[r]+c[s+1]
	      print('3');
	    arr[0]=Ball(user_input[0],0)
	    arr[1]=Ball(user_input[1],1)
	    arr[2]=Ball(user_input[2],2)
	    arr[3]=Ball(user_input[3],3)
	    #black,white=check(user_input,code)
	    black,white=game.check(user_input)
	    if black==NUM_DIGITS:
	      print('you won! you took {} trials.'.format(str(game.trialnum)))
	      break
	    print('Black: {} Whites: {} Trial Num: {}'.format(str(black), str(white), str(game.trialnum)))
	else:
	    print('you won! you took {} trials.'.format(str(game.trialnum)))
