from datetime import date
def main():
    member_file=open('members.txt','r')
    book_file=open('books.txt','r')
    #print(book_file.read().splitlines())
    d_members={}
    d_books={}
    for member in member_file:
        #print(member)
        member=member.split(',')
        phonenum1=change_phone_num(member[0])
        d_members[phonenum1]=member[1:2]
    for book in book_file:
        book=book.split(';')
        phonenum2=change_phone_num(book[len(book)-1])
        d_books[phonenum2]=book[0:len(book)-1]
        #print(book)
    #print(d_members)
    #print(d_books)
    #print(d_books['(780) 492 286'][0])
    #print(date(2018,1,19)-date(2017,5,4))
    t=late_days('2017/5/4')
    #print(t)
    #print(date(2018,1,19)-date(int(t)))
    d_late=find_late_member(d_books,d_members)
    print_out(d_late)
def change_phone_num(strings):
    new_string='('+strings[0:3]+')'+' '+strings[3:6]+' '+strings[6:9]
    return new_string
def late_days(due_date):
    y,m,d=due_date.split('/')
    year=int(y)
    month=int(m)
    day=int(d)
    late_time=date(2018,1,19)-date(year,month,day)
    return late_time.days
def penalty(late_days,book_cost_string):
    book_cost=float(book_cost_string)
    if late_days>90:
        return float(late_days*0.25+book_cost)
    else:
        return float(late_days*0.25)
def find_late_member(d_books,d_members):
    book_keys=d_books.keys()
    member_keys=d_members.keys()
    d_late={} 
    for book_key in member_keys:
        for member_key in book_keys:
            if book_key==member_key:
                phone_num=book_key
                book_code=d_books[phone_num][0]
                book_late_days=late_days(d_books[phone_num][1])
                book_cost=d_books[phone_num][1]
                book_penalty=penalty(book_late_days,book_cost)
                if phone_num in d_late:
                    d_late[phone_num][1]+=book_penalty
                    d_late[phone_num][2]+=d_late[phone_num]+'['+book_code+']('+str(book_late_days)+');'
                else:
                    d_late[phone_num][0]=d_members[phone_num][0]
                    d_late[phone_num][1]=book_penalty=book_penalty
                    d_late[phone_num][2]='['+book_code+']('+str(book_late_days)+');' 
    return d_late
def total_penalty(d_late):
    total_keys=d_late.keys()
    total=0
    for key in total_keys:
        total=total+d_late[key][1]
    return float(total)
def print_out(d_late):
    all_keys=d_late.keys()
    total_penalty_num=total_penalty(d_late)
    print('+--------------+------------------------------+--------+')
    print('| Phone Number | Name                         | Due    |')
    print('+--------------+------------------------------+--------+')
    for key in all_keys:
        print('|'+key+'|'+'%30s|$%5.2f|'%(d_late[key][0],d_late[key][1])+d_late[2:])
    print('+--------------+------------------------------+--------+')
    print('| Total Dues   |                            $    %5.2f|'%(total_penalty_num))
    print('+--------------+------------------------------+--------+')
main()