#!usr/bin/python

#fcfs
proc1={}
A_T=0
B_T=0
total=0

num=input("enter number of process: ")
for i in range(0,num):
   A_T=input("Enter Arrival time: ")
   if(i==0):
      min=A_T
   elif(min>A_T):
       min=A_T
   B_T=input("Enter Burst time")
   proc1[i+1]=[A_T,B_T]
print "process in fcfs order"
a_time=proc1.get(1)[0]
b_time=0
for index in range(1,num+1):
   #min=a_time
   exe=index
   for j in range(index+1,num+1):
      if(proc1.get(j)[0]<proc1.get(exe)[0]):
         exe=j
   temp=proc1.get(index)[1]
   proc1.get(index)[1]=proc1.get(exe)[1]
   proc1.get(exe)[1]=temp

   temp=proc1.get(index)[0]
   proc1.get(index)[0]=proc1.get(exe)[0]
   proc1.get(exe)[0]=temp
   print proc1.get(index)
total=min
if(total>0):
	print  "idle time","0----------",total
A_time=proc1.get(1)[0]
B_time=0
sum1=total
min1=total
wait_time=0
t_r_time=0
wait=[]
turn=[]
A_t=0
A_w=0
for i in range(1,num+1):
   min1=sum1
   wait_time=min1
   wait.insert(i-1,(min1-(proc1.get(i)[0])))
   A_w=A_w+wait[i-1]
   B_time=proc1.get(i)[1]
   sum1=sum1+B_time;
   print min1,"----------------",sum1
   
   turn.insert(i-1,(sum1-proc1.get(i)[0]))
   A_t=A_t+turn[i-1]
print "process"," ","Arrival time"," ","burst time"," ","waiting time"," ","turnaround time"
for i in range(1,num+1):
   print i,"\t\t",proc1.get(i)[0],"\t\t",proc1.get(i)[1],"\t\t",wait[i-1],"\t\t",turn[i-1]
print "average waiting time: ",A_w/num," average turnaround time: ",A_t/num  
