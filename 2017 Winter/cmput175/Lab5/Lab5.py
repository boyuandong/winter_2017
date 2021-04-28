def main():
    infile=open('infix_expression.txt')
    expression=infile.read()
    infix_expressions=expression.splitlines()
    # for each line in the infix expression
    for line in infix_expressions:
        # convert the infix to postfix and print
        postfix=infix_to_postfix(line)
        print(postfix)
        # calculate the reasut and print
        result=calculate_result(postfix)
        print(result)
        print('******')
    infile.close()  
def calculate_result(postfix):
    # calculate postfix result
    postfix_list=postfix.split()
    stack=Stack()
    # for each item in postfix expression
    for item in postfix_list:
        message=is_num(item)
        # if the item is a number then push it into the stack
        if message !='no_number':
            stack.push(item)
        # if the item is an operator
        else:
            operator=item
            # pop out two numbers in the stack and calculate the result of these two numbers
            operand2=int(stack.pop())
            operand1=int(stack.pop())
            if operator =='+':
                result=operand1 + operand2
            elif operator =='-':
                result=operand1 - operand2
            elif operator =='*':
                result=operand1 * operand2
            elif operator =='/':
                result=operand1 // operand2
            elif operator =='%':
                result=operand1 % operand2
            # push the result of two numbers into the stack
            stack.push(result)
    # pop out the result and return
    return stack.pop()
    
def infix_to_postfix(infix):
    # convert the infix to postfix
    # create a dictory of operators and level of the operators
    operator={}
    operator['+']=2
    operator['-']=2
    operator['*']=3
    operator['/']=3
    operator['%']=2
    operator['(']=1
    stack=Stack()
    postfix_list=[]
    token_list=infix.split()
    # for each token in the infix expression
    for token in token_list:
        message=is_num(token)
        # if the token is a number append it to postfix list
        if message=='is_number':
            postfix_list.append(token+' ')
        # if the token is a number contains '(' push '(' into stack and append the number to list
        elif message=='(in_number':
            stack.push('(')
            postfix_list.append(token[1:]+' ')
        # if the token is a number contains ')' append the number to list, then pop the numers in stack until '(' was popped out
        elif message==')in_number':
            postfix_list.append(token[0:len(token)-1]+' ')
            top_token=stack.pop()
            while top_token!='(':
                postfix_list.append(top_token+' ')
                top_token=stack.pop()
        # if the token is an operator 
        else:
            # when the stack is not empty and token is a lower level opertaor than the top stack operator, 
            # then append the top stack into list and finally push the token into the stack
            while (not stack.is_empty()) and (operator[stack.peek()]>=operator[token]):
                postfix_list.append(stack.pop())
            stack.push(token)
    # when stack is not empty append all the stock operators to the list and return the list
    while not stack.is_empty():
        postfix_list.append(stack.pop())
    return ''.join(postfix_list)
    
def is_num(string):
    # check if the string contains a number
    message=''
    try:
        # try if the string can be convertd to an int
        num=int(string)
        message='is_number'
    except ValueError:
        # if the string can not be converted to and int check if the stirng contains '('
        if '(' in string:
            try:
                # check if the string after '(' can be converted an int
                num=int(string[1:])
                message='(in_number'
            except ValueError:
                message='no_number'
        # check if the stirng contains ')'
        elif ')' in string: 
            try:
                # check if the string before the ')' can be converted to an int
                num=int(string[0:len(string)-1])
                message=')in_number'
            except ValueError:
                message='no_number'
        # if the string does not contain '(' or ')'
        else:
            message='no_number'
    return message
            
class Stack:
    
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)
        
    def pop(self):
        return self.__items.pop()
    
    def peek(self):
        return self.__items[len(self.__items)-1]
    
    def is_empty(self):
        return len(self.__items) == 0
    
    def size(self):
        return len(self.__items)  
main()