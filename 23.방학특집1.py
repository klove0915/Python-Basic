#!/usr/bin/env python
# coding: utf-8

# In[3]:


##################################################################################################################################

# 논리 자료형
# : TURE/FALSE을 나타내는 자료형

# 비교연산자
# :진술이 참이면 TRUE, 거짓이면 FLASE

print(3<5)   
print(7==5)
print(2>=10)
print(5!=10)


# In[4]:


# 논리 자료형의 연산

print(3==3 and 4<=5 and 6>2)
print(3==4 or 4<=5 or 6<2)
print(not 3==4)


# In[10]:


# 변수생성

a=1
b=2
print(a+b)

c = "Python"
print(c)


# In[14]:


# 조건문

a=3
if a>1 :
    print("a is greater than 1");
    
x=input()
if x in ['a','e','i','o','u']:
    print('모음입니다.')
else:
    print("자음입니다")


# In[13]:


# 빈복문

for a in [1,2,3]:
    print(a)
    
# => 실행해야 하는 문장을 여러번 반복해서 실행


i=0
while i <3:
    i=i+1
    print(i)


# In[16]:


#함수

def add(a,b):
    return a+b
add(3,4)


# In[17]:


###############################################################################################################################

# 자료형1 : 숫자

a=123 # 정수형
b=1.2 # 실수형
c=0o177 # 8진수
d=0x8ff # 16진수


# In[21]:


a=3
b=4
print(a+b)
print(a*b)
print(a/b)
print(a**b)
print(7%3) # 나머지 반환
print(7//4) # 몫을 반환


# In[22]:


## 14를 3으로 나누었을 때 몫과 나머지

print(14//3)
print(14%3)


# In[24]:


# 자료형2 : 문자

print("Hello World")
print('Python is fun')
print("""Life is too short, You need python""")
print('''Life is too short, You need python''')


# In[27]:


multiline="Life is too short \nYou need python"
print(multiline)

# \n : escape code


# In[28]:


head = "Python"
tail=" is fun"
head+tail


# In[29]:


a = "Python"
a*2


# In[35]:


a = "Life is too short"
len(a)


# In[41]:


## You need Python 을 문자열로 만들고 길이

b="You need Python"
len(b)


# In[45]:


# 문자열 인덱싱

a="Life is too short, you need Python"
print(a[3])
print(a[6])
print(a[7]) # 공백 출력(s와t사이의 공백)

#  -> 파이썬은 0부터 시작한다..


# In[52]:


a="Life is too short, you need Python"

print(a[0],a[12],a[-1])

# a[-1] 뒤에서 부터 첫 번째


# In[54]:


b=a[0]+a[1]+a[2]+a[3]
b


# In[55]:


a[0:4]


# In[56]:


a="20010331Rainy"
date=a[:8]
weather=a[8:]
print(date)
print(weather)


# In[60]:


## 문자열 포매팅(formatting)


print('I eat %d apples.' %3)
print('I eate %s apples' % "five")

number=3
"I eat %d apples" %number


# In[61]:


number=10
day="three"

"I ate %d apples. so I was sick for %s days" %(number, day)


# In[3]:


print("{0:<10}".format("hi")) #왼쪽정렬
print("{0:>10}".format("hi")) #오른쪽정렬
print("{0:^10}".format("hi")) #가운데정렬
print("{0:=^10}".format("hi")) #공백채우기


# In[4]:


y=3.141592
"{0:0.4f}".format(y)


# In[6]:


"{{ and }}".format()


# In[9]:


# f 문자열 포매팅

name = "홍길동"
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나의 이름은 {name}입니다. 나이는 {age+1}입니다.')


# In[11]:


d = {'name':'홍길동','age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'


# In[16]:


print(f'{"hi":<10}') #왼쪽정렬
print(f'{"hi":>10}') #오른쪽정렬
print(f'{"hi":^10}') #가운데정렬
print(f'{"hi":!<10}')

y=3.141592
print(f'{y:0.4f}') #소수점 4번째


# In[22]:


## format이나 f문자열 함수를 이용해 !!!Python!!! 출력

print("{0:!^12}".format("Python"))
print(f'{"Python" :!^12}')


# In[23]:


# 문자열 관련 함수

a = "hobby"
a.count('b') #a문자열 중 b가 몇 개 있나


# In[25]:


a="Python is the best choice"
print(a.find('b')) #a문자열 중 b가 어디에서 처음 등장하나
print(a.find('k')) #-1: 문자열에 해당 문자(k)가 없다


# In[26]:


a = "Life is too short"
print(a.index('t')) #a 문자열중 t가 어디 처음 등장하나
print(a.index('k')) # 문자열에 k가 없으므로 오류 출력


# In[28]:


",".join('abcd') # 문자열에 ,를 삽입해라


# In[29]:


a ="hi"
a.upper #소문자를 대문자로 


# In[31]:


a="HI"
a.lower() # 대문자를 소문자로


# In[34]:


a=" hi "
print(a.lstrip()) # 왼쪽 공백지우기 (left+strip=lstrip)
print(a.rstrip()) # 오른쪽 공백지우기
print(a.strip()) #양쪽 공백 지우기


# In[2]:


a = "Life is too short"
a.replace("Life", "Your leg") # 문자열 바꾸기


# In[4]:


a = "Life is too short"
print(a.split()) #공백기준으로 문자열 나눔

b = "a:b:c:d"
print(b.split(':'))


# In[ ]:




