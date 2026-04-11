# 1-Basic 
for i in  range(151):
  print(i)

# 2-Multiples of Five
for i in range(5,1001):
    if i%5==0:
      print(i)

# 3-Counting, the Dojo Way 
for i in range(1,101):
   if i%5==0:
      print("Coding")
   elif i%10==0:
      print("Coding Dojo")


#4-Whoa. That Sucker's Huge 
sum=0
for i in range(0,int(500e3)):
    if i%2 != 0:
        sum+=i
print(sum)


#5-Countdown by Fours
for i in range(2018, 0, -4):
    print(i)


# 6-Flexible Counter 
lowNum=2 
highNum=9
mult=3
for i in range(lowNum,highNum+1):
    if i%mult == 0 :
        print (i)
