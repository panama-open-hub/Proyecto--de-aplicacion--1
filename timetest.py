from datetime import datetime, timedelta
import time

#ini_time_for_now = datetime.now() 
#print ("initial_date", str(ini_time_for_now)) 
#minutostranscurridos = ini_time_for_now + timedelta(seconds = 10)


#while ini_time_for_now =/= (minutos trnascurridos + timedelta(second=10)) :
 #   time.sleep(5)
  #  now = datetime.datetime.now()
   # minute = now.minute

#start = time.time()

#while time.time() - start < 20:
#    print ("test")
#    time.sleep(3)

#timeout = time.time() + 60*2   # 5 minutes from now
#while True:
 #   test = 0
  #  if test == 5 or time.time() > timeout:
   #     break
    #test = test - 1

timeout = 5   # [seconds]

timeout_start = time.time()
test = 0
print(datetime.now())
while time.time() < timeout_start + timeout:
    
    if test == 5:
        #print("Works")
        #print(datetime.now())
        #break
    test = test + 1
    #print(datetime.now())
print(datetime.now())

   
