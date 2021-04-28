import os.path
def main():
    # determine if the input file is missing
    # if the input file exists
    if os.path.exists('accounts.txt'):
        # create a accounts_list of class Account objects
        account_list=create_accounts('accounts.txt')
        # enter the account name
        enter=input("Enter account name, or 'Stop' to exit: ")
        # while don't enter stop the programe continue running
        while enter!='Stop':
            name=''
            # for every class Account object in account_list
            for account in account_list:
                if account.get_name()==enter:
                    name=account.get_name()
                    change_num=input('Enter transaction amount: ')
                    # if the amount is a float 
                    if is_float(change_num):
                        account.change_amount(change_num)
                        print('New balance for account '+name+':%7.2f'%(account.get_amount()))
                    # if the amount is not a float
                    else:
                        print('Illegal value for transaction, transaction canceled')
            # if name is never assigned to any other string
            # the account does not exist in the class Account objects
            if name=='':
                print('Account does not exist, transaction canceled')
            enter=input("Enter account name, or 'Stop' to exit: ")
    # if the input file does not exist
    else:
        print('Input file not found, program will exit')
    
def create_accounts(filename):
    # -create the account_list of class Account objects
    infile=open(filename,'r')
    account_list=[]
    # for each line in file
    for line in infile:
        line=line.rstrip('\n')
        line=line.split(':')
        # if the amount is a float
        if is_float(line[1]):
            # create a class Account object contains name and float amount,then add to the list
            account=Account(line[0],line[1])
            account_list.append(account)
        # if the amount is not a float, do not add the account to the list
        else:
            print('Account for '+line[0]+' not added: illegal value for balance')
            
    infile.close()
    return account_list  

def is_float(amount):
    # -determine if the amount of string is a float
    if amount.count('.')==1:
        return True
    else:
        return False
class Account:
    # -a class contains the account name and amount
    def __init__(self,name,amount):
        # -initialize the instance atributes
        self.name=name
        self.amount=amount
    def get_amount(self):
        # -get the amount
        return self.amount
    def get_name(self):
        # -get the name
        return self.name
    def change_amount(self,num):
        # -update the amount
        self.amount=float(self.amount)
        self.amount+=float(num)
   
main()