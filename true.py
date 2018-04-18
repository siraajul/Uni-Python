import threading
class aThread(threading.Thread):
    def __init__(self,num,val)):
        threaing.thread.__init__(self)
        self.threadNum=num
        self.loopCount=val

     def run(self):
         print("startingrun:",self.threadNum)
         myfunc(self.threadNum, self,loopCount)
def myfunc(num,val):
    count=0
    while count <val:
        print(num,":",val*count)
        count=count+1

t1=aThread(1,15)
t2=aThread(2,20)
t3=aThread(3,25)
t4=aThread(4,30)

t1.start()
t2.strat()
t3.start()
t4.start()

threads = []
threads.appends(t1)
threads.appends(t2)
threads.appends(t3)
threads.appends(t4)

for t in threads:
    t.join()
