import random														
import time


name=raw_input("What is your name\n");
print "Hello",name
print "LETS PLAY, HOPE YOU ENJOY\n"
print " ____________     "
print "|	    |       "
print "|	    O  "
print "|	 ~~~|~~~    "
print "|	   / \      "

time.sleep(1)

list=["sarcasm","dance","sense","life","career","service","hardwork"]
word=random.choice(list)
ind=list.index(word)
l=len(word)
guesses=''
turns=6
print "WORD"
while turns>0:

	failed=0
	for char in word:
		if char in guesses:
			print char ,
		else:
			print "-",
			failed+=1


	if failed==0:
		print "\n"
		print " ____________     "
		print "|	    |       "
		print "|           O  "
		print "|	 ~~~|~~~    "
		print "|	   / \      "
		print "YOU SAVED ME\n THANK YOU"								
		break

	print 
	guess=raw_input("Guess the character?") 
	guesses+=guess
	if guess not in word:
		turns-=1
		print "OOPS! IT'S A WRONG GUESS\n TRY AGAIN IN ",turns,"TURNS"


		
		if turns<5:
				print "The first character is",list[ind][0],"last character is",list[ind][l-1]
		

		if turns==0:
			print " ____________     "
			print "|	 |           "
			print "|                 "
			print "|                 "
			print "|                 "	
		elif turns==1:
			print " ____________     "
			print "|	    |       "
			print "|           O  "
			
		elif turns==2:
			print " ____________     "
			print "|	    |       "
			print "|           O  "
			print "|	 ~~~|       "
		
		elif turns==3:
			print " ____________     "
			print "|	    |       "
			print "|           O  "
			print "|	 ~~~|~~~    "
		elif turns==4:
			print " ____________     "
			print "|	    |       "
			print "|           O  "
			print "|	 ~~~|~~~    "
			print "|	   /        "
		
	