#!/usr/bin/env python
# coding: utf-8

# # Q.1 Write a program to find all pairs of an integer array whose sum is equal to a given number?

# In[141]:


def print_pairs(arr,n,sum):
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i] + arr[j] == sum):
                print('(',arr[i],',',arr[j],')')


# In[142]:


arr = [1,5,7,-1,5]
n = len(arr)
sum = 6 
print_pairs(arr,n,sum)


# In[ ]:





# # Q.2 Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
# 
# 

# In[143]:


arr = [1,2,3,4,5,6,7]
arr=arr[-1::-1]
arr


# In[ ]:





# # Q.3 Write a program to check if two strings are a rotation of each other?

# In[144]:


def areRotations(str1,str2):
    size1 = len(str1)
    size2 = len(str2)
    temp=''
    
    if size1 != size2:
        return 0
    temp=str1+str2
    
    if(temp.count(str2)>0):
        return 1
    else:
        return 0

str1=input()
str2=input()

if areRotations(str1,str2):
    print('Strings are rotations of each other')
else:
    print("Strings are not rotations of each other")


# In[ ]:





# # Q.4 Write a program to print the first non-repeated character from a string?

# In[145]:


st= "tutorialspointfordeveloper"
s=""
for i in st:
    if st.count(i)==1:
        s=s+i
        break
    else:
        pass
print(s)


# In[ ]:





# # Q.5 Read about the Tower of Hanoi algorithm. Write a program to implement it.

# In[146]:


def TowerOfHanoi(n,source,destination,auxil):
    if n==1:
        print('Move disk 1 from source',source,'to destination',destination)
        return 
    TowerOfHanoi(n-1,source,auxil,destination)
    print('Move disk',n,'from source',source,'to destination',destination)
    TowerOfHanoi(n-1,auxil,destination,source)


# In[147]:


n=5

TowerOfHanoi(n,'A','B','C')


# In[ ]:





# # Q.6 Read about infix, prefix and postfix expressions. Write a program to convert postfix to prefix expression.

# In[148]:


def isOperator(x):
    
    if x=='+':
        return True
    
    if x=='-':
        return True
    if x=='/':
        return True
    if x=='*':
        return True
    return False


def postToPre(post_exp):
    s=[]
    length = len(post_exp)
    
    for i in range(length):
        if (isOperator(post_exp[i])):
            
            op1 = s[-1]
            s.pop()
            op2=s[-1]
            s.pop
            
            temp = post_exp[i]+op2+op1
            
            s.append(temp)
            
        else:
            s.append(post_exp[i])
            
    ans = ''
    for i in s:
        ans+=i
    return ans


# In[149]:


post_exp=input()
postToPre(post_exp)


# In[ ]:





# # Q7.Write a program to convert prefix expression to infix expression.

# In[150]:


def prefixToInfix(prefix):
   stack = []
   
   i = len(prefix) - 1
   while i >= 0:
       if not isOperator(prefix[i]):
           stack.append(prefix[i])
           i -= 1
      
       else:
           str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
           stack.append(str)
           i -= 1
           
       return stack.pop()
   

def isOperator(c):
   if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
       return True
   else:
       return False       
   
str1 = "*-A/BC-/AKL"

print(prefixToInfix(str1))  


# In[ ]:





# # Q8.Write program to check if all the brackets are closed in a given code snippet.

# In[151]:


class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        
    def push(self,node_value):
        new_node=node(node_value)
        new_node.next = self.top
        self.top=new_node
        return new_node
    
    def is_empty(self):
        return self.top is None
    
    def pop(self):
        if self.is_empty():
            print("['Error']:stack is empty")
            return
        temp_node=self.top
        self.top=self.top.next
        return temp_node.data
    
    def peek(self):
        return self.top.data
    
    def delete(self):
        self.top=None
    
    def traverse(self):
        curr_node = self.top
        while curr_node is not None:
            print('{}'.format(curr_node.data),end='->')
            curr_node=curr_node.next


# In[152]:


def check_brackets(str):
    S = Stack()
    for c in str:
        if c in ["[",'{','(']:
            S.push(c)
        else: # ],},)
            if S.is_empty():
                print('All brackets are not closed')
                return
            c_from_s = S.pop()
            
            if c_from_s is '[' and c is not ']':
                print("All brackets are not closed")
                return
            if c_from_s is '{' and c is not '}':
                print('All brackets are not closed')
                return
            if c_from_s is '(' and c is not ')':
                print('All brackets are not closed')
                return
    if S.is_empty():
        print("All brackets are closed")
    else:
        print("All brackets are not closed")
            
            
check_brackets('[)()]')


# In[ ]:





# # Q9. Write a program to reverse a stack.

# In[160]:


class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        
    def push(self,node_value):
        new_node=node(node_value)
        new_node.next = self.top
        self.top=new_node
        return new_node
    
    def is_empty(self):
        return self.top is None
    
    def pop(self):
        if self.is_empty():
            print("['Error']:stack is empty")
            return
        temp_node=self.top
        self.top=self.top.next
        return temp_node.data
    
    def peek(self):
        return self.top.data
    
    def delete(self):
        self.top=None
    
    def traverse(self):
        curr_node = self.top
        while curr_node is not None:
            print('{}'.format(curr_node.data),end='->')
            curr_node=curr_node.next
    def reversed(self):
        l=[]
        curr_node = self.top
        while not self.is_empty():
            if curr_node is None:
                break
            else:
                l.append(curr_node.data)
                curr_node=curr_node.next
        print(l[::-1])
        
    def getmin(self):
        minn = float('inf')
        curr_node = self.top
        while not self.is_empty():
            if curr_node is None:
                break
            elif(curr_node.data<minn):
                minn=curr_node.data
            curr_node=curr_node.next
        return minn   
        


# In[161]:


ss=Stack()


# In[162]:


for i in range(10,50,10):
    ss.push(i)
ss.traverse()


# In[163]:


ss.reversed()


# In[164]:


ss.getmin()


# In[ ]:





# # Q10. Write a program to find the smallest number in using a stack.

# In[165]:


def getmin(self):
        minn = float('inf')
        curr_node = self.top
        while not self.is_empty():
            if curr_node is None:
                break
            elif(curr_node.data<minn):
                minn=curr_node.data
            curr_node=curr_node.next
        return minn  


# In[159]:


ss.getmin()


# In[ ]:




