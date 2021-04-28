def main():
    # open the input text and read the information
    infile=open('input.txt','r')
    # create two dictionaries, one to store the information 
    #the other one to store the number of each interval
    d_data={}
    d_total={'0-9':0,'10-19':0,'20-29':0,'30-39':0,'40-49':0,'50-59':0,'60-69':0,'70-79':0,'80-89':0,'90-99':0}
    # split the lines and store the information into the dictionary d_data
    for line in infile:
        line=line.strip()
        id_num,score=line.split()
        d_data[id_num]=int(score)
    #print(d_data)
    max_score=0
    min_score=99
    total_score=0
    num=0
    for id_num in d_data:
        # for each id_num determine if the score is max or min and which interval it belongs to 
        # add up all the scores
        total_score+=d_data[id_num]
        num+=1
        # if the score greater than the max let max equal to this score
        if d_data[id_num]>max_score:
            max_score=d_data[id_num]
        # if the score less than the min let min equal to this score
        if d_data[id_num]<min_score:
            min_score=d_data[id_num]
        # determine which interval it belongs to 
        if d_data[id_num]>=0 and d_data[id_num]<=9:
            d_total['0-9']+=1
        elif d_data[id_num]>=10 and d_data[id_num]<=19:
            d_total['10-19']+=1
        elif d_data[id_num]>=20 and d_data[id_num]<=29:
            d_total['20-29']+=1
        elif d_data[id_num]>=30 and d_data[id_num]<=39:
            d_total['30-39']+=1 
        elif d_data[id_num]>=40 and d_data[id_num]<=49:
            d_total['40-49']+=1 
        elif d_data[id_num]>=50 and d_data[id_num]<=59:
            d_total['50-59']+=1 
        elif d_data[id_num]>=60 and d_data[id_num]<=69:
            d_total['60-69']+=1 
        elif d_data[id_num]>=70 and d_data[id_num]<=79:
            d_total['70-79']+=1   
        elif d_data[id_num]>=80 and d_data[id_num]<=89:
            d_total['80-89']+=1 
        elif d_data[id_num]>=90 and d_data[id_num]<=99:
            d_total['90-99']+=1  
            
    average_score=total_score/num
    infile.close()
    # call the function to write the index.html txt
    write_html(average_score,min_score,max_score,d_total)
    
def write_html(average_score,min_score,max_score,d_total):
    t=20
    message="""
<!DOCTYPE html>
<html>
<title>HTML Tutorial</title>
<body>

<h1>Welcom to statistics page!</h1>
<p>Average is: %8.4f
<br/>Minimum is: %d
<br/>Maximum is: %d
</p>

<table>

<tr>
<td valign="bottom">
<div style="width:30px;height:%dpx;background:blue;border:1px solid red;"></div>
</td>
<td valign="bottom">
<div style="width:30px;height:%dpx;background:blue;border:1px solid red;"></div>
</td>
<td valign="bottom">
<div style="width:30px;height:%dpx;background:blue;border:1px solid red;"></div>
</td>
<td valign="bottom">
<div style="width:30px;height:%dpx;background:blue;border:1px solid red;"></div>
</td>
<td valign="bottom">
<div style="width:30px;height:%dpx;background:blue;border:1px solid red;"></div>
</td>
<td valign="bottom">
<div style="width:30px;height:%dpx;background:blue;border:1px solid red;"></div>
</td>
<td valign="bottom">
<div style="width:30px;height:%dpx;background:blue;border:1px solid red;"></div>
</td>
<td valign="bottom">
<div style="width:30px;height:%dpx;background:blue;border:1px solid red;"></div>
</td>
<td valign="bottom">
<div style="width:30px;height:%dpx;background:blue;border:1px solid red;"></div>
</td>
<td valign="bottom">
<div style="width:30px;height:%dpx;background:blue;border:1px solid red;"></div>
</td>
</tr>

<tr>
<td>[0-9]</td>
<td>[10-19]</td>
<td>[20-29]</td>
<td>[30-39]</td>
<td>[40-49]</td>
<td>[50-59]</td>
<td>[60-69]</td>
<td>[70-79]</td>
<td>[80-89]</td>
<td>[90-99]</td>
</tr>

</table>

</body>
</html>"""%(average_score,min_score,max_score,t*d_total['0-9'],t*d_total['10-19'],t*d_total['20-29'],t*d_total['30-39'],t*d_total['40-49'],t*d_total['50-59'],t*d_total['60-69'],t*d_total['70-79'],t*d_total['80-89'],t*d_total['90-99'])
    
    # open the file and write the file
    outfile=open('index.htm','w')
    outfile.write(message)
    outfile.close()
    
    
    
main()