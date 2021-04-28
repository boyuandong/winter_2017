from datetime import date
def main():
    # get the list of member information
    members=create_member_list()
    # get the list of book information
    books=create_book_list()
    # get the list of summary information
    late_list=find_late_member(books,members)
    # sort the summary list
    late_list=sorted(late_list)
    # write the summary in the summary.txt
    write_file(late_list)
    # print out the summary in python shell
    print_out()
def create_member_list():
    # -a list including the information in members.txt
    # open the file read the txt
    member_file=open('members.txt','r')
    members=[]
    for member in member_file:
        # split each line and add the information of the line to a member_list
        member_list=[]
        member=member.split(',')
        # change the format of the phone number then add it to the list
        phonenum1=change_phone_num(member[0])
        member_list.append(phonenum1)
        member_list.append(member[1])
        # add every member_list to the members list
        members.append(member_list) 
    member_file.close()
    return members
def create_book_list():
    # -a list including the information in members.txt
    # open the file read the txt    
    book_file=open('books.txt','r')
    books=[]
    for book in book_file:
        # split each line and add the information of the line to a book_list
        book_list=[]
        book=book.split(';')
        # change the format of the phone number then add it to the list
        phonenum2=change_phone_num(book[len(book)-1])
        book_list.append(phonenum2)
        book_list[1:4]=book[0:3]
        # add every book_list to the books list
        books.append(book_list)   
    book_file.close()
    return books
def change_phone_num(strings):
    # -change the format of the phone number then add it to the list
    new_string='('+strings[0:3]+')'+' '+strings[3:6]+' '+strings[6:10]
    return new_string
def late_days(due_date):
    # -calculate how many days delay
    y,m,d=due_date.split('/')
    year=int(y)
    month=int(m)
    day=int(d)
    late_time=date(2018,1,19)-date(year,month,day)
    return late_time.days
def penalty(late_days,book_cost_string):
    # -calculate the amount of the penalty
    book_cost=float(book_cost_string)
    late_days=int(late_days)
    total=0
    if late_days>90:
        # when the delay more than 90 days the penalty is $0.25 per late day plus the full cost of the book
        total=float(late_days*0.25+book_cost)
    else:
        # when the delay less than 90 days the penalty is $0.25 per late day
        total=float(late_days*0.25)
    return total
def find_late_member(books,members):
    # -summarize the information and add the information to a new list in an new order
    # the order should be 1.phone number 2.name 3.penalty 4.[bookcode](delaydays) in each list in the late_list
    late_list=[]
    for member in members:
        # for every member information in the members list
        inform_list=[]
        for book in books:
            # for every book information in the books list
            if book[0]==member[0]:
                # if the phone number are the same
                # identify the phone number,book code, delay days,cost of book
                phone_num=book[0]
                book_code=book[1]
                book_late_days=int(late_days(book[-1]))
                book_cost=float(book[2])
                # calculate the penalty
                book_penalty=penalty(book_late_days,book_cost)
                if phone_num in inform_list:
                    # if phone number has already exist
                    # change the penalty
                    inform_list[2]+=book_penalty   
                else:
                    # if phone number has not been added in the list
                    # add the phone number,name, penalty at the right order
                    inform_list.append(phone_num)
                    inform_list.append(member[1])
                    inform_list.append(book_penalty)
                # add [book code](delaydays) to the list
                inform_list.append('['+book_code+']('+str(int(book_late_days))+' days); ')
        # add the list to the whole list
        late_list.append(inform_list)               
    return late_list

def total_penalty(late_list):
    # -calculate the total penalty
    total=0
    for member in late_list:
        # for every person on the summary list
        # add all the penalty
        total+=member[2]
    return total
def write_file(late_list):
    # -write the summary in a new file named summary.txt
    # add '\n' at the end of each line
    new_file=open('summary.txt','w')
    total_penalty_num=total_penalty(late_list)
    new_file.write('+--------------+------------------------------+--------+\n')
    new_file.write('| Phone Number | Name                         | Due    |\n')
    new_file.write('+--------------+------------------------------+--------+\n')
    for member in late_list:
        # use the correct format print the information
        # 1.phone number should be formatted as (999) 999 9999
        # 2.name should be 30 characters wide
        # 3.amount due should be printed with 7 positions and only 2 after the decimal point         
        new_file.write('|%s|%-30s|$%7.2f|'%(member[0],member[1],member[2])+''.join(member[3:])+'\n')
    new_file.write('+--------------+------------------------------+--------+\n')
    new_file.write('| Total Dues   |                            $   %7.2f|'%(total_penalty_num)+'\n')
    new_file.write('+--------------+------------------------------+--------+\n')  
    # close the file
    new_file.close()
def print_out():
    # -print out the summary on python shell
    infile=open('summary.txt','r')
    txt=infile.read()
    txt=txt.splitlines()
    for item in txt:
        print(item)
    infile.close()

main()