#!/usr/bin/env python
# coding: utf-8

# In[2]:


################################################################################

# 리스트 자료형
# : 숫자 모음을 표현하기 좋음

odd = [1,3,5,7,9]
odd


# 리스트명 = [요소1, 요소2, 요소3, 요소4 ...]


# In[4]:


a=[]
b=[1,2,3]
c=['Life','is','too','short']
d=[1,2,'Life','is']
e=[1,2,['Life','is']]

print(a,b,c,d,e)

# 리스트 안에는 어떠한 자료형 포함시킬 수 있다


# In[8]:


# 리스트 인덱싱

a = [1,2,3]
print(a)

print(a[0])
print(a[0]+a[2]) #1+3=4
print(a[-1]) #뒤에서 처음


# In[11]:


# 이중 리스트 인덱싱

a=[1,2,3,['a','b','c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[3][0]) 


# In[12]:


# 삼중 리스트 인덱싱

a = [1,2,['a','b',['Life','is']]]
print(a[2][2][0])


# In[13]:


# 리스트 슬라이싱 : 나누기

a = [1,2,3,4,5]
a[0:2] # 파이썬은 마지막 미포함 즉 0,1 번째만 추출


# In[15]:


## 문자열 슬라이싱

a = "12345"
a[0:2]


# In[16]:


a=[1,2,3,4,5]
b=a[:2]
c=a[2:]

print(b)
print(c)


# In[19]:


## ?? A=[1,2,3,4,5] 슬라이싱으로 [2:3] 만들기 ??

A=[1,2,3,4,5]
A[1:3]


# In[21]:


# 중첩리스트 슬라이싱

a = [1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])# a에서 3번째 객체의 0-1까지 추출


# In[24]:


# 리스트 연산

a = [1,2,3]
b = [4,5,6]
print(a+b) # 리스트 더하기

print(a*3) #리스트 반복하기

print(len(a)) #리스트 길이 구하기


# In[29]:


### 주의

a = [1,2,3]
print(a[2]+'hi') 

# 오류 발생 : 문자형태의 통합이 이루어 지지 않았기 때문에 (정수+문자=오류)


# In[30]:


str(a[2])+'hi' #str : 정수형을 문자형으로 


# In[32]:


# 리스트 수정

a = [1,2,3]
a[2]=4
print(a)


# In[33]:


# 리스트 삭제

a = [1,2,3]
del a[1]  # del : 뒤에 나오는 객체를 삭제한다
print(a)


# In[34]:


a = [1,2,3,4,5]
del a[2:]
print(a)


# In[38]:


# 리스트 관련 함수

# append ; 리스트에 요소를 추가
a=[1,2,3]
a.append(4)
print(a)

a.append([5,6])
print(a)


# In[39]:


# sort : 리스트를 순서대로 정렬
a = [1,4,3,2]
a.sort()
print(a)

a = ['a','c','b']
a.sort()
print(a)


# In[40]:


# reverse : 리스트를 역순으로 뒤집는다
a = ['a','c','b']
a.reverse()
print(a)


# In[43]:


# index : 특성 객체의 위치를 반환
a =[1,2,3]
print(a.index(3)) #3은 a의 a[2]번째 요소

print(a.index(0)) #0은 없기 때문에 오류


# In[44]:


# insert :리스트에 객체 삽입
a = [1,2,3,1,2,3]
a.remove(3)
print(a) # 처음에 등장한 3만 삭제


# In[48]:


# pop :리스트 요소 추출후 삭제
a = [1,2,3]
print(a.pop())
print(a)

b=[1,2,3]
print(b.pop(1))
print(b)


# In[49]:


# count ; 특정한 객체 개수세기
a = [1,2,3,1]
a.count(1)


# In[52]:


# extend :리스트 확장
a = [1,2,3]
a.extend([4,5])
print(a)

b=[6,7]
a.extend(b)
print(a)


# In[55]:


#################################################################################

# 튜플자료형
# : 거의 리스트와 흡사하지만 다르다
# 차이점 1 : 리스트 [] 튜플 ()
# 차이점 2 : 리스트는 값의 생성, 삭제, 수정 가능, 튜플은 불가능


t1=()
t2=(1,)
t3=(1,2,3)
t4=1,2,3
t5=('a','b',('ab','cd'))

print(t1,t2,t3,t4,t5)


# In[57]:


t1 = (1,2,'a','b')
del t1[0] #튜플의 객체는 삭제 될 수 없다 = 오류
t1[0]='c' #튜플의 객체는 변경 될 수 없다 = 오류


# In[58]:


# 튜플 인덱싱
t1 = (1,2,'a','b')
print(t1[0])
print(t1[3])


# In[59]:


# 튜플 슬라이싱
t1 = (1,2,'a','b')
t1[1:]


# In[62]:


# 튜플 연산

t2 = (3,4)
print(t1+t2) # 튜플 더하기

print(t2*3) # 튜플 곱하기

t1=(1,2,'a','b')
print(len(t1)) # 튜플 길이


# In[64]:


## ??(1,2,3)이라는 튜플에 값 4를 추가해 출력

a = (1,2,3)
a+(4,)


# In[65]:


###############################################################################3

# 딕셔너리 자료형
# : 대응관계를 가지고 있는 자료형
# key : value

dic = {
    'name':'pey',
    'phone':'01199993323',
    'birth' : '1118'
}

print(dic)


# In[66]:


a = {1:'hi'}
print(a)


# In[67]:


a = {'a' : [1,2,3]}
print(a)


# In[68]:


# 딕셔너라 쌍 추가, 삭제

a = {1:'a'}
a[2]='b'  # {2:'b'}라는 쌍을 추가
print(a)


# In[69]:


a['name']='pey'
print(a)


# In[71]:


# 딕셔너리에서 key를 통해 value 얻기

grade = { 'pey' :10, 'julliet':99}
grade['pey']


# In[74]:


a = {1:'a',2:"b"}

# key를 이용한 인덱싱
print(a[1])
print(a[2])


# In[75]:


dic = {
    'name':'pey',
    'phone':'01199993323',
    'birth' : '1118'
}

dic['name']


# In[77]:


a={1:'a',1:'b'}
print(a) # key가 중복되어 한 값 무시


# In[78]:


a = {[1,2]:'hi'}
a # key에 리스트 사용 불가


# In[82]:


# 딕셔너리 관련 함수

# keys ; key 리스트 만들기
a = {'name':'pey', 'phone':'0119993323','birth':'1118'}
print(a.keys()) # dict_keys의 형태로 반환

# key를 리스트로

for k in a.keys():
    print(k)

list(a.keys())


# In[83]:


# values : valuse 리스트 만들기

a.values()


# In[84]:


# items : key, value 쌍 얻기
a.items()


# In[85]:


# clear : key, value 다 지우기
a.clear()
print(a)


# In[90]:


# get : key로 value 얻기
a = {'name':'pey', 'phone':'0119993323','birth':'1118'}
print(a.get('name'))

print(a.get('foo','bar')) # foo라는 key가 없으면 bar를 반환(bar=디폴트)


# In[91]:


# in : 해당 key가 딕셔너리 안에 존재하는가
'name' in a


# In[92]:


## ?? 항목 : name, birth, age // 값 : 홍길동, 1128, 30 을 딕셔너리로 만드시오

dic = {'name':'홍길동','birth':'1128','age':30}
print(dic)


# In[ ]:




