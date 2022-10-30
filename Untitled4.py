#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#5a
a=int(input("Enter first numbr:"))
b=int(input("enter second number:"))
sum=a+b
diff=a-b
mul=a*b
div=a/b
rem1=a%b
rem2=-a%b
rem3=a%-b
rem4=-a%-b
exp=a**b
flr=a//b
print("sum of {} and {} is:{}".format(a,b,sum))
print("differnce of {} and {} is:{}".format(a,b,diff))
print("multiply of {} and {} is:{}".format(a,b,mul))
print("division of {} and {} is:{}".format(a,b,div))
print("reminder of {} and {} is:{}".format(a,b,rem1))
print("reminder of -{} and {} is:{}".format(a,b,rem2))
print("reminder of {} and -{} is:{}".format(a,b,rem3))
print("reminder of -{} and -{} is:{}".format(a,b,rem4))
print(" expotential of {} and {} is:{}".format(a,b,exp))
print("floor function of {} and {} is:{}".format(a,b,flr))


# In[ ]:


#assignment operators
x=5
print('x=',x)
x+=15
print('x=',x)
x-=5
print('x=',x)
x*=2
print('x=',x)
x/=2
print('x=',x)
x%=2
print('x=',x)
x//=2
print('x=',x)
x**=2
x=10
print('x=',x)
x&=2
print('x=',x)
x|=2
print('x=',x)
x^=1
print('x=',x)
x>>=4
print('x=',x)
x<<=5
print('x=',x)


# In[ ]:



#5b
rate=12
overtime=0
payoff=0
total=0
for i in range(0,10):
    hours=int(input('Enter the total work hours of employee{}:'.format(i+1)))
    if hours>40:
        overtime=hours-40
        payoff=overtime*rate
        total+=payoff
        print("Overtime payoff of employee {} is {}".format(i+1,payoff))
    else:
        print("Employee {} is not eligible for overtime".format(i+1))
print("Total overtime cost:",total)


# In[ ]:





# In[ ]:





# In[ ]:




