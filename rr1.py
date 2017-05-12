#!usr/bin/python
proc={}
total=0
num=input("Enter the number of process:  ")
Qt=input("Enter Quantum time of processes: ")
for i in range(0,num):
   arrival=input("Enter Arrival time of process: ")
   burst=input("Enter burst time of proces: ")
   if(i==0):
       min=arrival	
   elif(min>arrival):
       min=arrival	
   proc[i+1]=[arrival,burst,i+1]  
total=min
if(total>0):
	print  "idle time","0----------",total
A_time=proc.get(1)[0]
B_time=0
exe=0
for index in range(1,num+1):
   exe=index
   for j in range(index+1,num+1):
      if(proc.get(j)[0]<proc.get(exe)[0]):
         exe=j
   temp=proc.get(index)[1]
   proc.get(index)[1]=proc.get(exe)[1]
   proc.get(exe)[1]=temp

   temp=proc.get(index)[0]
   proc.get(index)[0]=proc.get(exe)[0]
   proc.get(exe)[0]=temp
	
   temp=proc.get(index)[2]
   proc.get(index)[2]=proc.get(exe)[2]
   proc.get(exe)[2]=temp
remain=0
count=0
index=1
last=num+1
wait=[]
turn=[]
min1=min
while(count!=num):
      remain=(proc.get(index)[1])-Qt
      if(proc.get(index)[1]>Qt):
         proc[last]=[proc.get(index)[0],remain,index]
         last=last+1
      if(remain>0):
         total=total+Qt
         print "process ",index," ",min1,"-----",total," "
      if(remain==0):
         total=total+proc.get(index)[1]
         print "process ",index," ",min1,"-----",total," "
         new_ind=proc.get(index)[2]
         proc1[count+1]=[proc.get(new_ind)[0],proc.get(new_ind)[1],total]
         count=count+1
      if(remain<0):
         total=total+proc.get(index)[1] 
         print "process ",index," ",min1,"-----",total," "
         cntn=proc.get(index)[2]
         proc1[count+1]=[proc.get(new_ind)[0],proc.get(new_ind)[1],total]
         count=count+1
      min1=total
      index=index+1
A_t=0
A_w=0 
for i in range (1,num+1):
   wait.insert(i-1,(proc1.get(i)[2]-proc1.get(i)[0]-proc1.get(i)[1]))
   turn.insert(i-1,(proc1.get(i)[2]-proc1.get(i)[0]))
   A_t=A_t+turn[i-1]
   A_w=A_w+wait[i-1]
print "process"," ","Arrival time"," ","burst time"," ","waiting time"," ","turnaround time"
for i in range(1,num+1):
   print proc.get(i)[2],"\t\t",proc1.get(i)[0],"\t\t",proc1.get(i)[1],"\t\t",wait[i-1],"\t\t",turn[i-1]
print "average waiting time: ",A_w/num," average turnaround time: ",A_t/num 
 

   
