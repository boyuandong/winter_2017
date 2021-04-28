def main():
  
  filename=input("Enter the input filename: ")
  infile=open(filename,'r')
  content=infile.read()
  data=content.splitlines()
  code_list=[]
  # for each item in the data
  for item in data:
    alist=[]
    # split the item divide the whole string into two parts: secret code and key number
    item=item.split()
    # if do not have the key number
    if len(item)==1:
      alist.append(item[0])
      alist.append(0)
    # if have the key number
    elif len(item)==2:
      alist.append(item[0])
      alist.append(int(item[1]))
    # if alist append the secret code and key number
    if len(alist)!=0:
      # append the alist to code_list
      code_list.append(alist)
  infile.close()
  # call the decryption to decode the secret code 
  decryption(code_list)
   
def decryption(code_list):
  # -decode the secret_code by using the secret code and key number
  # for every item(including secret_code and key number) in code_list
  for item in code_list:
    key_num=item[1]
    # if the key number is 0
    if key_num==0:
      print("Missing key!")
    else:
      word=''
      # for every letter in the secret_code string
      for letter in item[0]:
        letter_num=ord(letter)
        new_letter_num=calculate(letter_num,key_num)
        new_letter=chr(new_letter_num)
        word+=new_letter
      print(word)
      
def calculate(letter_num,key_num):
  # -calculate the new letter number
  # if the new letter number less or equal ord('Z')
  if letter_num+key_num<=ord('Z'):
    return letter_num+key_num
  # if the new letter number larger than ord('Z')
  elif letter_num+key_num>ord('Z'):
    num=key_num+letter_num-ord('Z')+ord('A')-1
    return num
  
main()