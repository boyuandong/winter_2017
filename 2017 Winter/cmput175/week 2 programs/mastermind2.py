import random
def validate_input(alphabet,wordLength):
# Function to read the suggested code and to only accept characters from alphabet with some minimum length
	correctInput=False
	while not correctInput:
		guessedWord=input("Guess code of %d letters with alphabet [A..H]:"%(wordLength))
		guessedWord=guessedWord[:wordLength].upper()
		if (len(guessedWord)>=wordLength):
			correctInput=True		
			for i in range(wordLength):
				if guessedWord[i] not in alphabet:
					correctInput=False
	return list(guessedWord)

def generate_secret(alphabet, wordLength):
# Function that generates a secret code of given length out of characters from the alphabet	
	secretList=[]
	for i in range(wordLength):
		j=random.randrange(0,len(alphabet))
		secretList.append(alphabet[j])
	print("Welcome gamer, this is the code:",secretList)

	return secretList

# Intialization
ALPHABET=list("ABCDEFGH")
WORD_LENGTH=5
MAX_ATTEMPTS=10
secretList=generate_secret(ALPHABET, WORD_LENGTH)

gameOver=False
attempts=0
# Loop for Guesses and Verification
while not gameOver :
	guessedList=validate_input(ALPHABET,WORD_LENGTH)
	nbRightPlace=nbRightColour=0
	remaining=list(secretList)
	for i in range(WORD_LENGTH):
		if guessedList[i]==secretList[i]:
			nbRightPlace+=1
			remaining[i]="*"
	for i in range(WORD_LENGTH):
		if guessedList[i] in remaining:
			nbRightColour+=1
	attempts+=1
	
	print (attempts,":",guessedList, "(", end=" ")
			
	for i in range(nbRightPlace):
	        print("+", end=" ")
	for i in range(nbRightPlace,nbRightPlace+nbRightColour):
		print ("-", end=" ")
		
	for i in range(nbRightPlace+nbRightColour, WORD_LENGTH):
		print (".", end=" ")
	print (")", end=" ")			
	gameOver=(attempts>=MAX_ATTEMPTS or nbRightPlace==WORD_LENGTH)
if (nbRightPlace==WORD_LENGTH): print ("Well done!")  
else: print ("The secret code was:",secretList)
print ("Thank you for playing Mastermind")