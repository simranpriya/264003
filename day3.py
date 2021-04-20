#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"Hello Python"
print(__doc__)


# In[3]:


a = input("enter a number:")      # let's enter 10
b = input("enter a number:")      # let's enter 20
res = a + b
print(res)
print (type(res))
print(type(a))
print(type(b))


# In[ ]:


hh,mm,ss=10,12,25
# print time in hh:mm:ss format


# In[5]:


x=10
y=2.3
s1="hello"
ch='A'
flag=True
c1=2+3j
print(type(c1))
# similarly check type of others
print(isinstance(x,int))


# In[ ]:


a=10
b=20
del a
c=a+b
print(c)


# In[ ]:


fval=2.3
ival=int(fval)
print(ival)

ch='A'
#ival=int(ch,10)
aval=ord(ch)
print(aval)

s1="2378"
ival=int(s1)
s2="45a64"
#ival=int(s2)

ival=23
s3=str(ival)
print(s3)

hval="23"
ival=int(hval,16)
print(ival)

s4="12.235"
fval=float(s4)

print(int(0x1D))
print(hex(45))
print(oct(0o23))
print(bin(13))
print(int(0b11011))


# In[ ]:


a=32
b=10
c=a/b
d=a//b
print(c,d)
x=2
y=5
z=x**y
q=x(y-5)
x+=5


# In[ ]:


a=10
b=2
c=0
print(a and b)
print(b and a)
print(a and c)
print(c and b)
print(a or b)
print(b or a)
print(a or c)
print(c or b)


# In[ ]:


s1="Hello"
s2="Hello"
ch='e'
c2='x'
print(s1==s2)
print(s1 is s2)
print(ch in s1)
print(c2 not in s2)


# In[ ]:


xval = -12.785
print(abs(xval))
print(round(xval,2))


# In[ ]:


s1="abcd"
s2='xyz'
print(s1+s2)


# In[ ]:


s1="10"
s2="20"
s3=int(s1)+int(s2)
print(s3)


# In[ ]:


s1="abcd"
s1*=3    
print(s1)
s1+="xyz"
print(s1)
print("hello " * 3)
print(4 * "hello ")     


# In[44]:


a,b=10,20
a,b=b,a
print(a,b)


# In[46]:


a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)


# In[47]:


n=2378
a=(n/100)%10
b=(n/10)%10
c=(n%100)/10
d=(n%1000)/100