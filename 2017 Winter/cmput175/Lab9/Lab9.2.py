def main():
    infile=open('students.txt','r')
    students=[]
    #read and parse sample input
    for line in infile:
        line=line.strip()
        line=line.split(',')
        # create the student objects and store the data into a list of Student objects
        students.append(Students(line[0],line[1],line[2]))
    infile.close()
    
    print("Students information: ")
    for student in students:
        print(str(student))
    # ask the user to choose a way to sort the students
    way=input('Please choose the way to sort the students(ID,name,score):')
    while way!='ID' and way!='name' and way!='score':
        way=input('Please choose the way to sort the students(ID,name,score):')     
    Sort(students,way)
    # show the sorted information
    print('Sorted students information:')
    # store the sorted information into the file
    outfile=open('sorted_students.txt','w')
    outfile.write('sorting by %s:\n'%str(way))
    for student in students:
        print(str(student)) 
        outfile.write(str(student)+'\n')
    outfile.close()

def Sort(data,way):
    # -The textbook selection sort
    # go through the whole list
    for index in range(len(data)): 
        smallIndex = index
        # find the smallest element's index
        for i in range(index,len(data)):
            if data[i].compare(data[smallIndex],way): 
                smallIndex=i  
        # swap the elements
        temp=data[index] 
        data[index]=data[smallIndex] 
        data[smallIndex]=temp
        
class Students:
    # -A calss with student ID, name and score
    def __init__(self,ID,name,score):
        self.ID=ID
        self.name=name
        self.score=score
    def compare(self,student,way):
        # compare this student object to the other
        if way=='ID':
            return self.ID<student.ID
        elif way=='name':
            return self.name<student.name
        elif way=='score':
            return self.score<student.score
    def __str__(self):
        return '%s, %s, %s'%(str(self.ID),str(self.name),str(self.score))
       
main()