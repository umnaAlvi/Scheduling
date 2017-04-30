#!usr/bin/python
proc={1:[0,4,2],2:[0,8,1],3:[0,9,4],4:[0,1,3]}
st_info=proc.get(1)
st_info1=proc.get(2)
st_info2=proc.get(3)
st_info3=proc.get(4)
tol=0
min=0
tim=0
pri=0
trt=[]
b_time=0
exe=0
a_time=proc.get(1)[0]
for k,b in proc.items():
   print("process :{0},AT,BT:{1}".format(k,b))
print "process in priority order"
for index in range(1,5):
   min=a_time
   exe=index
   for j in range(index+1,5):
      if(proc.get(j)[2]<proc.get(exe)[2]):
         exe=j
   temp=proc.get(index)[2]
   proc.get(index)[2]=proc.get(exe)[2]
   proc.get(exe)[2]=temp

   temp=proc.get(index)[1]
   proc.get(index)[1]=proc.get(exe)[1]
   proc.get(exe)[1]=temp

   temp=proc.get(index)[0]
   proc.get(index)[0]=proc.get(exe)[0]
   proc.get(exe)[0]=temp
   b_time=proc.get(index)[1]
   print proc.get(index)
   pri=tol
   tol=tol+b_time;
   
a_time=proc.get(1)[0]
b_time=0
total=0
tol=total
tim=total
wit=0
trt=0
wait=[]
turn=[]
j=0
A_w=0
A_t=0
for i in range(1,5):
   tim=tol
   wit=tim
   wait.insert(i-1,(tim-(proc.get(i)[0])))
   b_time=proc.get(i)[1]
   tol=tol+b_time;
   print tim,"----------------",tol
   turn.insert(i-1,(tol-proc.get(i)[0]))
   A_w=A_w+wait[i-1]
   A_t=A_t+turn[i-1]
print "process"," ","arrival time"," ","burst time"," ","priority"," ","waiting time"," ","turnaround time"
for i in range(1,5):
   print i," \t  ",proc.get(i)[0]," \t\t  ",proc.get(i)[1],"\t\t",proc.get(i)    [2],"\t\t ",wait[i-1],"\t\t ",turn[i-1]

print "average waiting time: ",A_w/4," average turnaround time: ",A_t/4 
