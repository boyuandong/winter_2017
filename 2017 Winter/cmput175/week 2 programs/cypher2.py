import random
#------------------------------------------------------------------------------------------------
# Function to Encript 
#------------------------------------------------------------------------------------------------
def Encrypt(ClearMessage,PrivateKey,Order):
    myNewMessage=ClearMessage.replace('#','@%%@')
    myNewMessage=myNewMessage.replace('_','@^^@')
    # adding spaces at the end of message to make sure length of message is a multiple of PivateKey length
    while len(myNewMessage)%len(PrivateKey)!=0:
        myNewMessage+=' '
    # creating snips of the size of the PrivateKey length
    i=0
    snips=[]
    while i<len(myNewMessage):
        snip=myNewMessage[i:i+len(PrivateKey)]
        i=i+len(PrivateKey)
        snips.append(snip)
    # encoding the message by slicing the snips
    myEncodedMessage=[]
    j=0
    while j<len(Order):
        i=0
        while i<len(snips):
            snip=snips[i]
            myEncodedMessage.append(snip[Order[j]])
            i=i+1
        R=random.uniform(0,1)
        if R<0.5:
            c='#'
        else:
            c='_'
        myEncodedMessage.append(c)
        j=j+1    
    return ''.join(myEncodedMessage)
#------------------------------------------------------------------------------------------------
# Functionto decrypt
#------------------------------------------------------------------------------------------------

def Decrypt(cipher,Order):
    # getting the sequence in the ordering
    mySequence=[]
    i=0
    while i<len(Order):
        j=0
        while j<len(Order):
            if i==Order[j]:
                mySequence.append(j)
            j+=1    
        i+=1
    # getting the slices from the cipher
    mySlices=[]
    k=0
    code=[]
    lengthMessage=0
    while k<len(cipher):
        if cipher[k]=='#' or cipher[k]=='_':
            slice=''.join(code)
            mySlices.append(slice)
            code=[]
            j=0
        else:
            code.append(cipher[k])
            lengthMessage+=1
        k=k+1
        
    # stiching the slices based on the sequence in the ordering of the key
    decipher=[]
    j=0
    k=0
    while j<lengthMessage:
        i=0
        while i<len(Order):
            decipher.append(mySlices[mySequence[i]][k])
            i+=1
        j=j+len(Order)
        k+=1
    
    myDecipher=''.join(decipher)
    myDecipher=myDecipher.replace('@%%@','#')
    myDecipher=myDecipher.replace('@^^@','_')
    return myDecipher

myPrivateKey="^"
while myPrivateKey.find("^")!=-1:
    print ("Private key cannot have the character \"^\"")
    myPrivateKey=input ("Enter your private key: ")

mySortedKey=sorted(myPrivateKey)
myListedPK=list(myPrivateKey)
#print (myListedPK)
#print (mySortedKey)
i=0
myOrder=[]
while i<len(myListedPK):
    j=mySortedKey.index(myListedPK[i])
    myOrder.append(j)
    mySortedKey[j]='^'
    i=i+1
#print (myOrder)

q="0"
while q!="5":
    print ("1- Enciphering a Message")
    print ("2- Enciphering a text file")
    print ("3- Deciphering a Message")
    print ("4- Deciphering a file")
    print ("5- quit")
    q="0"    
    while q not in ['1', '2', '3', '4', '5']:
        q=input("Enter your option between 1 and 5 => ")
    if q== '1':		# Enciphering a Message
        myMessage=input("Enter your message to encode: ")
  
        cypher=Encrypt(myMessage,myPrivateKey,myOrder)
        print ("your encyphered message is:")
        print(cypher)

    elif q== '2':		#Enciphering a text file
        fileName=input("Enter the file name of the text to be encyphered: ")
        fileT = open(fileName, "r")
        myMessage=fileT.read()
        fileT.close()
        cypher=Encrypt(myMessage,myPrivateKey,myOrder)
        fileName=input("Enter the file name to store the encyphered text: ")
        fileT = open(fileName, "w")
        fileT.write(cypher)
        fileT.close()
    
    elif q== '3':
        # decyphering
        cypher=input("Enter your encrypted message to decypher: ")
           
        decypher=Decrypt(cypher,myOrder)
        print ("Your original message:")
        print (decypher)

    elif q== '4':
        fileName=input("Enter the file name of the encrypted text to decypher: ")
        fileT = open(fileName, "r")
        cypher=fileT.read()
        fileT.close()
        decypher=Decrypt(cypher,myOrder)

        fileName=input("Enter the file name to store the clear text: ")
        fileT = open(fileName, "w")
        fileT.write(decypher)
        fileT.close()

        print ("Your original message:")
        print (decypher)
    End=" "
    while End.upper() not in 'Y N'.split():
        End=input("Do you want to continue with the program (Y/N)? ")
    if End.upper()=="N":
        q="5"

