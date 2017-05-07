#!usr/bin/python
proc={}
total=0
num=input("Enter the number of process:  ")
Qt=input("Enter Quantum time of processes: ")
for i in range(0,num):
   arr=input("Enter Arrival time of process: ")
   bT=input("Enter burst time of proces: ")
   if(i==0):
       min=arr	
   elif(min>arr):
       min=arr	
   proc[i+1]=[arr,bT,i+1]  
total=min
if(total>0):
	print  "idle time","0----------",total
a_time=proc.get(1)[0]
b_time=0
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
rem=0
count=0
i=1
j=num+1
wait=[]
turn=[]
tim=min
while(count!=num):
      rem=(proc.get(i)[1])-Qt
      if(proc.get(i)[1]>Qt):
         proc[j]=[proc.get(i)[0],rem,i]
         j=j+1
      if(rem>0):
         total=total+Qt
         print "process ",i," ",tim,"-----",total," "
      if(rem==0):
         total=total+proc.get(i)[1]
         print "process ",i," ",tim,"-----",total," "
         cntn=proc.get(i)[2]
         proc1[count+1]=[proc.get(cntn)[0],proc.get(cntn)[1],total]
         count=count+1
      if(rem<0):
         total=total+proc.get(i)[1] 
         print "process ",i," ",tim,"-----",total," "
         cntn=proc.get(i)[2]
         proc1[count+1]=[proc.get(cntn)[0],proc.get(cntn)[1],total]
         count=count+1
      tim=total
      i=i+1
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
 

   
