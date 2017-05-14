#!usr/bin/python
#sjf
proc1={}
A_T=0
B_T=0
total=0
min1=0
num=input("enter number of process: ")
def inputfunc():
 for i in range(0,num):
   A_T=input("Enter Arrival time: ")
   if(i==0):
      min1=A_T
   elif(min1>A_T):
       min1=A_T
   B_T=input("Enter Burst time: ")
   proc1[i+1]=[A_T,B_T]
 a_time=proc1.get(1)[0]
 return (min1)

catch=inputfunc()

def sortArrivalTime():
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

sortArrivalTime()
#accordting t and w
def sortSJFfunc():
 b_time=0
 next1=2
 for j in range(1,num+1):
  b_time=proc1.get(j)[1]+b_time
  min=next1
  for i in range(j+1,num+1):  
       if(b_time>=proc1.get(i)[0] and proc1.get(i)[1]<proc1.get(next1)[1]):
          temp=proc1.get(next1)[0]
          proc1.get(next1)[0]=proc1.get(i)[0]
          proc1.get(i)[0]=temp
     
          temp=proc1.get(next1)[1]
          proc1.get(next1)[1]=proc1.get(i)[1]
          proc1.get(i)[1]=temp
  next1=next1+1
sortSJFfunc()
print "process in sjf order"
def printfunc():

 for i in range(1,num+1):
  print proc1.get(i)[0]," ",proc1.get(i)[1]
printfunc()
a_time=proc1.get(1)[0]

wait=[]
turn=[]

def waitandTurnFunc(catch1):
 total=catch1
 b_time=0
 sum1=total
 min2=total
 wait_time=0
 turn_time=0
 A_w=0
 A_t=0
 for i in range(1,num+1):
   min2=sum1
   wait_time=min2
   wait.insert(i-1,(min2-(proc1.get(i)[0])))
   b_time=proc1.get(i)[1]
   sum1=sum1+b_time;
   print min2,"----------------",sum1
   turn.insert(i-1,(sum1-proc1.get(i)[0]))
   A_w=A_w+wait[i-1]
   A_t=A_t+turn[i-1]
 print "avg waitng time ",A_w/num,"avg turnaround time:  ",A_t/num 
waitandTurnFunc(catch)
print "process"," ","Arrival time"," ","burst time"," ","waiting time"," ","turnaround time"
for i in range(1,num+1):
   print i,"\t\t",proc1.get(i)[0],"\t\t",proc1.get(i)[1],"\t\t",wait[i-1],"\t\t",turn[i-1]

