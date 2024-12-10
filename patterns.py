import sortedcontainers
import re
import math
from abc import ABC, abstractmethod
from collections import Counter
import functools
import string
import random



n=5

for i in range(0,n+1):
    a = i
    for k in range(n-i):
        print(end=" ")
    b=False
    for j in range(1, 2*i-2):
        print(a, end="")
        if a<3:
            b=True
        if b:
            a+=1
        else:
            a-=1
    print("\r")

n=5
for i in range(n+1):
    for j in range(n-i):
        print(end=" ")
    for k in range(2*i-1):
        if k==0 or k==2*i-2:
            print("*", end="")
        else:
            if i==n:
                print("*", end="")
            else:
                print(end=" ")
    print("\n")

num=18
flag=False
if num == 1:
    print("Not prime")
elif num > 0:
    for i in range(2, num):
        if(num%i==0):
            flag=True
            break
    
if flag:
    print("Not prime")
else:
    print("Prime")

n=6

for i in range(1,n+1):
    for k in range(n-i):
        print(end=" ")
    for j in range(1, i):
        print(j,end=" ")
    print(1)

n=6
a=0
for i in range(n):
    for j in range(i):
        a=a+1
        print(a,end=" ")
    print("\n")

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")

n=12

for i in range(n+1):
    for j in range(i*2):
        print("*",end=" ")
    for k in range(1):
        print("*",end=" ")
    print("\n")

n=1
run=True
for i in range(1, n+1):
    for j in range(1, n+1):
        if j>n-i:
            print("",j,end="")
        else:
            print(end=" ")
    print("\n")

n=5
for i in range(1, n+1):
    for j in range(0, n+1):
        if j<i:
            print(end="  ")
        else:
            print(" *", end="")
    print("\n")

n=5
for i in range(1, n+1):
    for j in range(n+1):
        if j>=i:
            print("*",end="")
        else:
            print(end=" ")
    print("\r")

n=5
for i in range(1, n+1):
    for j in range(1,n+1):
        if j<=(n+1)-i:
            print("*",end="")
        else:
            print(end=" ")
    print("\n")

n=5
def display(limit):
    print("Crossroads")
    if limit > 1:
        display(limit - 1)
    
display(n)

n=5
for i in range(1, n+1):
    for j in range(1, i+1):
        if i==5 or j==1 or j==5:
            print("*", end=" ")
        else:
            print(end=" ")
    print(end="\n")

n=5
for i in range(1, n+1):
    for j in range(1, n*2+1):
        if(j<=i or j>n*2-i):
            print("*",end=" ")
        else:
            print(end="  ")
    print("\n")

n=5
for i in range(1, n*2+1):
    for j in range(1, i+1):
        if(j<=i and i<=n):
            print("*",end=" ")
        elif(j<=n*2-i):
            print("*", end=" ")
        
    print("\n")

n=10
for i in range(1, n+1):
    for j in range(1, n+1):
        if j<=n-i:
            print(end=" ")
        elif i%2!=0:          
            print(i,end=" ")
    print("")

n=5
for i in range(1, n+1):
    for k in range(1, n+2-i):
        print(end="  ")
    for j in range(1, 2*i):
        print(j,end=" ")
    
    print("\n")

n=5
for i in range(1, n*2+1):
    for j in range(1, n+1):
        if j<=n+1-i and i<=n:
            print("*",end=" ")
        elif j<=i-n and i>n:
            print("*",end=" ")
    print("\r")

n=10
for i in range(1, n+1):
    for j in range(1, n+1):
        if j<=i or j>n-i:
            print("*", end=" ")
        else:
            print(end="  ")
    print("\n")

n =5
count = 1
for i in range(0, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print("1\n")

n=5
for i in range(1, n+1):
    for j in range(1, i*2):
        print("*",end=" ")
    print("\n*\n*\n")

n=5
for i in range(1, n+5):
    for j in range(1, 2*i):
        print("*",end=" ")
    print("\n")

n=9
for i in range(1,n):
    for j in range(2,n):
        if j<=i or j>n-i:
            print("*", end=" ")
        else:
            print(end="  ")
    if i>=5:
        break
    print("\n")

size=5
i=0
j=0
while i<=size:
    i=i+1
    while j<=size:
        j=j+1
        if j<=i or j>size-i:
            print("*", end=" ")
        else:
            print(end=" ")
        
    print("\n")

print("Enter numbers")
array = []

for i in range(0,5):
    array.append(int(input()))
count =0
for i in range(4):
    for j in range(i,5):
        if(array[i]==array[j]):
            count = count+1
            print(i,j)
print(count,"*")


class Solution:
    def isValid(self, s: str) -> bool:
        array=[]
        count=0
        if(len(s)%2==0):
            flag=True
            for i in s:
                array.append(i)
            i=0
            while i<len(array):
                if(i%2==0 and array[i]=="(" and array[i+1]==")" or array[i]=="[" and array[i+1]=="]" or array[i]=="{" and array[i+1]=="}" or i<=len(array)/2 and array[i]=="(" and array[(len(array)-1)-i]==")" or array[i]=="[" and array[(len(array)-1)-i]=="]" or array[i]=="{" and array[(len(array)-1)-i]=="}"):
                    if(ord(array[i+1])-ord(array[i])<5 and ord(array[i+1])-ord(array[i])>0):
                        i=i+1
                else:
                    print(i)
                    flag=False
                i=i+1
        else:
            flag=False
        if(flag):
            print(True)
        else:
            print(False)
    s="([])"
    isValid(0, s)

nums1=[0]
nums2=[1]
m=0
n=1
k=0
for i in range(m,m+n):
    nums1[i] = nums2[k]
    k=k+1
for s in range((m+n)-1):
    for j in range(s+1, m+n):
        if(nums1[s]>nums1[j]):
            temp=nums1[s]
            nums1[s]=nums1[j]
            nums1[j]=temp
print(nums1)

x=101
a=str(x)
array=[]
isPalindrome=True
for i in a:
    array.append(i)

for i in range(len(array)):
    if(int(array[i])!=int(array[len(array)-1-i])):
        isPalindrome=False
if(isPalindrome):
    print(True)
else:
    print(False)

def isPalindrome(x):
    return x == x[::-1]

res=isPalindrome("122")
print(res)


array=[]
pos=[]
nums=[-1,0,1,2,-1,-4]
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            if((nums[i]+nums[j]+nums[k])==0 and i!=j and i!=k and j!=k):
                if([nums[i],nums[j],nums[k]] or [nums[i],nums[k],nums[j]] or [nums[j],nums[i],nums[k]] or [nums[j],nums[k],nums[i]] or [nums[k],nums[i],nums[j]] or [nums[k],nums[j],nums[i]] in array):
                    pos.append([i,j,k])
                else:
                    array.append([nums[i],nums[j],nums[k]])
print(array,"\n")
print(pos)

x=[1,2,3,3,2]

val = set(x)
st = list(val)
print(st)

s="fly me   to   the moon  "
a=s[::-1]
count=0
alph=False
for i in a:
    if i!=" ":
        alph=True
    if alph and i==" ":
        break
    if alph and i!=" ":
        count=count+1
print(count)

n=3
i=n-1
k=2
pro=n
val=n-k
j=val-1
den=val
while i>0:
    pro=pro*i
    i=i-1
while j>0:
    den=den*j
if den==0:
    den=1
print(pro/den)

s="A man, a plan, a canal: Panama"
resp=""
spc=[",",".",";",":","-","_"]
for i in s:
    if i!=" " and i not in spc:
        resp=resp+i
resp=resp.lower()
if resp==resp[::-1]:
    print( True)
else:
    print( False,resp)

array=[]
nums=[3,3,4]
for i in range(len(nums)):
    count=1
    for j in range(len(nums)):
        if(nums[i]==nums[j] and i!=j):
            count=count+1
    array.append(count)
lar=array[0]
pos=0
for i in range(0,len(array)):
    if lar<array[i]:
        lar=array[i]
        pos=i
print( lar)

array=[0,1,2,2,3,0,4,2]
val=2
i=0
while i<len(array)-k:
    if array[i]==val:
        array.pop(i)
        i=i-1
    i=i+1
print(len(array), array)

array=[3,9,3]
count=0
for i in range(len(array)):
    for j in range(len(array)):

        if(array[i]>array[j]):
            if(array[i]%2==0):
                array[i]=int(array[i]/2)
                array.insert(i+1, int(array[i]))
            else:
                array[i]=int((array[i]+1)/2)-1
                array.insert(i+1, int(array[i]+1))
print(array)


s="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"       
array=[]
stg=[]
lar=0
def ins(length, pos, val):
    for i in range(0,length):
        stg.insert(pos, val)
        pos=pos+1

for i in range(len(s)):
    count=1
    for j in range(len(s)):
        if(s[i]==s[j] and i!=j):
            count=count+1
    array.append(count)

for k in range(len(array)):
    if(array[k]%2==0):
        if(len(stg)==0):
            for i in range(array[k]):
                stg.append(s[k])
        else:
            if(s[k] not in stg):
                pos=int(len(stg)/2)
                ins(array[k], pos, s[k])
    else:
        if(array[k]>lar):
            lar=array[k]
            val=k
print(s[val])
if(lar>0):
    if(lar==1):
        hlf=int(len(stg)/2)
        stg.insert(hlf, s[val])
    elif(len(stg)==0):
        for i in range(lar):
            stg.append(s[val])
    else:
        hlf=int(len(stg)/2)
        ins(lar, hlf, s[val])
print(array)

s="cccdd"
dict={}
array=[]
lar=0
def ins(length, pos, val):
    for i in range(0,length):
        array.insert(pos, val)
        pos=pos+1
for i in range(len(s)):
    count=1
    for j in range(len(s)):
        if(s[i]==s[j] and i!=j):
            count=count+1
    dict={**dict, s[i]:count}
for i in dict.keys():
    if(dict[i]%2==0):
        if(len(array)==0):
            for j in range(dict[i]):
                array.append(i)
        else:
            pos=int(len(array)/2)
            ins(dict[i], pos, i)
    else:
        if(dict[i]>lar):
            lar=dict[i]
            val=i

if(lar>0):
    if(lar==1):
        hlf=int(len(array)/2)
        array.insert(hlf, val)
    elif(len(array)==0):
        for i in range(lar):
            array.append(val)
    else:
        hlf=int(len(array)/2)
        ins(lar, hlf, val)

print(dict)

s_len = len(s)
if s == s[::-1]:
    print(s_len)

chars = {}
palindrome_length = 0

for n in s:
    if chars.get(n):
        chars[n] += 1
        if chars[n] % 2 == 0:
            palindrome_length += 2
    else:
        chars[n] = 1

print(palindrome_length + 1 if s_len - palindrome_length != 0 else palindrome_length)

nums = [2,0]
size=0
while size<len(nums):
    pos=size
    if(nums[size]==0):
        break
    size=(size+nums[size])
if(size-pos+1==len(nums)):
    print (True)
else:
    print (False)

s = "ab"
t = "baab"
same=True
array=""
lar=-1
for i in range(0,len(s)):
    for j in range(0,len(t)):
        if(s[i] == t[j] and j>lar):
            array=array+s[i]
            if(j>lar):
                lar=j
if array == s:
    print(True)
else:
    print(array)

s="XIX"
res=0
dict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

for i in s:
    res=res+dict[i]
if(s[len(s)-2]=='I' and dict[s[len(s)-1]]>1):
    res=res-2

print(res)

array=[1,2,2,3,4,5]
count=0
size=len(array)-1
for i in range(size):
    if(count>0 and array[i-1] == array[i]):
        array[i]=array[i+1]
        size=size-1
    print(array[i])
    count=count+1

s=""
sdict={}
tdict={}
if(len(s)!=len(t)):
    print (False)
for i in range(len(s)):
    scount=1
    tcount=1
    for j in range(len(s)):
        if(s[i]==s[j] and i!=j):
            scount=scount+1
        if(t[i]==t[j] and i!=j):
            tcount=tcount+1
    sdict={**sdict,s[i]:scount}
    tdict={**tdict,t[i]:tcount}
if(sdict==tdict):
    print (True)
else:
    print (False)

dominoes=[[2,1],[1,2],[1,2],[1,2],[2,1],[1,1],[1,2],[2,2]]
array=[]
k=[]
l=[]
count=0
for i in range(len(dominoes)-1):
    for j in range(i+1,len(dominoes)):
        k=(dominoes[i])
        l=(dominoes[j])
        if(k[0] in dominoes[j] and k[1] in dominoes[j] and l[0] in dominoes[i] and l[1] in dominoes[i] or dominoes[i]==dominoes[j]):
            count=count+1
            print(dominoes[i],i, dominoes[j],j,count)
    array.append(dominoes[i])
print (count)

dominoes = [[2,1],[1,2],[1,2],[1,2],[2,1],[1,1],[1,2],[2,2]]

# Create a dictionary to count the occurrences of each unique sorted domino
domino_count = {}

count = 0

for domino in dominoes:
    # Sort the domino to ensure consistent representation
    domino.sort()
    
    # Convert the sorted domino to a tuple for hashing
    domino_tuple = tuple(domino)
    print(domino_tuple)
    # If the domino is in the dictionary, increment the count
    if domino_tuple in domino_count:
        count += domino_count[domino_tuple]
        domino_count[domino_tuple] += 1
    else:
        domino_count[domino_tuple] = 1

print(domino_count)

count=0
dict={}
for domino in dominoes:
    domino.sort()
    tup=tuple(domino)

    if(tup in dict):
        count+=dict[tup]
        dict[tup]+=1
    else:
        dict[tup]=1
print (count)

nums = [3,1]
lis = set(nums)
res=list(lis)
res.sort()
nums.sort()
if(lis==nums):
    print (False)
else:
    print (res,nums)

n=8
array=[]

for i in range(8):
    tem=[1] 
    for j in range(len(array)):
        if(j==len(array)-1):
            tem.append(1)
        else:
            pre=array[i-1]
            for k in range(len(pre)):
                if k>0 and len(tem)<=len(pre)-1:
                    tem.append(pre[k-1]+pre[k])
    temp=tem
    array.append(tem)
    
print(array)

date = "1992-09-14"
array=[31,28,31,30,31,30,31,31,30,31,30,31]


d=date.split("-")
m=int(d[1])
count=0
for i in range(m-1):
    count=count+array[i]
    print(array[i])
y=int(d[0])
if y%4==0 and m>2 and y!=1900:
    count=count+1
print(count+int(d[2]))


nums = [2,2,1,1,1,2,2,3,3]
dict={}

for i in nums:
    if i in dict:
        count=dict[i]+1
        dict={**dict,i:count}
    else:
        dict={**dict,i:1}
lar=0
for i in dict:
    if dict[i]>lar:
        lar=dict[i]
        max=i
print(max)

num=25
array=[0,0,1]
for i in range(2,num+1):
    array.append(array[i-2]+array[i-1]+array[i])
print(array[num+1])

n=4
num=n*2
i=num
com=1
while i>0:
    com=com*i
    i-=1

print(int(com/2**n))

nums = [-1,-1,2]
dict={}
value=True
for i in nums:

    if i in dict:
       
        count=dict[i]
        dict[i]=count+1
    else:
        dict={**dict, i:1}
temp=100
for j in dict:
    if dict[j]<temp:
        temp=dict[j]
        val=j
print(val)

nums = [1,3,5,6]
target = 7
position=None
val=nums[0]
if target in nums:
    for i in range(len(nums)):
        if nums[i]==target:
            position=i
            break
elif target<nums[len(nums)-1]:
    for i in range(len(nums)):
        if target<nums[i]:
            nums.insert(i, target)
            position=i
            break
else:
    nums.insert(len(nums), target)
    position=len(nums)-1
print(position, nums)

haystack = "sadbutsad"
needle = "but"

if needle in haystack:
    print(haystack.index(needle))
else:
    print(-1)
arr=[]
arr.sort()

s="hello"
vowel=['a','e','i','o','u','A','E','I','O','U']
alph=""
k=""
s=list(s)
for i in s:
    if i in vowel:
        alph+=i
count=len(alph)-1
for i in range(len(s)):
    if s[i] in vowel:
        s[i]=alph[count]
        count-=1
for i in s:
    k+=i
print (k)

s = "lEetcOde"
vowels=['a','e','i','o','u','A','E','I','O','U']
array=[]
vowel=""
res=""
s=list(s)
for i in s:
    if i in vowels:
        array.append(ord(i))
array.sort()
for j in array:
    print(chr(j))
    vowel+=chr(j)
count=0
for k in range(len(s)):
    if s[k] in vowels:
        res+=vowel[count]
        count+=1
    else:
        res+=s[k]

print (res)

s="pwwkew"
array=[]
res=""
for i in s:
    array.append(i)
array=set(array)
for j in array:
    res+=j

print(res)

n = 3
i=n
while i>2:
    i/=2
    
print(i)

nums = [0,0,1,0,3,12]
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]==0 and nums[j]!=0:
            nums[i]=nums[j]
            nums[j]=0
print(nums)

nums = [0,1,0,3,12]
for i in nums:
    if i==0:
        nums.remove(i)
        nums.append(0)
print(nums)

nums = [1,2,2,1,1,0]
for i in range(len(nums)-1):
    if nums[i]==nums[i+1]:
        nums[i]*=2
        nums[i+1]=0

for i in nums:
    if nums[i]==0:
        nums.remove(nums[i])
        nums.append(0)
print(nums)

num = 8
dict={1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
i=num
out=""
while i>0:
    if i>=1000:
        i-=1000
        out+=dict[1000]
    elif i>=900:
        i-=900
        out+=dict[100]
        out+=dict[1000]
    elif i>=500:
        i-=500
        out+=dict[500]
    elif i>=400:
        i-=400
        out+=dict[100]
        out+=dict[500]
    elif i>=100:
        i-=100
        out+=dict[100]
    elif i>=90:
        i-=90
        out+=dict[10]
        out+=dict[100]
    elif i>=50:
        i-=50
        out+=dict[50]
    elif i>=40:
        i-=40
        out+=dict[10]
        out+=dict[50]
    elif i>=10:
        i-=10
        out+=dict[10]
    elif i>=9:
        i-=9
        out+=dict[1]
        out+=dict[10]
    elif i>=5:
        i-=5
        out+=dict[5]
    elif i>=4:
        i-=4
        out+=dict[1]
        out+=dict[5]
    else:
        i-=1
        out+=dict[1]
print(out)
        
num1 = "-123"
num2 = "456"
print(int(num1)*int(num2))

arr=[4,2,1,3]
arr.sort()
diff=[]
for i in range(len(arr)-1):
    diff.append(arr[i+1]-arr[i])
mins= min(diff)

for i in range(len(arr)-1):
    if arr[i+1]-arr[i]==mins:
        print([arr[i+1],arr[i]])

i=0
arr=[1,2,3,4,5,6,7,8,9,10]
while i<len(arr):
    if arr[i]%2==0:
        
        arr.insert(i+1,0)
        arr.insert(i+2,0)
        i+=3
    else:
        i+=1
print(arr)

i=0
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
while i<len(arr):
    if arr[i]%5==0 and i<len(arr)-1:
        arr.remove(arr[i+1])
        arr.remove(arr[i+1])
    i+=1
print(arr)

coordinates=[[0,0],[0,1],[0,-1]]
diff=False
diffx=[]
diffy=[]
h=0
out=True
for i in range(len(coordinates)):
    k=coordinates[i]
    if(i<len(coordinates)-1):
        l=coordinates[i+1]
    for j in range(len(coordinates[i])-1):
        if(diff):
            if(k[0]-k[1]==diff):
            
                if i<len(coordinates)-1: 
                    diffx.append(l[0]-k[0])
                    diffy.append(l[1]-k[1])
                    if diffx[h-1]==diffx[h] and diffy[h-1]==diffy[h]:
                        h+=1
                        print(True)
                    elif(diffx[h]%diff==0 and diffy[h]%diff==0):
                        h+=1
                    else:
                        out=False
                        break
            else:
               out=False
               break
        else:
            diff=k[0]-k[1]
print(out)

arr=[7,6,4,3,1]
diff={}

for i in range(len(arr)-1):
    minval=arr[0]
    for j in range(i+1, len(arr)):
        if arr[i]-arr[j]<minval:
            minval=arr[i]-arr[j]
            buyval=arr[i]
            sellval=arr[j]
    diff={**diff,minval:[buyval, sellval]}
get=min(diff)
val=diff[get]
res=val[1]-val[0]
if res<=0:
    res=0
print(res)

minval=arr[0]
for i in arr:
    if i<minval:
        minval=i
print(minval)

size=2
for i in range(1,4):
    for j in range(i):
        print("*\n")

    for k in range(i):
        for l in range(size):
            print("*",end=" ")
        print("\n")
    size*=2

arr=[7,3,5,2,10,6,8,1,4,9]
size=len(arr)
n=size-1
i=0
diff=[]
for i in range(size//2):
    if i==n:
        break
    if arr[i]>arr[n]:
        diff.append(arr[i]-arr[n])
    else:
        diff.append(arr[n]-arr[i])
    i+=1
    n-=1
print(diff)

n=234
s=str(n)
product=1
sum=0
for i in s:
    sum+=int(i)
    product*=int(i)
print(product-sum)

n=7
sum=0
for i in range(1, n):
    if i%3==0 or i%5==0 or i%7==0:
        sum+=i
print(sum)

num = 555
s=str(num)
large=""
small=""
for i in range(len(s)):
    large+="9"
    small+="1"
large=int(large)
small=int(small)
print(large-small)

nums = [-100,-98,2,3,4]
product=1
for i in nums[::-1]:
    product*=i
    print(i)
print (product)

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

for i in range(9):
    for j in range(9):
        print(int(board[j]))

strs = ["cir","car"]
retstr=strs[0]
for i in range(1,len(strs)):
    val=strs[i]
    rem=retstr.strip(val)
    retstr=retstr.strip(rem)
print(retstr)

arr = [72693,6006,61535,76909,63966,24927,45368,39107,90656,46356,38,15620,55905,31188,69368,64534,56257,83027,56098,52945,26106,72676]
for i in range(len(arr)-1):
    arr[i]=0
    for j in range(i+1,len(arr)):
        if arr[j]>arr[i]:
            arr[i]=arr[j]
arr[len(arr)-1]=-1
print(arr)
array=list(arr)
for i in range(len(arr)):
    array[i]=0
    val=max(array)
    arr[i]=val
arr[len(arr)-1]=-1
print(arr)

import random
n=6
array=[]
count=0
i=0
while len(array)<n-1:
    val=random.randint(-n,n)
    if val not in array and val!=0:
        array.append(val)
        count+=array[i]
        i+=1
if -count not in array:
    array.append(-count)
else:
    zindex=array.index(-count)
    array[zindex]=0
    array.append(-count+-count)
print(array, count, -count)

strs =["aa","a"]

retstr=strs[0]
for i in range(1,len(strs)):
    val=strs[i]
    rem=retstr.strip(val)
    if rem and retstr.index(rem[-1])<len(retstr)-1:
        rem=retstr.strip(val[:-1])
    retstr=retstr.strip(rem)
print (retstr)

num = 969
num = str(num)
ins=True
ret=""
for i in range(len(num)):
    if int(num[i])<9 and ins:
        temp=9
        ins=False
    else:
        temp=int(num[i])
    ret+=str(temp)
print(int(ret))
i=num
print(num)
count=0
while i>1:

    if(i%10==6):
        mul=3*(10**count)
        num+=mul
        break
    count+=1
        
    i=int(i/10)
print(num)

rowIndex=0
array=[]
for i in range(rowIndex+1):
    temp=[1]
    if i>0:
        k=array[i-1]
        for j in range(1,len(array[i-1])):
            temp.append(k[j-1]+k[j])
        temp.append(1)
    array.append(temp)
print(array[rowIndex])

nums = [1,2,3,4,5]
array=[nums]
size=len(nums)
for i in range(1,len(nums)):
    temp=[]
    k=array[i-1]
    for j in range(len(k)-1):
        if k[j]+k[j+1]>=10:
            temp.append((k[j]+k[j+1])-10)
        else:
            temp.append(k[j]+k[j+1])
    array.append(temp)
    retrn=temp[0]
print(array)


s = "11111222223"
k = 3
array=[[s]]

for i in range(len(array)):
    temp=[]
    for j in range(len(s)):
        
        if len(temp)<k:
            temp.append(s[j])

        else:
            array.append(temp)
            temp=[]
            temp.append(s[j])
array.append(temp)

print(array)

#2293. Min Max Game
nums = [9089,6622,866,6984,6570,3,2,54,676,1,1,1,2,3,1,1,1,2,3]
array=[nums]
Flag=True
for i in range(len(nums)//2):
    k=array[i]
    j=0
    temp=[]
    while j<len(k)-1:
        if k[j]>k[j+1]:
            minval=k[j+1]
            maxval=k[j]
        else:
            minval=k[j]
            maxval=k[j+1]
        if Flag:
            temp.append(minval)
            Flag=False
        else:
            temp.append(maxval)
            Flag=True
        j+=2
    if len(temp)>0:
        array.append(temp)
print(array)

nums = [1,3,4,2,2,2]
dict={}
maxval=0
pos=0
for i in nums:
    if i in dict:
        count=dict[i]
        dict={**dict,i:count+1}
    else:
        dict={**dict,i:1}
    if dict[i]>maxval:
        maxval=dict[i]
        pos=i

print(i)

arr=[-388569,306282,287409,-219412,-467061,455422,368053,1568,59695]
array=list(arr)
array.sort()
dict={}
rank=[]
size=1
sets=set(array)
arry=list(sets)
arry.sort()
for i in range(len(array)):
    if array[i]==array[i-1]:
        dict={**dict, array[i]: arry.index(array[i])}
    else:
        dict={**dict, array[i]: size}
        size+=1
for i in arr:
    rank.append(dict[i])
print(arry)
print(array)
print(rank)

s="abb"
r=s[::-1]
t=""
for i in range(len(s)):
    print(s[i],s[len(s)-1-i])

height = [2,3,5,2,1,3,6,2,7]
diff=[]
for i in range(len(height)-1):
    temp=0
    for j in range(i+1,len(height)):
        if height[i]<height[j]:
            length=height[i]
        else:
            length=height[j]

        breadth= j-i

        if length*breadth>temp:
            temp=length*breadth
    diff.append(temp)

area=max(diff)
print(area)

n = 19
res=False
j=0
while j<100:
    n=str(n)
    product=0
    
    for i in n:
        product+=int(i)*int(i)
        
    
#     n=product
#     print(product)
#     if n==1:
#         break
#     j+=1

# if n==1:
#     res=True

mat=[
    [1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]
]
k=3
dictionary={}
array=[]
for i in range(len(mat)):
    arr=mat[i]
    count=0
    for j in range(len(arr)):
        if arr[j]==1:
            count+=1
    dictionary={**dictionary,i:count}
    array.append(count)
array.sort()


x=dict(sorted(dictionary.items(), key=lambda item: item[1]))
lis=[]
for i in x:
    lis.append(i)
    if len(lis)>=k:
        break
print(lis)

s = "ab"
t = "baab"
same=True
array=""
lar=-1
for i in range(0,len(s)):
    for j in range(0,len(t)):
        if(s[i] == t[j] and j>lar):
            array=array+s[i]
            if(j>lar):
                lar=j
if array == s or s in t:
    print (True)
else:
    print (False)

num=38
sum=0
num=str(num)
i=0
while True:

    if len(str(num))<=i:
        num=sum
        i=0
        sum=0
        num=str(num)

    sum+=int(num[i])
    i+=1


    if len(str(num))<=1:
        break
print(type(num))

nums=[8,1,2,2,3]
arr=[]
for i in range(len(nums)):
    count=0
    for j in range(len(nums)):
        if nums[i]>nums[j]:
            count+=1
    arr.append(count)
print(arr)

nums1 = [1,2,2,1]
nums2 = [2,2]

set1=set(nums1)
set2=set(nums2)

inter=list(set1.intersection(set2))
print(inter)

s="malayala"
t=s[::-1]
if s==t:
    print(1)
else:
    print(2)

word1 = "abc"
word2 = "pqr"
val=""
len1=len(word1)
len2=len(word2)

if(len1>len2):
    long=len1
else:
    long=len2

for i in range(long):
    if i<len1:
        val+=word1[i]
    if i<len2:
        val+=word2[i]
print(val)

nums = [1,2,3,4]
val=-1
for i in nums:
    strg=str(i)
    if len(strg)>1:
        strg=strg[::-1]
        strg=int(strg)
        if strg in nums and i+strg>val:
            val=i+strg

print(val)

s="leetcode"
val=""
dict={}
arr=[]

for i in s:
    arr.append(i)
arr.sort()
for i in s:
    if i in dict:
        count=dict[i]
        dict={**dict, i:count+1}
    else:
        dict={**dict, i:1}

sets=set(arr)

lis=list(sets)
lis.sort()

reverse=False
i=0
const = False
while len(val)<=len(s):
    print(dict, lis)
    print(i, len(lis))
    if(dict[lis[i]]<=0):

        lis.remove(lis[i])
        if len(lis)==0:
            break
    
    if dict[lis[i]]>0:
        count=dict[lis[i]]
        val+=lis[i]
        dict={**dict, lis[i]:count-1}
    
    if i==0:
        reverse=False
        if const and dict[lis[i]]>0:
            val+=lis[i]
            count=dict[lis[i]]
            dict={**dict, lis[i]:count-1}

    elif i==len(lis)-1:
        reverse=True
        if const and dict[lis[i]]>0:
            val+=lis[i]
            count=dict[lis[i]]
            dict={**dict, lis[i]:count-1}


    const=True

    if len(lis)<=1:
        i=0
    elif reverse:
        i-=1
    else:
        i+=1

print(val, dict)

nums = [-1,1,2,3,1]
target = 2
count=0
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if (nums[i]+nums[j]) < target and i != j:
            count+=1
print(count)

nums = [0,1,7,4,4,5]
lower = 3
upper = 6
count=0

for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if (nums[i]+nums[j]) <= upper and i != j and (nums[i]+nums[j]) >= lower:
            count+=1
print(count)

words = ["alice","bob","charlie"]
s = "ab"
isTrue=True
if len(words) != len(s):
    print(False)
for i in range(len(words)):
    temp=words[i]
    if temp[0] != s[i]:
        isTrue=False
print(isTrue)

nums = [[3,6],[1,5],[4,7]]
arr=[]
for i in nums:
    k = i
    for j in range(k[0], k[1]+1):
        arr.append(j)
arr = set(arr)
print(len(arr))

obj = [False, 0]

print(len(obj))

nums=[0,1,2,3,4]
index=[0,1,2,2,1]
arr=[]
for i in range(len(nums)):
    if len(arr)-1 >= index[i]:
        
            arr.insert(index[i], nums[i])
    else:
        arr.append(nums[i])

print(arr)

a=885
b=885
c=0
if a < b:
    c = a
else:
    c = b
for i in range(1,c+1):
    if a%i==0 and b%i==0:
        print(i)


n = 10
logs = [[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]]

diff = 0
id = 0
pos = 0
kdiff=0
for i in range(len(logs)):
    k = logs[i]
    diff = k[1] - pos
    if kdiff < diff:
        kdiff = diff
        id = k[0]
    pos = k[1]
print(id)

nums = [-1,2,-3,3]

nums.sort(reverse=True)
for i in nums:
    if -i in nums:
        print(-i,"9")

s = "abcd"
t = "abcde"
arrs=[]
arrt=[]
for i in range(len(t)):
    i

ret=""
for i in val:
    ret+=i
print(ret)

x = 2.00000
n = 10
print(x**n)

low = 3
high = 7

count = high - low

print(count)

salary = [8000,2000,3000,6000]
average=0
count=0
for i in salary:
    average+=i
    count+=1
print(average/count)

nums = [1,2,3,4,5,6,7]
k = 3

for i in range(k):
    nums.insert(0, nums[len(nums)-1])
    nums.pop()
print(nums)

arr=[2,0,3,3,2]
arr.sort(reverse=True)
dict={}
count=0
s=-1
for i in arr:
    if i in dict:
        count = dict[i]
        dict={**dict, i:count+1}
    else:
        dict={**dict, i:1}
for i in dict:
    if i == dict[i]:
        s=i
        break

print(s)

s = "ddcccdd"
count=1
lar=1
res=1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count+=1
    else:
 
        lar=count
        count=1
    if lar>res:
        res=lar
if count>res:
    res=count
print(res)

dict={'1':1,'2':2,'3':3}
arr = dict.keys()
print(arr)

class A:
    @abstractmethod
    def printf():
        print("hi")

class B(A):
    def Scan():
        print("Hey")

B.printf()

n=5
arr=[1,2]
for i in range(3,n+1):
    arr.append((arr[len(arr)-1])+(arr[len(arr)-2]))
print(arr[n-1])

class Vehicle:
    

    def __init__(self):
        print('Vehicle created.')
    def __del__(self):
        print('Destructor called, vehicle deleted.')
    
    def disply(self):
        print(
            
            'hello'
        )




car = Vehicle()
del car
car.disply()

dict={}
maxval=0
pos=0
for i in nums:
    if i in dict:
        count=dict[i]
        dict={**dict,i:count+1}
    else:
        dict={**dict,i:1}
    if dict[i]>maxval:
        maxval=dict[i]
        pos=i
print( pos)

nums = [1,3,4,2,2]
arr=[]
for i in nums:
    if i not in arr:
        arr.append(i)
    else:
        print(i)

nums = [1,3,4,2,2]

res = [item for item in set(nums) if nums.count(item) > 1]

print(res[0])

s="string"
t="S"
t+=s[1::]
print(t)

nums = [2,5,1,3,4,7]
arr=[]
n = 3
for i in range(n):
    arr.append(nums[i])
    arr.append(nums[n+i])
print(arr)

s = "words and 987"
arr = s.split(" ")
num=0
for i in arr:
    try:
        num = int(i)
    except:
        pass
print(num)

strs = ["flower","flow","flight"]
val=strs[0]
res=""
out=""

for i in range(1,len(strs)):
    stg = strs[i]
    for j in range(len(stg)):
        if val[j] == stg[j]:
            res+=val[j]
        else:
            break
    rem=out.strip(res)
    out=res
    out=out.strip(rem)
    res=""
    
print(out)

nums = [1,1,2]
j=0
for i in range(len(nums)):
    if nums[i] != nums[j]:
        j+=1
        print(nums[j], nums[i], j)
        nums[j] = nums[i]

print (j+1)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

for i in emails:
    arr = i.split(".")
    email=""
    for j in arr:
        email+=j
    array = email.split("+")
    out=""
    for k in array:
        out+=k
    print(out)

prices = [8,4,6,2,3]

for i in range(len(prices)-1):
    for j in range(i+1, len(prices)):
        if prices[i]>prices[j]:
            prices[i] = prices[i]-prices[j]
            break
            
print(prices)

mat = [ [1,2,3],
        [4,5,6],
        [7,8,9]]
sum = 0
for i in range(len(mat)):
    arr = mat[i]
    for j in range(len(arr)):
        if i == j or i == (len(arr)-1)-j:
            sum+=arr[j]

print(sum)

grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
isTrue = True
for i in range(len(grid)):
    arr = grid[i]

    for j in range(len(arr)):
        if i == j and arr[j] == 0:
            isTrue = False
        else:

            if i != j and arr[j] != 0:
                isTrue = False
print(isTrue)

n = 4
start = 3
arr = []
i = start
xor = False
j = 0
while len(arr) < n:
    arr.append(i)
    xor ^= arr[j]
    i+=2
    j+=1
print(xor)

hours = [0,1,2,3,4]
target = 2
count = 0
for i in hours:
    if i >= target:
        count+=1
print(count)

accounts = [[1,5],[7,3],[3,5]]
value = 0
for i in range(len(accounts)):
    arr = accounts[i]
    sum = 0
    for j in range(len(arr)):
        sum+=arr[j]
    if sum > value:
        value = sum
print(value)

nums = [1,2,3,1,1,3]
count = 0
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            count+=1
print(count)

nums = [1,2,1]

for i in range(len(nums)):
    nums.append(nums[i])

print(nums)

operations = ["++X","++X","X++"]
x = 0
for i in range(len(operations)):
    if operations[i] == "X++" or operations[i] == "++X":
        x+=1
    else:
        x-=1
print(x)

candies = [2,3,5,1,3]
extraCandies = 3
maxval = max(candies)
arr = []
for i in range(len(candies)):
    if candies[i] + extraCandies >= maxval:
        arr.append(True)
    else:
        arr.append(False)
print(arr)

nums = [1,2,3,4]
arr = []
sum = 0
for i in range(len(nums)):
    sum+=nums[i]
    arr.append(sum)
print(arr)

sentences = ["please wait","continue to fight","continue to win"]
array = []
for i in sentences:
    arr = i.split(" ")
    if len(arr) > len(array):
        array = arr

print(array)

nums = [10,4,8,3]
leftnums = []
rightnums = []
leftsum = 0
righsum = 0
arr = []
for i in range(len(nums)):
    leftnums.append(leftsum)
    rightnums.append(righsum)

    leftsum+=nums[i]
    righsum+=nums[(len(nums)-1)-i]

for i in range(len(nums)):
    arr.append(abs(leftnums[i] - rightnums[len(rightnums)-1-i]))

print(arr)

n=5

for i in range(n*n):
    for j in range(n*n):
        if(i==0 and j==((n*n)//2) or i>0 and j>((n*n)/2)-2 and j<((n*n)/2)+1 or i>((n*n)/2)-2 and j>1 and j<5 or i>((n*n)/2)-2 and j>5 and j<9 or i>((n*n)/2)-2 and j>(n*n)-6 and j<(n*n)-2 or i>((n*n)/2)-2 and j>(n*n)-10 and j<(n*n)-6 or i>((n*n)//2) or i==12 and j>0 and j<(n*n)-1):
            print("*",end=" ")
        else:
            print(end="  ")
    print("\n",end="")

dict = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
res=""
day=""
date = "20th Oct 2052"
arr = date.split(" ")
out = arr[0]
if len(arr[0]) < 4:
    day="0"+out[0]
else:
    day=out[0]+out[1]
res+=arr[2] + "-" + dict[arr[1]] + "-" + day
print(res)

low = 8
high = 10
count = 0

for i in range(low, high+1):
    if i%2!=0:
        count+=1
        
print(count)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
ord = {}
for i in range(len(indices)):
    ord = {**ord, indices[i]:s[i]}
ord = dict(sorted(ord.items()))
s=""
for i in ord:
    s+=ord[i]

nums = [1,2,3,4]
arr = []
for i in range(0,len(nums),2):
    for j in range(nums[i]):
        arr.append(nums[i+1])
print(arr)

s = "Hello how are you Contestant"
k = 4
s = s.split(" ")
val = ""

for i in range(k):
    val += s[i]
    if i < k-1:
        val += " "
print(val)

word1 = ["ab", "c"]
word2 = ["a", "bc"]
stg1 = ""
stg2 = ""
if len(word2) > len(word1):
    temp = word1
    word1 = word2
    word2 = temp
for i in range(len(word1)):
    stg1 += word1[i]
    if i<=len(word2):
        stg2 += word2[i]

if stg1 == stg2:
    print(True)
print(False)

nums = [1,15,6,3]
sum = 0
ing = 0
for i in nums:
    sum += i
    stg = str(i)
    for j in stg:
        ing += int(j)
print(sum - ing)

nums = [3,2,1,5,4]
k = 2
count =0
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if abs(nums[i] - nums[j]) == k:
            count += 1
print(count)

nums = [1,2,3,4]
k = 1
count = 0
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j] and (i*j)%k == 0:
            count += 1

print(count)

n = 123006767677667
val = n
s = False
if n >= 1000:
    val = ""
    n = str(n)
    count = 0
    s = True
    for i in range(len(n)):
        
        if count == 3:
            val+="."
            count = 0
        
        val+= n[len(n)-1-i]

        count+=1
if s:

    val = val[::-1]
print(val)

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

count = 0

for i in words:
    isTrue = True
    for j in i:
        if j not in allowed:
            isTrue = False
    if isTrue:
        count+=1
print(count)

arr = [1,4,2,5,3]
sum = 0
for i in range(len(arr)):
    
    for j in range(len(arr)):
        temp = []
        for k in range(i,j+1):
           temp.append(arr[k])
        if len(temp)%2 == 1:
            for l in range(len(temp)):
                sum += temp[l]
print(sum)

address = "1.1.1.1"
arr = address.split(".")
address = ""
for i in range(len(arr)):
    address += arr[i]

    if i < len(arr)-1:
        address += "[.]"
print(address)

jewels = "aA"
stones = "aAAbbbb"
count = 0
for i in stones:
    if i in jewels:
        count += 1
print(count)

command = "G()(al)"
val = ""
for i in range(len(command)):

    if command[i] == "(" and command[i+1] == ")":
        val += "o"
    else:
        if command[i] != "(" and command[i] != ")":
            val += command[i]
print(val)

s = "K1:L2"
d = "A"
for i in range(5):

    print(d)
    d += 1

text = " practice   makes   perfect"
arr = text.strip(" ")
arr = arr.split(" ")
array = []
for i in range(len(arr)):
    if arr[i] != "":
        array.append(arr[i])


count = 0

for i in range(len(text)):
    if text[i] == " ":
        count += 1
if count > 0 and (len(array)-1) > 0:
    n = int(count/(len(array)-1))
else:
    n = 0

text = ""
space = " "
sum = count - (len(array)-1) * n
for i in range(len(array)):
    text += array[i]

    if i < len(array)-1:
        text += space*n
           
text += space*sum
print(text)


height = [1,8,6,2,5,4,8,3,7]
val=0
for i in range(len(height)-1):
    
    for j in range(i+1, len(height)):
        if height[i] < height[j]:
            high = height[i]
        else:
            high = height[j]
        if val < high * (j-i):
            val = high * (j-i)            
print(val)
        
s = "cabbac"
dict = {}
count = 0
val = ""
isTrue = True
for i in s:
    if i in dict:
        count = dict[i]
        dict = {**dict, i : count+1}
    else:
        dict = {**dict, i : 1}

for i in dict:
    if dict[i] == 1:
        val += i
    if dict[i] > 1:
        isTrue = False
if isTrue:
    print(-1)
print(len(val))

s = "cbzxy"
arr = [-1]
for i in range(len(s)-1):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            arr.append(j-i-1)
            
print(max(arr))

nums = [0,4,3,0,4]

nums.sort()
lower = False
count = 0
arr = []
for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        arr.append(nums[i])
    elif nums[i] < lower and nums[i] not in arr or lower in arr:
        lower = nums[i]

for i in nums:
    if i >= lower:
        count += 1
       
print(count)

nums = [3,9,7,8,3,8,6,6]
nums.sort()
ord = {}
total = 0
for i in range(len(nums)):
    if nums[i] in ord:
        count = ord[nums[i]]
        ord = {**ord, nums[i]:count+1}
    else:
        ord = {**ord, nums[i]:1}

lower = sorted(ord.items(), key=lambda x:x[1])
low = lower[0]

for i in range(len(nums)):
    if nums[i] >= low[0]:
        total += 1
        print(i, nums[i])

print(total)

n = 5

for i in range(1,n+1):
    for j in range(n):
        if j<i and i<=3 or i>3 and j<=n-i:
            print(" ",end="  ")
        else:
            print("*",end="  ")
    print("\n")

n=5

for i in range(n*n):
    for j in range(n*n):
        if j<13-i*i or j>11+i*i:
            print("*", end=" ")
        else:
            print("  ",end="")
    print("\n")
            

arr = [17,89,1,72,69,70,18,39,92,51,47,99,71,5,16,57,67,26,62,24,23,15,61,37,81,30,82,96,3,94,7,41,43,2,66,8]
pieces = [[4,93],[3],[19],[87,62],[49],[54],[13,21],[82],[5],[73],[34],[28],[29],[27],[42],[45,67],[85,16],[58,31,37],[64],[81],[72,60],[59],[17],[6],[97],[1,92],[84]]
array = []
nums = []
for i in range(len(pieces)):
    
    for k in range(len(arr)):
        for l in range(len(pieces)):
            if arr[k] in pieces[l] and pieces[l] not in nums:
                nums.append(pieces[l])
    if len(nums) > i:
        temp = nums[i]

        for j in range(len(temp)):

            array.append(temp[j])
    else:
        print (False)


if array == arr:
    print(True)
print(False, array)

arr = [3,5,1]
arr.sort()
diff = None
isTrue = True
for i in range(len(arr)-1):
    if diff == None:
        diff = arr[i+1] - arr[i]
    if arr[i+1] - arr[i] != diff:
        isTrue = False

if isTrue:
    print(True)

print(False)

nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]

nums.sort()
l.sort()
r.sort()
arr = []
arr.append(nums)
arr.append(l)
arr.append(r)
array = []
for i in range(len(arr)):
    diff = None
    temp = arr[i]
    isTrue = True
    for j in range(len(temp)-1):
        if diff == None:
            diff = temp[j+1] - temp[j]
        if temp[j+1] - temp[j] != diff:
            print(temp[j+1] - temp[j], diff)
            isTrue = False
    array.append(isTrue)

print(array)

sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaabaaaabaaaabaaaaba"
x = sequence.replace(word,"")


print(int((len(sequence)-len(x))/len(word)))

print(sequence.count(word))

k=0

while True:
    if k*word not in sequence:
        print (k-1)
        break
    k+=1

n=7
count=0
i=n
while i>1:
    sub=i//2
    i=i-sub

    count+=sub
print(count)

s = "PAYPALISHIRING"
numRows = 4
stg = ""
i=0
diff=numRows
while len(stg)<len(s):
    if i >= len(s):
        i-=len(s)
        if i%2==0:
            diff=2
            i=1
        else:
            diff=numRows
    print(i)
    stg+=s[i]
    i+=diff
print(stg)

s = "textbook"
arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
length = int(len(s)/2)
fir = s[:length]
las = s[length:]
firCount = 0
lasCount = 0
print(fir,las)
for i in range(length):
    if fir[i] in arr:
        
        firCount += 1
    if las[i] in arr:
        lasCount += 1

if firCount == lasCount:
    print(True)
print(False)

votes = ["ABC","ACB","ABC","ACB","ACB"]
ords = {}
for i in range(len(votes)):
    if votes[i] in ords:
        count = ords[votes[i]]
        ords = {**ords, votes[i] : count+1}
    else:
        ords = {**ords, votes[i] : 1}

sor = sorted(ords.items(), key=lambda x:x[1])
val = sor[len(sor)-1]

print(val[0])

s = "LLLLRRRR"
r = "R"
l = "L"
count = 0
for i in range(len(s)):
    val = r*i + l*i
    if val in s:
        count += 1
        print(s.count(val), val)

print(count)

items = [["ii","iiiiiii","ii"],["iiiiiii","iiiiiii","ii"],["ii","iiiiiii","iiiiiii"]]
ruleKey = "color"
ruleValue = "ii"
count = 0
if ruleKey == "type":
    pos = 0
elif ruleKey == "color":
    pos = 1
else:
    pos = 2
for i in range(len(items)):
    temp = items[i]
    if ruleValue == temp[pos]:
        count += 1
print(count)

grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
arr = [[0, 2], [0, len(grid)-1]]
for i in range(len(grid)):
    temp = grid[i]
    for j in range(len(temp)):
        print(temp[j])

nums = [1,2,3,2]
sum=0
for i in range(len(nums)):
    isUnique = True
    for j in range(len(nums)):
        if i!=j and nums[i]==nums[j]:
            isUnique=False
    if isUnique:
        sum+=nums[i]

n = 20
count = 0
pos = 1
sum = 0
for i in range(n):
    
    if count == 7:
        count=0
        pos+=1
    sum+=count+pos
    count+=1
print(sum)

nums = [0,2,1,5,3,4]
arr = []

for i in range(len(nums)):
    arr.append(nums[nums[i]])

print(arr)

n = 10
m = 3
sum = 0
count = 0
for i in range(1, n+1):
    if i%m !=0:
        sum+=i
    else:
        count+=i
print(sum-count)

n = 77
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150]
for i in range(31):
    if i*n in arr:
        print(i*n)
        break
array=[]
for i in range(1,1001):
    array.append(i*2)
print(array)

nums = [2,5,6,9,10]

low = min(nums)
high = max(nums)

for i in reversed(range(1, low+1)):

    if high%i==0 and low%i==0:
        print(i)

n = 5
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count += 1
if count == 3:
    print(True)
print(False)

nums = [2,1,3,4]

srtnums = list(nums)
srtnums.sort()
arr = []
i=0
while i<len(nums)-1:
    if nums[i+1] < nums[i]:
        j=i+1
        while j<len(nums):
            arr.append(nums[j])
            del nums[j]
    i+=1
            

if arr+nums == srtnums:
    print(True)
print(False)

print(arr+nums)

str1 = "ACABCD"
str2 = ""
arr = []
if str2 in str1:
    for i in range(len(str2)):
        temp = ""
        arr = []
        for j in range(len(str1)):

            if temp == str2:
                break
            temp += str1[j]
            arr.append(j)
            
            if temp not in str2:
                temp = ""
                arr = []
                temp += str1[j]
                arr.append(j)

    
res = ""
if len(arr) > 0:
    if arr[0] == 0:
        res = str1[len(arr):]
    elif arr[len(arr)-1] == len(str1)-1:
        res = str1[:arr[0]]
    else:
        res = str1[:arr[0]-1]+str1[arr[-1]:]
print(res)


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
sum = 0

for i in range(len(triangle)):
    arr = triangle[i]
    minval = arr[0]
    for j in range(len(arr)):
        if arr[j] < minval:
            minval = arr[j]

    sum += minval
print(sum)

number = "1231"
digit = "1"
res = ""
arr = []
for i in range(len(digit)):
    for j in range(len(number)):
        if digit[i] == number[j] and i not in arr:
            arr.append(i)
        else:
            res += number[j]
print (res, arr)

arr = [1,2,2,1,1,3]
dict = {}

for i in range(len(arr)):
    if arr[i] in dict:
        count = dict[arr[i]]
        dict = {**dict, arr[i] : count+1}
    else:
        dict = {**dict, arr[i] : 1}



array = list(dict.values())

sets = set(array)
sets = list(sets)
array.sort()
sets.sort()
if array == sets:
    print(True)
print(False)



strlen = len(s)
one = s.count("1")
zero = s.count("0")
if one > zero:
    high = one
else:
    high = zero

s1 = "bank"
s2 = "kan0"
counts1 = Counter(s1)
counts2 = Counter(s2)
count = 0
res = ""
if(counts1 == counts2):
    arr = list(s2)
    for i in range(len(s1)):
        if count > 2:
            break
        elif s1[i] != arr[i]:

            arr[i] = s1[i]
            count += 1
        res += arr[i]
print(res == s1)


s = "10010100"
one = ""
zero = ""
countone = 0
countzero = 0
for i in range(len(s)):
    if i%2 == 0:
        zero += "0"
        one += "1"
    else:
        zero += "1"
        one += "0"
for i in range(len(s)):
    if s[i] != zero[i]:
        countzero += 1
    if s[i] != one[i]:
        countone += 1
if countzero < countone:
    print(countzero)
print(countone)
for i in range(len(s)-1):
    
    if s[i] == s[i+1]:
        count += 1
        if s[i+1] == "0":
            s[i+1] = "1"
        else:
            s[i+1] = "0"
print(count)



words = ['2']
arr = [0]

for i in range(len(words)-1):
    word = words[i]
    
    for j in range(i+1, len(words)):
        flag = True
        for k in range(len(word)):

            if word[k] in words[j]:
                flag = False
        if flag:
            arr.append(len(word)*len(words[j]))
            if len(word)*len(words[j]) == 35:
                print(word , words[j])
print(max(arr))

for i in range(len(words)):
    word = words[i]
    flag = True
    k = 0
    j = i+1
    if len(word) != 988:
        print(len(word))
    while j<len(words):
        
        if word[k] in words[j]:
            flag = False
        
        if flag and k == len(word)-1:         
            arr.append(len(word)*len(words[j]))
        k += 1
        if k >= len(word):
            j += 1
            k = 0
            flag = True
            
print(max(arr))

original = [1,2,3,4]
m = 2
n = 2

arr = []
k = 0
if len(original) == m*n:
    for i in range(m):
        new = []
        for j in range(n):
            new.append(original[k])
            k += 1
        arr.append(new)
print(arr)

mat = [[1,2],[3,4]]
r = 1
c = 4
array = []
arr = []
for i in range(len(mat)):
    temp = mat[i]
    for j in range(len(temp)):
        arr.append(temp[j])
        
        if len(arr) == c or len(arr) == len(temp):
            array.append(arr)
            arr = []

print(array)

word = "a123bc34d8ef34"
stg = ""
arr = []
word += "."
for i in range(len(word)):
    try:
        num = int(word[i])
        stg += str(num)
    except:
        if stg != "":
            arr.append(stg)
            stg = ""
sets = set(arr)
print(sets)

mat = [[]]
r = 127
c = 4
array = []
arr = []
length = len(mat[0]) * len(mat)
if c*r > length or c*r < length :
    print (mat)

for i in range(len(mat)):
    temp = mat[i]
    for j in range(len(temp)):
        arr.append(temp[j])
        if len(arr) == length/r:
            array.append(arr)
            arr = []
print(array, length, r*c)

s = "anviaj"
res = ""
arr = []
if len(s) == 1:
    print(1)
i = 0
a = 1
while i < len(s):
    if s[i] in res:
        arr.append(len(res))
        if s[i-1] != s[i]:
            i = a
            a += 1
        res = "" 
    res += s[i]
    i += 1
    print(res)
arr.append(len(res))
print(max(arr), arr)

nums = [7648,832,5069,5153,4385,8593,3391,6075,4886,1631,4858,8086,3194,1452,2251,4714,9818,8292,7555,7299,5933,9479,2874,2750,6088,2410,822,1214,4895,4509,4440,7778,8758,5228,4945,7172,7044,1208,7738,9192,9472,5485,4308,8792,7893,4577,1178,5266,7316,5521,2877,4085,7193,8236,6070,1474,9860,7364,8936,8040,9698,9441,422,1329,6364,2400,6584,6611,7031,6516,5913,291,2765,7343,2556,9282,5668,2412,6956,2164,485,886,6257,9719,3210,7499,6937,6242,4752,9918,916,3115,4682,4427,6907,3486,2996,63,7833,8387,757,2444,9041,6535,5859,652,3174,7084,4887,3795,8923,2904,9974,128,9385,3828,8393,1952,264,9732,9153,269,3164,5701,4649,4627,6493,9774,3151,9382,8939,601,8825,9164,1440,4001,8712,447,143,8748,1841,8867,5549,4532,8285,8529,5191,596,8873,3080,3951,481,3218,7778,241,5222,3308,83,882,8768,9217,3951,9207,4598,6703,1933,9201,9855,5934,2181,2454,6090,7932,1261,6054,9104,69,7523,4890,8016,1895,1824,4896,359,9052,3030,5786,9292,8506,392,8844,4629,3031,9604,1844,3388,7247,8615,4576,3491,4758,6508,6441,7433,389,4274,6375,8729,5461,4684,6085,1729,6598,7684,8265,5913,264,1060,2478,6458,5227,3743,2367,9989,6208,121,3103,9822,136,5619,116,6372,3552,3156,1335,602,5071,6169,2578,9349,7506,6003,6597,2940,6964,4091,7488,6851,1239,9613,1180,2585,2159,6158,6450,1206,2470,3720,9569,2313,9602,433,1432,9326,9067,8859,8024,5670,5530,999,5096,1244,1315,3406,3394,2862,7907,7651,7619,361,8763,2964,4023,4239,937,2055,523,2841,8941,8846,4109,9055,8171,3918,9357,2476,9088,30,5833,8000,5539,4360,9678,1072,2817,402,9130,7368,6476,7055,4577,1912,2177,3135,4443,382,7033,4655,2826,1562,657,3796,2481,7259,8495,4511,6207,3065,1150,5918,2511,5974,5913,7648,1138,8304,7296,2400,1834,5827,1378,1250,1779,611,1615,6630,4094,7532,1605,602,6892,3438,574,9407,1910,5615,4538,9317,2531,4082,7492,6875,4894,106,5846,5345,3899,5433,7914,1167,1167,6996,9305,9853,6425,9223,125,174,5499,9705,6250,604,1350,2577,3619,930,6403,3586,7337,7336,7481,1200,5169,2019,3715,93,1298,5229,8680,2511,822,1917,4516,8660,3181,8218,7491,3645,5588,5282,4369,4400,2055,6513,4310,5505,4004,4422,7811,2369,9668,9791,7701,2732,6542,1065,9345,3483,9236,134,5920,5734,5638,8771,3667,692,5213,4298,8862,3323,2153,7897,1067,5160,8787,5559,7804,1455,8501,4578,8212,3746,7330,8736,707,8565,4665,4337,4817,6984,5178,5754,8589,4083,3600,9737,5839,2177,2435,6163,9362,1829,2639,3269,8702,4944,1638,9672,332,7706,7819,4212,2717,7767,6848,4857,7625,1876,4541,4677,5828,3122,8303,4571,2844,5878,2599,1236,1428,3122,2522,4268,2154,1132,3641,2831,1340,4153,8910,9686,9396,6045,2133,8691,7246,2368,2082,6297,1912,1109,1902,9663,8395,3881,3141,4179,5156,909,3983,1036,7496,6502,2988,5124,807,9850,6339,2420,6579,9715,4946,6758,716,2156,4606,8205,1023,3768,9601,3195,1946,9216,8692,3736,3195,5188,1335,6703,9908,5756,4099,226,6036,2080,5081,3670,9735,1030,5988,8815,7158,3982,2112,3942,8254,2447,2310,1361,4531,5125,3568,4443,5210,6554,3357,3448,2135,871,2672,8281,7956,982,7016,9164,6138,2138,2742,9160,6503,9395,1880,2431,7592,4917,501,607,4947,5730,4160,2779,6125,8073,941,1684,3618,8148,5944,3820,5190,7042,1757,5081,9407,9813,4669,8904,7875,2697,2302,3847,9184,681,800,4541,7548,9454,2553,4936,6030,5267,4587,1294,1799,8561,6281,8174,8789,4235,7584,3615,3014,9348,3078,4531,8171,6898,4929,3293,7085,7119,5722,4065,931,9962,6236,9343,5495,9750,8314,7767,5057,3693,4472,643,887,6172,4730,1427,2859,1273,5429,5321,9235,1443,5793,2464,4365,5292,4341,2436,8813,4,552,7081,9476,497,2548,4373,4580,1419,5407,2455,5777,8529,5667,6617,4222,1752,4350,8626,1549,8044,1269,7692,6364,5492,5420,5891,7545,8253,4859,755,7407,537,3031,2924,2307,1304,1785,7281,2011,9707,5264,5279,3773,9874,5701,9363,5708,3896,6690,6188,5778,7959,1684,6470,2493,4360,1213,6811,576,8136,1440,7665,502,2078,1764,9935,2169,235,9982,4661,884,5788,633,3262,9124,1212,858,285,242,188,8348,3157,982,6186,3049,8839,2686,2247,8732,1301,570,4191,3718,5035,380,7454,1216,3586,1707,2815,8048,416,1864,9810,7871,5622,4913,4308,7165,6408,5553,1597,9595,2224,5681,7669,7100,8875,9045,8462,1633,732,7998,9438,4656,8926,2012,2495,6773,1498,7391,858,1856,5700,9007,772,2841,3552,7994,7689,4396,2882,9208,5900,1434,6713,3919,2469,2873,4253,1909,9157,3153,3275,8882,6880,995,37,1548,7992,9728,6213,7531,2195,6344,8069,701,2254,8482,9283,6520,5222,9587,5034,5816,3159,4334,6485,7091,1030,6039,3166,9497,2579,843,444,4063,7901,1920,8341,4598,3232,5224,3508,7716,564,6868,3082,3061,4769,8910,9150,8416,3309,1844,1604,4234,9689,8311,7182,6750,8956,2511,8578,8764,7005,1471,8328,9853,2352,8931,9585,88,866,2852,4446,6449,5232,6689,7064,2720,8579,8506,4534,7173,3345,2065,3796,9220,4367,8487,2958,1127,4407,210,1328,7184,4439,4437,7082,374,7456,3620,5346,7767,1202,6729,4477,7430,6902,1416,6184,7702,7614,9137,8401,9270,6188,109,397,9724,7384,8335,9514,50,8369,8535,4137,2745,2454,270,6114,6265,543,1589,1507,2551,7919,291,9020,3630,5733,1642,2508,452,5413,2751,8689,7032,8221,8407,6196,8177,332,9529,8569,7854,8235,3580,5805,9641,4757,1074,5562,6127,9919,6229,81,4420,9670,1550,3533,290,6395,6240,2617,8250,8227,1323,248,9527,2615,3900,4367,5787,3632,2646,7930,8525,8724,7731,5384,348,5135,8209,1772,9183,1035,7523,9923,2971,8748,9426,9584,1764,9667,4646,6832,5731,8250,5743,2531,9312,4921,2020,1393,6477,9707,4891,1516,8055,7168,4928,3264,450,2969,507,9573,4735,7149,7365,8338,9068,9208,7028,4017,5585,4708,8968,2215,3872,4133,8668,1105,9441,9255,1436,1706,232,5562,796,1406,626,6092,2356,7508,1215,6137,5102,1598,6444,8016,4148,3611,3493,5925,1012,774,7403,3389,9748,450,6643,7475,3857,8255,7406,8308,5112,5230,1332,2582,922,2351,6448,8052,383,8329,9430,6475,6898,9980,7964,9497,4202,7486,479,6708,5168,1999,6340,5371,7710,9889,5917,1077,4927,9156,1086,4991,7541,4499,6833,3450,9478,5307,4921,5574,3170,9188,6439,4207,7276,134,8363,1109,1114,8513,4422,4705,1633,3696,2474,2010,5360,5448,8758,7536,7510,9519,7075,5496,173,6114,596,8028,5727,1002,5232,4544,8319,4736,2317,6781,4473,6227,4975,6100,4642,4154,2660,8401,6650,3330,8158,707,9383,7975,2836,7777,6523,3138,8766,5603,3773,2979,4319,418,9300,987,2095,2255,8322,6150,2026,2452,8780,571,9713,9317,9238,8465,6286,2495,5671,436,7612,981,9198,8210,7054,4436,8785,8770,4876,539,245,1897,4505,1666,3604,2447,8422,6174,4944,3169,1658,8950,2166,8531,8252,206,3578,4062,6641,9815,3320,2550,807,6344,5604,6437,8579,9535,4613,6757,783,3610,4571,556,1480,8101,8407,5029,2139,7354,9477,465,6443,8044,3120,4861,8736,3097,7225,691,4852,9796,2644,150,280,9772,7273,1231,2969,2207,8323,9293,9141,5564,9763,1757,7266,3055,8598,7835,9439,6694,4406,2022,9283,4132,3046,5457,7495,447,3031,1635,2667,7789,8415,4850,3965,5514,8091,1465,3651,778,7397,1824,4301,4435,6235,4192,6238,1986,3726,830,2584,3906,4391,1863,8063,3383,5412,3820,8602,343,5588,5190,362,6483,995,874,1662,3853,9571,6507,8906,2151,9107,8454,2245,5511,7392,1345,589,7759,1868,6517,6875,7007,4442,6016,1934,9432,8411,6536,5146,8476,8447,2108,6116,4418,3298,1850,3534,2017,1469,485,8776,3437,5428,6364,6380,2267,3829,7404,3400,9318,1137,6554,497,3492,5537,3979,8654,6513,1963,7526,7932,182,88,3817,7796,3476,6238,9228,2408,7342,5945,5992,4472,7247,9086,2978,7658,1231,1994,1629,3541,9977,9905,6042,2915,6701,7289,4842,9925,4051,4727,34,3146,86,3520,6996,3952,5309,4505,5099,1381,5928,7695,9003,3009,2841,8713,6834,9697,6059,1441,5002,369,2582,4254,1213,7874,5495,9323,8880,8524,2952,2638,1934,8094,7810,6956,1472,8505,6785,3513,5072,9258,5854,4826,7178,4424,4508,6580,7205,9384,3486,2171,9506,5153,2252,6463,911,8244,248,8937,3376,3832,5954,8607,2567,4030,6803,7262,1608,4153,7986,6244,9577,5079,2025,3368,7342,3102,504,8723,9341,3801,10,4505,6999,8424,6030,5053,2006,8668,6575,101,8428,4974,4477,7561,191,1161,1733,2236,1395,8310,4442,4683,7114,4672,1282,3354,4457,2888,8465,3644,7743,9003,3404,2536,5448,1699,5778,1616,5940,2107,8087,8623,8860,4626,3355,3888,6588,46,6576,5887,2104,9062,9007,3293,1072,7772,5066,9608,9674,1376,4225,2416,6601,3853,834,3887,2345,4911,2871,1224,9554,3059,2666,3056,3090,2633,6957,578,7525,4358,356,4180,4150,6823,7189,2206,8527,4501,949,9062,8904,804,9321,175,8720,6445,8141,6393,6901,5547,4306,8688,5288,3162,9048,7588,2812,8242,9783,9708,9719,3389,334,6157,7231,46,8023,7782,5125,8985,7133,2002,2273,7223,2091,18,4207,8479,8408,5451,8586,5041,1749,7206,3881,1739,8493,5303,7956,8129,9353,7580,6994,5871,4905,4512,4714,1533,4708,612,7846,400,1050,3867,302,2256,8769,3484,9748,1874,8309,6132,6836,4639,845,9351,3984,5354,9919,5990,79,2836,1491,9403,4552,176,7016,7598,6368,3843,3682,6694,6743,5584,364,2716,1092,7819,7831,2526,9864,5113,6039,600,6556,3997,6375,8920,6768,7849,4443,561,3795,8338,8565,6901,5203,4458,5004,2377,2388,120,1563,3114,9232,3933,3736,454,7927,2791,858,827,5258,1400,586,4857,1960,5115,5901,203,9442,442,3151,490,4735,5196,504,6501,1552,8510,5664,1207,3504,1677,2750,7064,4134,7825,6852,2904,4087,9233,6749,8676,4842,3817,3948,3247,6620,3577,9327,5291,9897,7646,7792,6515,6381,5397,3965,9733,2411,1689,3228,5087,141,7787,4575,2101,7933,5080,4041,1972,610,3372,5168,9841,8226,9832,2257,325,7675,3688,2345,4223,7801,577,5479,4894,8682,1911,6153,9912,4324,9363,8174,7860,4951,7074,4444,9987,6016,60,3942,6528,9490,2516,2348,7448,9795,3646,4091,4419,9548,1040,5092,1803,7674,8416,8894,7620,6464,4571,9952,8210,4569,779,1257,4908,7591,2342,8042,4295,5444,205,14,5106,7346,2614,9178,3869,2503,7914,6950,737,9549,7790,2657,2844,9314,4838,1490,7162,319,8498,2210,9281,5997,9435,7869,9826,3387,5164,120,3844,3392,4566,3753,1529,2648,2572,9832,3506,4502,7246,3596,8796,5130,8601,8478,4710,6301,9328,848,8770,5593,8635,6197,4521,7209,4220,9321,4283,1282,1571,706,4430,7264,6984,3071,9213,19,1269,2459,1680,2884,1935,4287,5604,8165,5857,7288,9620,7177,4772,2257,6350,812,2172,4466,2523,927,9942,2501,7402,9203,2185,6025,3653,6779,4299,4117,6094,3888,3257,4355,6470,8248,5291,6066,5692,292,763,267,8217,182,1529,3892,5414,3301,9456,7613,5800,1729,1439,164,9262,5360,4752,2538,1724,2711,8774,3116,4263,8551,8074,3817,8589,3982,7399,2741,203,3568,3861,9779,9221,3885,3735,8848,7645,7006,4780,5953,4681,2157,6873,6441,9476,8148,2867,9463,931,9956,9111,2437,2613,617,7978,2662,2112,9608,504,5207,6663,6096,8063,3625,1479,3076,6933,6495,2101,6537,982,2170,7932,5329,3651,4101,2871,5403,3241,7809,1778,2483,5984,3408,3841,8326,9944,3420,8673,7758,3960,6538,6651,9548,2432,1392,7527,2575,7101,7796,3373,9663,8967,5489,3948,8705,2910,4642,2841,7389,5206,8321,5096,2738,2696,6145,6510,3560,68,9006,1263,8056,2223,4671,4551,4276,6056,5992,2257,4670,5752,422,2900,9369,1236,4576,4295,1618,1819,6319,9658,7100,8485,1988,8545,6348,7974,8879,5670,7103,1546,2461,4061,6497,5321,1326,9299,5447,9865,6192,8235,2524,1090,7977,7681,8894,7989,1685,5376,5344,5392,3141,2250,4828,2630,7552,1248,7594,9152,6984,5893,9147,5170,7781,4735,9210,6070,1839,9108,1511,6949,5511,8200,5572,500,7250,4622,2877,2039,3589,6829,6646,9867,6870,1146,8903,2659,3617,2565,1268,4300,7618,1425,1601,1624,9246,5242,861,7112,5820,7500,2571,378,3408,6836,6038,9031,6632,5028,9705,3668,3272,7784,1347,7460,8030,1400,4995,7364,5931,7462,1050,8116,7482,8218,6306,7238,8493,6108,108,8228,4328,5045,1777,1987,1922,8176,9391,9473,9292,2097,9520,4602,2652,8407,7556,2643,313,8054,3174,3710,8528,8733,4860,8582,9208,5009,7900,6424,5983,7159,8497,7578,8888,6668,1832,1613,6940,2020,2401,7849,531,6611,2830,1499,2702,8077,5374,2293,7536,3459,8765,4951,2881,6549,4116,5339,5137,4909,1983,2031,595,7843,6027,1575,447,7435,549,7804,9845,1939,4896,4841,7232,9121,4286,4623,9131,125,5104,151,3961,6695,6033,6677,5614,6263,6873,3170,7829,1486,2845,1929,7117,5271,9503,3468,6152,6009,2647,1561,5779,7968,4488,440,3661,4403,8551,6932,9022,5336,1265,6211,2676,7310,6041,8652,8974,809,5843,5327,2326,6206,3678,1274,3431,8134,7156,2503,8839,196,6683,9186,5508,1191,6277,7948,580,6682,5055,8067,375,7093,1920,9152,6077,3160,7370,5838,7936,1553,3165,3188,5460,2029,3362,8009,149,9315,9644,6932,6020,6435,7252,4419,1362,6863,1006,1148,6278,7003,729,8654,1955,9627,6522,8717,9405,3182,4424,6541,6233,9177,13,4527,18,4524,4858,2131,962,4617,1356,3933,3808,1627,1578,4340,9950,3216,1313,6912,7668,2912,4309,6284,3816,9262,7960,3586,7017,5375,8352,8042,5312,6194,8827,683,3364,3553,4071,709,4167,1711,9291,7996,8413,6852,6942,9276,1229,2569,1303,8226,3639,2149,3887,6958,2017,1263,6733,3596,3991,746,7139,9906,8567,6235,1197,3206,7462,5976,1757,4410,7172,6457,5416,4841,2204,8090,8041,6327,8013,4073,8326,4730,7671,4651,8866,5600,9904,5852,16,4325,5385,2183,2322,5548,9981,1034,8157,1331,9028,9528,7158,9002,5706,4574,3289,8345,2269,2735,1776,5221,4349,6582,1091,1429,3874,5524,2498,2073,4818,2956,4651,2761,1445,511,7826,7041,558,9758,3934,1251,9235,5382,2534,8969,5195,6969,3139,2702,5005,2409,5619,279,7365,7546,2646,5053,370,8587,8942,7239,4394,6222,6944,5667,8649,1285,6323,2821,501,4333,2181,9638,8522,6709,7976,7277,5280,888,3482,7093,5264,8892,5457,3555,1114,4955,3489,4846,8312,7284,4402,8587,1879,8992,2105,3696,9578,5760,605,7145,8037,5225,4841,2653,3459,8068,5878,3114,4016,1270,6180,7846,6677,3037,9948,2395,4672,3578,4488,9018,9823,3906,5753,4521,8528,5943,9880,2946,9864,6441,5858,9716,9765,8905,2825,6192,8001,8190,8280,4373,6794,367,4865,4499,1384,6858,892,4459,8150,2112,2156,6061,8668,8085,4602,9533,5491,4694,877,1557,9867,6734,464,3907,2100,493,450,6656,6317,2293,9080,1570,5120,780,3262,331,7280,7447]
count = 0
for i in range(len(nums)-1):
    while nums[i] >= nums[i+1]:
        nums[i+1] += 1
        count += 1

print(count)

count = 0
for i in range(len(nums)-1):
    if nums[i+1] <= nums[i]:
        inc = nums[i] - nums[i+1] + 1
        nums[i+1] += inc
        count += inc
print(count)

nums = [9,7,8]
k = 9
pro = 1
i = 0
while k > 0:
    nums.sort()
    if i >= len(nums)-1:
        i = 0
    if nums[i] <= nums[i+1]:
        nums[i] += 1
        k -= 1
    else:
        i += 1
for i in nums:
    pro *= i
print(pro)

x = 1534236469
x = str(x)
x = x[::-1]
stdout = ""

for i in x:
    if "-" == i:
        stdout = "-" + stdout
    else:
        stdout += i
print(stdout)


pref = [859749,590030,427815,497488,577205,74022,627629,656625,631572,108013,520702,851771,912649,164667,97750,680969,970906,48747,575688,368809,389448,549365,222749,824520,290537,126870,588788,401094,813341,805629,260527,852326,372970,692805,636811,717697,664593,847757,101859,231434,242643,638842,815918,921285,249560,582535,854026,564006,278071,746215,894255,975760,485040,269003,112374,773033]
arr = []
xor = 0
for i in range(len(pref)):
    for j in range(1000000):
        if xor ^ j == pref[i]:
            arr.append(j)
            xor = xor ^ j
            break
print(arr)


n = 64
k = 2
base = 0
zero = "0"
count = 0
a = 1
isTrue = False
for i in range(1, n+1):
    base += 1
    count += 1

    if base == (int(str(k-1)*a))+1:
        base = int("1" + zero * a)
        a += 1
        count = 0

    elif count == k:
        base += 10 - k
        count = 0
    
    print(base, i)
base = str(base)
sum = 0
for i in base:
    sum += int(i)
print(sum)

num = 2932
num = str(num)
arr = list(num)
arr.sort()
print(int(arr[0]+arr[3]) + int(arr[1]+arr[2]))

n = 111
n = str(n)
sum = 0
for i in range(len(n)):
    if i%2 == 0:
        sum += int(n[i])
    else:
        sum -= int(n[i])
print(sum)

nums = [13,25,83,77]
arr = []
for i in range(len(nums)):
    for j in str(nums[i]):
        arr.append(int(j))
print(arr)

num = 1000
count = 0
for i in range(1, num+1):
    sum = 0
    for j in str(i):
        sum += int(j)
    print(sum)
    if sum%2 == 0:
        count += 1
print(count)

s = "iiii"
k = 2
dict = {"a":"1", "b":"2", "c":"3", "d":"4", "e":"5", "f":"6", "g":"7", "h":"8", "i":"9", "j":"10", "k":"11", "l":"12", "m":"13", "n":"14", "o":"15", "p":"16", "q":"17", "r":"18", "s":"19", "t":"20", "u":"21", "v":"22", "w":"23", "x":"24", "y":"25", "z":"26"}
res = ""
sum = 0
for i in s:
    res += dict[i]
for j in range(k):
    sum = 0
    for i in res:
        sum += int(i)
    res = str(sum)
print(sum)

strs = ["aabbcc", "aabbcc","c"]
array = []
length = -1
for i in range(len(strs)-1):
    for j in range(i+1, len(strs)):
        arr = []
        for k in strs[i]:
            if k in strs[j]:
                arr.append(False)
            else:
                arr.append(True)
        array.append(arr)
for i in array:
    if True in i:
        if length < len(i):
            length = len(i)
print(length, array)

total = 10
cost1 = 10
cost2 = 5
if cost2 > cost1:
    cost2 += cost1
    cost1 = cost2 - cost1
    cost2 = cost2 - cost1
count = 0
prd = 0
for i in range(total//cost1):
    ttl = total
    ttl -= cost1 * i
    count += 1
    while ttl > 0:
        count += 1
        ttl -= cost2
    if ttl == 0:    
        prd += count
        count = 0
print(prd+1)

s = "a1c1e1"
stg = "abcdefghijklmnopqrstuvwxyz"
res = ""
for i in range(len(s)):
    if s[i] in stg:
        res += s[i]
    else:
        ind = stg.index(s[i-1]) + int(s[i])
        res += stg[ind]
print(res)

nums = [1,5,3,4,5]
target = 5
start = 2

for i in range(start, len(nums)):
    if nums[i] == target:
        ind = i
        break

print(ind)

num = "35427"
res = ""
largest = 0
for i in reversed(range(len(num))):
    if int(num[i])%2 == 1:
        res = num[:i+1]
        break
print(res)

num = "6777133339"
dict = {}
arr = []
out = ""
for i in num:
    if i in dict:
        count = dict[i]
        dict = {**dict, i:count+1}
        if dict[i] >= 3 and int(i) not in arr:
            arr.append(int(i))
    else:
        dict = {**dict, i:1}
val = max(arr)
out = str(val) * 3
print(out)
        
num = "67767133339"
grt = -1
res = ""
for i in num:
    if i*3 in num and int(i) > grt:
        grt = int(i)
if grt > -1:
    res = str(grt) * 3
print (res)

my_dict = {'apple': 3, 'banana': 2, 'cherry': 1, 'date': 3}

# Example: Count the elements with a value greater than 2
count = len({key: value for key, value in my_dict.items()})

ranges = [[1,10],[10,20]]
left = 21
right = 21
isLeft = False
isRight = False
for i in ranges:
    if left in i or isLeft:
        isLeft = True
        if right in i:
            isRight = True
if isLeft and isRight:
    print(True)
print(False)

nums = [5,6,2,7,4]
nums.sort()

lock = ["0", "0", "0", "0"]
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
target = list(target)
i = 0
count = 0
while lock != target:
    if i <= len(lock)-1:
        if lock[i] != target[i]:
            lock[i] = str(int(lock[i]) + 1)
            count += 1
        else:
            i += 1
print(lock, count)

n = 100
sqSmTplCnt = 0
for idx in range(1, n+1):
    for jdx in range(1, n+1):
        if jdx == idx:
            continue
        else:
            maxLoop = idx if idx > jdx else jdx
            for kdx in range(maxLoop+1, n+1):
                if idx*idx + jdx*jdx == kdx*kdx:
                    sqSmTplCnt += 1
                    print(idx, jdx, kdx)
print (sqSmTplCnt)

n = 100
count = 0
for k in range(1, n+1):
    for i in range(1,k):
        for j in range(1,k):
            if i == j:
                continue
            elif i*i + j*j == k*k:
                count += 1
print(count)

nums = [4,4,2,4,3]
arr = []
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] != nums[j]:
            if nums[i] not in arr:
                arr.append(nums[i])
            elif nums[j] not in arr:
                arr.append(nums[j])
print(len(arr))

s = "abacbca"
val = s.count(s[0])
for i in s:
    if val != s.count(i):
        print(False)
print(True)


it = "the dog is jumping over the fense"
arr = it.split(" ")
dict = {}

for i in arr:
    if i in dict:
        count = dict[i]
        dict = {**dict, i:count+1}
    else:
        dict = {**dict, i:1}
print(dict)

nums = [87063,61094,44530,21297,95857,93551,9918]
k = 6
arr = []
nums.sort(reverse=True)
for i in range(len(nums)-k):

    for j in range(i+1, i+1+k):
        arr.append(nums[i]-nums[j])
print(arr)

word = "abcdefd"
ch = "d"

ind = word.index(ch)
res = word[:ind+1]
res = res[::-1]
res += word[ind+1:]
print(res)

nums = [999,997,980,976,948,940,938,928,924,917,907,907,881,
        878,864,862,859,857,848,840,824,824,824,805,802,798,
        788,777,775,766,755,748,735,732,727,705,700,697,693,
        679,676,644,634,624,599,596,588,583,562,558,553,539,
        537,536,509,491,485,483,454,449,438,425,403,368,345,
        327,287,285,270,263,255,248,235,234,224,221,201,189,
        187,183,179,168,155,153,150,144,107,102,102,87,80,57,
        55,49,48,45,26,26,23,15]
arr = [-1]
for i in range(len(nums)-1):
    temp = []
    for j in range(i+1, len(nums)):
        if nums[j] > nums[i]:
            temp.append(nums[j]-nums[i])
    if len(temp)>0:
        arr.append(max(temp))
print((arr))

colors = [1,1,1,6,1,1,1]
arr = -1

for i in range(len(colors)-1):
    for j in range(i+1, len(colors)):
        if colors[i] != colors[j] and j - i > arr:
            arr = j - i
print(arr)

s = "mkgfzkkuxownxvfvxasy"
shifts = [505870226,437526072,266740649,224336793,532917782,311122363,567754492,595798950,81520022,684110326,137742843,275267355,856903962,148291585,919054234,467541837,622939912,116899933,983296461,536563513]
arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
res = ""
for i in range(len(s)):
    sum = 0
    for j in range(i, len(shifts)):
        sum += shifts[j]
    sum += arr.index(s[i])
    while sum > 25:
        sum %= 26
    print(sum)
    res += arr[sum]
print(res)


original = [1,2,3,4]
m = 2
n = 2
arr = []
k = 0
for i in range(m):
    temp = []
    for j in range(n):
        temp.append(original[k])
        k+=1
    arr.append(temp)
print(arr)

nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
arr = []
longest = nums1
shortest = nums2
if len(nums2) > len(longest):
    longest = nums2
    shortest = nums1
i = 0
while i < len(shortest):
    long = longest[i]
    short = shortest[i]
    
    if long[0] == short[0]:
        long[1] += short[1]
    else:
        arr.append(short)
    i+=1
for i in range(len(arr)):
    temp = arr[i]
    ind = temp[0]-1
    longest.insert(ind, temp)
print(longest)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in range(0, len(arr), 5):
    if i + 1 < len(arr):
        print(arr[i])
        print(arr[i + 1])

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
arr = []
for i in [nums1, nums2, nums3]:
    for j in i:
        if i == nums1:
            print(i)
            if j in nums2 and j not in arr or j in nums3 and j not in arr:
                arr.append(j)
        elif i == nums2:
            print(i)
            if j in nums1 and j not in arr or j in nums3 and j not in arr:
                arr.append(j)
        else:
            print(i)
            if j in nums1 and j not in arr or j in nums2 and j not in arr:
                arr.append(j)
print(arr)


s = "english"
print(s==s[::-1])

def gen(num):
    for i in range(1,num+1):
        return i*i

values = gen(5)

print(values)
for i in values:
    print(i)

nums = [4,3,2,1]

for i in range(len(nums)):
    print(i%10==nums[i])


for j in reversed(range(1,6)):
    for i in range(1,j+1):
        print("*",end=" ")
    print("")


s = "abacbcbd"
dict ={}

for i in s:
    if i in dict:
        count = dict[i]
        dict = {**dict, i: count+1}
    else:
        dict = {**dict, i:1}

arr = set(dict.values())
print(len(arr)==1)


words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
count = 0
for i in words1:
    if i in words2 and words1.count(i) == 1:
        count += 1
print(count)

nums = [1,1,2]
j=0
for i in range(len(nums)):
    if nums[i] != nums[j]:
        j+=1
        nums[j] = nums[i]
print (nums)

strs = ["flower","flow","flight"]

ord = {}
for i in range(len(strs)-1):
    val = strs[i]
    for j in range(i+1,len(strs)):
        res  = val.strip(strs[j])
        val = val.strip(res)
    
    if val in ord:
        count = ord[val]
        ord = {**ord, val:count+1}
    else:
        ord = {**ord, val:1}
ord = dict(reversed(sorted(ord.items(), key=lambda item:item[1])))
print(next(iter(ord)) if ord[next(iter(ord))]>1 else "")

keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  

ord = {k:v for k,v in zip(keys, values)}
a = zip(keys,values)
print(dict(a))
print(dict)

arr = (x for x in range(10) if x%2==0)

print(list(arr))
s = 10
l=2
for i in range(0,s,l):
    if i>100:
        break
    print(i)
    l*=2

arr = [1,2,3,1,4,1,2,6,3,1,7,3]
dict = {}
ar = []
for i in arr:
    if i in dict:
        count = dict[i]
        dict = {**dict, i:count+1}
    else:
        dict = {**dict, i:1}

    if dict[i]>1 and i not in ar:
        ar.append(i)

print(ar)

def les(n):
    return len(n)>5

a = r(les,('apple', 'banana', 'cherry'))
print(list(a))

def dis(hey):
    print("hello")
    return hey

@dis
def hey():
    print("hey")

hey()



words = ["cd","ac","dc","ca","zz"]
count = 0
for i in range(len(words)-1):
    for j in range(i+1,len(words)):
        temp = words[j]
        if words[i] == temp or words[i] == temp[::-1]:
            count += 1

print(count)


nums = [1,2,3,3]
k = 4
arr = list(nums)
ar = []
arr.sort(reverse=True)
for i in range(k):
    pass

print(ar)

nums = [1,2,3,3]

ord = {x:nums.count(x) for x in nums if x == 3}
print(dict(ord))

k = 2
arr = list(nums)
arr.sort()
for i in range(len(nums)-k):
    nums.remove(arr[i])
print(nums)

def mapper(i):
    return i*i >1

x = map(mapper, nums)

print(list(x))




dic = {'a':2, 'c':4, 'v':1}
x = dic.items()
print(x, )

ord = dict(sorted(dic.items(), key= lambda item:item[1]))

print(ord)




def dis(*args, **kwargs):
    print(args, kwargs)

dis(5,7,4,a=1,b=2,c=4)


triangle = [[-1],[2,3],[1,-1,-3]]

ind = 0
arr = []
sum = 0
for i in range(len(triangle)):
    minval = triangle[i][0]
    for j in range(len(triangle[i])):
        if abs(j-ind)<=1:
            if triangle[i][j] < minval:
                minval = triangle[i][j]
                print(minval)
    sum += minval
    ind = j
print(sum)

sum = triangle[0][0]
for i in range(len(triangle)-1):
    minval = triangle[i+1][0]
    for j in range(len(triangle[i])):
        for k in range(len(triangle[i+1])):
            if abs(j-k)<=1:
                if triangle[i+1][k] < minval:
                    minval = triangle[i+1][k]
    sum += minval
print(sum)

for i in range(len(triangle)-1):
    for j in range(len(triangle[i+1])):
        pass

dict = {'a':2, 'c':4, 'v':1}
ord = { k:v for v,k in dic.items() }

print(ord)

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
arr = []
for i in range(len(triangle)-1):
    for j in range(len(triangle[i])):
        for k in range(len(triangle[i+1])):
            if abs(j-k)<=1:
                print(triangle[i+1][k])
        print()

words = ["abc","car","ada","racecar","cool"]

for i in words:
    if i == i[::-1]:
        print(i)
print("")

nums = [1,5,3,4,5]
target = 5 
start =2

arr = []
for i in range(start, len(nums)):
    if nums[i] == target:
        arr.append(abs(i-start))
    if nums[start-i] == target:
        arr.append(abs(start-i))

print(min(arr))



nums = [1,5,3,4,5]

x = functools.reduce(lambda a,b: a+b, nums)

print(x)

def sam(i):
    yield i*i


my_dict = {'apple': 3, 'banana': 2, 'cherry': 1, 'date': 3}

ord = dict(sorted(my_dict.items(), key=lambda item:item[1]))
print(ord)

nums = [1,5,3,4,5]

def mapper(i):
    return i>3

x = filter(mapper, nums)
print(list(x))


for i in range(len(strs)-1):
    val = strs[i]
    for j in range(i+1,len(strs)):
        res  = val.strip(strs[j])
        val = val.strip(res)
    print(val)
    if val in ord:
        count = ord[val]
        ord = {**ord, val:count+1}
    else:
        
        ord = {**ord, val:1}
ord = dict(reversed(sorted(ord.items(), key=lambda item:item[1])))
x = dict(sorted(ord.items(), key=lambda item:item[1]))
for i in x:
    if x[i]:
        print(i)
    print("")
strs = ["flower","flow","flight"]
ord = {}
val=0
res=""
for i in range(len(strs)):
    for j in range(len(strs[i])):
        if strs[i][:j+1] in ord:
            count = ord[strs[i][:j+1]]
            ord = {**ord, strs[i][:j+1]:count+1}

            if ord[strs[i][:j+1]]>=val:
                val=ord[strs[i][:j+1]]
                res=strs[i][:j+1]
    
        else:
            ord = {**ord, strs[i][:j+1]:1}

        
print(res)
isTrue=True
arr=[]
for i in range(len(strs[0])):
    for j in range(1,len(strs)):
        if strs[0][:i+1] != strs[j][:i+1]:
            isTrue=False
    if isTrue:
        arr.append(strs[0][:i+1])
print(arr)

nums = [2,3,5]
arr = []
for i in nums:
    sum=0
    for j in nums:
        sum+=abs(i-j)
    arr.append(sum)
print(arr)



num = 4
t = 1

print(num+t*2)


arr = list(s)
if len(s)%2==1:
    print(False)
else:
    i=0
    size = 0
    while i<len(arr):
        j=i+1
        while j<len(arr):
            
            if arr[i] in dict:
                
                if dict[arr[i]] == arr[j]:
                    del arr[i]
                    del arr[j-1]
                    i -= 1
                    j -= 1
            j+=1
        i+=1

print(arr)

s = "[([]])"
lis = list(s)
dict = { "(":")", "[":"]", "{":"}" }
i=0
k=0
arr=[]
while i<len(s)-1:
    j=i+1
    l=k+1
    if s[i] in dict:
            arr.append(s[i])
    while j<len(s):
        if k<len(lis)-1 and l<len(lis) and len(lis)>0 and lis[k] in dict and dict[lis[k]] == lis[l]:
            del lis[k]
            del lis[l-1]
            k -= 1
            l -= 1
    
        if len(arr)>0 and dict[arr[-1]] == s[j]:
             arr.pop() 
        elif s[j] in dict:
            arr.append(s[j])
        j+=1
        if l<len(lis):
            l+=1
    if k<len(lis):
        k+=1
    i+=1
print(arr, lis)

num = 526
print(str(num)[::-1])

target = []
n = 2
res=[]
arr = []
i=1
k=0
while i<=n and arr!=target:
    arr.append(i)
    res.append("Push")
    if len(target)>0 and arr[k]!=target[k]:
        arr.pop()
        res.append("Pop")
    else:
        k+=1
    i+=1
print(res)

arr = [1,25,35,42,68,70]
k = 1
dict = {}
i = 1
count = 0
j = 2 if k>1 else 1
while count!=j:
    if i>=len(arr):
        i-=len(arr)
    great = arr[i] if arr[i]>arr[i-1] else arr[i-1]
    if great in dict:
        count = dict[great]+1
        dict = {**dict, great: count}
    else:
        count = 1
        dict = {**dict, great: count}
    i+=1
print(great)

s = "abcd"
t = "abcdeaaa"
res=""
dict = Counter(t)

for i in s:
    if i in dict:
        dict = {**dict, i:dict[i]-1}
    else:
        dict = {**dict, i:1}
for i in dict:
    if dict[i]>0:
        res+=i
print(res)

sentence = "i love eating burger"
searchWord = "burg"

sentence = sentence.split(" ")

for i in range(len(sentence)):
    if searchWord in sentence[i]:
        print(i+1)

words = ["a","b","c","ab","bc","abc"]
s = "abc"
count=0
for i in words:
    if i in s[:len(i)]:
        count+=1

words = ["pay","attention","practice","attend"]
pref = "at"
count=0
for i in words:
    if pref in i[:len(pref)]:
        count+=1
print(count)

s = "iloveleetcode"
words = ["i","love","leetcode","apples"]
res=""
for i in words:
    if len(res)>=len(s):
        break
    res+=i
print(res==s)

nums = [1,2,0]
nums.sort()
for i in range(1, len(nums)+1):
    if i not in nums:
        print(i)
print(-1)

s = "babad"
out = ""
for i in range(len(s)):
    res=""
    for j in range(i,len(s)):
        res+=s[j]
        if res == res[::-1] and len(res)>len(out):
            out = res
print(out)

s = "abcdefghi"
k = 4
fill = "x"
arr = []
res=""
for i in s:
    if len(res)>=k:
        arr.append(res)
        res=i
    else:
        res+=i
if len(res)<k:
    res+=fill*(k-len(res))
arr.append(res)
print(arr)


s = "abbxxxxzzy"
arr=[]
i=0
while i<len(s):
    count=0
    j=i
    while j<len(s):
        if s[i]!=s[j]:
            break
        print(s[i],s[j])
        count+=1
        j+=1
    if count>2:
        arr.append([i,j-1])
    i=j
print(arr)

s=[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
print(len(s[2]))

s = "egg"
t = "add"
sarr=[]
tarr=[]
for i in range(len(s)):
    sarr.append(s.count(s[i]))
    tarr.append(t.count(t[i]))
print(sarr==tarr)

nums = [1,2,3,1,2,3]
k = 2
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j] and abs(i-j)<=k:
            print (True)
print (False)

i=0
j=i+1
while i<len(nums)-1:

    if nums[i]==nums[j] and abs(i-j)<=k:
        print(nums[i], nums[j])

    if j>=len(nums)-1:
            i+=1
            j=i+1
    else:
         j+=1
    
print(False)

for i in range(len(nums)):
    if nums[i] in nums[i+1:] and abs(i - (nums[i+1:].index(nums[i])))<=k:
        print(True)
print(False)

path = "/a/./b/../../c/"
# res=""
# for i in range(len(path)):
#     if i==len(path)-1 and path[i]=="/" or len(res)>0 and res[-1]=="/" and path[i]=="/":
#         continue
#     elif path[i]==".":
#         res=""
#         continue
#     res+=path[i]
# print(res)

path=path.split("/")
res="/"
for i in path:
    res+=i
print(res)

s = "string"
res=""

for i in s:
    if i == "i":
        res = res[::-1]
    else:
        res += i

print(res)

s = "a-bC-dEf-ghIj"
res = ""
arr = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R',  'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z' ]
for i in s[::-1]:
    if i in arr:
        res+=i
for i in range(len(s)):
    if s[i] not in arr:
        res=res[:i]+s[i]+res[i:]
print(res)

words = ["one.two.three","four.five","six"]
separator = "."
arr=[]
for i in words:
    s = i.split(separator)
    for j in s:
        if j!="":
            arr.append(j)
print(arr)

arr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a=701//26
print(arr[(a%26)-1], arr[(701%26)-1])

s = "abcdefg"
k = 2
count = 0
res=""
out=""
for i in range(len(s)):
    res+=s[i]
    if count == k-1:
        out += res[::-1]
        res=""
    if count == (k*2)-1:
        out += res
        res=""
        count=0
    count+=1
if count != 2 or count != 4:
    out += res
print(out)

nums = [2,7,1,19,18,3]
sum = 0
for i in range(len(nums)):
    if len(nums)%(i+1)==0:
        sum+=nums[i]*nums[i]
print(sum)

s = "010"
s = list(s)
s.sort()
res=""
for i in reversed(range(len(s)-1)):
    res+=s[i]
res+=s[-1]
print(res)

c = 4
for i in range(0,c+1):
    for j in range(1, c+1):
        if (i*i) + (j*j) == c:
            print (True)
print (False)

words = ["leet","code"]
x = "e"
arr=[]
for i in range(len(words)):
    if x in words[i]:
        arr.append(i)
print (arr)

nums = [1,5,1,1,6,4]
nums.sort()
arr=[]
isTrue=True
i=0
while len(arr)<len(nums):
    if isTrue:
        arr.append(nums[i])
        isTrue=False
    else:
        arr.append(nums[-i])
        isTrue=True
    i+=1
print(arr)

nums = [1,2,3,4,5]
k = 3

sum=0
for i in range(max(nums),max(nums)+k):  
    sum+=i

n = 11
print(bin(n))
count = dict(Counter(bin(n)))
print (count['1'] if '1' in count else 0)

a = "1010"
b = "1011"
print(bin(int(a,2)+int(b,2)))

num = [1,2,0,0]
k = 34
res = ""
for i in num:
    res+=str(i)
num=[]
for i in str(int(res)+k):
    num.append(int(i))

s = "egcfe"
s = list(s)
for i in range(len(s)):
    if s[i] != s[-i-1]:
        if s[i]<s[-i-1]:
            s[-i-1]=s[i]
        else:
            s[i]=s[-i-1]
res=""
for i in s:
    res+=i
print(res)

s = "PABC"

while "AB" in s or "CD" in s:
    res=""
    i=0
    print(s)
    while i<(len(s)):
        if i<len(s)-1 and s[i]=="A" and s[i+1]=="B" or len(s)>(i+1) and s[i]=="C" and s[i+1]=="D":
            i+=1
            
        else:
            res+=s[i]
        i+=1
    s=res
print(len(s))

s = "ab#c"
t = "ad#c"

while "#" in s or "#" in t:
    ress=""
    rest=""
    i=0
    larger = len(s) if len(s)>=len(t) else len(t)
    while i<larger:
        
        if i<len(s):
            if s[i]=="#":
                ress = ress[:-1]      
            else:
                ress+=s[i]
        if i<len(t):
            if t[i]=="#":
                rest = rest[:-1]
            else:
                rest+=t[i]
        i+=1  
    s=ress
    t=rest
          
print(s,t)    


arr = [1,2,3,4,5,6,7,8,9,10]

sums = ([x for x in arr] )
print(sums)

dict = ({k:k for k in arr})

print(dict)

ord = {'H': 8,'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
ord = dict(sorted(ord.items(), key=lambda item:item[1]))
print(ord)


lis = ([dict[x] for x in dict])
print(lis)

it = iter(arr)
for i in range(len(arr)):
    print(next(it))

def maps(i):
    return i*i

x = (lambda x,y : x+y)
print(int(x))

mp = functools.reduce((lambda x,y : x+y), arr)
print(mp)

for i in x:
    print(i)

x = functools.reduce((lambda x,y:x+y), arr)
print(x)



s=Sum
s.display(2,4)

arr = [2,12,36,108,0,0.8]
arr.sort(reverse=True)
print(arr)
ar = [102,48]

s="000"

print(bin(95))

arr.extend(ar)

print(arr)

class Main(ABC):
    @abstractmethod
    def sum(self):   
        pass
    
class Sum(Main):
    def sum(length,width):  
        print(length+width)

a=Sum
a.sum(1,2)
arr=[1,2,34,4,5,5]

def gen(i):
    yield i*i

for i in gen(arr):
    print(i)


def hey(hello):
    print("hey")
    return hello

@hey
def hello():
    print("hello")
    
hello()

arr = [2,12,36,108,0]

a= functools.reduce(lambda x,y:x+y, arr)
print(a)


s = "aaabbb"

if s=="a"*s.count("a")+"b"*s.count("b"):
    print("a"*s.count("a")+"b"*s.count("b"))
print(False)


s = "1 box has 3 blue 4 red 6 green and 12 yellow 1 marbles"
s=s.split(" ")
arr=[]
for i in s:
    try:
        num = int(i)
        arr.append(num)
    except:
        continue

ar = set(arr)
ar 
ar.sort()
print(ar)

s = "is2 sentence4 This1 a3"
s = s.split(" ")
arr = []
for i in s:
    arr.append(i[::-1])

arr.sort()
res = ""

for i in range(len(arr)):
    res+=arr[i][::-1][:-1]
    if i<len(arr)-1:
        res+=" "
print(res)

nums = [-1,1,-1,1,-1]
sum=1
for i in nums:
    sum*=i
print(sum)

sentence = "thequickbrownfoxjumpsoverthelazydog"
isTrue=True
for i in string.ascii_lowercase:
    if i not in sentence:
        print (False)
print (True)


logs = [[1950,1961],[1960,1971],[1970,1981]]

for i in range(len(logs)):
    pass

strs = ["alic3","bob","3","4","00000"]
lar = 0
for i in strs:
    try:
        if int(i)>lar:
            lar=int(i)
    except:
        if len(i)>lar:
            lar = len(i)
print(lar)

nums = [-2,1,-3,4,-1,2,1,-5,4]
arr = []

for i in range(len(nums)):
    temp=[]
    sum=0
    for j in range(i, len(nums)):
        sum+=nums[j]
        temp.append(sum)
    arr.append(max(temp))
print(arr)

words = ["1","2","prev","prev","prev"]
arr=[]
prev = 0
bal = 0
i=0
while i<len(words):
    if words[i] == "prev":
        del words[i]
        arr.append(-1)
        prev+=1
        i-=1
    else:
        words[i] = int(words[i])
    i+=1
if prev - len(words) > 0:
    bal = prev - len(words)
print(words[-prev:][::-1]+arr[:bal])



mat = [[0,1],[1,0]]
count = 0
for i in range(len(mat)):
    if mat[i].count(1)>count:
        count=mat[i].count(1)
        index = i
print(index, count)

words = ["1","2","prev","prev","prev"]
arr=[]
prev = 0
i=0
while i<len(words):
    if words[i] == "prev":
        del words[i]
        if i>0:
            arr.append(int(words[i-1]))
            del words[i-1]
            i-=1 
        else:
             arr.append(-1)    
        i-=1
    i+=1
print(arr)

amt = 100
purchaseAmount = 9
sub = 10
val = purchaseAmount//10
dec = purchaseAmount%10
amt-=10*val
if dec>=5:
    amt-=10
print(amt)

nums = [0,1,2,4,5,7]
arr=[]
i=0
while i<(len(nums)):
    for j in range(nums[i], nums[-1]+1):
        if nums[j] == j:
            print(i)
        else:
            i=j
            break
        j+=1
    i+=1

names = ["Mary","John","Emma"]
heights = [180,165,170]

for i in range(len(names)-1):
    for j in range(i+1, len(names)):
        if heights[i]<heights[j]:
            temp=heights[i]
            name=names[i]
            heights[i]=heights[j]
            names[i]=names[j]
            heights[j]=temp
            names[j]=name

nums = [2,3,1,3,2]
nums.sort(reverse=True)
arr=[]
ord = dict(Counter(nums))
ord = dict(sorted(ord.items(), key=lambda item:item[1]))
for i in ord:
    for j in range(ord[i]):
        arr.append(i)
print(arr)

nums = [0,0,1,1,2,2]
i=0
count = 0
while i<len(nums)-1:
    j=i+1
    while j<len(nums):
        if nums[i]==nums[j]:
            del nums[i]
            j-=1
            del nums[j]
            i-=1
            print(nums)
            count+=1
            break
        j+=1
    i+=1
print(count, len(nums), nums)

nums = [1,1000,2]
key = 1000
ord={}
for i in range(len(nums)):
    if nums[i]==key:
        if nums[i+1] in ord:
            count = ord[nums[i+1]]
            ord={**ord, nums[i+1]:count+1}
        else:
            ord={**ord, nums[i+1]:1}
ord = dict(reversed(sorted(ord.items(), key=lambda item:item[1])))
for i in ord:
    if len(ord)>1 and i!=key:
        print(i)
    else:
        print(i)

words = ["cat","bt","hat","tree"]
chars = "atach"
count=0
for i in words:
    isTrue=True
    arr=list(chars)
    for j in i:
        if j not in arr:
            isTrue=False
            break
        else:
            arr.remove(j)
    if isTrue:
        count+=len(i)
print (count)

s = "code"
target = "code"

ord = dict(Counter(s))
isTrue=True
count = -1
while isTrue:
    for i in target:
        if ord[i]==0:
            isTrue=False
            break
        ord[i] -= 1
    count+=1
print(count)





points = [[3,2],[-2,2]]
count=0
for i in range(len(points)-1):
    x=points[i][0]
    y=points[i][1]
    while [x,y] != points[i+1]:
        if x<points[i+1][0]:
            x+=1
        elif x>points[i+1][0]:
            x-=1
        if y<points[i+1][1]:
            y+=1
        elif y>points[i+1][1]:
            y-=1
        count+=1
print(count)

words = ["alan","amal"]
arr = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
for i in words:
    k=0
    
letters = ["c","f","j"]
target = "a"

letters.sort()
for i in letters:
    print(i>target)

def mapper(i):
    return i>3

arr=[1,2,3,4,5,6]
con = map(mapper, arr)

for i in con:
    print(i)


s = "Let's take LeetCode contest"
s = s.split(" ")
res = ""
i=0
while i<len(s):
    res += s[i][::-1]
    if i<len(s):
        res += " "
    i += 1
print(res)

words = ["cool","lock","cook"]
arr = []
i=0
while i<len(words[0]):
    j=0
    flag = True
    count = words[0].count(words[0][i])
    while j<len(words):
        if words[0][i] not in words[j]:
            flag = False
        if words[j].count(words[0][i])<count:
            count=words[j].count(words[0][i])
        j+=1

    if flag and arr.count(words[0][i])<count:   
        arr.append(words[0][i])
    i+=1
print(arr)

nums1 = [1,2,2,1]
nums2 = [2,2]
arr=[]
i=0
while i<len(nums1):
    count = nums1.count(nums1[i]) if nums1.count(nums1[i])<=nums2.count(nums1[i]) else nums2.count(nums1[i])
    if nums1[i] in nums2 and arr.count(nums1[i])<count:
        arr.append(nums1[i])
    i+=1
print(arr)


nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
arr=[]
i=0
while i<len(nums[0]):
    flag=True
    j=0
    while j<len(nums):
        if nums[0][1] not in nums[j]:
            flag=False
        j+=1
    if flag:
        arr.append(nums[0][i])

nums1 = [2,2]
nums2 = [2]
i=0
while len(nums1)>0 and i<len(nums1):
    if nums1[i] in nums2:
        target=nums1[i]
        while target in nums1 or target in nums2:
                if target in nums1:
                  nums1.remove(target)
                  i-=1
                if target in nums2:
                  nums2.remove(target)
                print(nums1, nums2)
    i+=1
print([nums1, nums2])


nums = [57,57,57,57,57,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,85,85,85,86,86,86]
count = 0
i=1
while i<len(nums)-1:
    while i<len(nums)-2 and nums[i]==nums[i+1]:
        del nums[i+1]
    if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
        count+=1
    elif nums[i]<nums[i-1] and nums[i]<nums[i+1]:
        count+=1
    print(nums[i])
    i+=1
print(count)


nums = [4,3,10,9,8]
nums.sort(reverse=True)
i=0
sum=0
res=0
while i<len(nums):
    sum+=nums[i]
    i+=1
k=0
while res<=sum:
    res+=nums[k]
    sum-=nums[k]
    k+=1
print(nums[:k])



numBottles = 15
numExchange = 4

i=numBottles
count=i
if numBottles%numExchange==0:
    while i>=numExchange:
        i=i%numExchange+int(i/numExchange)
        count+=i
else:
    while i>=numExchange:
        i=i%numExchange+int(i/numExchange)
        count+=i
print(count+1)
count=0
while i>=numExchange:
    count+=numExchange
    i-=numExchange
    i+=1
print(count+i)



height = [0,1,0,2,1,0,1,3,2,1,2,1]
count=0
i=0
z=len(height)-1
while i<=z:
    j=i+1
    y=z-1
    while j<=y:

        print(j,y)
        j+=1
        y-=1
    i+=1
    z-=1
print(count)

def mapper(i):
    return i>3


arr = [1,2,3,4,5,6]

fun = functools.reduce(lambda x,y:x+y, arr)
print(fun)
for i in fun:
    print(i)

strg = "I am zayyan"
strg = strg.split(" ")
s=""
for i in strg[::-1]:
    s+=i
    s+=" "
print(s)

arr = [1,2,3,4,5]
ar = [6,7,8,9,10]

array=[]

for i in zip(arr,ar):
    array.extend(list(i))

print(array)

nums = [1,3,5,2,4,8,2,2]
i=0
isTrue=True
temp=[]
while len(nums)>1:
    if isTrue:
        temp.append(min(nums[i],nums[i+1]))
        isTrue=False
    else:
        temp.append(max(nums[i],nums[i+1]))
        isTrue=True
    i+=2
    if i>=len(nums)-1:
        nums=temp
        temp=[]
        i=0
print(nums)



arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,15]
even=[]
odd=[]
out=[]
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

for i in range(max(len(odd), len(even))):
    if i<len(even):
        out.append(even[i])
    if i<len(odd):
        out.append(odd[i])
print(out)


n = 6
arr = []
i=1
while i<=n:
    arr.append(i)
    i+=1
isTrue=True

while len(arr)>1:
    i=0
    while i<len(arr):
        del arr[i]
        i+=1
    arr = arr[::-1]
            
print(arr[0])

i=0
arr=[]
while i<len(nums):
    res=str(nums[i])
    j=nums[i]
    k=i
    while j<=nums[-1] and k<len(nums):
        if j != nums[k]:
            i=k-1
            break
        j+=1
        k+=1
    if res != str(nums[i]):
        res+="->"+str(nums[i])

    arr.append(res)
    i+=1
print(arr)

nums = [0,2,3,4,5,6,9,10,11]
i=0
res=""
arr=[]
while i<len(nums):
    if len(res)==0:
        res+=str(nums[i])
    elif int(res)!=nums[i]-i:
        res+="->"+str(nums[i-1])
        arr.append(res)
        res=""
        i-=1
    i+=1
print(arr)

pref = [253587,980555,886549,989108,446471,924548,945243,918448,927141,206562,984323,670844,796596,338814,291203,4564,966711,995744,944077,707887,110604,169201,982423,791987,915489,873484,567252,747653,957642,205591,768857,73967,534124,458380,749578,581649,781447,341818,537944,284823,741971,879530,30697,94484,137718,223934,212659,750705,332146,653082]
dict={1:0, 2:0, 3:10, 4:100, 5:1000, 6:10000, 7:100000}
i=0
xor=0
arr=[]
while i<len(pref):
    j=dict[len(str(xor))]
    while xor^j!=pref[i]:
        j+=1
    xor^=j
    arr.append(j)
    i+=1
print(arr)

num = 14
count=0
while num!=0:
    if num%2==0:
        num/=2
    else:
        num-=1
    count+=1
print(count)

target = 19
maxDoubles = 2
i=1
count=0
while i!=target:
    if maxDoubles>0:
        i*=2
        maxDoubles-=1
    else:
        i+=1
    count+=1
print(count)

s = "tree"
s = dict(Counter(s))
s=dict(reversed(sorted(s.items(), key=lambda item:item[1])))
res=""
for i in s:
    res+=i*s[i]
print(res)

nums = [1,1,1,2,2,3]
k = 2

nums = dict(reversed(sorted(dict(Counter(nums)).items(), key=lambda item:item[1])))
arr=[]
for i in nums:
    arr.append(i)
    if len(arr)>=k:
        break
print(arr)

s = "leetcode"

ord=dict(sorted(dict(Counter(s)).items(), key=lambda item:item[1]))
print(ord)
for i in ord:
    if ord[i]==1:
        print(s.index(i))

s="izspyzhxvhmvsqekrauyugcbepvifvgnpthxrqunslwvgfdnzfzdxockaoomqybnsfzewkcspwpepvbyohccnoivagjhzplnkcvr"

dict={}
i=0
while i<len(s):
    print(i)
    if s[i] in dict:
        print (s[i])
        break
    else:
        dict[s[i]] = 1
    i+=1
print(dict)

nums = [1,2,2,4]
i=0
arr=[]
while i<len(nums):
    if i+1!=nums[i]:
        arr.append(i)
    i+=1
arr.append(i-1)
print (arr)

nums = [1,5,0,3,5]
if 0 in nums:
    sets=set(nums)
    sets.remove(0)
    sub = min(sets)
else:
    sub = min(nums)
count = 0
while nums.count(0) != len(nums):
    i=0
    while i<len(nums):
        if nums[i]!=0:
            nums[i]-=sub
        i+=1
    print(nums)
    count+=1
print(count)

nums = [1,5,0,3,5]
nums = list(set(nums))
if 0 in nums:
    nums.remove(0)
count=0
while len(nums)!=0:
    i=0
    sub = min(nums)
    while i<len(nums):
        nums[i]-=sub
        if nums[i]<1:
            del nums[i]
            i-=1
        i+=1
    count+=1
print(count)

s = "daabcbaabcbc"
part = "abc"

while part in s:
    i=0
    while i<len(s):
        if s[i:i+len(part)] == part:
            s=s[:i]+s[i+len(part):]
            break
        i+=1
    print(s)

x = range(10)
print(x)

start = 10
goal = 7

zero = 0
start = list(str(zero)*(30-len(str(bin(start)[2:])))+str(bin(start)[2:]))
goal = list(str(zero)*(30-len(str(bin(goal)[2:])))+str(bin(goal)[2:]))
count = 0
i=29
while i>=0:
    if goal[i] != start[i]:
        start[i] = goal[i]
        count+=1
    i-=1
print(count)

num = "1210"

i=0
isTrue=True
while i<len(num):
    if num.count(str(i))!=int(num[i]):
        print(i)
    i+=1
print(isTrue)

left = 1
right = 22
arr=[]
while left<=right:
    flag=True
    i=0
    while i<len(str(left)):
        if int(str(left)[i])==0 or left%int(str(left)[i])!=0:
            flag=False
        i+=1
    if flag:
        arr.append(left)
    left+=1
print(arr)

num = 7
i=0
count = 0
while i<len(str(num)):
    print(int(str(num)[i]))
    if num%int(str(num)[i])==0:
        count+=1
    i+=1
print(count)

n=1
arr = list(x for x in range(1,n+1,2))
arr=arr[::-1]

print(arr)       
while len(arr)>1:
    i=0
    
    while i<len(arr):
        del arr[i]
        i+=1
    arr = arr[::-1]
                    
print(arr)

mat = [[1,0,0],[0,0,1],[1,0,0]]
arr = []
i=0
while i<len(mat):
    j=0
    while j<len(mat[i]):
        if mat[i][j]==1:
            if j not in arr:
                arr.append(j)
            else:
                arr.remove(j)
        j+=1
    i+=1
print(arr)

nums=[2,1]
i=0
j=i+1
nums[j]=nums[i]+nums[j]
nums[i]=nums[j]-nums[i]
nums[j]=nums[j]-nums[i]
print(nums[i], nums[j])




class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head =  node

    def print(self):
        if self.head == None:
            print("Linked List is empty")
            return
        current = self.head
        while current.next:
            print(current.data)
            current = current.next

ll = LinkedList()
ll.insert_at_begining(1)
ll.insert_at_begining(4)
ll.insert_at_begining(5)
ll.insert_at_begining(6)
ll.print()


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            self.tail = current.next
    
    def insert_at_begining(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            self.head = node
            self.head.next = current

    def insert_at_end(self, data):
        node = Node(data)
        current = self.tail
        self.tail = node
        current.next = self.tail

    def insert(self, data, target):
        node = Node(data)
        current = self.head
        while current.data != target:
            current = current.next
        new_node = node
        new_node.next = current.next
        current.next = new_node

    def delete(self, target):
        current = self.head
        while current.data != target:
            previus = current
            current = current.next
        previus.next = current.next
        
    
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

pref = [253587,980555,886549,989108,446471,924548,945243,918448,927141,206562,984323,670844,796596,338814,291203,4564,966711,995744,944077,707887,110604,169201,982423,791987,915489,873484,567252,747653,957642,205591,768857,73967,534124,458380,749578,581649,781447,341818,537944,284823,741971,879530,30697,94484,137718,223934,212659,750705,332146,653082]
ll = LinkedList()
for i in pref:
    ll.add_node(i)
ll.insert(8, 206562)
ll.insert_at_begining(7)
ll.insert_at_end(10)
ll.delete(653082)
ll.print()




mat = [[0,0,0,0,0,1,0,0],
       [0,0,0,0,1,0,0,1],
       [0,0,0,0,1,0,0,0],
       [1,0,0,0,1,0,0,0],
       [0,0,1,1,0,0,0,0]]
arri = []
arrj = []
i=0
while i<len(mat):
    j=0
    while j<len(mat[i]):
        if mat[i][j] == 1:
            arri.append(i)
            arrj.append(j)
        j+=1
    i+=1
i=0
j=0
k=0
while i<len(mat):
    if arri.count(arri[i])==1:
        j+=1
    if arrj.count(arrj[i])==1:
        k+=1
    i+=1
print(arri, arrj)

low = 1200
high = 1230
count=0
while low<=high:
    if len(str(low))%2==0:
        i=0
        first=0
        second=0
        while i<len(str(low))/2:
            first += int(str(low)[:len(str(low))//2][i])
            second += int(str(low)[len(str(low))//2:][i])
            i+=1
        if first == second:
            count+=1
    low+=1
print(count)

array = [1,2,3,4,5,6,7,8,9,10]
target = 7
i=0
while i<len(array):
    if array[i]==target:
        print(i)
    i+=1
i=(len(array)//2)-1
while array[i]!=target and len(array)>1:
    if array[i]<target:
        array=array[i:]
    else:
        array=array[:i]
    i=(len(array)//2)-1
print(array[i])



class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            current.next.prev = current
            self.tail = current.next

    def print(self):
        if self.head == None:
            print("Linked List is empty")
            return
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def reversal(self):
        if self.tail==None:
            print("Linked List is empty")
            return
        current = self.tail
        while current:
            print(current.data)
            current = current.prev
        
ll = LinkedList()
array = [1,2,3,4,5,6,7,8,9,0]
for i in array:
    ll.append(i)
ll.reversal()

dict={}
j=0
for i in string.ascii_letters:
    dict[i]=j
    j+=1
print(dict)

def mapper(i):
    if i<1:
        return 1
    return i*mapper(i-1)

print(mapper(5))

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
sum=0
boxTypes = list(reversed(sorted(boxTypes, key=lambda item:item[1])))
i=0
while i<len(boxTypes):
    i+=1

ar = []

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            current.next.prev = current
            self.tail = current.next
    
    def print(self):
        if self.head == None:
            print("Linked List is empty")
            return
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def reversal(self):
        if self.tail == None:
            print("Linked List is empty")
            return
        current = self.tail
        while current:
            print(current.data)
            current = current.prev

    def insert_at_begining(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            self.head = node
            self.head.next = current
    
    def insert_at_end(self, data):
        node = Node(data)
        if self.tail == None:
            self.tail = node
        else:
            current = self.tail
            self.tail = node
            current.next = self.tail

    def insert_after(self, data, target):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            current = self.head
            while current:
                if current.data == target:
                    node.next = current.next
                    current.next = node
                    return
                current = current.next
            current = self.tail
            self.tail = node
            current.next = self.tail

    def insert_before(self, data, target):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            current = self.head
            while current:
                if current.next.data == target:
                    node.next = current.next
                    current.next = node
                    return
                if current.next == self.tail:
                    new_node = current
                current = current.next
            node.next = self.tail
            new_node.next = node

    def delete(self, target):
        if self.head:
            current = self.head
            if current.data == target:
                self.head = current.next
                return
            while current:
                if current.next.data == target:
                    current.next = current.next.next
                    return
                current = current.next

    def remove_duplicate(self):
        current = self.head
        while current.next != None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        


arr = [1,2,2,2,2,2,2,3,4,5,6,7,8,9,2,4,6,8]
ll = LinkedList()
for i in arr:
    ll.append(i)
ll.insert_at_end(10)
ll.insert_at_begining(0)
ll.insert_after(100,11)
ll.insert_before(1512,6)
ll.delete(0)
ll.remove_duplicate()
ll.print()


n = 13

i = 1
arr = []
while i<=n:
    i+=1
arr = ['flower', 'flow','flight']

for i in range(len(arr[0])):
    for j in range(1,len(arr)):
        print((arr[0][:i+1]),arr[j][:i+1])


paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
arr = []
ar = []
for i in paths:
    arr.extend(i)

for i in arr:
    if arr.count(i)==1:
        ar.append(i)
print(ar)

boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
truckSize = 35
load=0
sum=0
boxTypes = list(reversed(sorted(boxTypes, key=lambda item:item[1])))
i=0
while i<len(boxTypes) and load<truckSize:
    if boxTypes[i][0]<1:
        i+=1
    print(i)
    if i<len(boxTypes) and boxTypes[i][0]>0:
        load+=1
        sum+=boxTypes[i][1]
        boxTypes[i][0] -= 1

print(sum)
    

paths = [["A","Z"]]
dict={}
i=0
while i<len(paths):
    j=0
    while j<len(paths[i]):
        if paths[i][j] not in dict:
            dict[paths[i][j]] = j
        else:
            dict.pop(paths[i][j])
        j+=1
    i+=1
for i in dict:
    if dict[i]==1:
        print (i)

event1 = ["15:19","17:56"]
event2 = ["14:11","20:02"]

ae1=float(event1[0].replace(':','.'))
ae2=float(event1[1].replace(':','.'))
be1=float(event2[0].replace(':','.'))
be2=float(event2[1].replace(':','.'))

if be1 >= ae1 and be1 <= ae2 or be2 >= ae1 and be2 <= ae2 or be1 <= ae1 and be1 >= ae2 or be1<=ae1 and be2>=ae2:
    print(True)


intervals = [[1,4],[4,5]]
intervals = list(sorted(intervals, key=lambda item:item[0]))
arr = []

i=0
while i<len(intervals):
    temp = []
    temp.append(intervals[i][0])
    j=i
    while j<len(intervals)-1 and intervals[j][1]>=intervals[j+1][0]:
        j+=1
        i+=1
    temp.append(intervals[j][1] if intervals[j][1]>intervals[j-1][0] else intervals[j-1][0])
    arr.append(temp)
    i+=1

print(arr)

s1 = "abcd"
s2 = "cdab"
s1 = list(s1)
s2 = list(s2)

i=0
while i<len(s1)-1:
    j=i+1
    while j<len(s1):
        temp = s2[i:]
        s2[i:] = s2[j:]
        s2[j:] = temp
        if s1 == s2:
            print(True)
        else:
            temp = s2[i:]
            s2[i:] = s2[j:]
            s2[j:] = temp
        j+=1
    i+=1
print(False)


n = 24

dict={}
i=1
while i<=n:
    j=0
    sum=0
    while j<len(str(i)):
        sum+=int(str(i)[j])
        j+=1

    if sum in dict and i not in dict:
        print(i, sum)
        count = dict[sum]
        dict = {**dict, sum:sum+i}
    else:
        dict[i] = i
    i+=1
arr = list(reversed(sorted(dict.items(), key=lambda item:item[1])))
print(arr)


nums = [5,1,4,1]
indexDifference = 2
valueDifference = 4

i=0
while i<len(nums)-1:
    j=i+1
    while j<len(nums):
        if abs(i-j)>=indexDifference and abs(nums[i]-nums[j])>=valueDifference:
            print ([i, j])
        j+=1
    i+=1
    
s = "aaaabbbbcccc"
out = dict(Counter(s))
out = dict(sorted(out.items()))
res=""
j=1
while len(res)<len(s):
    val=""
    for i in out:
        if out[i]>0:
            val+=i
            out[i]-=1
        continue
    if j%2==0:
        val=val[::-1]
    res+=val
    j+=1
print(res)


strs = ["eat","tea","tan","ate","nat","bat"]
i=0
arr = []
while i<len(strs):
    i_count = dict(Counter(strs[i]))
    j=i+1
    temp = [strs[i]]
    while j<len(strs):
        j_count = dict(Counter(strs[j]))
        if i_count == j_count:
            temp.append(strs[j])
            del strs[j]
        else:
            j+=1
    arr.append(temp)
    i+=1
print (arr)

values = [8,1,5,2,6]
arr = []
i=0
while i<len(values)-1:
    j=i+1
    while j<len(values):
        arr.append((values[i]+values[j])+(i-j))
        j+=1
    i+=1
print(arr)

arr = [0,2,1,-6,6,7,9,-1,2,0,1]
sum = functools.reduce(lambda x,y : x+y, arr)
print(sum)

s = "abbaca"

i=0
while i<len(s):
    j=len(s)
    while j>i:
        if s[i:j] == s[i:j][::-1]:
            s = s[:i]+s[j:]
            break
        j-=1
    i+=1
print(s)

s = "011101"
arr = []
i=0
while i<len(s)-1:
    arr.append(s[:i+1].count("0")+s[i+1:].count("1"))
    i+=1
print(arr)

n = 5
i = 0
x = 1
while i<n:
    sum = x+4*i
    i+=1
print(14%2)

path = "NES"
count = dict(Counter(path))
if "N" in count:
    if "S" not in count:
        print(False)
if "E" in count:
    if "W" not in count:
        print(False)
if "S" in count:
    if "N" not in count:
        print(False)
if "W" in count:
    if "E" not in count:
        print(False)
print(True)



nums = nums = [4,4,2,4,3]

arr = []
i=0
temp=[]
while i<(len(nums)-1):
    j=i+1
    while j<(len(nums)):
        if len(temp)<1:
            temp.append(nums[i])
        if nums[j] not in temp:  
            temp.append(nums[j])
        if len(temp)>=3:
            arr.append(temp)
            temp=[]
        j+=1
    i+=1
print(arr)

s = "sad"

i=0
while i<len(s)-1:
    if s[i] == s[i+1]:
        s = s[:i]+s[i+2:]
        i-=1
    else:
        i+=1
print(s)
    

s = "pbbcggttciiippooaais"
k = 2

i=0
while i<len(s):
    if s[i:i+k] == s[i]*k:
        s=s[:i]+s[i+k:]
        if i>k:i-=k
        else:i=0
    else:
        i+=1
print(s)

s = "226"
arr = []
i = 0
while i<len(s):
    j=i
    while j<=len(s):
        if s[i:][:j] != "" and int(s[i:][:j])>0 and int(s[i:][:j])<27 and int(s[i:][:j]) not in arr:
            arr.append(int(int(s[i:][:j])))
        j+=1
    i+=1
print(len(arr))

path = "SN"

path = dict(Counter(path))
vert = False
horz = False
for i in path:
    if i == "N":
        if "S" in path and path[i]<=path["S"]:
            vert = True
    elif i == "S":
        if "N" in path and path[i]<=path["N"]:
            vert = True
    elif i == "E":
        if "W" in path and path[i]<=path["W"]:
            horz = True
    else:
        if "E" in path and path[i]<=path["E"]:
            horz = True
    if vert and horz or vert and "W" not in path and "E" not in path or horz and "S" not in path and "N" not in path:
        print (True)
print (False)

words = ["ab","a"]

i=0
res=""
while i<len(words):
    res+=words[i]
    i+=1
count = dict(Counter(res))

for i in count:
    if count[i]%len(words)!=0:
        print(False)
print(True)

n = 1

while n>1:
    if n/2 == n//2:
        n/=2
    elif n/3 == n//3:
        n/=3
    elif n/5 == n//5:
        n/=5
    else:
        print(False)
        break
    print(n)
print(True)


nums = [3,1,3,2,4,3]
count = dict(reversed(sorted(dict(Counter(nums)).items(), key=lambda item:item[1])))
print(count)

s = "1212"
1,21
1,12
2,12
2,21
1,2
i = 0
arr = []
while i<len(s):
    j=i
    while j<=len(s):
        if s[i:][:j] != "" and int(s[i:][:j])>0 and int(s[i:][:j])<27 and int(s[i:][:j]) not in arr:
            arr.append(int(int(s[i:][:j])))
        j+=1
    i+=1
print(arr)

s = "WWEQERQWQWWRWWERQWEQ"
i=0
count = 0
print(count, s, dict(Counter(s)), len(s))
while i<len(s):
    if s.count(s[i]) > len(s)/4:
        if s.count('Q') < len(s)/4:
            s = s[:i] + 'Q' + s[i+1:]
            count += 1
        elif s.count('W') < len(s)/4:
            s = s[:i] + 'W' + s[i+1:]
            count += 1
        elif s.count('E') < len(s)/4:
            s = s[:i] + 'E' + s[i+1:]
            count += 1
        elif s.count('R') < len(s)/4:
            s = s[:i] + 'R' + s[i+1:]
            count += 1
        
    i+=1
print(count, s, dict(Counter(s)), len(s))

nums1 = [1,2,3]
nums2 = [2,4]

nums1 = set(nums1)
nums2 = set(nums2)
num = list(nums1.intersection(nums2))
num.sort(reverse=True)
print(num)

g = [1282,1257,334,407,337,1349,1110,1454,1464,703,109,1293,1000,1304,713,778,1482,1136,1295,1205,822,917,1485,1019,963,1294,249,1465,567,1207,1006,938,1051,52,977,268,115,915,937,966,405,1088,1458,460,1179,790,283,1430,603,192,1419,862,310,159,1371,545,367,955,70,1255,1114,148,1151,61,399,916,503,1075,325,774,223,1076,339,838,594,33,1514,736,1343,653,244,1052,840,511,895,858,638,240,332,417,1269,1162,1541,1213,685,240,268,517,64,473,1167,836,572,763,988,461,717,915,1496,1199,646,517,627,1197,1027,853,1161,1072,556,886,1245,1308,1509,191,570,29,137,1405,102,26,1489,965,1216,1537,1290,64,61,1255,1168,280,343,1383,1060,121,954,110,1179,647,145,324,915,865,300,971,93,1289,191,30,926,1124,327,568,661,603,1022,519,395,954,551,981,1168,930,578,1516,1300,408,70,1094,1335,292,1214,717,538,1080,1270,912,1345,310,831,307,1161,314,990,225,182,561,742,1472,1061,1227,947,97,1009,566,1017,353,142,1234,617,1289,180,1045,541,1211,1550,180,274,627,253,653,1141,826,1191,888,774,398,803,413,95,226,1389,976,1505,1517,991,768,171,1085,614,1019,538,130,1533,1309,1217,845,628,886,151,208,686,814,626,1268,1330,83,928,847,385,733,1181,329,648,741,1496,359,1150,34,88,1308,623,680,1257,735,251,309,456,900,1348,554,1369,574,141,661,1399,63,515,231,1194,29,51,621,958,984,265,1326,1164,1063,925,471,1407,397,500,224,1479,1449,167,1144,711,93,643,1274,616,343,101,1352,1114,1304,1314,1087,897,109,898,1229,473,304,1142,484,1346,1506,1200,889,1071,1298,254,1531,874,836,103,1036,40,1162,910,472,686,994,1206,508,535,154,700,428,924,908,223,734,1476,173,722,961,1540,100,1503,887,1287,417,564,1069,453,874,1058,1124,1046,696,463,1346,367,792,574,1255,892,862,535,262,473,502,1102,1184,1015,1041,436,177,1277,829,1255,624,553,865,1233,1355,76,1446,734,1456,211,366,1104,140,265,1485,1481,60,1148,259,1151,1439,526,667,1239,111,971,550,1522,428,1006,361,1544,1243,163,860,1239,83,1342,1406,296,267,1205,602,63,1081,1534,1240,717,1045,119,1274,1000,80,304,617,912,1257,297,959,1489,805,278,1198,912,150,120,1218,1005,201,1210,734,88,94,485,777,1087,936,695,1351,120,120,63,159,509,373,1194,409,568,861,483,1486,689,976,406,799,862,449,356,27,42,1222,1393,1152,432,760,611,385,268,914,820,224,973,543,902,252,277,1386,1131,762,812,447,1024,207,168,1171,408,407,985,221,798,1491,882,1240,234,1287,1304,752,920,57,484,941,357,1122,1051,830,682,63,203,650,1494,1108,381,1454,817,1323,516,714,1334,1519,511,580,669,128,1115,1402,1419,1493,1250,320,1536,1516,339,1311,1036,651,1142,144,1147,1494,178,848,1203,942,131,289,1341,136,1407,1192,378,51,1502,384,222,126,27,1343,51,768,56,213,342,445,470,57,1533,1402,536,978,1395,335,1327,1423,601,1166,1224,1014,705,218,1154,269,522,596,1243,1088,370,1140,529,494,222,1283,936,930,203,208,1074,1184,67,250,495,679,1504,779,1534,669,1227,1037,476,800,963,41,1056,514,571,231,598,918,1231,1456,389,1045,780,394,1423,1237,178,254,185,139,1047,1145,917,327,685,1280,951,1096,767,40,1268,415,1182,500,957,1125,911,1166,272,1019,1240,1388,358,984,1004,1421,1443,1042,479,1283,1283,383,1549,674,1027,770,1386,869,937,449,378,1389,521,427,664,400,1324,979,1463,750,1482,1082,116,619,1052,126,1038,412,351,644,450,1528,253,71,27,565,1343,1229,229,1163,1142,751,36,908,551,566,635,1124,1207,1269,1323,623,1456,592,1107,474,802,928,63,526,1259,251,804,1312,1164,1393,114,1003,931,518,497,804,275,576,516,1498,130,744,1285,1419,1441,355,674,1013,1090,1473,761,805,499,713,1523,217,608,687,864,1087,840,1356,715,493,1188,46,1211,109,1415,1123,964,918,1430,343,201,772,1183,999,1483,591,800,1323,514,357,699,1041,948,1513,777,483,387,198,1520,1314,836,1542,1329,295,340,1055,1312,481,1520,388,555,1388,878,1449,106,1402,1458,276,318,535,406,358,402,1434,1434,1029,607,429,351,513,433,64,44,79,792,517,838,930,179,567,1542,1233,863,1027,1224,670,588,329,672,1209,220,1020,1346,76,1228,254,217,985,1388,1424,1538,722,1294,1274,1368,555,1026,531,465,490,115,445,1458,602,1088,362,161,494,657,979,925,1250,514,806,1067,847,27,1109,639,1248,1039,536,1514,934,362,1167,33,224,1313,1079,1493,107,1085,690,1174,200,1059,905,184,1080,367,129,1033,618,1020,96,1071,484,547,1439,1239,435,52,808,1127,171,507,1051,279,1506,1153,88,1022,602,540,1180,1392,534,909,660,1380,56,1411,1283,1445,1050,1315,1038,310,1400,501,600,1425,534,1309,1052,1389,581,107,928,1080,706,902,1174,1256,1415,211,68,262,634,557,1042,1130,1203,1437,166,398,917,270,495,842,329,1061,229,97,683,1017,241,798,79,206,445,86,424,133,632,416,762,441,648,1511,454,1521,329,465,1130,402,708,417,1390,89,1073,680,1464,76,391,846,1498,799,635,922,1408,86,849,232,192,768,1396,1378,1070,1429,493,1144,666,545,194,175,1499,474,778,1284,111,453,293,716,1161,686,345,707,1194,927,830,454,341,276,1447,1294,687,29,968,398,85,254,145,762,735,798,1138,762,1497,1173,1454,1448,1187,178,949,734,679,547,234,1250,1305,1270,293,912,253,558,329,406,365,651,702,813,472,598,249,1121,1339,89,366,79,792,948,27,72,830,1251,1036,1213,259,966,874,766,320,1337,75,406,187,1227,934,1193,326,345,818,131,598,806,776,1538,321,947,1341,1029,155,1150,1511,1223,656,85,1372,135,434,707,785,1402,847,744,1113,365,1542,384,1441,716,1029,947,1351,1022,278,1469,312,1019,1076,1530,1193,1287,1077,494,1495,465,1124,1405,270,1451,1291,872,427,210,60,214,854,854,713,990,521,128,147,1512,1302,1518,664,388,555,1291,59,1243,1365,71,291,834,1059,241,1522,1482,1036,851,670,557,314,1007,70,676,108,694,513,255,988,599,750,1312,1028,1517,768,164,620,74,377,646,1116,1085,207,479,289,41,545,1018,556,301,906,1067,1200,477,862,1064,678,771,522,520,1433,1290,117,44,1404,509,1507,239,1522,998,701,902,166,947,95,396,1338,1194,1455,736,1452,264,203,737,1145,1506,33,860,542,657,704,588,1298,1447,1047,297,980,640,1152,1000,1401,1059,47,1258,569,80,1377,769,184,1283,1541,1014,522,532,513,950,1476,486,606,711,253,1146,591,324,740,47,1136,862,1281,1002,563,298,420,1027,1531,729,821,1012,780,953,116,1248,1308,135,585,528,1442,1309,138,736,1406,72,687,1403,604,1109,431,603,517,958,433,568,543,1005,1378,630,343,783,1129,40,1048,648,936,1159,1315,231,1144,1401,857,751,1141,423,385,1478,456,1197,1431,1044,1482,198,1440,1354,1397,1062,281,654,1081,202,1546,438,294,445,273,950,255,1217,1076,123,1435,1412,1349,1438,525,1273,133,1330,505,1207,532,1348,269,938,1011,234,139,334,1012,710,1231,1333,1320,698,1508,1243,316,1294,1314,321,83,516,510,1256,1116,363,63,1330,1393,967,265,784,1088,361,345,506,1177,394,1123,175,297,48,1035,970,1249,1260,827,916,544,1432,1435,140,1043,223,433,318,183,1223,1506,804,1457,883,1450,149,880,826,1348,167,240,1191,1158,1021,1218,865,1145,1125,1031,665,624,1191,1518,1520,723,770,234,646,152,258,1250,984,116,570,1515,441,703,329,58,526,304,967,254,1041,510,968,253,322,1357,952,213,158,517,1004,674,349,1033,506,40,1050,1266,246,868,229,1165,436,794,1492,983,171,1027,692,648,701,1040,1043,750,629,820,1429,1306,1018,1186,1264,562,456,851,412,28,684,1244,82,963,895,1065,823,1154,1360,890,456,575,261,1356,65,118,930,686,907,75,369,510,562,252,1180,1124,251,640,1470,754,67,1436,1215,1107,442,364,564,1247,1412,992,764,142,837,536,1524,575,52,289,605,710,754,666,1283,470,1421,552,809,631,960,481,784,1378,303,1512,1378,1524,1309,225,49,1450,389,1228,1310,1500,1233,931,793,1326,749,51,909,562,652,876,533,1018,600,1342,89,1433,297,708,69,786,506,1337,688,1460,980,284,79,274,1151,329,1518,345,604,1352,303,633,851,1439,367,1049,1524,704,191,296,446,1156,359,746,561,736,477,1179,722,70,444,264,269,685,556,981,1319,1176,1117,435,1212,1204,699,457,1482,749,477,1131,750,606,1255,220,265,1402,1081,437,957,406,629,739,386,853,414,640,862,321,90,347,1353,1125,1098,1460,1097,1348,425,1039,1328,602,616,762,674,842,613,1221,265,1112,1100,1303,1292,883,1071,707,580,1024,853,419,84,902,691,774,258,250,991,1253,1503,1428,120,475,1324,243,271,108,493,616,490,493,705,1046,484,1303,1134,1289,746,112,1257,561,1010,1422,598,262,656,1260,251,1446,1473,1044,913,522,1395,1100,1228,1217,214,41,295,357,132,1539,1545,719,1123,429,616,614,104,1362,1513,158,697,370,643,893,1340,590,302,680,1035,741,857,147,309,1544,896,1377,1359,1081,1431,244,55,929,1370,379,1148,642,436,852,120,651,1481,66,892,922,600,1291,359,412,906,1211,1422,1153,649,641,1202,223,452,791,864,1435,29,508,89,1110,37,905,742,49,475,1398,1304,1353,693,106,834,687,1354,1506,1385,1279,196,1138,47,829,140,1306,211,1371,1293,1146,269,798,103,986,996,1068,191,199,757,1217,248,590,1300,585,114,145,194,829,1134,1129,640,1534,341,1240,1247,1010,508,506,658,1541,1260,171,1372,54,264,1382,1224,369,768,1211,71,865,599,388,639,881,626,1164,1161,894,978,381,1269,736,251,1298,1007,367,308,663,38,1439,1265,57,1206,1265,184,1227,549,1457,1247,895,1473,957,834,1197,686,295,759,1205,971,1040,1251,863,1218,1551,795,96,884,248,1369,636,1285,1128,258,1049,649,1231,1431,428,1195,975,503,163,37,375,559,863,1319,760,77,1189,257,202,613,1271,41,1307,1266,1443,830,162,231,444,1051,558,1328,1065,415,1128,442,1274,720,917,222,102,474,917,874,115,1127,1083,52,125,480,1497,991,470,1230,158,797,1234,589,285,58,758,1458,699,234,590,1101,1286,400,982,848,1443,660,1074,181,821,159,858,403,266,26,611,868,379,1056,892,561,417,1112,86,194,661,886,886,1383,922,1165,476,785,1295,1181,1175,243,1404,259,952,1030,1442,629,1142,795,254,1318,1422,503,428,1166,279,198,435,344,664,81,1299,248,835,1433,396,1112,407,1319,142,635,1438,37,450,1136,1375,562,1047,543,1344,1406,558,1077,324,1037,1052,1223,1141,1532,65,1116,907,1484,677,1216,1360,105,1508,210,1256,305,353,763,1040,532,1360,145,1495,962,37,1236,342,885,1455,1535,829,76,1453,94,1374,1076,401,228,1492,1492,1427,1482,1412,1109,746,1478,638,415,1271,1302,672,282,322,349,305,1124,497,1320,1437,1501,772,600,489,112,707,369,71,500,1455,1094,93,938,1194,242,702,220,493,1397,521,965,1532,1422,224,1288,631,167,1203,317,980,28,509,1149,241,723,578,1179,427,173,339,327,1129,265,1079,1195,1431,313,161,990,782,634,1388,123,1205,1500,499,1352,87,1448,887,840,1494,1056,772,444,846,68,924,89,896,231,264,582,960,429,306,1073,508,827,774,950,147,474,883,108,1536,347,942,1276,1299,1120,1330,1272,164,675,1068,1176,1538,1033,952,86,1177,1019,1023,917,325,1488,109,323,1374,500,945,1275,1242,35,168,874,1053,967,119,391,190,927,798,812,1183,52,168,1087,1006,185,640,1314,386,958,804,479,729,276,1115,1151,1528,828,780,1237,634,425,907,337,1278,499,1275,726,94,1346,818,498,1052,1341,165,488,1292,1121,1478,957,904,905,298,1413,788,649,1133,366,742,1369,1373,1498,709,687,741,1366,101,973,990,522,366,921,1261,219,1083,625,1418,820,373,650,1227,1273,858,800,378,887,416,157,1001,1324,768,1114,1070,1024,1455,1150,1146,1148,113,1404,1159,36,680,1374,282,565,1275,818,343,605,759,43,846,133,476,615,772,808,411,1423,412,1343,488,1197,718,80,574,358,1200,785,1167,850,805,889,906,369,200,785,1013,1512,34,1011,355,589,130,983,1116,1377,864,750,453,756,711,999,1053,1243,1167,1514,627,304,1249,1465,937,856,214,1371,959,379,500,629,895,330,1230,1521,146,1499,767,1032,905,768,1169,590,481,887,911,1078,889,1214,962,1188,931,1093,839,418,1476,1011,951,1229,1356,976,937,947,1000,1081,154,1441,1233,1099,1427,544,1129,1114,1481,533,216,1207,808,1083,1363,906,1362,842,659,1334,1334,67,745,944,853,275,514,39,291,564,208,1537,726,931,1444,1212,197,415,578,1378,281,1210,998,117,1386,362,1018,228,645,901,106,747,587,651,1470,441,89,1319,271,815,1510,241,780,1090,704,1501,547,1513,699,325,1477,1443,1426,1086,629,141,974,1429,1350,511,1005,1286,43,881,996,1117,964,427,1199,1492,1311,865,1346,328,919,935,888,930,335,414,686,180,1446,535,245,305,1297,399,1193,275,802,97,1451,541,1055,1189,423,163,1061,961,62,200,244,1528,76,394,625,1196,447,100,84,263,1214,605,1425,177,300,307,722,1381,507,1545,499,981,1446,1182,547,870,1027,1367,949,367,86,609,1102,1318,809,263,1069,219,175,1443,851,1281,1531,720,1313,1084,1193,1522,293,1028,600,991,1037,1350,194,941,1075,164,872,1442,389,730,613,1156,1310,1518,736,1316,1099,746,577,886,66,968,888,962,1381,653,749,798,576,862,705,88,240,919,365,1281,909,1274,255,905,675,162,1421,1388,780,1037,857,26,827,1341,325,956,1226,199,571,806,936,534,904,282,895,1543,354,229,352,768,1314,687,951,1248,551,1544,684,977,27,1387,811,1311,218,1502,345,248,164,550,540,1518,607,1481,891,1218,358,682,615,836,753,725,1035,1518,1151,998,930,120,1074,1334,429,487,986,672,613,626,1301,230,229,849,1413,119,277,741,504,1336,1544,1226,1233,611,1028,1114,505,662,1312,323,1288,1006,513,247,219,385,829,962,1339,1466,51,1068,661,273,977,1186,172,768,1416,1329,1497,256,341,975,210,921,599,393,946,330,183,350,1071,442,648,846,241,864,863,994,407,1236,479,1151,944,1451,1017,235,1160,592,1163,483,340,1098,580,1434,1540,94,1311,195,1333,1364,1212,952,809,989,712,188,413,1035,29,636,551,111,145,926,236,395,771,928,453,801,228,846,906,665,250,1535,702,1116,478,62,316,104,1446,551,46,144,404,1502,1332,685,1162,322,529,691,442,706,791,94,104,613,1338,386,325,335,1256,873,1226,1087,1156,1152,332,1095,121,1361,1119,644,1221,718,468,1414,1190,777,1409,1115,1460,388,757,1510,923,1042,1078,323,771,564,71,1282,784,325,1069,998,1023,499,1418,803,666,1191,1120,488,981,775,193,1311,1377,1018,740,511,1123,224,1312,277,684,1515,1240,1168,74,428,1114,907,251,808,656,1465,546,739,204,562,765,772,327,1179,1091,36,240,411,188,1494,509,1435,649,521,754,597,396,583,894,1141,383,1110,81,1021,251,828,1346,1384,360,417,1123,878,1015,976,513,1109,1005,1522,1028,173,560,738,982,72,290,305,1139,242,1477,1228,165,883,1195,168,800,714,959,427,866,1208,1211,1300,344,312,1119,710,780,1004,731,477,622,387,229,1172,999,1468,301,842,1270,1423,1059,648,685,1288,778,1388,108,722,370,112,1255,94,498,535,790,765,1422,424,46,877,268,1287,729,793,927,677,939,436,1017,1125,258,1267,278,660,660,873,129,1372,642,259,943,1533,1022,550,1205,833,89,262,1449,1111,828,432,209,1063,145,892,1416,1076,1155,195,522,686,292,470,549,1295,38,733,1116,1392,532,715,647,804,952,861,104,1006,226,1370,326,26,730,1392,907,1300,445,155,1157,230,296,1246,885,669,1141,147,1261,139,1152,1389,784,1456,922,168,1038,824,874,337,78,955,1261,544,133,886,1482,1322,505,1122,125,1223,1231,869,340,1314,1333,245,1451,447,1104,693,924,871,1519,277,980,916,913,772,780,29,1294,1510,1303,250,379,598,1113,1074,38,370,744,605,274,1389,285,307,209,1478,508,1508,729,114,678,1261,987,107,674,585,1256,824,740,181,33,1225,1275,938,119,507,225,789,369,669,1381,1526,1142,787,238,945,588,1462,926,589,918,100,1257,1468,783,497,45,98,1509,1463,419,1016,35,1468,623,848,748,1409,1235,427,649,1262,306,324,1424,980,1369,191,849,370,975,435,404,392,1439,517,917,1203,1464,1179,1311,912,271,942,1509,122,381,1484,542,760,1527,1411,1233,623,762,1059,701,1129,1025,513,219,186,427,1079,1116,471,976,1173,646,782,794,189,1542,1034,1276,420,207,1053,733,846,1063,1115,350,1516,747,1400,390,39,206,552,1243,965,1197,885,614,362,1047,369,956,346,795,1256,335,1235,132,760,515,571,1340,1377,418,1214,1165,1230,1405,183,462,547,1220,171,1146,630,1356,236,135,113,1179,775,807,321,1315,1435,76,556,567,483,1175,676,272,1117,430,482,128,169,1404,128,173,171,847,542,822,445,161,1264,77,1465,889,425,201,192,1124,537,1127,1511,599,62,551,280,380,380,92,1223,392,56,1494,1189,1496,1114,1275,292,132,1222,1201,538,920,933,1359,869,877,1490,398,339,1203,252,91,878,1421,1404,63,791,439,324,1503,698,187,409,1295,145,1010,440,1400,36,742,103,438,827,1433,728,959,420,1230,1206,28,421,994,592,430,1291,1535,567,1470,983,803,1190,1202,1295,553,49,1032,692,260,813,1197,458,930,400,540,223,1064,1528,654,447,472,1059,993,78,769,161,293,1458,1398,348,1378,704,1222,773,1281,1340,1420,699,1448,1541,117,1521,610,30,969,139,678,1199,183,987,881,1230,46,52,1365,1365,561,1496,282,429,693,207,906,30,500,183,1004,1255,1205,465,389,804,340,1094,966,896,1378,1378,51,108,88,142,398,856,704,508,393,1476,883,1227,419,825,852,314,1096,447,981,1216,600,136,1170,259,823,1194,1347,1530,767,1283,107,1368,793,996,1504,863,100,1422,661,1510,899,1140,172,468,1141,739,304,1276,393,405,451,723,911,1295,1040,1476,557,298,871,718,517,290,1501,312,444,1417,878,201,1344,1343,745,1427,566,1468,1094,903,181,127,224,512,1247,761,1032,439,1207,1485,614,118,1134,216,1208,1166,1197,638,1474,920,401,279,1027,1290,412,755,88,704,1300,842,295,801,505,671,171,1009,1099,322,710,379,661,1375,338,1512,1264,891,1435,413,124,479,966,957,897,158,316,882,655,428,834,343,289,1539,1014,1015,1140,244,733,1476,792,445,1286,1521,1080,334,1525,637,1541,312,258,557,156,974,1159,1244,876,307,276,717,1003,1317,1071,278,703,1515,1374,1006,1300,1432,525,630,426,246,873,44,930,810,623,600,1244,1225,134,787,1133,1392,1491,1157,1174,247,976,1265,131,1488,927,234,1145,1095,583,109,1072,792,394,1518,816,429,1179,922,741,927,353,109,647,1210,492,106,1469,742,1143,183,844,230,391,1226,235,701,380,100,1162,371,1146,793,401,262,95,73,804,616,721,628,528,356,29,367,1083,888,996,895,1533,1101,310,245,1492,1164,827,1260,139,94,1058,959,177,1289,1515,354,1338,298,297,227,189,408,1257,62,852,809,1334,1025,1169,599,1106,1372,677,904,1419,35,990,330,56,1057,1041,961,432,58,523,472,1118,970,921,863,646,763,1165,131,497,782,1541,418,767,987,439,1489,612,254,570,598,975,464,283,1119,898,857,526,347,1324,1146,770,1360,1385,239,1069,807,1416,1034,836,921,84,1388,30,1467,1310,1420,755,986,1410,776,1193,247,180,1116,870,1527,877,1542,430,1450,621,1065,818,1005,1278,676,329,136,346,386,387,1483,1451,753,1088,1234,1249,919,1060,112,1218,883,1338,133,541,530,713,57,141,182,1011,1371,1415,1326,1261,1466,382,904,680,1515,1541,1115,1094,679,685,762,994,1157,1414,848,497,1004,1062,632,1143,433,896,1425,143,899,1481,1297,1403,794,600,297,67,840,452,956,916,587,630,1509,1282,241,276,1274,575,1124,926,1183,1137,842,1120,716,919,1514,262,201,1193,1410,941,476,494,580,1394,737,751,785,1547,752,832,568,1457,58,932,61,1220,839,840,130,826,1521,1184,256,984,1439,337,237,634,1471,301,1145,350,825,138,371,1201,792,1246,739,1262,373,249,1070,724,1551,937,1257,898,245,753,106,886,1061,383,1478,547,1444,1355,1185,616,66,745,381,665,1083,673,696,1466,43,389,1493,350,1336,1290,386,281,170,878,1363,661,1491,1194,1371,1102,407,1498,1038,615,588,282,572,1238,975,1159,1260,625,948,138,779,337,677,744,1539,1138,1417,1237,123,1511,247,294,359,562,766,118,450,373,1434,1394,1281,1286,392,858,1404,388,33,1082,985,244,37,215,450,1023,1216,757,624,185,794,293,1063,26,121,172,245,1129,624,132,1527,1332,761,702,1066,1216,750,1203,154,990,1147,45,348,850,1513,308,318,358,222,530,814,1295,331,783,1004,483,449,1158,844,1503,1548,1337,1209,876,286,1136,29,1113,1459,104,715,1360,1392,26,1125,305,194,1306,474,1097,1391,807,564,77,148,1374,372,119,611,549,918,669,942,646,814,755,645,574,667,1046,48,502,424,109,210,1116,1448,272,1468,1016,344,1337,624,1223,992,651,145,68,1182,607,558,688,216,1115,1365,1315,459,921,367,446,1330,1546,840,1270,696,466,1129,642,640,421,1479,337,1495,756,759,926,1481,1394,692,1528,1289,1023,338,1108,519,351,384,767,1145,183,1146,1362,894,871,222,1141,1537,829,1372,856,934,1149,189,1057,906,551,858,1300,371,162,1019,586,177,84,986,558,1161,888,504,503,1034,1548,335,32,1254,506,671,1094,80,164,383,1262,315,237,1179,889,1443,345,742,80,535,211,859,422,1429,1015,1274,1405,543,540,944,1100,1541,164,513,1111,509,281,252,581,1301,635,1333,1239,604,1473,329,1013,980,1061,1367,1080,1403,328,286,548,413,557,226,258,934,998,1424,153,519,1423,238,723,1348,1487,948,690,748,1344,511,42,124,1290,1532,1046,1350,1396,1176,284,1176,1023,34,826,110,488,1523,1117,260,1455,461]
s = [1209,830,712,457,1373,1078,976,1487,1353,699,906,1092,362,385,1247,816,412,606,1325,108,1404,1382,587,350,1421,1071,60,278,571,501,891,471,920,785,387,1028,444,476,273,376,521,1037,1500,54,992,218,1006,381,419,185,74,334,998,1113,72,80,950,1433,808,1460,991,131,677,1214,1230,250,584,590,764,1096,692,953,892,805,784,1501,924,386,881,278,684,239,1391,865,730,975,846,63,1267,1453,289,1083,877,1539,1066,699,1546,1012,1285,1380,868,1026,856,397,861,602,934,915,386,1217,964,863,403,100,1498,1289,352,397,904,1307,847,1526,513,1467,63,1194,829,1051,857,873,1467,131,1515,1156,592,212,1395,223,55,447,1397,42,1004,1452,1264,62,977,663,973,108,1292,693,1479,1392,397,275,1253,992,167,42,981,427,48,751,579,508,574,1505,659,1044,1211,847,1131,655,161,175,101,1195,121,237,1143,1359,702,189,1077,257,658,479,504,1260,414,633,894,1068,209,1531,1054,430,48,1129,542,596,466,1147,148,70]
i=0
count=0
while i<len(s):
    if s[i] in g:
        g.remove(s[i])
        del s[i]
        count+=1
    else:
        i+=1
if len(g)>0 and len(s)>0:
    g.sort()
    s.sort()
    i=0
    j=0
    while i<min(len(g), len(s)) and len(g)>0 and len(s)>0:
        if s[j]>=g[i]:
            del s[j]
            del g[i]
            count+=1
        else:
            j+=1
        if j >= len(s)-1:
            i+=1
            j=0
print(g, s, count) 

nums = [1,3,4,1,2,3,1]
arr=[]
temp=[]
i=0
while len(nums)>0:
    if nums[i] not in temp:
        temp.append(nums[i])
        del nums[i]
    else:
        i+=1
    if i>=len(nums):
        i=0
        arr.append(temp)
        temp=[]
print(arr)

g = [1,2,3]
s = [1,1]
g.sort()
s.sort()
count=0
i=0
while i<len(s):
    j=0
    while j<len(g):
        if s[i]>=g[j]:
            del s[i]
            del g[j]
            count+=1
            i-=1
        else:
            j+=1
    i+=1
print(count)

num = "100001"
k = 4
arr=[]
i=0
while i<len(num)-(k-1):
    arr.append((num[:i]+num[i+k:]))
    i+=1
print((arr))

nums = [5,14,13,8,12]
i=0
sum=0
while i<len(nums)//2:
    sum+=int(str(nums[i])+str(nums[len(nums)-1-i]))
    i+=1
if len(nums)%2==1:
    sum+=nums[len(nums)//2]
print(sum)


nums = [2,3,3,2,2,4,2,3,4]
count=0
i=0
while len(nums)>0:
    if nums.count(nums[i])==1:
        print(-1)
    elif nums.count(nums[i])%2==0:
        j=nums[i]
        del nums[i]
        nums.remove(j)
        count+=1
    else:
        j=nums[i]
        del nums[i]
        nums.remove(j)
        nums.remove(j)
        count+=1
print(count)
    

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            self.head = node
            self.head.next = current
    
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def pop(self):
        self.head = self.head.next
    
    def push(self, data):
        node = Node(data)
        current = self.head
        self.head = node
        self.head.next = current

    def dequeue(self):
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def enqueue(self, data):
        node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = node


arr = [1,2,3,4,5,6,7,8,9,10]
ll = Stack()
for i in arr:
    ll.append(i)
ll.pop()
ll.pop()
ll.push(11)
ll.dequeue()
ll.enqueue(3)
ll.print()

num = 4325
num = list(str(num))
num.sort()
i=0
j=""
k=""
while i<len(num):
    if i%2==0:
        j+=num[i]
    else:
        k+=num[i]
    i+=1
print(int(j)+int(k))


nums = [1,5,11,5]
nums.sort()
i=0
while i<len(nums):
    try:
        if(functools.reduce(lambda x,y : x+y, nums[i:]) == functools.reduce(lambda x,y : x+y, nums[:i])):
            print(True)
    except:
        pass
    i+=1
print(False)

arr = [1,5,2,12,52,46,100,4]

i=0
while i<len(arr):
    i+=1

numOnes = 3
numZeros = 2
numNegOnes = 0
k = 2
i=0
sum=0
while i<k:
    if numOnes>0:
        sum+=1
        numOnes-=1
    elif numZeros>0:
        numZeros-=1
    elif numNegOnes>0:
        sum-=1
        numNegOnes-=1
    i+=1
print(sum)

s = "01000111"
i = len(s)//2
while i>0:
    if "1"*i+"0"*i in s or "0"*i+"1"*i in s:
        print(i*2)
    i-=1

#Selection sort
arr = [3,6,4,1,7,10,6,2]
j=0
while j<len(arr):
    i=0
    while i<len(arr)-1:
        if arr[i]>arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
        i+=1
    j+=1
print(arr)

#Insertion sort
arr = [3,6,4,1,7,10,6,2]
i=1
while i<len(arr):
    if arr[i] < arr[i-1]:
        j=i-1
        if arr[i]<arr[0]:
            arr.insert(0, arr[i])
            del arr[i+1]
        else:
            while arr[j]>arr[i]:
                j-=1
            arr.insert(j+1, arr[i])
            del arr[i+1]
    else:
        i+=1
    print(arr)

#Selection sort
arr = [3,6,4,1,7,10,6,2]
i=0
while i<len(arr)-1:
    j=i+1
    while j<len(arr):
        if arr[j]<arr[i]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j+=1
    i+=1
print(arr)

Quick sort
arr = [3,6,4,1,7,10,6,2]

def swap(leftIndex, rightIndex):
    temp = arr[leftIndex]
    arr[leftIndex] = arr[rightIndex]
    arr[rightIndex] = temp

def quick_sort(startIndex, endIndex):
    if startIndex >= endIndex:
        return
    pivot = startIndex
    leftIndex = startIndex+1
    rightIndex = endIndex
    while leftIndex <= rightIndex:
        if arr[leftIndex] > arr[pivot] and arr[rightIndex] < arr[pivot]:
            swap(leftIndex, rightIndex)
            leftIndex+=1
            rightIndex-=1
        if arr[leftIndex] <= arr[pivot]:
            leftIndex+=1
        if arr[rightIndex] >= arr[pivot]:
            rightIndex-=1

    swap(pivot, rightIndex)
    quick_sort(startIndex, rightIndex-1)
    quick_sort(rightIndex+1, endIndex)
    
quick_sort(0, len(arr)-1)
print(arr)

nums=[2,5,3,7,5,1]

def swap(left, right):
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp

def quick_sort(start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:
        if nums[left]>nums[pivot] and nums[right]<nums[pivot]:
            swap(left, right)
            left+=1
            right-=1
        if nums[left]<=nums[pivot]:
            left+=1
        if nums[right]>=nums[pivot]:
            right-=1
    swap(pivot, right)
    quick_sort(start, right-1)
    quick_sort(right+1, end)
    return
    
quick_sort(0, len(nums)-1)
print(nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]

i=0
while i<len(nums):
    j=0
    while j<len(nums[:i]):
        print(nums[:i][j:])
        j+=1
    i+=1

s = "bab"
t = "aba"

count=0
sCount=dict(Counter(s))
tCount=dict(Counter(t))
for i in sCount:
    if i in tCount:
        if sCount[i]>tCount[i]:
            count+=sCount[i]-tCount[i]
    else:
        count+=sCount[i]
print(count)

word1 = "cabbba"
word2 = "abbccc"

word1Count = dict(sorted(dict(Counter(word1)).items(), key=lambda item:item[0]))
word2Count = dict(sorted(dict(Counter(word2)).items(), key=lambda item:item[0]))

print(word1Count , word2Count)

num = []
for i in range(10):
    num.append(random.randint(0,10))
print(num)

def swap(left, right):
    temp = num[left]
    num[left] = num[right]
    num[right] = temp
    return

def selection_sort():
    i=0
    while i<len(num)-1:
        j=i+1
        while j<len(num):
            if num[i]>num[j]:
                swap(i,j)
            j+=1
        i+=1
    print(num)
    return

def bubble_sort():
    i=0
    while i<len(num):
        j=0
        while j<len(num)-1:
            if num[j]>num[j+1]:
                swap(j,j+1)
            j+=1
        i+=1
    print(num)
    return

def insertion_sort():
    i=1
    while i<len(num):
        j=i-1
        while num[j+1]<num[j] and j>=0:
            swap(j+1,j)
            j-=1
        i+=1
    print(num)
    return

def quick_sort(start, end):
    if start>=end:
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:
        if num[left]>num[pivot] and num[right]<num[pivot]:
            swap(left, right)
            left+=1
            right-=1
        if num[left]<=num[pivot]:
            left+=1
        if num[right]>=num[pivot]:
            right-=1
    swap(pivot, right)
    quick_sort(start, right-1)
    quick_sort(right+1, end)

def join(left, right):
    array = []
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            array.append(left[i])
            i+=1
        else:
            array.append(right[j])
            j+=1
    while i<len(left):
        array.append(left[i])
        i+=1
    while j<len(right):
        array.append(right[j])
        j+=1
    return array

def merge_sort(num):
    if len(num)<=1:
        return num
    
    mid = len(num)//2
    left = num[:mid]
    right = num[mid:]

    return join(merge_sort(left), merge_sort(right))
    

arr=[1,2,3,4,9,6,5,3,5]

print(merge_sort(arr))

print(merge_sort(num))
selection_sort()

word1 = "cabbba"
word2 = "abbccc"

word1Count = dict(sorted(dict(Counter(word1)).items(), key=lambda item:item[1]))
word2Count = dict(sorted(dict(Counter(word2)).items(), key=lambda item:item[1]))


word1Val = list(word1Count.keys())
word2Val = list(word2Count.keys())

print(word1Val,word2Val)


nums = [1,5,11,5]

sum = functools.reduce(lambda x,y : x+y, nums)
i=0
while i<len(nums):
    arr = list(nums)
    j=0
    while j<len(nums):
        if arr[j]<=sum//2 and functools.reduce(lambda x,y : x+y, arr):
            pass
        j+=1
    i+=1
    

position = [2,3,3]
count = dict(reversed(sorted(dict(Counter(position)).items(), key=lambda item:item[1])))
ls = list(count.keys())
position = list(set(position))
index = position.index(ls[0])%2
sum=0
i=0
while i<len(position):
    if i%2!=index:
        sum+=count[position[i]]
    i+=1
print(sum)

grid = [[1,3],[2,2]]
arr = []
i=0
while i<len(grid):
    arr.extend(grid[i])
    i+=1
arr.sort()
i=0
min=arr[0]
nums=[]
notin=0
while i<len(arr):
    if arr.count(arr[i])>1:
        repeat = arr[i]
    if min not in arr:
        notin = min
    i+=1
    min+=1
print(repeat, notin)


paragraph = "L, P! X! C; u! P? w! P. G, S? l? X? D. w? m? f? v, x? i. z; x' m! U' M! j? V; l. S! j? r, K. O? k? p? p, H! t! z' X! v. u; F, h; s? X? K. y, Y! L; q! y? j, o? D' y? F' Z; E? W; W' W! n! p' U. N; w? V' y! Q; J, o! T? g? o! N' M? X? w! V. w? o' k. W. y, k; o' m! r; i, n. k, w; U? S? t; O' g' z. V. N? z, W? j! m? W! h; t! V' T! Z? R' w, w? y? y; O' w; r? q. G, V. x? n, Y; Q. s? S. G. f, s! U? l. o! i. L; Z' X! u. y, Q. q; Q, D; V. m. q. s? Y, U; p? u! q? h? O. W' y? Z! x! r. E, R, r' X' V, b. z, x! Q; y, g' j; j. q; W; v' X! J' H? i' o? n, Y. X! x? h? u; T? l! o? z. K' z' s; L? p? V' r. L? Y; V! V' S. t? Z' T' Y. s? i? Y! G? r; Y; T! h! K; M. k. U; A! V? R? C' x! X. M; z' V! w. N. T? Y' w? n, Z, Z? Y' R; V' f; V' I; t? X? Z; l? R, Q! Z. R. R, O. S! w; p' T. u? U! n, V, M. p? Q, O? q' t. B, k. u. H' T; T? S; Y! S! i? q! K' z' S! v; L. x; q; W? m? y, Z! x. y. j? N' R' I? r? V! Z; s, O? s; V, I, e? U' w! T? T! u; U! e? w? z; t! C! z? U, p' p! r. x; U! Z; u! j; T! X! N' F? n! P' t, X. s; q'"
banned = ["m","i","s","w","y","d","q","l","a","p","n","t","u","b","o","e","f","g","c","x"]
paragraph+="."
paragraph=paragraph.lower()
arr=[]
i=0
res=""
while i<len(paragraph):
    if paragraph[i] == "." or paragraph[i] == " " or paragraph[i] == "," or paragraph[i] == "!" or paragraph[i] == "?" or paragraph[i] == "'" or paragraph[i] == '"' or paragraph[i] == ";" and len(res)>0:
        arr.append(res)
        res=""
    else:
        res+=paragraph[i]
    i+=1
count = dict(reversed(sorted(dict(Counter(arr)).items(), key=lambda item:item[1])))
for i in count:
    if i not in banned and i != "":
        print(i)
        break
print(count)

s = "xyzzaz"
count=0
i=0
while i<len(s)-2:
    if len(set(list(s[i:i+3]))) == len(s[i:i+3]):
        count+=1
    i+=1
print(count)


text = "hello world"
brokenLetters = "ad"
text = text.split(" ")
count=0
i=0
while i<len(text):
    flag = True
    j=0
    while j<len(brokenLetters):
        if brokenLetters[j] in text[i]:
            flag=False
        j+=1
    i+=1
    if flag:
        count+=1
print(count)


nums = [1,2,2,3,1,4]
count=0
ord = dict(reversed(sorted(dict(Counter(nums)).items(), key=lambda item:item[1])))
max=None
for i in ord:
    if max == None:
        max=ord[i]
    if ord[i]>=max:
        count+=ord[i]
print(count)

arr = ["d","b","c","b","c","a"]
k = 2

count = dict(Counter(arr))
i=0
for i in count:
    if count[i]==1:
        res=i
        i+=1
    if i>=k:
        break

if i<k:
    print ("")
print (res)


nums1 = [2,4]
nums2 = [1,2,3,4]

arr = []

i=0
while i<len(nums1):
    j=nums2.index(nums1[i])
    arr.append(-1)
    while j<len(nums2):
        if nums2[j]>nums1[i]:
            arr[i]=nums2[j]
            break
        j+=1
    i+=1
print(arr)

n = 6
stg = str(bin(n))[2:]
count = 0
i=0
while i<len(stg):
    print(stg)
    if stg[i]=="1":
        stg=stg[:i]+"0"+ "1"*len(stg[i+1:])
        count+=1
        
    i+=1
print(count)
nums = [1,1,2,1,2,2,1]
nums.sort()
size=(len(nums)//2)
i=1
j=size
if len(nums)%2==1:
    j+=1
while j<len(nums):
    nums.insert(i, nums[j])
    del nums[j+1]
    i+=2
    j+=1

print(nums)

n = 10
i=2
count=0
while i<n:
    j=2
    prime=True
    while j<i:
        if i%j==0:
            prime=False
        j+=1
    if prime:
        count+=1
    i+=1

print(count)

list1 = ["tt","ymlmxswzgfjgwrwky","m","sptlmcdijdsywqlkyaeborjerjgspr","pfsbenffrarsleywfigzjeg","cy","mzrzpqzpcmznthjtldoxixvr","ighiqrknopkufowwf","q","zfkkxbbbjmonswpuoydwsrp","pxcunqlu","kxyitdrbnkngbdidm","eidmpivxzlnjhy","aiochdomqqto","pppxnyvwqmxhekdoheopipt","gruaoodyqclmztxwqfvxcdiftqcmv","ezrbsqwxbl","qhtlpdmwjiwvshy","dlcualtjzitrm","lttzxyppzqsddnleyhrrwtr","olbcoxoe","dzwhbfpl","snwgqh","moenxwpxgeizwmufgkyhi","unqmbftbgvoyfstobeulvvmvlpee","abyle","tezdwinrsimiuciyznjuwlctxbd","rpgah","ruhbpsxisdbwbvjpuezllajdp","vqwwhrzcqcccijccwikcbdyywzf","rvwooywwwx","boqqs","gerqdhe","dglhczubhmheo","cflekpdqfmziof","ryhxeq","tzrkhpwcrvkvqleobdapwmbhbh","fgdfvpdo","liqksnspsbyfaw","kmbxchexjfbycaxrvpnxp","rdijvcrelhcc","jaqccc","sbjwli","shnmyyqvmugsqus","itiruoigrsxxcxkuzaegq","uowrlaosvjmfaiojlweyfvlhx","uaehrbdowsxhelsfpxmzz","im","cbt","mifmzxpbqdgfol","ttpf","x","yjfwkjzgqftbocqgzeehey","uxxuevlbosj","uhhghualhayhdyoaznsrvesgs","fohviowvodtbq","hwyhfiqkzlyovepiwkzhfwlrywza","hbnodwnukxncktihnl","axcqwbnsrhkybglggetxm","ighymdmvytynnkz","eagbltmrydioadrqatpykeh","kopriuq","klujzrrblyonoubyzkblp","lzpfeyeulppuhscgbhtlmgpq","lphswbpeimsxhgi","hfrkvs","ttcwsjadcdfyrxolvzeqxwkqdsynnr","fgjpjnppqlevugjbvftlvibwot","hyhuerngb","dkzwxkymsongsxdmofvlxg","lmpzzmznsdhc","mwvgmzmyxfwitdgmkf","iffrmao","ndgkcizbkvumzmzlxqzulufnk","ufvlrkufwzdbsmtp","ckqqqsqgjodjwuesljkptryjcvjkds","kgnuabcrcshxihlhzl","gndwjnpyh","kuonak","nbaqu","dmkxnxzmureedlnchvezafxyr","zlpbf","uuf","ipjlhkdqecqpluljgywtbtxfdo","hwkzehtdigrgyzblniwattix","jbfjbqeydufnjndtbkl","plimghfsewdodaymlx","kunuvkb","hlmm","raqrtgesxygacsmtoddxjqdeknkg","epcgiqvvctrpfrhytp","hubvsfxtquipnyfmm","jbbprjsksrtbguockujlttymqzxpdb","bpejstdjdknpvayyfhdda","lfeepxgaftg","ljilplbiunur","qxjxxswcjhgs","gnqkog","uuwvicikcbktan","rxkbrqqh","ttjegqr","flotflku","hbygsyrxlurojfavyez","hzyooxmpmpznvnbvnkdzfqs","biexiddklhyxax","nrhyqpefhmi","kvawxecueveec","cincvqvpuxfnxi","ucyxyt","ajeudmewgsqu","ibojejvcfgpbjfdwbyelwwpyn","euqxdmin","ljdulbzcymlivlftemeo","l","uamnqpaksqyzpkla","nqmpmnqgypsmhuudospfnwuv","ugeoewxqc","uarqpvoucbygszdhmprvlyy","ltjpmoal","jfzgcntikvmij","umgpgp","lkuteqaztfuxy","nngrj","brwdoswsxtfdncudilixmzofe","h","aojeds","edgobnpjzybqpa","odwnasfykr","gpshguadkjeklryqtduekmxd","qrpyqadebkuzzofhkvqbfwhpugp","ozssgeyddyjoolwulodcerkk","hxmogniktdprfvtbrwozkwupud","xazalitftocoo","sidakvzftpidoozvemb","hlknbwig","zijqituuyckvmpdizmghdl","rzzawwlrfttlsvpkmeopvw","sgdfirsnbphen","nkeyroehfvwfiteepgvzjyevry","pczpoajmlhvkkmawkbpalsmvvvm","yeaxuyjyrxtrsfrvlwc","a","jcdwooajlrdswuxhyivepcqigs","uixegudsskgndlehkxgslrr","otgyzbuxrjlhoujf","lxtlftfvk","skgfasgfqlilnkqisaxmvhkwdhnt","xduopjsuzrlsabgxapzeuld","dzsndweobhzcakrueevdg","aklibpzclbpxlqfauxevsnp","tqdrovqozuul","es","xsmhrisrkjmb","s","qxm","tiyaczwh","cxkfyrxupgwztwtfequztu","ouxtsutdlt","vtzf","hpbuztstzffkqlmlelulfodsj","saiobwffifhjekxnortkxsogkgce","pbmrd","hdyzraajvfbnzvwggjvxpqzxb","tfvllzrgoqgticq","jbodoxiqetkknul","hqqumsnbcawjmfbcwprjzod","qihtkg","dztilrjzzhwmmlybfpmegrxnefhu","xymwezglkhk","fluupktpkkqomozjbtebccjaxoogx","gahnnjgqcuhhrkbhraenlplss","himzsnjhxhxaersjleptlehia","lsfgbkwguheafpaxffhfxbpr","qktnvhyqzrfekbcgknpndoethl","se","xvoitdqnxslptrzbbbgvvond","govqvxxqkvgq","knxnrmqxzgzxrxbmvjijmegmqs","fsgeiqyzkotqwovwmsgoufkom","mtmxmvemslsoikkpforhecawjpthbs","iqapcatbmjv","wrjbfwkerzwg","tfnzkpzqjeveuzynauprcqtsuyafz","ukethqmdefjny","ifuidehgebxfnjww","dbptzbbzisaripjffjllwygwpzrxjf","xpzboyyugirhzemuyczhwm","hhqxqffxxfv","hgoesyvhlqgrzzkbmkx","cifvkapnwhlwge","wzhicdsciqcsn","zxmieefjwihlw","xtxazeffclcexzmeaycjjmajshv","xqkrqiowhqtmvktkzw","sdcjazwkoaxzvfibezuobaapzxt","mfnxfzjfkhhsg","ezzemdjhnsfi","vqosfqzswjb","kvdeqxesnbfhjbxuweyy","frugxsadoonqjt","zbswentubjugaaazjopvorij","jbyqcqtulsgrev","mcmlolerusdcswu","joqlzhffhwt","tzbubujkseyfkyngmyxoggwjqfyx","dnhhkdkchtvedfvvqhvcyomraih","rgvqedd","rgcwuyvxcedojsqsvguq","piyi","ogiuntjpfsvaahppvbmvblmg","elmawzkeisceowvgqu","hnkekswifkp","fjlhveplzxjkboerra","qobibsgjpzeo","kzvzcmylggozqyuhdv","qgdygmxmhndsnfasrequy","cfikawuztjfgbjq","iytaamorcwdvsvbopaoibgimwdgoq","jazjsenkuhwxyadoj","hzfdtbkltppxifzaqd","ngwrwbitnizquzubcmbqnty","rsfkpeucjvcvsyzdxqovfe","xexp","zbmfnskvsprfkmnlceyhwnmmleqr","ayhndlmoncvz","bzlqiynizzxmalbwcqjjllrplkv","vwaxdwgyocqxcbeiragiujyz","qkgbyibl","smygecysrkctzdaxrnoujhe","wkmmafwgtuqax","ovnxkpueoll","ikbobzuxwqtqiysopsp","toefaqhryjvufau","wcknyykbdgdqfoiyxwykkjgfmmgeup","ijqjcftcefcvsobsnywb","zzipzeaupqnsuugxicjojthg","ancbmeoklxzocevj","cqthrpqqkoffarsvl","ypdccysrhavpemcfw","hcaegubchzymfiymhrx","dlttlinurazlzzohstawpzrm","zijxdvyeryowylzemzpxmmi","ysxoyobphudyfz","oigzvomuntci","xategdafpthfyimy","eqvozcnrrtwivsxulpthgqgo","icgnxvf","prygvdkn","vrlipcacfsbqpdorzcetfdifg","izkoaumsaxykmmxrmqkailci","tkukbvzyqmingifrsagroqlskc","xqbewkuapzsbxkmij","cbqhxfyddsljmejqlrkpnsywpo","wpatkadvzgkuzdex","ovbqoeyowayrgyzyghyzjh","zxhqqmlbwuwpmipheqdk","agdwzefqjefqxjqqnkgnzkarovbtsy","jqkyy","trwxntdkqugaszdrhlliuxwtdsdte","ovxyhvtuln","fepdap","loyolizemdjbjtswrmevpwx","ggsifyfxlcmczbbsews","keydevouytrexndpxgjeklro","zikcykvdegerdxrpludstkdedgpvka","rgcfeqtnurfissqbzrvnozsvglgouo","eppxarvxswjngpgaoqimpwbnn","zroawyqqjsen","wiedrwfuhku","uwunzghrwfmubaiskqkgdpof","cwzyawjshlkamlrfepgahy","wxkqsbgbybxiundraolkidmq","rjoiqdyqcjpgmmkdhwzejjnbhszcce","irppitpnfeaupwovgmqilhxvdnhx","yyuptiwveukajjqy","nviswxjohavescjh","vuxujjgrnu","vvnllmcnhumomimsgcapoalroesjv","kxkmdhubufprfcaqiesgeskpk","qzsbqpkhdwxlujevptcuybxudzp","wjvvhpvhzrwskfqjawuxrsbqiqhugq","mmmmgivtylfha","xnfyfhqfnaysweif","lftckbrjqgugrtyyekabfpgf","gzfkwfkugdlohilycwgitmrbjx","huzlsrzvxuvuatuoohtcmijkc","lhjqhozpjqamxkkeyyrefmfyvso","sekitazbmshnzwsvsbiucrm","mxqxrhurfwzttcvohjmuxqarex","upxlcmivftjaowwozghzstlvciblwa","zjkkyugzmbtldazxdtsugsx","kjampmqrbbadf","wupxdaex","mfzizdcrhejnfntemslpmpbrv","mlcjbhsovogdhrddwmege","ftjbkbwwbmqhidftjow","lplvmrrspw","cnpadyfbsrscwyjnszlmapnjlv","hjojmzaaanwgl","yxhxgsinachceuhtdcmy","pxwllxjvcqepoqlccb","uuicetphghvkyeuerlipqlkmg","yyotfcpvitma","txzinypknlytydalfuqftkxot","aeqebtbstp","fsmuvbntbdyr","lpvawbrntrwzaxospvvepcvvdsn","hgehk","pbfmvhlxauzuwkipau","bvksdpuahbraombxpodjayaj","fhiljxxefqvjxpinukhxcohkda","xvzafbijvagqtwvzywqlvzdw","mdkwgbuawwzyquwegq","eyju","yubtvxrurykefarjnbz","uscrnqvolsjwbruo","kxnbmeusrvrmeihlcfhbfmzlc","qtjopibbhwfgvbseemlyahizea","yztuaagcvuoolimkjvxwatvp","hnsriqceqhxszer","vfkmxiewgzfxejabo","bvmpabbjscjyvqbrijdmnvwcp","hmbowfjzsuebtwdyzuzzkxqetipfre","xwguauoyuyukrsogmk","kwbmcubzosg","hzrcbftnoeqzdujzphanrmm","ub","dejdxtjgmwoiqtrhwoqiqa","ntridmgeuzhb","vkkhroagkeewav","owfqaovcjpvpqnpgrcgofbpcp","shwmezsrmrkygfbsmloajs","fiknafypwglwc","utqghqkavkuwlewcy","limeivcruynrkfcq","hwfrtdkgsihtrevob","lfuqmyrahzqkksqcjes","ztdtghnsgoerwp","qxtpbzjikguzoeiwbtb","zkgbhfxcoqisxvynu","awlkxp","nuvioxoftodogtkaailbpdptsatg","vlrrafhtzqss","hrvqewtxvljnvqbcwg","syvijkrallqrpgsopka","olajgsznpe","ryqgfxhdxsshfykugurhlbd","kqmvsexjvvnhnlpl","eohzhcpmhuvllout","ywspqowuqlcyunbqlimwngfxelfz","qmtjjhghsvbkkmxqkzufyxfpzzujf","yuzglufiwpsgtmqjoupzul","twndfgfjzhnrgiouciaa","crftcllsqkaxarsgpchaetgswujela","lrxlwodfshltzquorts","vjsjmoiwxcxtdq","uvvjnpuooevtcdz","cqxwconuyujrogmolju","zovzxzkqejjlhacuazaordmagpglun","txyfcikkpjjjusiuvrtagsuf","htysagzjgvjlizvonlqt","mxfkeckppjywrzfyuimcyem","ezisrxdvwexzzgnx","chebkaevvrgggqyhfujstzgiwzxrsu","kwxheyqmeiiq","tpgwfccafzbzbhrstnhlwaevaa","cxdgrxpoo","jzxlhlvmptbtxwwsppomorghhuy","ygvfcgsvakzaaalxcjqlgblcsigy","psrljsjdwuhqoazmvkirjgrppmurem","ksbpjxizdlodonhfbvss","raowzggriibccpte","kesiryhpas","ptsprvmhntujnwoseyavujzfc","uppoeskbbeawahzu","wzuxduheaffxl","jmqomtmksfajjtzbfrrsg","xcuewwbbhjqhktwy","zvjkoufzudabvvfmqygevutsi","alsfnvjualdffcsciabpzjlfsh","bftkbxnvpy","takwmclgdtuqpxbxpfgydxyopgkpnk","qxmfsobbzybrx","yvj","qipaehcfof","bvsaoqqecsiktxrfqmcr","gzrvh","thgcmqndebjwroeztebctmdkxgll","kyvmufripmexmhgl","ttxepmhwbgbzypmuybyeaaoqwqka","jfosgwsoqynnewzydiz","vpqinqlylpiqxlvaxirmxpyahdew","tnfnoaqpcyfybsxywkiioo","ndclpgzajmsibmz","xjqwkayccpfstqglebkhdk","vhdadutwcmhyugtjljlnbgtjh","hitimcysgpsxs","yzvizqequnckaynxhsocusuji","vxpxemgnvkdtopmgcqq","zvmopohgcavuskhpyorghggwfze","oxuyylozmnuqhdrnyiwlqvi","mwohrfmpfstsghjazakuzf","anfoesoelmfsjxraatwztrzeuvh","ypfykmezswsqdf","oabrzjdvxrjgcolklajadgdujzshdi","sfssrgjdgtfmcgrxifmvust"]
list2 = ["lukgfhvzphndszxuu","wjuvgbvhiktyqsacjtyj","jeodsxoelkczggbbtvxbtlp","gtthhcfvmzjamnkxmlkf","mggnscyymkzbhhl","kbxbjcvlndl","elqovvhvbsmz","qknyqioavygbvzvynlct","ejhqwqnakghnhot","pshmnjewjfywtznpk","biq","jigmfclthonqp","fbubljitauzrgpxsegytyklzdo","yrrvueuvz","lemzr","d","wwmiomcgornpnjvu","ottyflggzfmtcouvdxusiphlqabejv","rcpyogdx","khleqhbaj","fqdcfoqra","omzllqjowxovptsxvhmpt","ekqvfygk","bacujeberpw","nguieyrtcxjyslvtdlrrsseertfs","fzniocjpzuuxnwwkaotseddjdhvqy","vpnzccwjgatsi","ndzprgzwfdpfdbteaiushwqs","hyhkvavecqfxjyq","nwykqd","tivvjiree","qrttqwagqimmtuenqsbhdotil","gttdfyflksyvdofzycaiir","wazmep","xsobmxe","kvqmwhrsvpqvjcughiirovb","nirpnokripyakcyhcbcsxi","nswfgvjbzqkixsfphpd","jod","pngc","qe","fydsrxrofhzralfrdssgjxzpmeu","tbkbvnhbelozqdasqibgecxagfeap","rywrxli","xusssllpjgvf","bakkzqmrvrwjlwtupzrsiwbhnlfw","cjrayjfslfnuq","w","rkdbqqsgpcjmwikfeynqtbdyir","erniwixhftjpigfgqe","tvrqdgvvxl","dvzdfoaqbvrhdkasoc","uay","uegcvwmgtxmdrqjm","ixtifakiluvz","xlwcgdyyrawlhjfnsjekh","bvhvizthdfoxxfakngygm","onxkskxkrkxevesdemncaphmao","gwzbfavhxkahqedofzmxthfys","juiq","qpxnaaiygn","xskikotkrtcmfrkzipcg","ixpadfrugophitf","meqilsxqwwdxsbdxhwuykhgee","svjnqdl","ghibpasmxygfnb","xrum","hqvjygbysqhmuliejnfhrvdksvj","mxuefhqsrre","hfwbgbziuaxfqwglihpxinlzonwslw","qxfgsgwvapshtvhujksaphbzaj","glavu","gclqhjfywelsamicqfprgmep","wiuay","aqpyysoktbvdfyy","szi","ezkrpbzxtqkugqv","yesofvitaddedgzqlhkf","psyjtsftxbohwieemuqyqcmxmqbkoi","lcqtickcvpbzskrtjrgmbxcn","ooupjfmxtzzghhpbtfhdrnzwbay","igryxtyxrsciiteyykpwsejzkoudls","ngdxa","pgghiszypqlsqapw","juyb","hdypcofnn","ltmiloashemqqyxrrmrfigxtz","ngjjqgokcgxaysi","jgqddgfqtesfmijlnmt","dgkprzspgmxncfrimiv","eusookwietituirowwtwbfdrpcfkj","jwerlwszrqjco","eiephnrdeqrzmmsiz","yxmqw","jeixuxwksrgattabh","bzqbpgtuysksrgljopibyk","hfixtzswlpzmcauiwhki","zvxjsmkcryfafhyrjoeymwg","rxyzkxczdgxubheounure","bomoysvocabceeauvobofltf","fiwozzuztcmtxnj","ndsgskwqjwqgwghrfrviqtvn","ql","wmsahdmviukfym","govxqung","ebajmltgtpj","rczedbgzfwztbrpyhuzscziwq","zjfcoggrvzjt","jrbcqxnoxlxdtkhevfihgbsc","pzzuucthxysonvwdclxi","pxufhfjteuhnzw","dwrfvtcotfefapujit","tleqbkhvvmkjwghke","rgyqabklalhefdywyuwn","lhftqpquxefzwgyuz","zieoxszmgn","mcj","ivfrpdoyqcmxya","xxtphbtf","gzjvbqogsuqvdjuewi","qpyemyekea","hxgrxkcmuajbnbmnnesnxfiba","mr","ahptxezuyxig","bipxskuuydjguuvqpouoclcxg","erqiejjtcwrgtdvmpmr","ovur","pmpphe","t","swdeosuwqeynspzdqzadmtopejocg","hcnarsjqc","vijzmkbdzu","k","nzbretavyrrby","lfcknoeld","cmdpmvasomwasfgfjyitqjr","vwfmsbh","nzrqtdm","wbhhtmtuiyqrr","drfwehgbc","toniqxic","wrvikxgymuekjufrmfpttxzhu","beiompq","tqhazkkobqo","qmrbnhrbprhlbtqotofgps","mdesjgnktbguginwmfz","ifbzpvykgswhnpaarecwmzcp","joiwkuqzevkqzekmcvynekvdvnfe","dagsoucuafxxbwkucctmrl","yoll","cty","ircleszyobxrwlfljyuwjgmxrcror","pkidfteoxwseosmoox","pumn","qrlr","nmyijjdvygqarjejdkan","akvuxbobyikzdpbylmt","ahpzluyihm","vjyaytwmlepxxpsyf","ycnubuqxcuaixwpnwatyeltiscl","fvbcykmjpvbjm","tqdweyhamvrr","bcjtmymzuafhrzzhdwx","xiamvhcbeti","ahillprlywqazflvnolvzapsywnr","ggwbjytfhvpbfwdfyjuticzpl","jlda","hkmcmyfjlzkxvsvbojkhtrzunoonqx","rxkzvmsyqggzulc","vvotkltcrcxqdtajgdyyucos","zf","svikkvfzneghmd","uudrvnhsowhfyqleckc","rhrtdaqovhodvherzvl","jert","jbkpsxfhtz","tpntjtrpmdixizyufnar","ozmhcdagffcuatcfwvexkhvmxx","ixxtfevrgzdzazazmdtcnxs","ilmuwlgufseopcsalajopfktdag","ic","quldbzqkv","zzznxpueqvbzqjbsdryvvxevvpgqgm","kkyahaqwtchrhzxsjpz","zurhwpuwohlrkgtglrwdrjp","ilpavqasaihfxovifhrgw","wycees","egqdvriwqvfgo","jxqrjruibvnwu","yvg","okkfan","vofywesozpcbicdvjfkarblyvamgwp","xzcdfhaqbybbeiqithdpfbpyxaomnp","fgkixdogvpuomdpcmdwc","uqptskmgjzaupsmuhchqbkgsunv","awrmmnbvfrr","ogjedtdgzkguuwwvlek","tjaievlh","atewfh","hzzycyabbivqwzyzoflgkkvmsjntgi","valzywfbipdkoinudoygrkggvrqpta","gerrltdkyhovccinxrzddakg","gxcvqacdicoyluultv","abvwdprt","pcvyxdndhxhkpkgvzqligv","ibdifhzewvxe","bemh","vceqlinqehb","pcxnm","tzgtjxzcvcmkyafyi","gzeoncreoxxhihgi","vfrcz","zfvqqzenzlpvfnvjiebeksp","eggiiguelerjrjqnldwlqynce","idzbrqfumsxzh","oiigypiajdumxd","quultahiwjjjhglnhjfvsn","umvpjkvsbqafvos","hwxzoqfuivmx","lopdgvqraroalxmtgo","mkqwrozeasy","fvtgthauirejp","adrishxrrakbymujyhybukaksqako","cpyaxrgxzqzd","kpkjmczgkrncoiaseujblttcapafi","qxqqledvinyldkexjrlhuc","qvedperkfbihclqnktptbfqnvispyg","iddfyoqvfrmaebcznesd","dufrqlwxnsstamgykxgopothviqbmi","eaudalgibns","wdvhbmnjwlmdzakyagbpyudbd","cebqiuefwcmyxogudfvrhsko","qitoxttm","weqzatuzixwtcilieiwrgpu","pkgzgjitnnyenxsriobgoclqm","pvdsx","gjjhym","vrlsqnavivjezfbmlasvnfppae","ay","yviqhkt","eaafmgkmvehkpo","rqkgidjsiat","jmwwonyxicnayxursry","zakskyquxrs","czbnvcmpfsfbxjczuigrsz","frnproerfhikhiimkzoxarpipowl","tuaqqboxivgvbvztog","kmhonsugrnvwkdmqqinqbehn","uwebakbvouyzoqvfqna","tlahsqopgqgvyhiymvxvmdsfw","fytrazlfbbffwkkunuemkcxyeqalbv","ldwqxohm","mlgsbjrfsgwlgujwqjbw","wgyvdxitdl","boaavxt","vsscmtnvdvwweud","guzorktskrtmfxuopcbmyatz","u","hslzvtmmx","mllspvqablhntgubd","jqckujv","wegvncc","jlwitntwvwpmyiyyrahhvnu","jlgjmxworiow","gfyspy","zvfkwlbpqmnrcgflc","peeta","ykcingdx","sbdxynjnkbwxaajyponvzkzon","xjbzqvhruuqyrxr","ltcvztsmxwgqrxymgc","ydjnaonwjkbvsiysefcyrqgjqbeph","dbhvwypiw","ubsvfdzzvpjmhlujo","kghexntvcnc","smxmpovd","htlmxuzwmemyeprtuihuyehrl","tifpshkyyfz","qkejdvjgcocpfsmjhmpevae","mnnwxtvnzbymek","aatlygcyknnxmezcotqttfzxftntek","ijalnzmkcdyfsiwwggmbezxmsjpz","sz","etcxvxyvbpysnxlgimssijehcfv","fctzcrbxbindlvsbruqwtxjo","uwqba","nzta","gf","qvlafropazglytfissukgcprgc","syarjfzpefvdiyo","kegczncp","kapqgczkzohtjtvlezxlyi","ygvqbbcoawhuhkqiwrdmz","wctukgtfvrnwxmusarashgpteuz","slzkazpagckwdenpsglymvsmuz","yzjsvarsktamgohtntrpp","pmwj","hdgbzbok","apocjag","qgmqnstukjspervoox","cmyqiqdfvfhakrsruekfl","vqsfzhuvbmlbze","pbxavkqhongpasfhox","zjvdphpzzve","lobjkzrmugrvcmk","gjcoyoqwqdk","wcgiufzldphwkduukjdquveib","rneympfghwjsvzaw","icqmvnwdjtwjkv","kmri","zlmjztyfnicepnvkoulswa","tgkfhgp","ebghxamukquf","ymbhojhcssco","ekpclqdyouhdya","fwrs","likho","jrobastcxnel","xahgsfzkeyenuts","gtsqdzrqqgnsijasieeiehvg","qrixocsoihedmvpf","xpjqllxvrhwrhflxd","pefblawfoaczmuvgbo","kablo","cuarcbazoi","wbhenigtfzelyfrngh","hisbgots","imdqvob","znemsneyrobbdlvnafbmdtcv","jrwkkzpgtnqrd","mwljadohvyeazfnhjvx","zozkxjuaopfszzk","ptdrnzuddcuorqbqzwrlvngsmkap","rh","qafjyvoju","xuqtxdnavhnbsxzuiqcvxrlhkr","putvgvsqtfrbcl","ibgyjqjqgvghyfgvdjahzxukjlbvzv","matunkznewjrqowokqfpiyacqrxq","ibuiacqcojcvyqspcztbjmabdqw","wgowwulnglkzxeyy","igcmvomnzi","fpxlf","ywulwfkppwozgvhtct","cvfnuibyxdaqejycrfjly","ghmbdaqjhtgiecitqooxuclezx","vw","dijxyd","spt","vhinhtuzrpbjitemoskoukojfj","jxhqmihjq","fvjpz","wincnzcdumff","kgr","kxlqwxvqvbteq","kbimhfetqhocthhyams","fiaqbuhxrziynkzvznjuupiqy","ewxqumcwvxlghwohgycq","gxhkpikkstucheihxrfgmpxgri","wwcguoabznntaeke","pwe","cizmywkpzlrittzfwrsvtoomgxwni","odvkhtrfwrpzibkidzaqdcbbbused","g","wjagjzezootium","dmzoxtguccjox","pbu","vtqpkjrplhxihlvfkncaxi","wfdvejqimfvunjldttwtzbyms","mgsbvdxvzbxehetrcdvv","xotzopcdlddwmdxdeg","mxzcvxneiroyoecyfko","y","n","eocl","beszsqsfemgtfipgjvgvwye","wofzxpqucxabywfjdivcpxz","yrkziunj","saqhgomhjmltbsxltgeoracriv","hndclklsstpbmvtyecbo","gfbuprwnoksbsknfub","znaylpg","psjavbogafyeuea","oaxyr","vcsxbzri","plyxswhlypxurgwm","hfxrgtzkfonwfohcqcdcwqxpqxox","lnroixczynpsssqdurfsqxfhjnt","auaxgmnnfrnrhypfz","mnsggibecipmolkr","vjyeiukhfaigpv","pptiwqfqpamapm","lizbmxovptpcmwymjtwakqxrnpodoq","ymsdqqvzolrcws","bzblrbnawn","lgmmlyrbtbkofufestjrieasux","iqhyjqifyx","bwagxaajhcsqrtdcwjfbvowzkqcry","qwsfph","kwqlkioucosaqwovcxevycprn","mmeltnktryvpormcqrfm","cwddqobkbewjeiothaycvfsxgg","stzavalphrqmmgyl","knkihawunfobepvbug","ryowgmfufm","gntleif","txffoidzwhhogimirfnwcow","osercemuzinmuqujcth","gacisrdkkesnygwmxefzbkglqkein","jta","ktiisxakxjsgssyznblffrlorvj","nndnt","uzbfaxkocqwklzanucy","zqynbaau","zeghjpjdsyzijnrhlrrtzapcc","cgrqqtellrfdu","dddjtluxrzvabqymawohkghe","ngjfjby","yfyvozzsb","kqxvqeejjwozaexonylweffewhydy","mixphl","paqzkfhurempgpimesfzzedplnubt","isnbtigafwuj","isngrmeivpnvyfnolemaplrhifiei","kafihqwvcnlqyhn","gnyjyzwukvyxpxbixviy","fn","xysybsszrqvjfot","pcnidiakpmrsfd","iirbiviewrldvebcoikcczayls","zazveqgjurxrciqcaib","mlzjzntjtotxa","gjunjqfywj","sdartmbugpieahhcwbbfpnbnlhdkvy","hbfujhfk","xbliovle","jdlvqwk","pcricqvtulqqfmcghyydtdfibmo","wgtgtcnfganbjwob","tgmnyyjdvejhk","ymyahklayyfronpsbpjxchg","jamlgxdijfcqanvvrcclffwsppmkbb","laiqoanffmeoslxjgzbfacwuajsipl","oaxzvr","wzgwavmkt","waj","avudil","lyehwatmyk","vwfd","fysob","hbshtjopwjnurzfyrrrmmkiy","xommcvvbwlaj","kvpcxysgnlgivshhpfmqpiaqkqb","qc","drmhelcxcg","pnffvnwrhnlhunewteppbqjol","lazmsyclqa","icnjnuvqgmprgwc","ndacfbv","xdtugscgjbnfuwxogtnbhxwjz","ewjxhnmp","gujmuzzbvsgzejw","evqrklcxgxdqkisvfgakhkmkoik","qwj","azzgsuttjj","ympdvitsczwdhxylusdhbivocikw","sxkygzfdohpqdmybnjpqvjr","eqwynrvlqh","aqunhvdbcudwbduuflahia","ljdslqaivfzhczbf","zxxvwcdlszfjphldhrfvblpakj","hv","xlirwzok","wk","otsyjxubiobajcfnh","vwve","kuhgxpmahrtzreknawgdfctodo","dlf","ujhml","ps","bdcraaqaaxusvnkrrrxplzudbl","vloqkeqznietcxtkcmj","qahxofzboem","xwqemizptcavrd","trd","qxqnmljjzlq","uvxzdyiuld","aptwscecfjzsvuk","jhhsgldmicsoboogdjrjbsxofmc","be","airdvhjssgbymc","jrabmvtbfxtxgocrrmgaazakwxv","uieawxkhkfjhfkzkfche","hdeedhdmaak","vuioh","rfiffadb","tzbwcxxwnabqgrasfg","noeahrjqbcculkrosvazd","qjckctqhasjykliaibeazx","wbogcpjp","crvxbznrvggnooioim","uzkwbdccovdtzpxgtyqjo","wqpgfblpdrttja","omyggchtnicqi","lmjgaahecand","yb","udjghqivyqzei","wvdnxeg","exjjkgdzgdp","znbqzxcyvtokkibmizwm","zsdigazu","gokorkmrncdm","bjllahmwmyzltxikaiiegrdpkps","jqbntbubwsyydc","kqrnhhsblsfuuadgelid","nbwonvyfftxlxifwq","atoxozzrviyafxfgzlkpucig","afrhhitwqomffbfmskfszur","yoakflecltptt","yxremwixkukmiwxq","uarcmh","yxmauxoddlathty","mcbrvfmwwcl","yqpdtekk","xigfajgp","aebjspyjzoytzwetdohjuylpams","nmpehaeouawcsidbkpbroispabpyqf","ytrimxnoihfafpsq","jxdrejppbgpvolfocboqcfvbkr","apkxbvq","kmgpjsbzgottvhmplmzbmtxsofdhtt","mthntbkqfedysvvgmitakeke","dvq","qmdlgxstkirameaoh","stcvmuuwv","xufoxmwckynqcphlkiv","nxegbfphvwvbtjjipsdt","pgmeiusqkyywdploaulobinsyy","imkgclqsygxsjcpwmfj","eeikcgkwxsrrzddocdbfgnjwhvb","qjthnfiiiujwh","nwrqjxgdmezankluvrj","gynxnfyjyukpmguydp","oogbdnrppt","vyxfrjyjeccwzl","omht","fsoma","uyvarmohopfpnsdkvbkvzy","mvz","ixyxcjy","tazhtiqiyxzbetdqqsqbtgh","bb","ky","wolkk","gxvhphjfr","etswuhhwobt","lbogmbrapntwdpxqzoqvthvorjh","lazqcjc","frsbm","higxphnvzpiqdzxtialuwfxxyx","wthpyqlpvybirkaozeweudkpiakt","hehsuxgviatzq","ofgycixomi","by","zgwfiycyxrrhisbzkijn","atlozwagevmcuclisovnxwhnlooqa","oabrzjdvxrjgcolklajadgdujzshdi","ypfykmezswsqdf","anfoesoelmfsjxraatwztrzeuvh","mwohrfmpfstsghjazakuzf","oxuyylozmnuqhdrnyiwlqvi","zvmopohgcavuskhpyorghggwfze","vxpxemgnvkdtopmgcqq","yzvizqequnckaynxhsocusuji","hitimcysgpsxs","vhdadutwcmhyugtjljlnbgtjh","ox","ukhpqmsp","tnfnoaqpcyfybsxywkiioo","vpqinqlylpiqxlvaxirmxpyahdew","jfosgwsoqynnewzydiz","ttxepmhwbgbzypmuybyeaaoqwqka","kyvmufripmexmhgl","thgcmqndebjwroeztebctmdkxgll","f","wsjrwnviiwbiltjyfweynqrqlhahdw","swrosmbskrormwnttirfnkh","cglaboshwlqunxhzdvcnrffrcnbinz","qxmfsobbzybrx","takwmclgdtuqpxbxpfgydxyopgkpnk","bftkbxnvpy","alsfnvjualdffcsciabpzjlfsh","zvjkoufzudabvvfmqygevutsi","qucbscbd","jmqomtmksfajjtzbfrrsg","wzuxduheaffxl","ssfymbzikhtrboqt","ptsprvmhntujnwoseyavujzfc","kesiryhpas","raowzggriibccpte","ksbpjxizdlodonhfbvss","psrljsjdwuhqoazmvkirjgrppmurem","ygvfcgsvakzaaalxcjqlgblcsigy","jzxlhlvmptbtxwwsppomorghhuy","oguezmqs","tpgwfccafzbzbhrstnhlwaevaa","kwxheyqmeiiq","chebkaevvrgggqyhfujstzgiwzxrsu","ezisrxdvwexzzgnx","mxfkeckppjywrzfyuimcyem","htysagzjgvjlizvonlqt","pc","zovzxzkqejjlhacuazaordmagpglun","yq","uvvjnpuooevtcdz","vjsjmoiwxcxtdq","lrxlwodfshltzquorts","crftcllsqkaxarsgpchaetgswujela","qvqbbhiocufckmeyyvr","yuzglufiwpsgtmqjoupzul","qmtjjhghsvbkkmxqkzufyxfpzzujf","ywspqowuqlcyunbqlimwngfxelfz","eohzhcpmhuvllout","kqmvsexjvvnhnlpl","ryqgfxhdxsshfykugurhlbd","olajgsznpe","jyxoaphhwgcbracqcqapqlagyqcjc","hrvqewtxvljnvqbcwg","vlrrafhtzqss","nuvioxoftodogtkaailbpdptsatg","hikvdszdonstggpwxtxwikpztevt","zkgbhfxcoqisxvynu","qxtpbzjikguzoeiwbtb","ztdtghnsgoerwp","wrrbnaueyniz","hwfrtdkgsihtrevob","limeivcruynrkfcq","utqghqkavkuwlewcy","fiknafypwglwc","shwmezsrmrkygfbsmloajs","owfqaovcjpvpqnpgrcgofbpcp","vkkhroagkeewav","ntridmgeuzhb","holwvhekup","waswwrdqxqdtzwfmm","hzrcbftnoeqzdujzphanrmm","kwbmcubzosg","xwguauoyuyukrsogmk","hmbowfjzsuebtwdyzuzzkxqetipfre","bvmpabbjscjyvqbrijdmnvwcp","vfkmxiewgzfxejabo","hnsriqceqhxszer","yztuaagcvuoolimkjvxwatvp","qtjopibbhwfgvbseemlyahizea","kxnbmeusrvrmeihlcfhbfmzlc","omjrvgtvlofaiufh","dvtaoqeacaaluskqqdhmuerjcyw","ttupgfb","mdkwgbuawwzyquwegq","xvzafbijvagqtwvzywqlvzdw","fhiljxxefqvjxpinukhxcohkda","bvksdpuahbraombxpodjayaj","pbfmvhlxauzuwkipau","pgxfnkbdgoztsaiexhugenlmz","zkxumizvzthjhqhiiyepfdhlimp","zmgd","aeqebtbstp","txzinypknlytydalfuqftkxot","yyotfcpvitma","uuicetphghvkyeuerlipqlkmg","pxwllxjvcqepoqlccb","uzsgdqvhfplpqrgrvicaxvkdhl","hjojmzaaanwgl","cnpadyfbsrscwyjnszlmapnjlv","lplvmrrspw","ftjbkbwwbmqhidftjow","mlcjbhsovogdhrddwmege","mfzizdcrhejnfntemslpmpbrv","iremxjh","nbogprsrilrmmsvcbwkwwobm","zjkkyugzmbtldazxdtsugsx","msfqrt","yfqexgfzzsz","sekitazbmshnzwsvsbiucrm","lhjqhozpjqamxkkeyyrefmfyvso","iigexfrelxlrkjckm","gzfkwfkugdlohilycwgitmrbjx","xa","xnfyfhqfnaysweif","qqrarmwasaibdcbeuswczzdmby","wjvvhpvhzrwskfqjawuxrsbqiqhugq","qzsbqpkhdwxlujevptcuybxudzp","kxkmdhubufprfcaqiesgeskpk","vvnllmcnhumomimsgcapoalroesjv","vuxujjgrnu","nviswxjohavescjh","yyuptiwveukajjqy","irppitpnfeaupwovgmqilhxvdnhx","ymontwijzcphsmpu","wxkqsbgbybxiundraolkidmq","cwzyawjshlkamlrfepgahy","uwunzghrwfmubaiskqkgdpof","wiedrwfuhku","zroawyqqjsen","eppxarvxswjngpgaoqimpwbnn","rgcfeqtnurfissqbzrvnozsvglgouo","zikcykvdegerdxrpludstkdedgpvka","keydevouytrexndpxgjeklro","ggsifyfxlcmczbbsews","loyolizemdjbjtswrmevpwx","lrkjarkkpo","ovxyhvtuln","trwxntdkqugaszdrhlliuxwtdsdte","xevtugwckxonclsqbbcgopz","agdwzefqjefqxjqqnkgnzkarovbtsy","zxhqqmlbwuwpmipheqdk","ovbqoeyowayrgyzyghyzjh","zdtdckehtsjrlvmaaafzykedesjw","nwlwgqnhktrdsolrywfpdhihyomcv","xqbewkuapzsbxkmij","tkukbvzyqmingifrsagroqlskc","cyy","vrlipcacfsbqpdorzcetfdifg","tmyeqibcdzebutginflfoagydhfs","wkexxrzhouquvchnplvtrocnxxaile","eqvozcnrrtwivsxulpthgqgo","xategdafpthfyimy","oigzvomuntci","ysxoyobphudyfz","zijxdvyeryowylzemzpxmmi","dlttlinurazlzzohstawpzrm","hcaegubchzymfiymhrx","ypdccysrhavpemcfw","cqthrpqqkoffarsvl","ancbmeoklxzocevj","zzipzeaupqnsuugxicjojthg","ijqjcftcefcvsobsnywb","wcknyykbdgdqfoiyxwykkjgfmmgeup","toefaqhryjvufau","ikbobzuxwqtqiysopsp","ovnxkpueoll","wkmmafwgtuqax","smygecysrkctzdaxrnoujhe","bthllqwgjhggvfqeriyh","vwaxdwgyocqxcbeiragiujyz","bzlqiynizzxmalbwcqjjllrplkv","aapifnzvepzobki","zbmfnskvsprfkmnlceyhwnmmleqr","quohumjpf","rsfkpeucjvcvsyzdxqovfe","ngwrwbitnizquzubcmbqnty","hzfdtbkltppxifzaqd","jazjsenkuhwxyadoj","iytaamorcwdvsvbopaoibgimwdgoq","cfikawuztjfgbjq","qgdygmxmhndsnfasrequy","kzvzcmylggozqyuhdv","qobibsgjpzeo","fjlhveplzxjkboerra","hnkekswifkp","elmawzkeisceowvgqu","ogiuntjpfsvaahppvbmvblmg","ctqdbxmkcgmfcyitoekmu","rgcwuyvxcedojsqsvguq","mwemijadtwkwunlztgmulocyrgj","dnhhkdkchtvedfvvqhvcyomraih","tzbubujkseyfkyngmyxoggwjqfyx","joqlzhffhwt","mcmlolerusdcswu","jbyqcqtulsgrev","zbswentubjugaaazjopvorij","frugxsadoonqjt","kvdeqxesnbfhjbxuweyy","vqosfqzswjb","ezzemdjhnsfi","mfnxfzjfkhhsg","sdcjazwkoaxzvfibezuobaapzxt","xqkrqiowhqtmvktkzw","xtxazeffclcexzmeaycjjmajshv","zxmieefjwihlw","wzhicdsciqcsn","njhka","hgoesyvhlqgrzzkbmkx","hhqxqffxxfv","npndzhkyctu","dbptzbbzisaripjffjllwygwpzrxjf","ccdagum","ukethqmdefjny","tfnzkpzqjeveuzynauprcqtsuyafz","wrjbfwkerzwg","iqapcatbmjv","mtmxmvemslsoikkpforhecawjpthbs","fsgeiqyzkotqwovwmsgoufkom","knxnrmqxzgzxrxbmvjijmegmqs","govqvxxqkvgq","xvoitdqnxslptrzbbbgvvond","fqotzrbknkunufganocgvddcpg","qktnvhyqzrfekbcgknpndoethl","lsfgbkwguheafpaxffhfxbpr","himzsnjhxhxaersjleptlehia","gahnnjgqcuhhrkbhraenlplss","fluupktpkkqomozjbtebccjaxoogx","gyhywm","dztilrjzzhwmmlybfpmegrxnefhu","rjmcgz","hqqumsnbcawjmfbcwprjzod","jbodoxiqetkknul","tfvllzrgoqgticq"]


if len(list1)>len(list2):
    temp = list1
    list1 = list2
    list2 = temp
i=0
sum=len(list2)
arr=[]
while i<len(list1):
    if list1[i] in list2:
        if i+list2.index(list1[i])<sum:
            arr=[]
            arr.append(list1[i])
            sum=i+list2.index(list1[i])
        elif i+list2.index(list1[i])==sum:
            arr.append(list1[i])
        else:
            arr.append(list1[i])
    i+=1
print(arr)

name="alan"
print(name[:-1])

arr = [1,2,3,4,5,6,7,8]
current=1
prev=0
for i in range(1,2):
    temp=current
    current=prev+current
    prev=temp
print(current)


arr = [1,2,3,4,5,6,7,8]
current=1
prev=0
count=0
while current<arr[-1]:
    temp=current
    current=prev+current
    prev=temp
    if current in arr:
        count+=1
        print(current)
print(count)

i=0
lar=0
while i<len(arr):
    current=1
    prev=0
    count=0
    j=i
    while j<len(arr):
        j+=1
    i+=1
        
cost = [10,15,20]

i=0
sum=0
while i<len(cost)-1:
    if cost[i]<cost[i+1]:
        sum+=cost[i]
        if i+2<len(cost) and cost[i+1]<cost[i+2]:
            i+=1
        else:
            i+=2
    else:
        sum+=cost[i+1]
        if cost[i+2]<cost[i+3]:
            i+=2
        else:
            i+=3
print(sum)

matrix = [[2,1,3],[6,5,4],[7,8,9]]

a=[2,1,3]
b=[6,5,4]
c = lambda x,y : x+y
print(dict(x for x in zip(a,b)))

n = 783
i=1

while i<10:
    if str(i) in str(n) or str(i) in str(n*2) or str(i) in str(n*3):
        pass
    else:
        print(False)
    i+=1
print(n*2, n*3)

s="101"
print(int(s,2))

num1 = "1"
num2 = "12"
min_sum = 1
max_sum = 8

count=0
i=int(num1)
while i<=int(num2):
    j=0
    sum=0
    while j<len(str(i)):
        sum+=int(str(i)[j])
        j+=1
    if sum>=min_sum and sum<=max_sum:
        count+=1
    i+=1

arr = [3,1,2,4]
sum=0
i=0
while i<len(arr):
    j=0
    while j<len(arr[i:]):
        sum+=min(arr[i:][:j+1])
        j+=1
    i+=1
print(sum)

for i, value in enumerate(arr):
    print(i, value)
nums = [1,2,2,4]
arr=[]
i=0
while i<len(nums):
    if nums.count(nums[i])>1 and nums[i] not in arr:
        arr.append(nums[i])
    if i+1 not in nums:
        arr.append(i+1)
    i+=1
print(arr)


nums = [4,4,2,4,3]
count=0
i=0
while i<len(nums)-2:
    j=i
    arr=[]
    while j<len(nums):
        if nums[j] not in arr:
            arr.append(nums[j])
        if len(arr)>=3:
            count+=1
            break
        j+=1
    i+=1
print(count)

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

if len(list1)>len(list2):
    temp = list1
    list1 = list2
    list2 = temp
res=""
less=len(list1)+len(list2)
i=0
while i<len(list1):
    if list1[i] in list2 and i + list2.index(list1[i]) < less:
        less = i + list2.index(list1[i])
        res = list1[i]
    i+=1

print(res)

num = "10"
k = 2
arr=[]
i=0
while i<len(num)-(k-1):
    try:
        arr.append(int(num[:i]+num[i+k:]))
    except:
        pass
    i+=1
print(arr)
print(str(min(arr)) if len(arr)>0 else "0")


nums = [2,3,4,4,4]



i=0
while i<len(nums)-1:
    j=i+1
    while j<len(nums):
        if nums[i]<nums[j]:
            del nums[j]
            del nums[i]
            i-=1
            break
        else:
            j+=1
    i+=1
print(nums)


nums = [2,3,4,4,4]
sum=None
count = dict(reversed(sorted(dict(Counter(nums)).items(), key=lambda item:item[1])))
for i in count:
    if sum==None:
        sum = count[i]
    else:
        sum -= count[i]
print(sum)


arr = [0,2,1,-6,6,-7,9,1,2,0,1]

sum = functools.reduce(lambda x,y:x+y, arr)//3

i=0
while i<len(arr)-1:
    j=i+1
    while j<len(arr):
        if sum-(arr[i]+arr[j]) in arr:
            val = sum-(arr[i]+arr[j])
            print(arr[i], arr[j], val)
            del arr[j]
            del arr[i]
            arr.remove(val)
            i-=1
        else:
            j+=1
    i+=1
print(arr)


arr = [3,3,6,5,-2,2,5,1,-9,4]

sum = functools.reduce(lambda x,y:x+y, arr)//3

size = len(arr)//3
left = arr[:size]
mid = arr[size:size*2]
right = arr[size*2:]

while functools.reduce(lambda x,y:x+y, left) != sum:
    val = functools.reduce(lambda x,y:x+y, left)
    

prices = [3,2,3]
money = 3
val = 0
i=0
flag=False
while i<len(prices)-1:
    j=i+1
    while j<len(prices):
        if money - (prices[i]+prices[j])>=0 and money - (prices[i]+prices[j]) > val:
            val = money - (prices[i]+prices[j])
            flag=True
        j+=1
    i+=1
if flag:
    print(val)
print(money)

text1 = "ezupkr"
text2 = "ubmrapg"

arr=0
count=0
i=0
j=0

while i<len(text1):
    if text1[i] in text2[j:]:
        count+=1
        j+=1
    i+=1
print(count)

n = 5

arr = []
i=0
while i<=n:
    arr.append(str(bin(i))[2:].count('1'))
    i+=1


nums = [7,12,9,8,9,15]
k = 4

for i in nums:
    print(i^k)


nums = [4,3,2,1]
k = 2

sum=0
i=0
while i<len(nums):
    if str(bin(i))[2:].count("1")==k:
        sum+=nums[i]
    i+=1
print(sum)

matrix = [[1,2,3],[4,5,6]]
arr=[]
temp=[]
i=0
j=0
while j<len(matrix[i]):
    if len(temp)<len(matrix):
        temp.append(matrix[i][j])
    if len(temp)>=len(matrix):
        arr.append(temp)
        temp=[]
    i+=1
    if i>=len(matrix):
        j+=1
        i=0
print(arr)

words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]

s = "aa"

count = dict(Counter(s))

sum=0
flag=False
for i in count:
    if count[i]%2==0:
        sum+=count[i]
    else:
        sum+=count[i]-1
        flag=True


print(sum+1)


num = "444947137"

count=dict(reversed(sorted(dict(Counter(num)).items(), key=lambda item:item[0])))
num=""
odd=0
for i in count:
    if count[i]%2==0:
        num=num[:len(num)//2]+i*count[i]+num[len(num)//2:]
    elif count[i]>odd:
        odd=count[i]
        res=i*count[i]
if odd>0:
    num=str(int(num))
    num=num[:len(num)//2]+res+num[len(num)//2:]

print(num)

num = 1
i=0
while i<=num:
    print(i, i*i, num)
    if i*i == num:
        print(i)
    if i*i > num:
        break
    i+=1
print(164-144)

s = ""

arr = []
for i in s.split(" "):
    if len(i)>0:
        arr.append(i)
print(arr)

equation = "x+5-3+x=6+x-2"

x=0
while x<100:
    temp = equation
    temp = temp.replace("X", str(x))
    temp = temp.replace("=","-")
    print(temp)
    x+=1

nums = [51,71,17,24,42]

val=-1
for i in nums:
    strg=str(i)  
    if len(strg)>1:
        strg=strg[::-1]
        strg=int(strg)
        print(i, strg)
        if strg in nums and i+strg>val:
            val=i+strg
print (val)

mat = [[1,0,0],[0,0,1],[1,0,0]]
arr = []
temp = []
i=0
j=0
size=0
while j<len(mat):
    temp.append(mat[i][j])
    if mat[i][j]==1:
        size+=1
    if len(temp)>=len(mat):
        arr.append(temp)
        temp=[]
    i+=1
    if i>=len(mat):
        j+=1
        i=0

count = 0
i=0
while i<len(mat):
    if mat[i].count(1)==1 and arr[i].count(1)<=1 and count<size or mat[i].count(1)<=1 and arr[i].count(1)==1 and count<size:
        print(mat[i], arr[i])
        count+=1
    i+=1
print(count, mat, arr)


mat = [[1,0,0],[0,1,0],[0,0,1]]

count=0
i=0
while i<len(mat):
    if mat[i].count(1)==1:
        j=mat[i].index(1)
        k=0
        size=0
        while k<len(mat):
            if mat[k][j]==1:
                size+=1
            k+=1
        if size<=1:
            count+=1
    i+=1
print(count)

nums = [51,71,17,24,42]

lar=-1
i=0
while i<len(nums)-1:
    j=i+1
    while j<len(nums):
        print(str(nums[i]+nums[j]))
        j+=1
    i+=1

path = "NNSWWEWSSESSWENNW"
logic={"N":"S", "S":"N", "E":"W", "W":"E"}
direction={"N":0, "S":0, "E":0, "W":0}
ord={"N":0, "S":0, "E":0, "W":0}
i=0
while i<len(path):
    if direction[logic[path[i]]]>0:
        direction[logic[path[i]]]-=1
    else:
        direction[path[i]]+=1
    i+=1
    print(direction)
    if(direction==ord):
        print(True)

arr = [18,12,-18,18,-19,-1,10,10]

sum = functools.reduce(lambda x,y:x+y, arr)//3
left=[]
mid=[]
right=[]
ord=[left,mid,right]
i=0
j=0
count=0
while i<len(ord):
    count+=1
    if len(ord[i])<1 or functools.reduce(lambda x,y:x+y, ord[i])+arr[j]<=sum:
        ord[i].append(arr[j])
        del arr[j]
    else:
        j+=1
    if j>=len(arr):
        j=0
    if functools.reduce(lambda x,y:x+y, ord[i])==sum:
        i+=1
        count=0
    if count>len(arr)*2:
        print(ord[i])
print(ord)

s = "aaaaaa"
t = "bbaaaa"

index=0
i=0
while i<len(s):
    if s[i] in t:
        t=t[t.index(s[i])+1:]
    else:
        print(False)
    i+=1
print (True)

nums = [3,1,2,4]

i=0
j=len(nums)-1

while i<j:
    if nums[i]%2==0:
        i+=1
    if nums[j]%2==1:
        j-=1
    if nums[i]%2==1 and nums[j]%2==0:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i+=1
        j-=1
print(0%2)

nums = [4,1,2,3]

even=[]
odd=[]

i=0
while i<len(nums):
    if nums[i]%2==0:
        even.append(nums[i])
    else:
        odd.append(nums[i])
    i+=1

nums=[]
even.sort()
odd.sort(reverse=True)
i=0
while i<len(even) and i<len(odd):
    nums.append(even[i])
    nums.append(odd[i])
    i+=1
while i<len(even):
    nums.append(even[i])
    i+=1
while i<len(odd):
    nums.append(odd[i])
    i+=1

s = "226"
s1 = "zzon"
s2 = "zozn"
s1=list(s1)
s2=list(s2)
i=0
while i<len(s1):
    if s1[i] in s2 and s1[i] != s2[i]:
        temp = s2[i]
        s2[i] = s2[s2.index(s1[i])]
        s2[s2.index(s1[i])] = temp

    i+=1
print(s1,s2)


s1 = "zzon"
s2 = "zozn"
s1=list(s1)
s2=list(s2)

i=0
while i<len(s1):
    if s1[i] in s2 and s1[i] != s2[i]:
        j=i+2
        while j<len(s2):
            if s2[j] == s1[i]:
                temp = s2[i]
                s2[i] = s2[j]
                s2[j] = temp
                break
            j+=1
    i+=1 
print(s1, s2)

nums = [2,3,4,3,4]
count=-1
if nums[1]-nums[0]==1:
    count=1
    flag=1
    i=1
    while i<len(nums)-1:
        if nums[i+1]-nums[i]==flag:
            count+=1
        if flag==1:
            flag=-1
        else:
            flag=1
        i+=1
print(count)

nums = [2,3,4,3,4]
arr=-1
i=0
while i<len(nums):
    count=0
    flag=1
    j=0
    while j<len(nums[i:])-1:
        
        if nums[i:][j+1]-nums[i:][j]==flag:
            if count==0:
                count+=1
            count+=1
        else:
            break

        if flag==1:
            flag=-1
        else:
            flag=1
        if count>arr:
            arr=count
        j+=1
    i+=1
print(arr)


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
sum=0
i=0
while i<len(tokens):
    if tokens[i]=="+":
        if sum==0:
            sum=add(int(tokens[i-2]), int(tokens[i-1]))
            del tokens[i]
            del tokens[i-1]
            del tokens[i-1]

        else:
            sum=add(sum, int(tokens[i-1]))
            del tokens[i]
            del tokens[i-1]
    elif tokens[i]=="-":
        if sum==0:
            sum=sub(int(tokens[i-2]), int(tokens[i-1]))
            del tokens[i]
            del tokens[i-1]
            del tokens[i-1]
        else:
            sum=sub(sum, int(tokens[i-1]))
            del tokens[i]
            del tokens[i-1]
    elif tokens[i]=="*":
        if sum==0:
            sum=mul(int(tokens[i-2]), int(tokens[i-1]))
            del tokens[i]
            del tokens[i-1]
            del tokens[i-1]
        else:
            sum=mul(sum, int(tokens[i-1]))
            del tokens[i]
            del tokens[i-1]
    elif tokens[i]=="/":
        if sum==0:
            sum=div(int(tokens[i-2]), int(tokens[i-1]))
            del tokens[i]
            del tokens[i-1]
            del tokens[i-1]
        else:
            sum=div(sum, int(tokens[i-1]))
            del tokens[i]
            del tokens[i-1]
    else:
        i+=1
print(sum)


forts = [0,0,1,-1]

size=0
j=-1
k=-1
i=0
while i<len(forts):
    if forts[i]==1:
        j=0
    elif forts[i]==-1:
        if j>size:
            size=j
        j=-1
    if forts[len(forts)-1-i]==1:
        k=0
    elif forts[len(forts)-1-i]==-1:
        if k>size:
            size=k
        k=-1
    if j>=0 and forts[i]==0:
        j+=1
    if k>=0 and forts[len(forts)-1-i]==0:
        k+=1
    
    i+=1
print(size)


nums = [4,2,5,7]

even=[]
odd=[]

i=0
while i<len(nums):
    if nums[i]%2==0:
        even.append(nums[i])
    else:
        odd.append(nums[i])
    i+=1

nums=[]
even.sort()
odd.sort(reverse=True)
i=0
while i<len(even) and i<len(odd):
    nums.append(even[i])
    nums.append(odd[i])
    i+=1
while i<len(even):
    nums.append(even[i])
    i+=1
while i<len(odd):
    nums.append(odd[i])
    i+=1

print(nums)

num = 27
main=str(num)[2:]
shift=str(num)[:2]
i=len(main)-1
while main[i]<shift[0]:
    print(main[i])
    i-=1
main = int(main[:i+1]+shift+main[i+1:])


low = 100
high = 3000

arr=[]
i=1
num=""
while i<=len(str(low)):
    num+=str(i)
    i+=1
num=int(num)
k=0
while num<low:
    num+=int("1"*(len(str(low))+k))
    if int(str(num)[0])==9:
        k+=1
k=0
while num<high:
    arr.append(num)
    num+=int("1"*(len(str(low))+k))
    if "9" in str(num):
        k+=1
print(arr)
    
    
words = ["hsdqinnoha","mqhskgeqzr","zemkwvqrww","zemkwvqrww","daljcrktje","fghofclnwp","djwdworyka","cxfpybanhd","fghofclnwp","fghofclnwp"]
target = "zemkwvqrww"
startIndex = 8
i=0
j=i
while i<words.count(target):
    print(words[j:].index(target))
    j=words[i:].index(target)
    i+=1


nums = [1,2,2,3]
diff = nums[1]-nums[0]

i=0
while i<len(nums)-1:
    if nums[i+1]-nums[i]!=diff:
        print (False)
    i+=1
print (True)

nums = [0,1,2,2,4,4,1]

print(Counter(s))
count=dict(reversed(sorted(dict(Counter(nums)).items(), key=lambda item:item[1])))
print(count)

for i in count:
    if i%2==0:
        print (i)
print (-1)

arr = [0,1,2,3,4,5,6,7,8]

i=0
while i<len(arr)-1:
    j=i+1
    while j<len(arr):
        if(str(bin(arr[i]))[2:].count("1")>str(bin(arr[j]))[2:].count("1")):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        j+=1
    i+=1
print(arr)

low = 100
high = 2000

arr=[]
i=1
num=""
while i<=len(str(low)):
    num+=str(i)
    i+=1
num=int(num)
k=0
while num<low:
    num+=int("1"*(len(str(low))+k))
    if int(str(num)[0])==9:
        k+=1
k=0
while num<high:
    arr.append(num)
    if "9" in str(num):
        if len(str(num))>=8:
            num+=100000000
        else:
            num+=int(str(len((str(num)))+1)*(len(str(num))-1) + str(len((str(num)))+2))
        k+=1
    else:
        num+=int("1"*(len(str(low))+k))
print(arr)

arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"

date = {"01":31, "02":28, "03":31, "04":30, "05":31, "06":30, "07":31, "08":31, "09":30, "10":31, "11":30, "12":31}

first = min(arriveAlice, arriveBob)
second = max(arriveAlice, arriveBob)

print(bin(8))


arr = [0,1,2,3,4,5,6,7,8]
ord={}
i=0
while i<len(arr):
    if str(bin(arr[i]))[2:].count("1") in ord:
        ord[str(bin(arr[i]))[2:].count("1")].append(arr[i])
    else:
        ord[str(bin(arr[i]))[2:].count("1")] = [arr[i]]
    i+=1
arr=[]
ord = dict(sorted(ord.items()))
for i in ord:
    ord[i].sort()
    arr.extend(ord[i])
print(arr)

nums = [75,34,30]
arr = list(nums)
arr.sort()
i=0
while i<len(nums)-1:
    j=i+1
    while j<len(nums):
        if nums[i]>nums[j] and str(bin(nums[i]))[2:].count("1")==str(bin(nums[j]))[2:].count("1"):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        print(nums[i], str(bin(nums[i])).count("1"))
        j+=1
    i+=1
print(nums)

text = "lloo"
count=dict(Counter(text))
n=0
stg="balloon"
flag=True
while flag:
    i=0
    while i<len(stg):
        try:
            if count[stg[i]]>0:
                print(count)
                count[stg[i]]-=1
            else:
                flag=False
                break
        except:
            pass
        i+=1
    if flag:
        n+=1
print(n)

arriveAlice ="01-20"
leaveAlice ="04-18"
arriveBob ="01-01"
leaveBob ="08-30"

date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if int(arriveAlice[:2])>1:
    arriveAlice = functools.reduce(lambda x,y : x+y, date[:int(arriveAlice[:2])-1]) + int(arriveAlice[3:])
else:
    arriveAlice = int(arriveAlice[3:])

if int(leaveAlice[:2])>1:
    leaveAlice = functools.reduce(lambda x,y : x+y, date[:int(leaveAlice[:2])-1]) + int(leaveAlice[3:])
else:
    leaveAlice = int(leaveAlice[3:])

if int(arriveBob[:2])>1:
    arriveBob = functools.reduce(lambda x,y : x+y, date[:int(arriveBob[:2])-1]) + int(arriveBob[3:])
else:
    arriveBob = int(arriveBob[3:])

if int(leaveBob[:2])>1:
    leaveBob = functools.reduce(lambda x,y : x+y, date[:int(leaveBob[:2])-1]) + int(leaveBob[3:])
else:
    leaveBob = int(leaveBob[3:])

if arriveBob<arriveAlice:
    first = arriveBob
    firstend = leaveBob
    second = arriveAlice
    secondend = leaveAlice
else:
    first = arriveAlice
    firstend = leaveAlice
    second = arriveBob
    secondend = leaveBob

fir=set()
sec=set()
i=first
while i<=firstend:
    fir.add(i)
    i+=1
i=second
while i<=secondend:
    sec.add(i)
    i+=1
print(len(fir.intersection(sec)))

strs = ["eat","tea","tan","ate","nat","bat"]
dict={}
i=0
while i<len(strs):
    j="".join(sorted(strs[i]))
    if j in dict:
        dict[j].append(strs[i])
    else:
        dict[j]=[strs[i]]
    i+=1
arr=[]
for i in dict:
    arr.append(dict[i])


words = ["abba","baba","bbaa","cd","cd"]

dict={}
i=0
while i<len(words):
    j="".join(sorted(words[i]))
    if j not in dict:
        dict[j]=words[i]
    i+=1
arr=[]
for i in dict:
    arr.append(dict[i])

str1 = "ABCABC"
str2 = "ABC"

while str2 in str1 and str2 != str1:
    i=0
    while i<len(str1)-len(str2):
        if str1[i:i+len(str2)]==str2:
            str1=str1[:i]+str1[i+len(str2):]
        i+=1
print(str1)

words = ["aba","aabb","abcd","bac","aabc"]

count=0
i=0
while i<len(words)-1:
    j=i+1
    while j<len(words):
        if "".join(sorted(set(words[i]))) == "".join(sorted(set(words[j]))):
            count+=1
        j+=1
    i+=1
print(count)

words = ["1","2","prev","prev","prev"]

arr=[]
num=[]
prev=[]
i=0
while i<len(words):
    try:
        num.append(int(words[i]))
        prev=[]
    except:
        prev.append(words[i])
    i+=1
    if len(prev)>0:
        if len(prev)>len(num):
            arr.append(-1)
        else:
            arr.append(num[-len(prev)])
print(arr)

flowerbed = [1,0,0,0,1,0,0]
n = 2
i=0
while i<len(flowerbed):
    if flowerbed[i]==0 and i==0 and i+1<len(flowerbed) and flowerbed[i+1]==0:
        flowerbed[i]=1
        n-=1
    elif i>0 and flowerbed[i]==0 and flowerbed[i-1]==0 and i+1<len(flowerbed) and flowerbed[i+1]==0:
        flowerbed[i]=1
        n-=1
    elif i==len(flowerbed)-1 and flowerbed[i]==0 and len(flowerbed)>1 and flowerbed[i-1]==0: 
        flowerbed[i]=1
        n-=1
    i+=1
print(n==0)

timeSeries = [1,4]
duration = 2

arr=set()
i=0
while i<len(timeSeries):
    arr.add(timeSeries[i])
    j=duration-1
    while j>0:
        arr.add(timeSeries[i]+j)
        j-=1
    i+=1
print(arr)

str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

if len(str2)>len(str1):
    temp=str1
    str1=str2
    str2=temp

print("".join(dict(Counter(str1)).keys()) == "".join(dict(Counter(str2)).keys()))

date1 = "2018-06-29"
date2 = "2019-05-30"

date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if int(date1[0:4]+date1[5:7]+date1[8:10])>int(date2[0:4]+date2[5:7]+date2[8:10]):
    temp=date1
    date1=date2
    date2=temp
y1=int(date1[0:4])
m1=int(date1[5:7])
d1=int(date1[8:10])
y2=int(date2[0:4])
m2=int(date2[5:7])
d2=int(date2[8:10])
days=0
i=y1
while i<y2:
    days+=365
    i+=1
print(days)


nums = [1,1,1,2,2,3]
i=0
while i<len(nums):
    if nums.count(nums[i])>2:
        del nums[i]
    else:
        i+=1
print(len(nums))

nums = [1,2,3,2,5]
sum=0
i=0
while i<len(nums):
    i+=1
nums = [1,5,1,1,6,4]
nums.sort()

i=1
j=len(nums)-1
while i<j:
    temp=nums[i]
    nums[i]=nums[j]
    nums[j]=temp
    i+=2
    j-=1
print(nums)

nums = [3,6,1,0]

i=0
while i<len(nums):
    j=0
    while j<len(nums):
        if i!=j:
            if nums[j]*2>nums[i]:
                break

s = "aaa"
arr=[]
i=0
while i<len(s):
    j=0
    while j<len(s[i:]):
        if s[i:][:j+1] not in arr:
            arr.append(s[i:][:j+1])
            print(s[i:][:j+1], s[i:][:j+1][::-1])
        j+=1
    i+=1

s = "bbbab"

i=0
while i<len(s):
    j=0
    while j<len(s[i:]):
        print(s[i:][:j+1])
        j+=1
    i+=1

nums = [1,2,1]

arr=[]
i=0

while i<len(nums):
    j=0
    while j<len(nums[i:]):
        if nums[i:][:j+1] not in arr and nums[i:][:j+1] != nums:
            print(len(nums[i:][:j+1])*len(nums[i:][:j+1]))
            arr.append(nums[i:][:j+1])
        j+=1
    i+=1

n = 10
count=6
i=7
while count<n:
    j=2
    prime=True
    while j<i:
        if i%j==0:
            prime=False
        j+=1
    if prime or i%7==0:
        count+=1
    if count>=n:
        print(i)
        break
    i+=1
print(count)

n=15

count=0
i=1
while count<n:
    if i<7:
        count+=1
    else:
        if i%7==0:
            i+=1
        j=2
        prime=False
        while j<i:
            if i%j==0:
                prime=True
            j+=1
    
        if prime:
            count+=1
            print(i)
    if count==n:
        break
    i+=1    
print(i)


folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]

dict={}
i=0
while i<len(folder):
    if (folder[i][:2]) in dict and len(folder[i])<len(dict[folder[i][:2]]):
        dict[folder[i][:2]]=folder[i]
    elif (folder[i][:2]) in dict and len(folder[i])==len(dict[folder[i][:2]]):
        dict[folder[i]]=folder[i]
    else:
        dict[folder[i][:2]]=folder[i]
    i+=1
print(dict)

nums = [7,12,9,8,9,15]
k = 4
xor=0
i=0
while i<len(nums):
    print(bin(nums[i]), nums[i])
    i+=1

a=707
b=2
if a == 0 and b != 0:
    print (b)
elif b == 0 and a != 0:
    print (a)

print (int(math.log(math.exp(a) * math.exp(b))))

arr=[1,2,3,4,5,6]

def mapper(x):
    if x%2==0:
        return x
a = map(mapper, arr)
for i in a:
    print(i)


nums = [-1]
k = 1

sum=False
i=0
while i<len(nums)-(k-1):
    if (functools.reduce(lambda x,y:x+y, nums[i:k+i])/k)>sum or sum==False:
        sum=functools.reduce(lambda x,y:x+y, nums[i:k+i])/k
        print(nums[i:k+i])
    i+=1

nums1 = [3,2,1,5,6,4]


def join(left, right):
    i=0
    j=0
    nums1=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            nums1.append(left[i])
            i+=1
        else:
            nums1.append(right[j])
            j+=1
    while i<len(left):
        nums1.append(left[i])
        i+=1
    while j<len(right):
        nums1.append(right[j])
        j+=1
    return nums1

def merge_sort(nums1):
    if len(nums1)<=1:
        return nums1
    mid=len(nums1)//2
    left=nums1[:mid]
    right=nums1[mid:]
    
    return join(merge_sort(left), merge_sort(right))

nums1=merge_sort(nums1)

print(nums1)

arr=[1,4,5,1,3,4,2,6]

def join(left, right):
    arr=[]
    i=0
    j=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1
    while i<len(left):
        arr.append(left[i])
        i+=1
    while j<len(right):
        arr.append(right[j])
        j+=1
    return arr
        
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    return join(merge_sort(left), merge_sort(right))

print(merge_sort(arr))

head = [4,2,1,3]

i=1
while i<len(head):
    if head[i]<head[i-1]:
        j=i-1
        while head[i]<head[j] and j>=0:
            j-=1
        head.insert(j+1, head[i])
        del head[i+1]
    else:
        i+=1
print(head)

head = [1]

i=1
j=len(head)-1
while j>i:
    head.insert(i, head[j])
    del head[j+1]
    i+=2
print(head)
print(head[:0+1])
print(functools.reduce(lambda x,y:x+y, head))

def f(): 
    print(x)
x = 1
f()

head = [0,1,2]
k = 3

arr=head[-(k%len(head)):].extend(head[:-(k%len(head))])

print(arr)


s = "wwwzfvedwfvhsww"
s=s[::-1]
dict={}

i=0
j=1
while i<len(s):
    j=i+1
    count=0
    while j<=len(s):
        print(s[i:j])
        if s[i:j] in dict:
            j+=1
            count+=1
        if s[i:j] not in dict:
            dict[s[i:j]]=1
            i+=count
            break
    i+=1
print(len(dict))

file = open("salman pattern.txt", 'a')
file.write("passwords")
file.close()
file = open("salman pattern.txt", 'r')
for i in file:
    print(i)

with open("salman pattern.txt", "a") as file:
    file.write("for i in range of target")

with open("salman pattern.txt", "r") as file:
    for i in file:
        print(i)

arr=[2,5,9]

i=0
while i<max(arr):
    if i not in arr:
        print(i)
    i+=1

head = [1,2,3,4,5,6,8]
left = 2
right = 4

ar = head[:left-1]
ar.extend(head[left-1:right][::-1])
ar.extend(head[right:])
print(ar)

head = [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15]
i=0
j=1
k=0
while i<len(head):
    print(head[i:j])
    i+=1
    j+=j-i

arr = [4,3,1,1,3,3,2]
k = 3
j=0
count = dict(sorted(dict(Counter(arr)).items(), key=lambda item:item[1]))
flag=False
for i in count:
    while count[i]>0:
        if k>0:
            count[i]-=1
            k-=1
            if count[i]<1:
                j+=1
        else:
            flag=True
            break
    if flag:
        break
print(len(count)-j)

arr = [1,2,3,4]
k = 2
num=[]
i=0
while i<len(arr):
    if i%k==0:
        num.extend(arr[len(num):i][::-1])
    i+=1
if i%k==0:
    num.extend(arr[len(num):i][::-1])
else:
    num.extend(arr[len(num):i])
print(num)

arr = [1,2,3,4,5,6,7,8,9,10]
nums=[]
i=0
k=1
while i<len(arr):
    if len(arr[i:k+i])%2==0:
        nums.extend(arr[i:k+i][::-1])
    else:
        nums.extend(arr[i:k+i])
    i=k*k-i
    k+=1
print(nums)

nums = [4,5,7,7,13]
count=0
while(nums != sorted(nums)):
    i=0
    while i<len(nums)-1:
        if nums[i+1]<nums[i]:
            del nums[i+1]
        i+=1
    count+=1
print(nums, count)

head = [0,1,2,3]
nums = [0,1,3]

count=0
i=0
while i<len(head):
    if head[i] in nums:
        count+=1
    i+=1
print(count)

head = [5,2,13]

val=max(head)
valind=head.index(val)
print(len(head[valind+1:]))

heights = [14,3,19,3]
bricks = 17
ladders = 0

i=0
while i<len(heights)-1:
    if heights[i+1]>heights[i]:
        if heights[i+1]-heights[i]>bricks and ladders>0:
            ladders-=1
        else:
            bricks-=heights[i+1]-heights[i]
    print(heights[i], bricks, ladders)
    if bricks<1 and ladders<1 and heights[i+1]>heights[i]:
        break
    i+=1

print(i)


arr = [18,6,10,3]
i=1
while i<len(arr):
    j=min(arr[i-1], arr[i])
    while j>0:
        if arr[i]%j==0 and arr[i-1]%j==0:
            arr.insert(i,j)
            i+=1
            break
        j-=1

    i+=1    
print(arr)


list1 = [0,1,2,3,4,5]
a = 3
b = 4
list2 = [1000000,1000001,1000002]


nums=list1[:a]
nums.extend(list2)
nums.extend(list1[b+1:])
print(nums)


arr = [10,4,6,4,10]

def swap(left, right):
    temp=arr[left]
    arr[left]=arr[right]
    arr[right]=temp

def quick_sort(start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:
        if arr[left]>arr[pivot] and arr[right]<arr[pivot]:
            swap(left, right)
            left+=1
            right-=1
        if arr[left]<=arr[pivot]:
            left+=1
        if arr[right]>=arr[pivot]:
            right-=1
    swap(pivot, right)
    quick_sort(start, right-1)
    quick_sort(right+1, end)
    return
    
quick_sort(0, len(arr)-1)
print(arr)

def swap(left, right):
    temp=arr[left]
    arr[left]=arr[right]
    arr[right]=temp

def quick_sort(start, end):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end
    while left<=right:
        if arr[left]>arr[pivot] and arr[right]<arr[pivot]:
            swap(left,right)
            left+=1
            right-=1
        if arr[left]<=arr[pivot]:
            left+=1
        if arr[right]>=arr[pivot]:
            right-=1

        swap(pivot, right)
        quick_sort(start, right-1)
        quick_sort(right+1, end)
quick_sort(0, len(arr)-1)
print(arr)
        

j=1
while arr != sorted(arr):
    i=0
    while i<len(arr)-j:
        if arr[i]>arr[i+1]:
            temp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=temp
        i+=1
    j+=1
print(arr)

dictionary={}
i=0
while i<len(arr):
    dictionary[i]=arr[i]
    i+=1
dictionary=dict(sorted(sorted(dictionary.items(), key=lambda item:item[0]), key=lambda item:item[1], reverse=True))
print(dictionary)
while i<len(arr):
    if i>=len(arr)-1:
        arr[i]=0
    else:
        j=i+1
        while j<len(arr):
            if arr[j]>arr[i]:
                break
            j+=1
        if j<len(arr):
            arr[i]=arr[j]
        else:
            arr[i]=0
    i+=1
print(arr)


arr=[10, 3, 12, 7, 2, 11, 9]

def swap(left, right):
    temp=arr[left]
    arr[left]=arr[right]
    arr[right]=temp

def quick_sort(start, end):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end
    while left<=right:
        if arr[left]>arr[pivot] and arr[right]<arr[pivot]:
            swap(left, right)
            left+=1
            right-=1
        if arr[left]<=arr[pivot]:
            left+=1
        if arr[right]>=arr[pivot]:
            right-=1
    swap(pivot, right)
    quick_sort(start, right-1)
    quick_sort(right+1, end)
quick_sort(0, len(arr)-1)
print(arr)

nums = [5,7,7,8,8,10]
target = 8
arr=[]
if target in nums:
    arr.append(nums.index(target))
    print(len(nums)-1-(nums[::-1].index(target)))

arr = [40,10,20,30]
i=0
dictionary={ k:sorted(set(arr)).index(k)+1 for k in sorted(set(arr)) }

i=0
while i<len(arr):
    arr[i]=dictionary[arr[i]]
    i+=1
print(arr, dictionary)

s = "bbbaaaab"
t = "aaabbbba"
sarr=[]
tarr=[]
for i in range(len(s)):
    sarr.append(s[i:].count(s[i]))
    sarr.append(s[:i].count(s[i]))
    tarr.append(t[i:].count(t[i]))
    tarr.append(t[:i].count(t[i]))
    
print(sarr==tarr)

pattern = "abba"
s = "dog cat cat fish"
s=s.replace(" ", "")
print(s)
dict={ k:v for k,v in zip(pattern, s)}
i=0
arr=[]
while i<len(pattern):
    arr.append(dict[pattern[i]])
    i+=1
print (dict, arr, s)

num = 2

if num == 0:
    print ("0")
count=abs(num)
base=[]
while count>0:
    base.append(str(count%2))
    count=count//2
print(2**10)

a = 2
b = [3]
print(pow(a,3,1337))

print(bin(-2**2)[3:])

if num == 0:
    print ("0")

base7_digits = []
while num > 0:
  remainder = num % 7
  base7_digits.append(str(remainder))
  num //= 7
print(base7_digits)
print("".join(base7_digits[::-1]))
print(100%7)


nums = [-1,0,3,5,9,12]
target = 2

i=len(nums)//2
start=0
end=len(nums)-1
while end-start>1:
    if target>nums[i]:
        start=i
        i=(start+end)//2
    elif target<nums[i]:
        end=i
        i=(start+end)//2
    else:
        print(i)
        break
print(False)

arr = [40,10,20,30]

dictionary={}
array=[]
i=0
while i<len(arr):
    dictionary[sorted(arr)[i]]=i+1
    i+=1

for i in arr:
    array.append(dictionary[i])
print(array)

print(eval("-9.1234"))

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class Binary:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root==None:
            self.root=node
            return
        current=self.root
        while True:
            if data<current.data:
                if current.left==None:
                    current.left=node
                    break
                else:
                    current=current.left
            else:
                if current.right==None:
                    current.right=node
                    break
                else:
                    current=current.right

    def exists(self, data):
        current=self.root
        while current:
            if data < current.data:
                current=current.left
            elif data > current.data:
                current=current.right
            else:
                return current.data
        return False
    
    def remove(self, data):

        def get_min(current):
            if current.left:
                get_min(current.left)
            else:
                return(current.data)
            
        def remove_helper(data, current, parent):
            current=self.root
            while current:
                parent=current
                if data<current.data:
                    current=current.left
                elif data>current.data:
                    current=current.right
                else:
                    if current.left != None and current.right != None: 
                        current.data = get_min(current.right)
                        remove_helper(current.data, )
                    

                    return
        
    def in_order(self):
        def in_order_helper(current):
            if current:
                in_order_helper(current.left)
                print(current.data)
                in_order_helper(current.right)
        
        in_order_helper(self.root)
            


binary=Binary()
arr=[4,6,3,7,2,8,5,1,9]
i=0
while i<len(arr):
    binary.append(arr[i])
    i+=1

print(binary.exists(10))
binary.in_order()

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.root=None
    
    def append(self, data):
        node=Node(data)
        if self.root == None:
            self.root=node
            return
        current=self.root
        while True:
            if data < current.data:
                if current.left == None:
                    current.left = node
                    break
                else:
                    current = current.left
            else:
                if current.right == None:
                    current.right = node
                    break
                else:
                    current = current.right

    def in_order(self):
        def helper(current):
            if current:
                helper(current.left)
                print(current.data)
                helper(current.right)
        helper(self.root)


    def remove(self, data):

        def get_min(current):
            if current.left==None:
                return current.data
            else:
                return get_min(current.left)

        def helper(data, current, parrent):
            while current != None:
                if data<current.data:
                    parrent=current
                    current=current.left
                elif data>current.data:
                    parrent=current
                    current=current.right
                else:
                    if current.left != None and current.right != None:
                        current.data=get_min(current.right)
                        return helper(current.data, current.right, current)
                    else:
                        if parrent == None:
                            if current.left == None:
                                self.root = current.right
                            else:
                                self.root = current.left
                        else:
                            if parrent.left == current:
                                if current.left == None:
                                    parrent.left = current.right
                                    current=current.right
                                else:
                                    parrent.left = current.left
                                    current=current.left
                            else:
                                if current.left == None:
                                    parrent.right = current.right
                                    current=current.right
                                else:
                                    parrent.right = current.left
                                    current=current.left



        parrent=None
        current=self.root       
        helper(data, current, parrent)



bst=BinarySearchTree()

arr=[6,5,7,4,8,1,9,2,4]
for i in arr:
    bst.append(i)


bst.remove(7)

bst.in_order()

left=2147483646
right=2147483647
print(right,2**23 -1)
i=left
left+=1
count=0
while left<=right:
    i&=left
    left+=1
    if count != i:
        count=i
        print(count)
    if i==0:
        break
print(i)
count=0
while left != right:
    left >>= 1
    right >>= 1
    count+=1
print(left<<count)
print(3&8)

nums = [1,3,8,48,10]

i=0
while i<len(nums)-1:
    count=1
    j=i+1
    while j<len(nums) and nums[i]&nums[j]==0:
        count+=1
        j+=1
    print(count)
    i+=1

prices = [7,1,5,3,6,4]

buy=prices[0]
profit=0

i=0
while i<len(prices)-1:
    profit = max(profit, prices[1:][i]-buy)
    buy = min(buy, prices[1:][i])
    i+=1
print(profit)
        
height = [1,8,6,2,5,4,8,3,7]
area=0
points=0
i=1
while i<len(height):
    area = max(area, min(points, height[i])* i-height.index(points))
    points = max(points, height[i])
    i+=1
print(area)
        

height = [1,8,6,2,5,4,8,3,7]
area=0
current=0
left=0
right=len(height)-1
while left<right:
    current=max(current, min(height[left],height[right])*(right-left))
    area=max(area, current)
    if height[left]<height[right]:
        left+=1
    else:
        right-=1
print(area)
        
def join(left, right):
    array=[]
    i,j = 0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            array.append(left[i])
            i+=1
        else:
            array.append(right[j])
            j+=1
    while i<len(left):
        array.append(left[i])
        i+=1
    while j<len(right):
        array.append(right[j])
        j+=1
    return array
def merge(array):
    if len(array)<=1:
        return array
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    
    return join(merge(left), merge(right))


arr=[9,4,9,6,1,3,0,8,6,2]

print(merge(arr))

height = [0,1,0,2,1,0,1,3,2,1,2,1]
current=0
count=0
i=0
while i<len(height):
    current = max(current, height[i])
    count+= current - height[i]
    i+=1
print(count)

items2 = [[3,1],[1,5], [3,1],[1,5]]

arr = list(x[0] for x in items2)
print(arr)

items1 = [[5,1],[4,2],[3,3],[2,4],[1,5]]
items2 = [[7,1],[6,2],[5,3],[4,4]]

arr = list(x[0] for x in items2)
i=0
while i<len(items1):
    if items1[i][0] in arr:
        items1[i][1]+=items2[arr.index(items1[i][0])][1]
        del items2[arr.index(items1[i][0])]
        del arr[arr.index(items1[i][0])]
    i+=1
i=0
while i<len(items2):
    items1.append(items2[i])
    i+=1
items1.sort()
print (items1)

s="alanest"
vowels = "aeiouAEIOU"
count = list(x for x in s if x in vowels)
print(s[:3])

def validate_bst_traversal(arr) -> bool:
  """
  This function checks if a list represents a valid Binary Search Tree (BST) based on its in-order traversal.

  Args:
      arr: A list containing the in-order traversal of the BST.

  Returns:
      bool: True if the list represents a valid BST, False otherwise.
  """
  prev = float('-inf')  # Initialize previous value to negative infinity
  for val in arr:
    if val <= prev:
      return False  # Current value must be greater than the previous encountered value in in-order traversal
    prev = val
  return True

# Example usage
arr = [32,26,47,19,27]  # Valid BST in-order traversal
if validate_bst_traversal(arr):
    print("The list represents a valid BST.")
else:
    print("The list does not represent a valid BST.")


s = "aabcb"

i=0
while i<len(s)-2:
    j=2
    while j<len(s):
        count=dict(Counter(s[i:j+1]))
        print(count)
        j+=1
    i+=1
print(0%2)


def max_sum_non_adjacent(arr):

  n = len(arr)

  if n == 0:
    return 0
  if n == 1:
    return arr[0]

  dp = [0] * n
  dp[0] = arr[0]

  for i in range(1, n):
    print(arr[i], dp[i-2], dp[i-1])
    include = arr[i] + dp[i - 2]
    exclude = dp[i - 1]
    dp[i] = max(include, exclude)

  return dp[n - 1]

arr = [2,7,9,3,1]
max_sum = max_sum_non_adjacent(arr)
print(max_sum)

nums = [1,2,3,1]
n=len(nums)
arr=[0]*n
arr[0]=nums[0]
i=1
while i<len(nums):
    j=nums[i]+arr[i-2]
    k=arr[i-1]
    arr[i]=max(j,k)
    i+=1
print(arr)


cost = [10,15,20]

n=len(cost)
arr=[float('inf')]*n
print(arr)
arr[0]=cost[0]
arr[1]=min(cost[0],cost[1])

for i in range(2, n):
    arr[i]=min(arr[i-1]+cost[i], arr[i-2]+cost[i])
print(arr)


def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

    return dp[n]

# Example usage:
cost = [1,10,15,7]
print(minCostClimbingStairs(cost))


cost = [10,1]

n=len(cost)
arr=[0]*(n+1)

for i in range(2, n+1):
    print(arr[i-1]+cost[i-1], arr[i-2]+cost[i-2])
    arr[i]=min(arr[i-1]+cost[i-1], arr[i-2]+cost[i-2])
print(arr[n])

nums = [0,0,0,3,2,0]

n=len(nums)

dp=[0]*(n+1)
dp[0]=nums[0]
for i in range(1,n):
    dp[i]=max(nums[i]+dp[i-2], dp[i-1])
print(dp[n-1])

s1 = "aabcc"
s2 = "dbbca"
s3 = "daabbcbcac"
s1+=s2
print(Counter(s1),Counter(s3))


nums = [0,0]

n=len(nums)
dp=[[0,False]]*(n)
dp[0]=[nums[0],True]
for i in range(1,n):
    if dp[i-2][0]+nums[i]>dp[i-1][0]:
       dp[i]=[dp[i-2][0]+nums[i], True if dp[i-2][1]==True else False]
    else:
        dp[i]=[dp[i-1][0], True if dp[i-1][1]==True else False]

if(dp[n-1][1]==True):
    dp[n-1][0] = (dp[n-1][0]-min(nums[n-1],nums[0]))
print(dp)
def find_max(lst):
    return functools.reduce(lambda x, y: max(x, find_max(y)) if isinstance(y, list) else max(x, y), lst, float('-inf'))
print(find_max(dp))


arr=["eat", "tea", "tan", "ate", "nat", "bat"]

nums=[]

i=0
while i<len(arr):
    count=dict(Counter(arr[i]))
    temp=[arr[i]]
    j=i+1
    while j<len(arr):
        if count==dict(Counter(arr[j])):
            temp.append(arr[j])
            del arr[j]
            j-=1
        j+=1
    nums.append(temp)
    i+=1
print(nums)


a=[5,2,3,1,4]
t=9

i=0
j=0
while i<len(a):
    if a[i]+a[j]==t:
        print(a[i],a[j])
        break
    if j==len(a)-1:
        i+=1
    j+=1


arr=[9,4,9,6,1,3,0,8,6,2]

def join(left, right):
    arr=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1
    while i<len(left):
        arr.append(left[i])
        i+=1
    while j<len(right):
        arr.append(right[j])
        j+=1
    
    return arr

def merge(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    return join(merge(left), merge(right))

print(merge(arr))


arr=[9,4,9,6,1,3,0,8,6,2]

def swap(arr, left, right):
    temp=arr[left]
    arr[left]=arr[right]
    arr[right]=temp

def helper(arr, start, end):
    if start>=end:
        return arr
    pivot=start
    left=start+1
    right=end

    while left<=right:
        if arr[left]>arr[pivot] and arr[right]<arr[pivot]:
            swap(arr, left, right)
            left+=1
            right-=1
        if arr[left]<=arr[pivot]:
            left+=1
        if arr[right]>=arr[pivot]:
            right-=1
    swap(arr, pivot, right)
    helper(arr, start,right-1)
    helper(arr, right+1, end)
    return arr

def quick(arr):
    start=0
    end=len(arr)-1
    return helper(arr, start, end)

print(quick(arr))

class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class Stack:
    def __init__(self):
        self.head=None
        self.tail=None

    def push(self, data):
        node=Node(data)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head=node

    def print(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

    def pop(self, data):
        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head
        previous=None
        while current.next:
            previous=current
            current=current.next

            if current.data==data:
                previous.next = current.next
                return

    def enque(self, data):
        node=Node(data)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node

    def deque(self):
        if self.head!=None:
            self.head=self.head.next

arr=[10,4,9,6,1,3,0,8,6,2]
ll=Stack()
for i in arr:
    ll.enque(i)
ll.deque()
ll.print()

class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class HashTable:
    def __init__(self, size):
        self.size=size
        self.table=self.create_baskucts()

    def create_baskucts(self):
        return [[] for _ in range(self.size)]
    
    def set_val(self, key, val):
        hashed_key = hash(key)%self.size

        baskuct = self.table[hashed_key]

        found_key=False
        for index, record in enumerate(baskuct):
            record_key, record_val = record

            if record_key == key:
                found_key=True
                break
        
        if found_key:
            baskuct[index]=(key, val)
        else:
            baskuct.append((key,val))

    def get_val(self, key):

        hashed_key = hash(key)%self.size

        baskuct = self.table[hashed_key]

        found_key=False
        for index, record in enumerate(baskuct):
            record_key, record_val = record

            if record_key==key:
                found_key=True
                break
        
        if found_key:
            print(record_val)
        else:
            print("No record found")
        
    def delete_val(self, key):

        hashed_key = hash(key)%self.size

        baskuct = self.table[hashed_key]

        found_key=False
        for index, record in enumerate(baskuct):
            record_key, record_val = record

            if record_key==key:
                found_key=True
                break
        if found_key:
            baskuct.pop(index)
        return
    
hash_table = HashTable(10)

arr=[10,4,9,6,1,3,0,8,6,2]

for i, j in enumerate(arr):
    hash_table.set_val(i, j)

hash_table.get_val(5)


class HashTable:
    def __init__(self, size=None):
        self.size=size
        self.table=self.create()

    def create(self):
        return [[] for _ in range(self.size)]
    
    def set_val(self, key, val):

        hashed_key = hash(key)%self.size

        arr = self.table[hashed_key]

        found_key = False
        for index, record in enumerate(arr):
            record_key, record_val = record

            if record_key==key:
                found_key=True
                break
        if found_key:
            arr[index] = (key, val)
        else:
            arr.append((key, val))

    def get_val(self, key):

        hashed_key = hash(key)%self.size

        arr=self.table[hashed_key]

        found_key=False
        for index, record in enumerate(arr):
            record_key, record_val = record

            if record_key == key:
                found_key=True
                break
        if found_key:
            print(record_val)
        else:
            print("No record found")

    def delete_val(self, key):

        hashed_key=hash(key)%self.size

        arr=self.table[hashed_key]

        found_key=False
        for index, record in enumerate(arr):
            record_key, record_val = record

            if record_key == key:
                arr.pop(index)
                return
            
    def print_val(self):
        for record in self.table:
            try:
                key, val = record[0]    
                print(key, val)
            except:
                continue

hash_table = HashTable(10)

arr=[10,4,9,6,1,3,0,8,6,2]

for i, j in enumerate(arr):
    hash_table.set_val(i, j)



hash_table.print_val()


arr=[10,4,9,6,1,3,0,8,6,2]

i=0
while i<len(arr):
    j=0
    while j<len(arr)-1:
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
        j+=1
    i+=1
print(arr)
    
def join(left, right):
    
    arr=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1
    while i<len(left):
        arr.append(left[i])
        i+=1
    while j<len(right):
        arr.append(right[j])
        j+=1
    return arr



def merge(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    return join(merge(left), merge(right))

arr = [9,4,9,6,1,3,0,8,6,2]

print(merge(arr))


s = "a"
print(s[0])
i=0
while i<len(s):
    if s[i]==s[-1]:
        s=s[i+1:-1]
    else:
        break
print(s)

nums = [3,2,1,4,5]


sum=nums[0]+nums[1]
count=0
i=0
while i<len(nums)-1:
    if nums[i]+nums[i+1]==sum:
        count+=1
        del nums[i]
        del nums[i]


words = ["abab","ab"]

n=len(words)
count=0
i=0
while i<n-1:
    t=1
    l=len(words[i])
    j=i+1
    try:
        while j<n:
            if words[j][:l] == words[i] and words[j][-l:] == words[i]:
                t+=1
                del words[j]
            else:
                break
    except:
        if t>1:
            count+=t
        break

    i+=1
print(count)


numerator = 4
denominator = 333
val=""
non=numerator//denominator
point=numerator/denominator
if point == non:
    val+=str(non)
else:
    val+=str(point)

print(val)

s = "cbaebabacd"
p = "abc"

dp=[]
i=0
l=len(p)
n=len(s)
p=list(p)
p.sort()
while i<n-(l-1):
    arr=list(s[i:i+l])
    if p == sorted(arr):
        dp.append(i)
    i+=1
print(dp)


s = "ADOBECODEBANC"
t = "ABC"

n=len(s)
l=len(t)
c=dict(Counter(t))
k=float('inf')
i=0
z=n
y=""
while i<n:
    j=i+l
    v=z-l
    while j<=n and j-i<=k:
        d=dict(Counter(s[i:j]))
        b=dict(Counter(s[v:z]))
        xflag=True
        yflag=True
        for x in c:
            if x not in d or c[x] > d[x]:
                xflag=False
            if x not in b or c[x] > b[x]:
                yflag=False
            if xflag==False and yflag==False:
                break
        if xflag and len(s[i:j])<k:
            k=len(s[i:j])
            y=s[i:j]
        if yflag and len(s[v:z])<k:
            k=len(s[v:z])
            y=s[v:z]
        j+=1
        v-=1
    i+=1
    z-=1
print(y)


def min_window_substring(s, t):
    if not s or not t:
        return ""
    
    target_counts = Counter(t)
    required_chars = len(target_counts)
    
    min_length = float('inf')
    min_window = ""
    
    left = 0
    char_count = 0
    window_counts = Counter()
    
    for right, char in enumerate(s):
        window_counts[char] += 1
        if window_counts[char] == target_counts[char]:
            char_count += 1
        
        while char_count == required_chars:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window = s[left:right+1]
            
            if window_counts[s[left]] == target_counts[s[left]]:
                char_count -= 1
            window_counts[s[left]] -= 1
            left += 1
    
    return min_window

# Test the function
s = "ADOBECODEBANC"
t = "ABC"
print(min_window_substring(s, t))  # Output: "BANC"

n = 9
s = "acdcdacdc"

i=0
k=1
l=0
r=""
while i<n-(k-1):
    j=i+k
    while j<=n:
        if len(s[i:j]) == len(set(s[i:j])):
            if len(s[i:j])>l:
                l=len(s[i:j])
                k=l
                r=s[i:j]
        else:
            break
        j+=1
    i+=1
print(r)

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class Heap:
    def __init__(self):
        self.root = None

    def append(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = node
                break
            else:
                queue.append(current.left)
            if current.right is None:
                current.right = node
                break
            else:
                queue.append(current.right)
    
    def print(self):
        def helper(current):
            if current:
                print(current.data)
                helper(current.left)
                helper(current.right)
            
        helper(self.root)
    

heap = Heap()

arr = [1,2,3,4,5,6,7,8]

for i in arr:
    heap.append(i)

heap.print()


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node = Node(data)
        if self.root is None:
            self.root=node
            return
        queue=[self.root]
        while queue:
            current=queue.pop(0)
            if current.left is None:
                current.left=node
                break
            else:
                queue.append(current.left)
            if current.right is None:
                current.right=node
                break
            else:
                queue.append(current.right)

    def print(self):
        level=0
        def helper(current, count):
            nonlocal level
            if current:
                count+=1
                level=max(level, count)
                print(current.data)
                helper(current.left, count)
                helper(current.right, count)
        helper(self.root, 0)


arr=[9,4,9,6,1,3,0,8,6,2]
binary_tree = BinaryTree()
for i in arr:
    binary_tree.append(i)
binary_tree.print()

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        current=self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left=node
                    break
                else:
                    current=current.left
            else:
                if current.right is None:
                    current.right=node
                    break
                else:
                    current=current.right
        
    def print(self):
        level=0
        def helper(current, count):
            nonlocal level
            if current:
                count+=1
                level=max(level, count)
                print(current.data)
                helper(current.left, count)
                helper(current.right, count)
        helper(self.root, 0)

arr=[9,4,9,6,1,3,0,8,6,2]
binary_tree = BinarySearchTree()
for i in arr:
    binary_tree.append(i)
binary_tree.print()

class HashMap:
    def __init__(self, size=None):
        self.size=size
        self.table = self.create()

    def create(self):
        return [[] for _ in range(self.size)]
    
    def set_value(self, key, value):
        hashed = hash(key)%self.size

        bucket = self.table[hashed]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if key == record_key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key,value))

    def print(self):
        for x in self.table:
            try:
                key, value = x[0]
                print(key, value)
            except:
                continue
    

hashmap = HashMap(10)
arr=[9,4,9,6,1,3,0,8,6,2]
for i, j in enumerate(arr):
    hashmap.set_value(i,j)
hashmap.print()


class HashMap:
    def __init__(self, size=None):
        self.size=size
        self.table=self.create()

    def create(self):
        return [[] for _ in range(self.size)]
    
    def append(self, key, value):
        hashed = hash(key)%self.size
        bucket = self.table[hashed]

        found_key=False
        for index, random in enumerate(bucket):
            random_key, random_value = random

            if key == random_key:
                found_key = True
                break
        
        if found_key:
            bucket[index]=(key,value)
        else:
            bucket.append((key, value))

    def print(self):
        for x in self.table:
            key, value = x[0]
            print(key, value)

    
hashmap = HashMap(10)
arr=[9,4,9,6,1,3,0,8,6,2]
for i, j in enumerate(arr):
    hashmap.append(i,j)
hashmap.print()


class Heap:
    def __init__(self):
        self.heap=[]

    def parent(self, i):
        return (i-1)//2
    
    def left_child(self, i):
        return 2*i+1
    
    def right_child(self, i):
        return 2*i+2
    
    def append(self, data):
        self.heap.append(data)
        self.shift_up(len(self.heap)-1)

    def shift_up(self, i):
        while i>0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def shift_down(self, i):
        min_index=i
        left=self.left_child(i)
        right=self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        if min_index != i:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.shift_down(min_index)

    def remove(self, data):
        for i, j in enumerate(self.heap):
            if i == len(self.heap)-1 and j == data:
                self.heap.pop(i)
                break
            elif j == data:
                self.heap[i] = self.heap[len(self.heap)-1]
                self.heap.pop(len(self.heap)-1)
                self.shift_down(i)
                self.shift_up(i)
                break
        
    
    def print(self):
        print(self.heap)


heap = Heap()

arr=[9,4,9,6,1,3,0,8,6,2,3]
for i in arr:
    heap.append(i)
heap.remove(0)
heap.print()

import heapq

heapq.heapify(arr)
print(arr)


class Heap:

    def __init__(self):
        self.heap=[]

    def parent(self, i):
        return (i-1)//2
    
    def left_child(self, i):
        return 2*i+1
    
    def right_child(self, i):
        return 2*i+2
    
    def append(self, data):
        self.heap.append(data)
        self.shift_up(len(self.heap)-1)

    def remove(self, data):
        for i, x in enumerate(self.heap):
            if x == data:
                self.heap[i] = self.heap[len(self.heap)-1]
                self.heap.pop(len(self.heap)-1)
                self.shift_down(0)
    
                
    def shift_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        while left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        while right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        if min_index != i:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.shift_down(min_index)

    def shift_up(self, i):
        while i>0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def print(self):
        print(self.heap)


arr=[8,5,4,7,9,3,3,9,3,1]
heap = Heap()
for i in arr:
    heap.append(i)
heap.remove(1)
heap.print()


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        current=self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left=node
                    break
                else:
                    current=current.left
            else:
                if current.right is None:
                    current.right=node
                    break
                else:
                    current=current.right

    def print(self):
        level=0
        def helper(current, count):
            nonlocal level
            if current:
                count+=1
                level=max(level, count)
                print(current.data)
                helper(current.left, count)
                helper(current.right, count)
        helper(self.root,0)
        print("Depth : ",level)

    def remove(self, data):
        def get_min(current):
            if current.left is None:
                return current.data
            else:
                return get_min(current.left)
        
        def helper(data, current, parent):
            while current:
                if data < current.data:
                    parent=current
                    current=current.left
                elif data > current.data:
                    parent=current
                    current=current.right
                else:
                    if current.left and current.right:
                        current.data = get_min(current.right)
                        return helper(current.data, current.right, current)
                    else:
                        if parent is None:
                            if current.left is None:
                                self.root = current.right
                            else:
                                self.root = current.left
                        else:
                            if parent.left == current:
                                if current.left == None:
                                    parent.left = current.right
                                    current=current.right
                                else:
                                    parent.left = current.left
                                    current=current.left
                            else:
                                if current.left == None:
                                    parent.right = current.right
                                    current=current.right
                                else:
                                    parent.right = current.left
                                    current=current.left
        helper(data, self.root, None)


arr=[5,4,7,9,3,3,9,3,1,8,6]
bst = BinarySearchTree()
for i in arr:
    bst.append(i)
bst.remove(5)
bst.print()

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        current=self.root
        while True:
            if data < current.data:
                if current.left:
                    current=current.left
                else:
                    current.left=node
                    break
            else:
                if current.right:
                    current=current.right
                else:
                    current.right=node
                    break

    def print(self):
        def helper(current):
            if current:
                print(current.data)
                helper(current.left)
                helper(current.right)
        helper(self.root)

    
    def remove(self, data):
        def get_min(current):
            if current.left:
                return get_min(current.left)
            else:
                return current.data
        
        def helper(data, current, parrent):
            while current:
                if data < current.data:
                    parrent=current
                    current=current.left
                elif data > current.data:
                    parrent=current
                    current=current.right
                else:
                    if current.left and current.right:
                        current.data=get_min(current.right)
                        return helper(current.data, current.right, current)
                    else:
                        if parrent is None:
                            if current.left:
                                self.root=current.left
                            else:
                                self.root=current.right
                        else:
                            if current == parrent.left:
                                if current.left:
                                    parrent.left=current.left
                                    current=current.left
                                else:
                                    parrent.left=current.right
                                    current=current.right
                            else:
                                if current.left:
                                    parrent.right=current.left
                                    current=current.left
                                else:
                                    parrent.right=current.right
                                    current=current.right
        helper(data, self.root, None)

    def delete(self, data):
        pass


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        current=self.root
        while True:
            if data < current.data:
                if current.left:
                    current=current.left
                else:
                    current.left=node
                    break
            else:
                if current.right:
                    current=current.right
                else:
                    current.right=node
                    break
    
    def remove(self, data):
        def get_min(current):
            if current.left:
                return get_min(current.left)
            else:
                return current.data
        
        def helper(data, current, parent):
            while current:
                if data < current.data:
                    parent=current
                    current=current.left
                elif data > current.data:
                    parent=current
                    current=current.right
                else:
                    if current.left and current.right:
                        current.data=get_min(current.right)
                        return helper(current.data, current.right, current)
                    else:
                        if parent is None:
                            if current.left:
                                self.root=current.left
                            else:
                                self.root=current.right
                        else:
                            if parent.left == current:
                                if current.left:
                                    parent.left=current.left
                                    current=current.left
                                else:
                                    parent.left=current.right
                                    current=current.right
                            else:
                                if current.left:
                                    parent.right=current.left
                                    current=current.left
                                else:
                                    parent.right=current.right
                                    current=current.right
        helper(data, self.root, None)

    
    def print(self):
        def helper(current):
            if current:
                print(current.data)
                helper(current.left)
                helper(current.right)
        helper(self.root)

    def find(self, data):
        value=float('inf')
        check=float('inf')
        def helper(current):
            nonlocal value
            nonlocal check
            if current:
                if abs(current.data - data)<check:
                    check=abs(current.data - data)
                    value=current.data
                helper(current.left)
                helper(current.right)
        helper(self.root)
        print(value)


arr=[5,4,7,9,3,3,9,3,1,8,6]
bst = BinarySearchTree()
for i in arr:
    bst.append(i)
bst.remove(4)
bst.print()
bst.find(3)



a=["Skiplist","add","add","add","add","add","add","add","add","add","erase","search","add","erase","erase","erase","add","search","search","search","erase","search","add","add","add","erase","search","add","search","erase","search","search","erase","erase","add","erase","search","erase","erase","search","add","add","erase","erase","erase","add","erase","add","erase","erase","add","add","add","search","search","add","erase","search","add","add","search","add","search","erase","erase","search","search","erase","search","add","erase","search","erase","search","erase","erase","search","search","add","add","add","add","search","search","search","search","search","search","search","search","search"]
b=[[],[16],[5],[14],[13],[0],[3],[12],[9],[12],[3],[6],[7],[0],[1],[10],[5],[12],[7],[16],[7],[0],[9],[16],[3],[2],[17],[2],[17],[0],[9],[14],[1],[6],[1],[16],[9],[10],[9],[2],[3],[16],[15],[12],[7],[4],[3],[2],[1],[14],[13],[12],[3],[6],[17],[2],[3],[14],[11],[0],[13],[2],[1],[10],[17],[0],[5],[8],[9],[8],[11],[10],[11],[10],[9],[8],[15],[14],[1],[6],[17],[16],[13],[4],[5],[4],[17],[16],[7],[14],[1]]
i=0
while i<len(a):
    if a[i]=="search":
        del a[i]
        del b[i]
    else:
        i+=1
print(b)

class Heap:
    def __init__(self):
        self.heap=[]
        self.length=0

    def parent(self, i):
        return (i-1)//2
    
    def left_child(self, i):
        return 2*i+1
    
    def right_child(self, i):
        return 2*i+2

    def append(self, data):
        self.heap.append(data)
        self.length+=1
        self.shift_up(self.length-1)

    def shift_up(self, i):
        while i>0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i=self.parent(i)

    def shift_down(self, i):
        min_index=i
        left=self.left_child(i)
        right=self.right_child(i)
        while left < self.length and self.heap[left] < self.heap[min_index]:
            min_index=left
        while right < self.length and self.heap[right] < self.heap[min_index]:
            min_index=right
        if min_index != i:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.shift_down(min_index)

    def remove(self, data):
        for i, x in enumerate(self.heap):
            if x == data:
                self.heap[i]=self.heap[self.length-1]
                self.heap.pop(self.length-1)
                self.length-=1
                self.shift_down(i)
                self.shift_up(i)
                break

    def print(self):
        for x in self.heap:
            print(x)

    def build(self, arr):
        self.length+=len(arr)
        self.heap.extend(arr)
        self.shift_down(0)
        self.shift_up(self.length-1)


arr=[9,4,9,6,1,3,0,8,6,2]
heap=Heap()
heap.build(arr)
heap.remove(1)
heap.print()

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        queue=[self.root]
        while queue:
            current=queue.pop(0)
            if current.left:
                queue.append(current.left)
            else:
                current.left=node
                break
            if current.right:
                queue.append(current.right)
            else:
                current.right=node
                break

    def print(self):
        def helper(current):
            if current:
                print(current.data)
                helper(current.left)
                helper(current.right)
        helper(self.root)
    

arr=[5,4,7,9,3,3,9,3,1,8,6]
bst = BinaryTree()
for i in arr:
    bst.append(i)
bst.print()

class Heap:
    def __init__(self):
        self.heap=[]
        self.length=0

    def parrent(self, i):
        return (i-1)//2

    def left_child(self, i):
        return 2*i+1
    
    def right_child(self, i):
        return 2*i+2

    def append(self, data):
        self.heap.append(data)
        self.length+=1
        self.shift_up(self.length-1)

    def shift_up(self, i):
        while i>0 and self.heap[self.parrent(i)] < self.heap[i]:
            self.heap[self.parrent(i)], self.heap[i] =  self.heap[i], self.heap[self.parrent(i)]
            i = self.parrent(i)
    
    def shift_down(self, i):
        min_index=i
        left=self.left_child(i)
        right=self.right_child(i)
        if left<self.length and self.heap[left] > self.heap[min_index]:
            min_index=left
        if right<self.length and self.heap[right] > self.heap[min_index]:
            min_index=right
        if min_index != i:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.shift_down(min_index)
    
    def helper(self,i,j):
        min_index=i
        left=self.left_child(i)
        right=self.right_child(i)
        if left<self.length-j and self.heap[left] > self.heap[min_index]:
            min_index=left
        if right<self.length-j and self.heap[right] > self.heap[min_index]:
            min_index=right
        if min_index != i:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.helper(min_index, j)

    def sort(self):
        i=0
        while i<self.length:
            self.helper(0,i)
            self.heap[0], self.heap[-i-1] = self.heap[-i-1], self.heap[0]
            i+=1
        

    def print(self):
        for x in self.heap:
            print(x)


arr=[9,4,9,6,1,3,0,8,6,2]
heap=Heap()
for i in arr:
    heap.append(i)
heap.sort()
heap.print()

arr=[1,2,4,5,6,7,8,9,10]
target=11
i=len(arr)//2
left=0
right=len(arr)
count=0
while True:
    count+=1
    if count>=len(arr):
        break
    if target==arr[i]:
        print(i)
        break
    elif target<arr[i]:
        left=i
        i=i//2
    elif target>arr[i]:
        right=i
        i=(len(arr)+i)//2
print(count)

class Node:
    def __init__(self, data=None):
        self.child={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=Node()

    def append(self, data):
        current=self.root
        parrent=None
        for key in data:
            parrent=current
            if key in current.child:
                current=current.child[key]
            else:
                current.child[key]=Node()
                current=current.child[key]
        parrent.end=True

    def print(self):
        def helper(current):
            if current:
                for key in current.child:
                    print(key)
                    if current.end:
                        print()
                    helper(current.child[key])
        helper(self.root)

    def exist(self, data):
        current=self.root
        parrent=None
        for key in data:
            parrent=current
            if current and key not in current.child:
                return(False)
            current=current.child[key]
        if parrent and parrent.end:
            return(True)
        else:
            return(False)
        
        

trie=Trie()
trie.append('alan')
trie.append('stefiya')
trie.append('annliya')
trie.append('dona')
trie.append('amal')
trie.append('diya')
trie.append('alan')
trie.append('amala')
trie.print()
print(trie.exist('stefiya'))


nums = [10,9,2,5,3,7,101,18]

dict={}
n=len(nums)
i=0
while i<n:
    j=i+1
    dict[i]=[]
    while j<n:
        if nums[j]>nums[i]:
            dict[i].append(j)
        j+=1
    i+=1
print(dict)

for i in dict:
    for j in dict[i]:
        count=1
        count+=len(dict[j])


class Node:
    def __init__(self):
        self.child={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=Node()

    def append(self, data):
        current=self.root
        parent=None
        for key in data:
            parent=current
            if key in current.child:
                current=current.child[key]
            else:
                current.child[key]=Node()
                current=current.child[key]
        parent.end=True
            
    
    def search(self, data):
        current=self.root
        parent=None
        for key in data:
            parent=current
            if current and key in current.child:
                current=current.child[key]
            else:
                return False
        if parent and parent.end:
            return True
        return False
    
    def print(self):
        def helper(current):
            if current:
                for key in current.child:
                    print(key,end="")
                    if current.end:
                        print()
                    helper(current.child[key])
        helper(self.root)

    def remove(self, data):
        current=self.root
        parent=None
        for key in data:
            parent=current
            if current and key in current.child:
                current=current.child[key]
            else:
                return
        parent.end=False

        


trie=Trie()
trie.append("alan")
trie.append("amala")
trie.append("arshad")
trie.append("irshad")
trie.append("stefiya")
trie.append("dilna")
trie.append("maria")
trie.append("ritu")
trie.append("mufeedha")
trie.append("shahana")
trie.remove("alan")
print(trie.search("amala"))
trie.print()
        

class Vertex:
    def __init__(self, data=None):
        self.data=data
        self.edge={}

class Graph:
    def __init__(self):
        self.root=None
        self.index={}

    def append(self, data, edge):
        if self.root is None:
            self.root=Vertex(data)
            self.index[data]=self.root
            self.root.edge[edge]=Vertex(edge)
            self.index[edge]=self.root.edge[edge]
            return
        if data not in self.index:
            vertex=Vertex(data)
            self.index[data]=vertex
            if edge not in self.index:
                vertex.edge[edge]=Vertex(edge)
                self.index[edge]=vertex.edge[edge]
            else:
                vertex.edge[edge]=self.index[edge]
        else:
            vertex=self.index[data]
            
            if edge not in self.index:
                vertex.edge[edge]=Vertex(edge)
                self.index[edge]=vertex.edge[edge]
            else:
                vertex.edge[edge]=self.index[edge]

    def print(self):
        dict={}
        def helper(current):
            nonlocal dict
            if current:
                for edge in current.edge:
                    print(current.data)
                    if current not in dict:
                        dict[current]=current.data
                        helper(current.edge[edge])
        for current in self.index:
            helper(self.index[current])


graph=Graph()
graph.append(9,9)
graph.append(4,5)
graph.append(9,3)
graph.append(6,9)
graph.append(1,9)
graph.append(3,6)
graph.append(0,8)
graph.append(8,8)
graph.append(6,9)
graph.append(2,8)
graph.print()


class Vertex:
    def __init__(self, data=None):
        self.data=data
        self.edges={}

class Graph:
    def __init__(self):
        self.index={}

    def append(self, data, edge):
        if data in self.index:
            vertex=self.index[data]
        else:
            vertex=Vertex(data)
            self.index[data]=vertex
        if edge in self.index:
            node=self.index[edge]
            vertex.edges[edge]=node
        else:
            node=Vertex(edge)
            self.index[edge]=node
            vertex.edges[edge]=node

    def print(self):
        dict={}
        def helper(current):
            nonlocal dict
            if current:
                for edge in current.edges:
                    print(current.data, end=" ")
                    if current not in dict:
                        dict[current]=current.data
                        helper(current.edges[edge])
                    else:
                        break
        for current in self.index:
            print(self.index[current])
            helper(self.index[current])



graph=Graph()
graph.append(9,8)
graph.append(4,5)
graph.append(9,4)
graph.append(6,7)
graph.append(1,9)
graph.append(3,3)
graph.append(0,3)
graph.append(8,9)
graph.append(6,3)
graph.append(2,1)
graph.print()

class Graph:
    def __init__(self):
        self.graph={}

    def append(self, data, edge):
        if data not in self.graph:
            self.graph[data]=[]
        self.graph[data].append(edge)

    def print(self):
        for vertex in self.graph:
            print(vertex,"->"," -> ".join(map(str, self.graph[vertex])))

    def remove(self, data, edge):
        if data in self.graph and edge in self.graph[data]:
            self.graph[data].remove(edge)

graph=Graph()
graph.append(0,0)
for i in range(50):
    graph.append(random.randint(0,10),random.randint(0,10))
graph.remove(0,0)
graph.print()

class Graph:
    def __init__(self):
        self.graph={}

    def append(self, data, edge):
        if data not in self.graph:
            self.graph[data]=[]
        self.graph[data].append(edge)

    def bfs(self, start):
        queue=[start]
        arr=set()
        while queue:
            current=queue.pop(0)
            if current not in arr:
                arr.add(current)
                print(current)
                queue.extend(self.graph[current])

    def bredth(self, start):
        queue=[start]
        visited=set()
        while queue:
            vertex=queue.pop(0)
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                queue.extend(self.graph[vertex])

    def dfs(self):
        visited=set()
        for vertex in self.graph:
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
            for edge in self.graph[vertex]:
                if edge not in visited:
                    print(edge)
                    visited.add(edge)


    def print(self):
        for vertex in self.graph:
            print(vertex, "->"," -> ".join(map(str, self.graph[vertex])))

arr=[9,4,9,6,1,3,0,8,6,2]
graph=Graph()
graph.append(0,0)
for i,j in enumerate(arr):
    graph.append(i,j)
graph.dfs()
print("----------------")
for i in range(10):
    graph.bfs(i)

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        queue=[self.root]
        while queue:
            current=queue.pop(0)
            if current.left:
                queue.append(current.left)
            else:
                current.left=node
                break
            if current.right:
                queue.append(current.right)
            else:
                current.right=node
                break
    
    def print(self):
        def helper(current):
            if current:
                print(current.data)
                helper(current.left)
                helper(current.right)
        helper(self.root)


arr=[9,5,3,9,9,6,8,8,9,8]
bt=BinaryTree()
for i in arr:
    bt.append(i)
bt.print()

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        current=self.root
        while True:
            if data < current.data:
                if current.left:
                    current=current.left
                else:
                    current.left=node
                    break
            else:
                if current.right:
                    current=current.right
                else:
                    current.right=node
                    break
    
    def remove(self, data):

        def get_min(current):
            if current.left:
                return get_min(current.left)
            else:
                return current.data
            
        def helper(data, current, parent):
            while current:
                if data < current.data:
                    parent=current
                    current=current.left
                elif data > current.data:
                    parent=current
                    current=current.right
                else:
                    if current.left and current.right:
                        current.data=get_min(current.right)
                        return helper(current.data, current.right, current)
                    else:
                        if parent is None:
                            if current.left:
                                self.root=current.left
                                break
                            else:
                                self.root=current.right
                                break
                        else:
                            if parent.left == current:
                                if current.left:
                                    parent.left=current.left
                                    break
                                    current=current.left
                                else:
                                    parent.left=current.right
                                    break
                                    current=current.right
                            else:
                                if current.left:
                                    parent.right=current.left
                                    break
                                    current=current.left
                                else:
                                    parent.right=current.right
                                    break
                                    current=current.right

        helper(data, self.root, None)

    def find(self, data):
        check=float('inf')
        key=0
        def helper(current):
            nonlocal check, key
            if current:
                if abs(data-current.data)<check:
                    check=abs(data-current.data)
                    key=current.data
                helper(current.left)
                helper(current.right)
        helper(self.root)
        return key

    def print(self):
        def helper(current):
            if current:
                print(current.data)
                helper(current.left)
                helper(current.right)
        helper(self.root)


arr=[9,5,3,9,9,6,1,2,0,8,6,2]
bt=BinarySearchTree()
for i in arr:
    bt.append(i)
bt.remove(9)
bt.print()
print(bt.find(6))


class Heap:
    def __init__(self):
        self.heap=[]
        self.length=0

    def parent(self, i):
        return (i-1)//2
    
    def left_child(self, i):
        return 2*i+1
    
    def right_child(self, i):
        return 2*i+2

    def append(self, data):
        self.heap.append(data)
        self.length+=1
        self.shift_up(self.length-1)

    def remove(self, data):
        for index, value in enumerate(self.heap):
            if value == data:
                self.heap[index]=self.heap[self.length-1]
                self.heap.pop(self.length-1)
                self.length-=1
                self.shift_down(index)

    def shift_down(self, i):
        min_index=i
        left=self.left_child(i)
        right=self.right_child(i)
        
        if left < self.length and self.heap[left] < self.heap[min_index]:
            min_index=left
        if right < self.length and self.heap[right] < self.heap[min_index]:
            min_index=right
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            return self.shift_down(min_index)

    def shift_up(self, i):
        while i>0 and self.heap[self.parent(i)]>self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i=self.parent(i)

    def print(self):
        print(self.heap)

arr=[9,5,3,9,9,6,1,2,0,8,6,2]
heap=Heap()
for i in arr:
    heap.append(i)
heap.remove(8)
heap.print()


class Heap:
    def __init__(self):
        self.heap=[]
        self.length=0

    def parent(self, i):
        return (i-1)//2
    
    def left_child(self, i):
        return 2*i+1
    
    def right_child(self, i):
        return 2*i+2

    def append(self, data):
        self.heap.append(data)
        self.length+=1
        self.shift_up(self.length-1)

    def remove(self, data):
        for index, value in enumerate(self.heap):
            if value == data:
                self.heap[index]=self.heap[self.length-1]
                self.heap.pop(self.length-1)
                self.length-=1
                self.shift_down(index)

    def shift_up(self, i):
        while i>0 and self.heap[i]>self.heap[self.parent(i)]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i=self.parent(i)
    
    def shift_down(self, i):
        min_index=i
        left=self.left_child(i)
        right=self.right_child(i)

        if left < self.length and self.heap[min_index] < self.heap[left]:
            min_index=left
        if right < self.length and self.heap[min_index] < self.heap[right]:
            min_index=right
        if i != min_index:
            self.heap[min_index], self.heap[i] = self.heap[i], self.heap[min_index]
            return self.shift_down(min_index)

    def helper(self, i, j):
        min_index=i
        left=self.left_child(i)
        right=self.right_child(i)

        if left < self.length-j and self.heap[min_index] < self.heap[left]:
            min_index=left
        if right < self.length-j and self.heap[min_index] < self.heap[right]:
            min_index=right
        if i != min_index:
            self.heap[min_index], self.heap[i] = self.heap[i], self.heap[min_index]
            return self.helper(min_index, j)

    def sort(self):
        for i in range(self.length):
            self.helper(0,i)
            self.heap[0], self.heap[self.length-i-1] = self.heap[self.length-i-1], self.heap[0]
        
    def print(self):
        print(self.heap)
        
arr=[9,5,3,9,9,6,1,2,0,8,6,2]
heap=Heap()
for i in arr:
    heap.append(i)
heap.sort()
heap.print()

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        current=self.root
        while True:
            if data < current.data:
                if current.left:
                    current=current.left
                else:
                    current.left=node
                    break
            else:
                if current.right:
                    current=current.right
                else:
                    current.right=node
                    break
    
    def remove(self, data):

        def get_min(current):
            if current.left:
                return get_min(current.left)
            else:
                return current.data
            
        def helper(data, current, parent):
            while current:
                if data < current.data:
                    parent=current
                    current=current.left
                elif data > current.data:
                    parent=current
                    current=current.right
                else:
                    if current.left and current.right:
                        current.data=get_min(current.right)
                        return helper(current.data, current.right, current)
                    else:
                        if parent is None:
                            if current.left:
                                self.root=current.left
                                break
                            else:
                                self.root=current.right
                                break
                        else:
                            if parent.left == current:
                                if current.left:
                                    parent.left=current.left
                                    break
                                    current=current.left
                                else:
                                    parent.left=current.right
                                    break
                                    current=current.right
                            else:
                                if current.left:
                                    parent.right=current.left
                                    break
                                    current=current.left
                                else:
                                    parent.right=current.right
                                    break
                                    current=current.right

        helper(data, self.root, None)

    def find(self, data):
        check=float('inf')
        key=0
        def helper(current):
            nonlocal check, key
            if current:
                if abs(data-current.data)<check:
                    check=abs(data-current.data)
                    key=current.data
                helper(current.left)
                helper(current.right)
        helper(self.root)
        return key

    def print(self):
        def helper(current):
            if current:
                print(current.data)
                helper(current.left)
                helper(current.right)
        helper(self.root)

    def validate(self):
        flag=True
        def helper(current):
            nonlocal flag
            if current:
                if current.left and current.left.data > current.data:
                    flag = False
                if current.right and current.right.data < current.data:
                    flag = False
                helper(current.left)
                helper(current.right)
        helper(self.root)
        return flag


arr=[9,5,3,9,9,6,1,2,0,8,6,2]
bt=BinarySearchTree()
for i in arr:
    bt.append(i)
print(bt.validate())

class Graph:
    def __init__(self):
        self.graph={}

    def append(self, data, edge):
        if data not in self.graph:
            self.graph[data]=[]
        self.graph[data].append(edge)

    def bfs(self, start):
        queue=[start]
        visited=set()
        while queue:
            vertex=queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" -> ")
                visited.add(vertex)
                queue.extend(self.graph[vertex])
        print()

    def dfs(self):
        for vertex in self.graph:
            print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))


arr=[9,4,9,6,1,3,0,8,6,2]
graph=Graph()
graph.append(0,0)
for i,j in enumerate(arr):
    graph.append(i,j)
graph.dfs()
print("----------------")
for i in range(10):
    graph.bfs(i)

class Node:
    def __init__(self, data):
        self.data=data

class HashSet:
    def __init__(self):
        self.size=1000
        self.map=[None]*self.size

    def _hash(self, key):
        return hash(key)%self.size
    
    def add(self, key, value):
        hashed=self._hash(key)
        if not self.map[hashed]:
            self.map[hashed]=Node()


class HashMap:
    def __init__(self, size):
        self.size=size
        self.map=self.create()

    def create(self):
        return [[] for _ in range(self.size)]
    
    def hash(self, key):
        return hash(key)%self.size

    def add(self, key, value):
        hashed=self.hash(key)
        queue=self.map[hashed]
        found=False
        for index, record in enumerate(queue):
            k, v = record
            if k == key:
                found=True
                break
        if found:
            queue[index]=(key, value)
        else:
            queue.append((key, value))


    def print(self):
        for x in self.map:
            key, value = x[0]
            print(key, value)


arr=[9,5,3,9,9,6,1,2,0,8,6,2]
bt=HashMap(len(arr))
for i, j in enumerate(arr):
    bt.add(i, j)
bt.print()

class HashSet:
    def __init__(self, size):
        self.size=size
        self.table=[None]*self.size

    def hash(self, key):
        return key%self.size
    
    def add(self, key):
        index = self.hash(key)
        if not self.table[index]:
            self.table[index]=[]
        if key not in self.table[index]:
            self.table[index].append(key)
        
    def print(self):
        print(self.table)
            

arr=[9,5,3,9,9,6,1,2,0,8,6,2]
hash=HashSet(len(arr))
for i in arr:
    hash.add(i)

hash.print()
        

class MyHashSet:
    def __init__(self):
        self.size = 10
        self.buckets = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = []
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if self.buckets[index] and key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return self.buckets[index] and key in self.buckets[index]
    
    def print(self):
        print(self.buckets)

# Example usage:
hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(9))  # Output: True
print(hashSet.contains(3))  # Output: False
hashSet.add(2)
print(hashSet.contains(2))  # Output: True
hashSet.remove(2)
print(hashSet.contains(2))  # Output: False
hashSet.print()

order = "kqep"
s = "pekeq"

i=0
while i<len(order):
    if order[i] in s:
        s=s[:s.index(order[i])]+s[s.index(order[i])+1:]
    else:
        order=order[:order.index(order[i])]+order[order.index(order[i])+1:]
    i+=1
print(order+s)


arr = [0,2]

while i<len(arr):
            if arr[i]==0:
                del arr[i]
                i-=1
            j=0
            while j<i:
                if(functools.reduce(lambda x,y:x+y, arr[j:i]) + arr[i] == 0):
                    temp = arr[:j]
                    temp.extend(arr[i+1:])
                    arr=temp
                    i=j-1
                    break
                j+=1
            i+=1
print(arr)

nums = [20,14,21,10]
divisors = [5,7,5]

ord={}
i=0
check=0
val=0
while i<len(divisors):
    if divisors[i] not in ord:
        ord[divisors[i]]=0
        j=0
        while j<len(nums):
            if nums[j]%divisors[i]==0:
                ord[divisors[i]]+=1
                if ord[divisors[i]]>check:
                    check=ord[divisors[i]]
                    val=divisors[i]
            j+=1
    i+=1

print(val)

nums = [0,1,1,1,1,1]
out=''
i=0
while i<len(nums):
    out+=bin(nums[i])[2:]
    print(int(out, 2))
    if int(out)%5==0:
        nums[i]=True
    else:
        nums[i]=False
    i+=1
print(out)

nums = [1,3,-1,-3,5,3,6,7]
k = 3

arr=[]
for i in range(len(nums)-(k-1)):
    print(sorted(nums[i:i+k]))

print(nums)

nums = [1,3,-1,-3,5,3,6,7]
arr=[0]*20
for i in range(len(nums)):
    arr[i]=nums[i]
print(arr[:i+1])

n=8
arr=[0]*n
for i in range(n):
    arr[i]=i+1
for i in range(1,len(arr)):
    print(arr[:i+1], arr[i:], functools.reduce(lambda x,y:x+y, arr[:i+1]),functools.reduce(lambda x,y:x+y, arr[i:]))

n=6
dp=[1]*n
for i in range(1,n):
    count=0
    for j in range(n):
        if i==1:
            if j%2==1:
                dp[j]=0

        elif i==2:
            count+=1
            if count==3:
                count=1
                dp[j]=0 if dp[j]==1 else 1

        else:
            dp[j]=0 if dp[j]==1 else 1
if n>3:       
    dp[-1]=0 if dp[-1]==1 else 1

n=6
dp=[1]*n
for i in range(2,n+1):
    for j in range(i-1,n,i):
        dp[j]=0 if dp[j]==1 else 1
    print(dp, i-1)

a=["MyLinkedList","addAtHead","addAtTail","addAtTail","get","get","addAtTail","addAtIndex","addAtHead","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","get","addAtHead","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtTail","deleteAtIndex","addAtHead","addAtHead","addAtIndex","addAtTail","get","addAtIndex","addAtTail","addAtHead","addAtHead","addAtIndex","addAtTail","addAtHead","addAtHead","get","deleteAtIndex","addAtTail","addAtTail","addAtHead","addAtTail","get","deleteAtIndex","addAtTail","addAtHead","addAtTail","deleteAtIndex","addAtTail","deleteAtIndex","addAtIndex","deleteAtIndex","addAtTail","addAtHead","addAtIndex","addAtHead","addAtHead","get","addAtHead","get","addAtHead","deleteAtIndex","get","addAtHead","addAtTail","get","addAtHead","get","addAtTail","get","addAtTail","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtHead","deleteAtIndex","get","addAtHead","addAtIndex","addAtTail","get","addAtIndex","get","addAtIndex","get","addAtIndex","addAtIndex","addAtHead","addAtHead","addAtTail","addAtIndex","get","addAtHead","addAtTail","addAtTail","addAtHead","get","addAtTail","addAtHead","addAtTail","get","addAtIndex"]
b=[[],[84],[2],[39],[3],[1],[42],[1,80],[14],[1],[53],[98],[19],[12],[2],[16],[33],[4,17],[6,8],[37],[43],[11],[80],[31],[13,23],[17],[4],[10,0],[21],[73],[22],[24,37],[14],[97],[8],[6],[17],[50],[28],[76],[79],[18],[30],[5],[9],[83],[3],[40],[26],[20,90],[30],[40],[56],[15,23],[51],[21],[26],[83],[30],[12],[8],[4],[20],[45],[10],[56],[18],[33],[2],[70],[57],[31,24],[16,92],[40],[23],[26],[1],[92],[3,78],[42],[18],[39,9],[13],[33,17],[51],[18,95],[18,33],[80],[21],[7],[17,46],[33],[60],[26],[4],[9],[45],[38],[95],[78],[54],[42,86]]
c={}
for i in range(len(a)):
    c[i]=(a[i],b[i])
for i in c:
    print(c[i])

print(c[45])


from sortedcontainers import SortedList

nums = [1,3,-1,-3,5,3,6,7]
k = 3

n=len(nums)
arr=[0]*(n-k+1)
dp=SortedList(nums[:k])
for i in range(n-k+1):
    if k%2==0:
        arr[i]=(dp[k//2]+dp[(k//2)-1])/2
    else:
        arr[i]=dp[k//2]
    if i+k<n:
        dp.remove(nums[i])
        dp.add(nums[i+k])
        print(dp)
print(arr)

nums=[1,-1,0]
k=0
count=0
n=len(nums)
i=0
while i<n:
    j=i+1
    while j<=n:
        if functools.reduce(lambda x,y:x+y, nums[i:j]) == k:
            count+=1
        j+=1
    i+=1
print(count)

candidates = [2,3,5]
target = 8

arr=[]
n=len(candidates)
i=0
while i<n:
    j=i+1
    while j<=n:
        k=0
        while True:
            if functools.reduce(lambda x,y:x+y, candidates[i:j])+candidates[i]*k > target:
                break
            if functools.reduce(lambda x,y:x+y, candidates[i:j])+candidates[i]*k == target:
                print(str(candidates[i])*k,candidates[i:j])
            k+=1
        j+=1
    i+=1


nums = [1,0,1,0,1]

arr = []

i=0
count = Counter(nums)

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
arr=[]
i=0
n=len(words)
while i<n:
    strs=' '
    count=0
    j=i
    while j<n:
        if len(words[j])+count < maxWidth:
            count+=len(words[j])+1
        else:
            break
        j+=1
    strs=strs*((maxWidth-(count-j+i))//(j-i-1) if j-i-1 >0 else j-1)
    arr.append(strs.join(map(str, words[i:j])))
    i=j
print(arr)

path = "/home///..//"
a='acb'

res='/'

for i in range(len(path)):
    if bool(re.match('^[/ _ .]+$',path[i])):
        if len(res)>1 and bool(re.match('^[/]+$',res[-1])) == False:
            res+='/'
        continue
    res+=path[i]
if len(res)>1 and res[-1]=='/':
    res=res[:-1]
print(res)

intervals = [[1,5]]
newInterval = [2,3]
arr=[]
n=len(intervals)
i=0
check=True
while i<n:
    j=i
    flag=False
    x=newInterval[0]
    y=newInterval[1]
    while j<n and intervals[j][0] in range(newInterval[0], newInterval[1]+1) or j<n and intervals[j][1] in range(newInterval[0], newInterval[1]+1):
        x=min(intervals[j][0],x)
        y=max(intervals[j][1],y)
        print(1)
        j+=1
        flag=True
    if flag:
        check=False
        arr.append([x,y])
        i=j
        continue
    elif newInterval[0] in range(intervals[i][0], intervals[i][1]+1) or newInterval[1] in range(intervals[i][0], intervals[i][1]+1):
        check=False
    arr.append(intervals[i])
    i+=1
if check:
    arr.extend([newInterval])
print(arr)

intervals = [[1,4],[0,2],[3,5]]
intervals.sort()
arr=[]
i=0
n=len(intervals)
while i<n:
    j=i+1
    flag=False
    x=intervals[i][0]
    y=intervals[i][1]
    while j<n and intervals[j][0] in range(intervals[i][0], intervals[i][1]+1) or j<n and intervals[j][1] in range(intervals[i][0], intervals[i][1]+1):
            flag=True
            x=min(intervals[j][0], x)
            y=max(intervals[j][1], y)
            intervals[i][0]=x
            intervals[i][1]=y
            j+=1
    if flag:
        arr.append([x,y])
        i=j
        continue
    arr.append(intervals[i])
    i+=1
print(arr)
 
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        queue=[self.root]
        while queue:
            current=queue.pop(0)
            if current.left:
                queue.append(current.left)
            else:
                current.left=node
                break
            if current.right:
                queue.append(current.right)
            else:
                current.right=node
                break
        
    def print(self):
        def helper(current):
            if current:
                print(current.data)
                helper(current.left)
                helper(current.right)
        helper(self.root)


arr=[9,4,9,6,1,3,0,8,6,2]
bt=BinaryTree()
for i in arr:
    bt.append(i)

bt.print()

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        current=self.root
        while True:
            if data<current.data:
                if current.left:
                    current=current.left
                else:
                    current.left=node
                    break
            else:
                if current.right:
                    current=current.right
                else:
                    current.right=node
                    break

    def print(self):
        def helper(current):
            if current:
                print(current.data)
                helper(current.left)
                helper(current.right)
        helper(self.root)

    def remove(self, data):
        def get_min(current):
            if current.left:
                return get_min(current.left)
            else:
                return current.data
            
        def helper(data, current, parent):
            while current:
                if data<current.data:
                    parent=current
                    current=current.left
                elif data>current.data:
                    parent=current
                    current=current.right
                else:
                    if current.left and current.right:
                        current.data=get_min(current.right)
                        helper(current.data, current.right, current)
                    else:
                        if parent is None:
                            if current.left:
                                self.root=current.left
                                current=current.left
                            else:
                                self.root=current.right  
                                current=current.right
                        else:
                            if current == parent.left:
                                if current.left:
                                    parent.left=current.left
                                    current=current.left
                                else:
                                    parent.left=current.right
                                    current=current.right
                            else:
                                if current.left:
                                    parent.right=current.left
                                    current=current.left
                                else:
                                    parent.right=current.right
                                    current=current.right
        helper(data, self.root, None)
        

arr=[9,4,9,6,1,3,0,8,6,2]
bt=BinarySearchTree()
for i in arr:
    bt.append(i)
bt.remove(9)
bt.print()

class Heap:
    def __init__(self):
        self.heap=[]
        self.length=0

    def parent(self, i):
        return (i-1)//2
    
    def left_child(self, i):
        return 2*i+1

    def right_child(self, i):
        return 2*i+2
    
    def append(self, data):
        self.heap.append(data)
        self.length+=1
        self.shift_up(self.length-1)

    def shift_up(self, i):
        while i>0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i=self.parent(i)

    def shift_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left<self.length and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right<self.length and self.heap[right] < self.heap[min_index]:
            min_index = right
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            return self.shift_down(min_index)
        

    def helper(self, i, j):
        min_index=i
        left=self.left_child(i)
        right=self.right_child(i)

        if left < self.length-j and self.heap[min_index] < self.heap[left]:
            min_index=left
        if right < self.length-j and self.heap[min_index] < self.heap[right]:
            min_index=right
        if i != min_index:
            self.heap[min_index], self.heap[i] = self.heap[i], self.heap[min_index]
            return self.helper(min_index, j)

    def sort(self):
        for i in range(self.length):
            self.helper(0,i)
            self.heap[0], self.heap[self.length-i-1] = self.heap[self.length-i-1], self.heap[0]
    
    def remove(self, index):
        if index < self.length:
            self.heap[index]=self.heap[self.length-1]
            self.heap.pop(self.length-1)
            self.length-=1
            self.shift_up(index)
            self.shift_down(index)

    def print(self):
        print(self.heap)



arr=[9,4,9,6,1,3,0,8,6,2]
heap=Heap()
for i in arr:
    heap.append(i)
heap.remove(0)
heap.sort()
heap.print()

class Graph:
    def __init__(self):
        self.log={}

    def append(self, key, edge):
        if key not in self.log:
            self.log[key]=[]

        if edge not in self.log[key]:
            self.log[key].append(edge)


    def remove(self, key, edge):
        if key in self.log and edge in self.log[key]:
            self.log[key].remove(edge)

    def print(self):
        for key in self.log:
            print(key," -> ", " -> ".join(map(str, self.log[key])))

    

graph=Graph()
for i in range(100):
    graph.append(random.randint(0,10), random.randint(0,10))
graph.print()

class Node:
    def __init__(self):
        self.child={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=Node()

    def add(self, data):
        parent=None
        current=self.root
        for key in data:
            parent=current
            if key in current.child:
                current=current.child[key]
            else:
                current.child[key]=Node()
                current=current.child[key]
        parent.end=True

    def check(self, data):
        parent=None
        current=self.root
        for key in data:
            if key in current.child:
                parent=current
                current=current.child[key]
            else:
                return False
        return True if parent.end else False

trie=Trie()
trie.add("alan")
trie.add("selena")
print(trie.check('selena'))

def bfs(start, graph):
    queue=[start]
    visited=set()
    while queue:
        current=queue.pop(0)
        if current not in visited:
            visited.add(current)
            print(current)
            queue.extend(graph[current])


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        current=self.root
        while True:
            if data < current.data:
                if current.left:
                    current=current.left
                else:
                    current.left=node
                    break
            else:
                if current.right:
                    current=current.right
                else:
                    current.right=node
                    break
        
    def remove(self, data):
        def get_min(current):
            if current.left:
                return get_min(current.left)
            else:
                return current.data

        def helper(data, current, parent):
            while current:
                if data < current.data:
                    parent=current
                    current=current.left
                elif data > current.data:
                    parent=current
                    current=current.right
                else:
                    if current.left and current.right:
                        current.data=get_min(current.right)
                        return helper(current.data, current.right, current)
                    else:
                        if parent is None:
                            if current.left:
                                self.root=current.left
                            else:
                                self.root=current.right
                        else:
                            if parent.left == current:
                                if current.left:
                                    parent.left=current.left
                                    current=current.left
                                else:
                                    parent.left=current.right
                                    current=current.right
                            else:
                                if current.left:
                                    parent.right=current.left
                                    current=current.left
                                else:
                                    parent.right=current.right
                                    current=current.right


        helper(data, self.root, None)

    def print(self):
        def helper(current):
            if current:
                print(current.data)
                helper(current.left)
                helper(current.right)
        helper(self.root)


arr=[9,4,9,6,1,3,0,8,6,2]

bst=BinarySearchTree()
for i in arr:
    bst.append(i)
bst.remove(1)
bst.print()


nums=[1,2,3,1,2,3]
k=2

n=len(nums)
i=0
while i<n-1:
    j=i+1
    while j<n:
        if nums[i]==nums[j] and abs(i-j)<=k:
            print(True)
        j+=1
    i+=1
print(False)

nums=[1,2,3,1,2,3]
k=2

n=len(nums)
dict={}
i=0
while i<n:
    if nums[i] in dict:
        if abs(dict[nums[i]]-i)<=k:
            print(True)
        else:
            dict[nums[i]]=i
    else:
        dict[nums[i]]=i

columnNumber = 2147483647
arr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print((columnNumber-(columnNumber%26)))

n=100
arr=[4,6,7,8,9]
m=len(arr)
i=2
j=1
while j<n:
    k=3
    prime=False
    while k<i:
        if i%k==0:
            prime=True
        k+=1
    l=0
    flag=True
    while l<m and arr[l]<i:
        if i%arr[l]==0:
            flag=False
        l+=1
    if prime and flag:
        print(i)
        j+=1

    i+=1

print(303%9)

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

sum=triangle[0][0]
current=triangle[0][0]
n=len(triangle)
for i in range(1, n):
    m=min(triangle[i])
    current=max(current, current+m)
    sum=max(sum, current)
print(sum)

arr=[9,8,7,6,5,4]

val=max(arr)
print(arr[arr.index(val):])

nums=[1,0,1]
k=2

i=0
n=len(nums)
last=-1
while i<n:
    if nums[i]==1:
        if last>=0:
            if i-(last+1) < k:
                print (False)
        last=i
    i+=1
print (True)

arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]

n=len(arr)

count=int(n*0.05)
arr=arr[count:n-count]
x=sum(arr)

a=b=c=0
print(a,b,c)

n=10

dp=[0]*n
dp[0]=1
x=y=z=0
for i in range(1,n):
    dp[i]=min(dp[x]*2, dp[y]*3, dp[z]*5)
    if dp[x]*2 == dp[i]:
        print(dp[x]*2)
        x+=1
    if dp[y]*3 == dp[i]:
        print(dp[y]*3)
        y+=1
    if dp[z]*5 == dp[i]:
        print(dp[z]*5)
        z+=1
print (dp[-1])



print(a[0]*a.count(a[0]))

print(3/2, 3//2)

class Node:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data=data
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        current=self.root
        while True:
            if data<current.data:
                if current.left:
                    current=current.left
                else:
                    current.left=node
                    break
            else:
                if current.right:
                    current=current.right
                else:
                    current.right=node
                    break

    def display(self):
        def helper(current):
            if current:
                print(current.data)
                helper(current.left)
                helper(current.right)
        helper(self.root)
    
    def remove(self, data):
        def get_min(current):
            if current.left:
                return get_min(current.left)
            else:
                return current.data
            
        def helper(data, current, parent):
            while current:
                if data < current.data:
                    parent=current
                    current=current.left
                elif data > current.data:
                    parent=current
                    current=current.right
                else:
                    if current.left and current.right:
                        current.data=get_min(current.right)
                        return helper(current.data, current.right, current)
                    else:
                        if parent is None:
                            if current.left:
                                self.root=current.left
                            else:
                                self.root=current.right
                        else:
                            if parent.left == current:
                                if current.left:
                                    parent.left=current.left
                                    current=current.left
                                else:
                                    parent.left=current.right 
                                    current=current.right
                            else:
                                if current.left:
                                    parent.right=current.left
                                    current=current.left
                                else:
                                    parent.right=current.right
                                    current=current.right
        helper(data, self.root, None)

arr=[9,4,9,6,1,3,0,8,6,2]
bst=BinarySearchTree()
for i in arr:
    bst.append(i)
bst.remove(0)
bst.display()
                        

arr = [10,13,17,21,15,15,9,17,22,22,13]
k=float('inf')
i=0
n=len(arr)
while i<n:
    j=i
    while j<n:
        if(arr[:i]+arr[j:] == sorted(arr[:i]+arr[j:]) and j-i<k):
            k=j-i
            print(arr[:i]+arr[j:])

        j+=1
    i+=1
print(k)

s = "RLRRLLRLRL"
print(len(s))
r="R"
l="L"
i=1
count=1
while i<len(s):
    if(s[:i*2] == (r*(i))+(l*(i))):
        s=s[i*2:]
        count+=1
        i=1
    else:
        i+=1
print(count, s)

print(s[::-1])


n = 3
start = 2

dp=[]
i=0
while i<2**n:
    stg=bin(start)[2:]
    stg=("0"*(n-len(stg)))+stg if n-len(stg)>0 else stg
    j=0
    while j<n:
        print(stg[:j]+stg[j+1:])
        j+=1
    start=stg
    i+=1
print(dp)

nums=[4,3,2,7,8,2,3,1]

arr=list(set(filter(lambda x:nums.count(x)>1, nums)))
print(arr)

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BST:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        current=self.root
        while True:
            if data < current.data:
                if current.left:
                    current=current.left


s = "aabaaaacaabc"
ls=set(s)
obj={}
count={}
n=len(s)
i=0
j=n-1
while i<=j:
    if i != j:
        if s[i] in obj:
            obj[s[i]].append(i+1)
        else:
            obj[s[i]]=[i+1]

        if s[j] in count:
            count[s[j]].append(n-j)
        else:
            count[s[j]]=[n-j]
    else:
        if s[i] in obj:
            obj[s[i]].append(i+1)
        else:
            obj[s[i]]=[i+1]
    i+=1
    j-=1

print(obj, count)
for i in ls:
    if i in obj and i in count:

arr=[1,2,3,4,5,6,7,8]

def split(arr):
    if len(arr)>=1:
        mid=len(arr)//2
        print(arr[mid])
        del arr[mid]
        left=arr[:mid]
        right=arr[mid:]
        
        split(left)
        split(right)
        
split(arr)

descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
obj={}
parent=[]
child={}
for x in descriptions:
    child[x[1]]=False
    if x[0] not in parent and x[0] not in child:
        parent.append(x[0])
    if x[1] in parent:
        parent.remove(x[1])
    if x[0] not in obj:
        obj[x[0]]={}
    if x[2]==0:
        obj[x[0]][1]=x[1]
    else:
        obj[x[0]][0]=x[1]

queue=[parent[0]]
while queue:
    print(queue[0])
    current=queue.pop(0)
    if current in obj:
        queue.extend(obj[current])


s = "PAYPALISHIRING"
numRows = 2
stg=""
dp=[[] for _ in range(numRows)]
i=0
flag=True
for x in s:
    dp[i].append(x)
    if flag:
        i+=1
    else:
        i-=1
    if i>=numRows-1:
        flag=False
    elif i<=0:
        flag=True

for x in dp:
    stg+="".join(map(str, x))
print(stg)

nums = [10,5,2,6]
k = 100

n=len(nums)
count=0
i=0
while i<n:
    j=i+1
    while j<n+1:
        if (functools.reduce(lambda x,y:x*y, nums[i:j])) < k:
            count+=1
        j+=1
    i+=1
print(count)

s = "bbbab"
n=len(s)
i=0
count=0
while i<n:
    j=i+1
    while j>i: 
        l=s[i:j]
        print(l)
        if l==l[::-1]:
            count=max(count,len(l))
        j-=1
    i+=1

s = "(1)+((2))+(((3)))"

dict={0:0}
count=0
for i in s:
    if i=='(':
        dict[0]+=1
    elif i==')':
        dict[0]-=1
    count=max(count, dict[0])
print(count)

s = "abBAcC"

i=0
while i<len(s)-1:
    if(s[i] == s[i].lower() and s[i+1] == s[i+1].upper() and s[i] == s[i+1].lower() or s[i] == s[i].upper() and s[i+1] == s[i+1].lower() and s[i].lower() == s[i+1]):
        s=s[:i]+s[i+2:]
        if i>0:
            i-=1
        continue
    i+=1
print(s)

s = "abcde1"

i=0
count=1
tot=1
n=len(s)-2
while i<n:
    if(ord(s[i+1])-ord(s[i]) == 1):
        count+=1
    else:
        count=1
    tot=max(tot,count)
    i+=1
print(tot)

s = "))(("

arr=[]
x=0
while x<len(s):
    if s[x] == '(':
        arr.append(s[x])
    elif s[x] == ')':
        if len(arr)>0:
            arr.pop()
        else:
            s=s[:x]+s[x+1:]
            continue
    x+=1
print(s)
        
height = [0,1,0,2,1,0,1,3,2,1,2,1]

n=len(height)
count=0
i=0
while i<n:
    j=i+1
    while j<n:
        if height[j]>=height[i]:
            i=j
            break
        count+=height[i]-height[j]
        print(count)
        j+=1
    i+=1
print(count)
    
pref = [13]

i=1
n=len(pref)
dp=[0]*n
dp[0]=pref[0]
j=0
while i<=n:
    if j>0:
        dp[i-1]=(functools.reduce(lambda x,y:x^y, dp[:i])^pref[j])
    i+=1
    j+=1
print(dp)

print(7^2)
import datetime

now = datetime.datetime.now()

print(now)

img = [[100,200,100],[200,50,200],[100,200,100]]
n=len(img)
arr = [0]*n*n
l=0
i=0
while i<n:
    j=0
    while j<n:
        k=img[i][j]
        count=1
        if i>0:
            k+=img[i-1][j]
            
            count+=1
        if i<n-1:
            k+=img[i+1][j]
            
            count+=1
        
        if j>0:
            k+=img[i][j-1]
            
            count+=1
        if j<n-1:
            k+=img[i][j+1]
           
            count+=1

        if i>0 and j>0:
            k+=img[i-1][j-1]
     
            count+=1
        if i>0 and j<n-1:
            k+=img[i-1][j+1]
            count+=1

        if i<n-1 and j>0:
            k+=img[i+1][j-1]
            count+=1

        if i<n-1 and j<n-1:
            k+=img[i+1][j+1]
            count+=1
        arr[l]=(k//count)
        l+=1
        j+=1
    i+=1
import itertools
keyfunc = lambda filename: filename[:3]
grouper = itertools.groupby(arr, keyfunc)
result = [list(arr) for _, arr in grouper]
print(arr)


s = "hello"
out = 0
for i in range(len(s)-1):
    out += abs(ord(s[i]) - ord(s[i+1]))

    print(out)

str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

n=len(str1)
m=len(str2)
print(m, n)
while len(str2)>1:
    print(str1 == str2)
    str2 = str2[:len(str2)//2]
    


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

n=len(arr1)
m=len(arr2)
k=0

for i in range(m):
    for j in range(n):
        if arr2[i] == arr1[j]:
            del arr1[j]
            arr1.insert(0, arr2[i])
            k+=1


print(arr1[:k][::-1]+sorted(arr1[k:]))


nums = [23,2,4,6,7]
k = 6

i=0
n=len(nums)
while i<n-1:
    j=i+2
    while j<=n:
        if(sum(nums[i:j])/k) == (sum(nums[i:j])//k):
            print(True)
        j+=1
    i+=1
print(False)

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "bbbcccdddaaa"

n=len(s)
count=0
k=0
for i in range(n):
    if k>100:
        count+=1
        k=widths[i]
    k+=widths[i]
if k>0:
    count+=1
print(count, k)


arr=[1,2,3,4,5]

dp=[]
for i in arr:
    temp=[]
    for j in range(1,i):
        n = (int((len(str(temp))/2)-1))
        eval('temp'+'[0]'*n).append([])
    dp.append(temp)  
print(dp)

seats = [3,1,5]
students = [2,7,4]

n=len(seats)
a = list(seats)
b = list(students)
k=0
for i in range(n):
    k += abs(seats.index(min(a)) - students.index(min(b)))
    del a[a.index(min(a))]
    del b[b.index(min(b))]

print(k)
    

arr = [3,6,4,7,9,5,2]
n=len(arr)
def helper(arr):
    if len(arr)==1:
        return arr[0]
   
    if arr[0]>arr[1]:
        del arr[1]
    else:
        del arr[0]
    return helper(arr)

print(helper(arr))
's'.capitalize()

class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
        

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self, data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.tail=self.head
        else:
            self.tail.next=node
            self.tail=node
        return
    
    def display(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        current=self.head
        previous=None
        while current:
            if current.data == data:
                previous.next=current.next
                return
            previous=current
            current=current.next

    def reverse(self):
        current=self.head
        previous=None
        while current:
            net = current.next
            current.next=previous
            previous=current
            current=net
        self.head=previous
        
        




ll=LinkedList()
arr=[1,2,3,4,5,6]
for i in arr:
    ll.append(i)


ll.reverse()
ll.display() 
arr=[1,2,3,4,5,6]
print(arr[::-1])


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left:
                    current=current.left
                else:
                    current.left = node
                    return
            else:
                if current.right:
                    current=current.right
                else:
                    current.right=node
                    return
    
    def display(self):

        def helper(current):
            if current:
                print(current.data)
                helper(current.left)
                helper(current.right)
        helper(self.root)

bst=BinarySearchTree()
arr=[1,2,5,3,4,5,6]
for i in arr:
    bst.append(i)

bst.display()

def join(left, right):

    i=0
    j=0
    arr=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1
    while i<len(left):
        arr.append(left[i])
        i+=1

    while j<len(right):
        arr.append(right[j])
        j+=1
    return arr
def merge(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    return join(merge(left), merge(right))

ls=[9,4,9,6,1,3,0,8,6,2]
print(merge(ls))

ls=[9,4,9,6,1,3,0,8,6,2]

def quick(start, end):
    if start>=end:
        return
    
    pivot = start
    left = start+1
    right = end

    while left<=right:
        if ls[left]>ls[pivot] and ls[right]<ls[pivot]:
            ls[left], ls[right] = ls[right], ls[left]
            left+=1
            right-=1
        
        if ls[left]<=ls[pivot]:
            left+=1
        
        if ls[right]>=ls[pivot]:
            right-=1
    
    ls[pivot], ls[right] = ls[right], ls[pivot]
    quick(start, right-1)
    quick(right+1, end)
    return ls

print(quick(0, len(ls)-1))


class Heap:

    def __init__(self):
        self.heap=[]

    def parent(self, i):
        return (i-1)//2
    
    def left_child(self, i):
        return 2*i+1
    
    def right_child(self, i):
        return 2*i+2
    
    def append(self, data):
        self.heap.append(data)
        self.shift_up(len(self.heap)-1)

    def remove(self, data):
        for i, x in enumerate(self.heap):
            if x == data:
                self.heap[i] = self.heap[len(self.heap)-1]
                self.heap.pop(len(self.heap)-1)
                self.shift_down(0)
    
                
    def shift_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        while left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        while right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        if min_index != i:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.shift_down(min_index)

    def shift_up(self, i):
        while i>0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def print(self):
        print(self.heap)


class Heap:

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)//2
    
    def left(self, i):
        return (i*2)+1
    
    def right(self, i):
        return (i*2)+2

    def append(self, data):
        self.heap.append(data)
        self.up(len(self.heap)-1)


    def up(self, i):
        while i>0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    
    def down(self, i):
        min_index = i
        left = self.left(i)
        right = self.right(i)

        while left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        while right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.down(min_index)

    def print(self):
        print(self.heap)

    def remove(self, data):
        for i, x in enumerate(self.heap):
            if x == data:
                self.heap[i] = self.heap[len(self.heap)-1]
                self.heap.pop(len(self.heap)-1)
                self.down(0)


arr=[8,5,4,7,9,3,3,9,3,1]
heap = Heap()
for i in arr:
    heap.append(i)
heap.remove(1)
heap.print()


class Heap:

    def __init__(self):
        self.heap=[]

    def parent(self, i):
        return (i-1)//2
    
    def left(self, i):
        return (i*2)+1
    
    def right(self, i):
        return (i*2)+2
    
    def append(self, data):
        self.heap.append(data)
        self.up(len(self.heap)-1)

    def remove(self):
        self.heap[0] = self.heap[len(self.heap)-1]
        self.down(0)
    

    def print(self):
        print(self.heap)

    def up(self, i):
        while i>0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i=self.parent(i)

    def down(self, i):
        min_index = i
        left = self.left(i)
        right = self.right(i)

        while left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        while right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
        
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.down(min_index)
    

heap = Heap()

arr=[9,4,9,6,1,3,0,8,6,2]
for i in arr:
    heap.append(i)
heap.remove()
heap.print()

arr=[9,4,9,6,1,3,8,6,2]

print(functools.reduce( lambda x,y:x*y, arr))

class Vertex:
    def __init__(self, data=None):
        self.data=data
        self.edges={}

class Graph:
    def __init__(self):
        self.index={}

    def append(self, data, edge):
        if data in self.index:
            vertex=self.index[data]
        else:
            vertex=Vertex(data)
            self.index[data]=vertex
        if edge in self.index:
            node=self.index[edge]
            vertex.edges[edge]=node
        else:
            node=Vertex(edge)
            self.index[edge]=node
            vertex.edges[edge]=node

    def print(self):
        dict={}
        def helper(current):
            nonlocal dict
            if current:
                for edge in current.edges:
                    print(current.data, end=" ")
                    if current not in dict:
                        dict[current]=current.data
                        helper(current.edges[edge])
                    else:
                        break
        for current in self.index:
            print(self.index[current])
            helper(self.index[current])



graph=Graph()
graph.append(9,8)
graph.append(4,5)
graph.append(9,4)
graph.append(6,7)
graph.append(1,9)
graph.append(3,3)
graph.append(0,3)
graph.append(8,9)
graph.append(6,3)
graph.append(2,1)
graph.print()


class Vertex:
    def __init__(self, data=None):
        self.data=data
        self.edges={}

class Graph:
    def __init__(self):
        self.index={}

    def append(self, data, edge):
        if data in self.index:
            vertex=self.index[data]
        else:
            vertex=Vertex(data)
            self.index[data]=vertex
        if edge in self.index:
            node=self.index[edge]
        else:
            node=Vertex(edge)
            self.index[edge]=node
        if edge not in vertex.edges:
            vertex.edges[edge]=node
    

class Node:
    def __init__(self):
        self.child={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=Node()

    def append(self, )

n='stg'
for i in n:
    print(ord(i))


s = "abc"
t = "bac"

s = {x:i for i,x in enumerate(s)}
t = {x:i for i,x in enumerate(t)}
k=0
for i in s:
    k+=abs(s[i]-t[i])
print(k)

print(ord('z'))

arr=[1]

print(arr[1:])

name = "alex"
typed = "aaleexa"

i,j,prev = 0,0,0

while i<len(name) and j<len(typed):
    if name[i] == typed[j]:
        prev=name[i]
        i+=1
        j+=1
    elif prev == typed[j]:
        j+=1
    else:
        print(False)
print(set(name[i-1:]), set(typed[j-1:]))

print(random.randint(1,3))

count = sorted()
        
print(sum([4,6,5,7,8]))

a = 'aabbcc'

print(''.join(Counter(a)))
arr = [1,2,3,4,5,6,7]
x = [x*2 for x in arr if x%2==0]
print(x)

arr = [1,2,3,4,5,6,7,8]

# x = functools.reduce( lambda x,y:x+y, arr)
# print(x)

x = lambda x,y : arr[1]+arr[2]
print(x)

arr = [1,2,3,45,5]

x = list(filter(lambda x : x%2==0, arr))
print(x)

def x_dx(x_dy):
    print(5*10)
    return x_dy

@x_dx
def x_dy():
    print(10*10)
    return x_dx(x_dy)

x_dy()

def x_gen():
    x, y = 0, 1
    while True:
        yield x*y
        x, y = y, x+y

x = x_gen()
for z in range(10):
    print(next(x))

s='justinram'

for x in s:
    print(x)

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def append(self, data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        current=self.root
        while True:
            if data<current.data:
                if current.left:
                    current=current.left
                else:
                    current.left=node
                    break
            else:
                if current.right:
                    current=current.right
                else:
                    current.right=node
                    break
        
    def print(self):
        def helper(current):
            if current:
                print(current.data)
                helper(current.left)
                helper(current.right)
        helper(self.root)


bst=BinarySearchTree()
arr=[9,4,9,6,1,3,0,8,6,2]

for el in arr:
    bst.append(el)
bst.print()

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name=name
        return self.name
    
p=Person('Alan', 23)
print(p.get_name())
p.set_name('Stefiya')
print(p.get_name())

from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def display(self):
        pass

class Call(Person):

    def display(self):
        return "Name"
    

c=Call()
print(c.display())


arr=[3,2,4,6,8,1]
x= lambda x,y:x+y, arr
print(x)
dp=[x*2 for x in arr]
print(dp)

def quickSort(arr, start, end):
    if start>=end:
        return 
    pivot=start
    left=start+1
    right=end

    while left<=right:
        if arr[left]>arr[pivot] and arr[right]<arr[pivot]:
            arr[left], arr[right]=arr[right], arr[left]
            left+=1
            right-=1
        
        if arr[left]<=arr[pivot]:
            left+=1
        if arr[right]>=arr[pivot]:
            right-=1

    arr[pivot], arr[right]=arr[right], arr[pivot]
    quickSort(arr, start, right-1)
    quickSort(arr, right+1, end)
    return arr


arr=[9,4,9,6,1,3,0,8,6,2]
print(quickSort(arr, 0, len(arr)-1))

s = "Express.js, or simply Express, is a back end web application framework for building RESTful APIs with Node.js"

s=s.split(' ')
s=Counter(s)
print(s)

class Person:
    def __init__(self, name):
        self.name=name

    def display(self):
        print(self.name)


class User(Person):
    def get(self):
        print()
p=Person('Alan')
p.display()

u=User('Alan')
u.display()

arr=[1,2,3,4,5,6,7,8,9]

dp=[x*x for x in arr ]
print(dp)

x=2
y=4

d = lambda x,y:x*y
print(d)

arr=[1,2,3,4,5,6,7,8,9]

obj={}

for i in arr:
    obj[i]=i*i

print(obj)

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

class Binary:

    def __init__(self):
        self.root=None

    def append(self, data):
        node = Node(data)

        if self.root is None:
            self.root=node
            return
        current = self.root

        while True:

            if data < current.data:
                if current.left:
                    current=current.left
                else:
                    current.left=node
                    break
            else:
                if current.right:
                    current=current.right
                else:
                    current.right=node
                    break

    def print(self):

        def helper(current):
            if current:
                
                helper(current.left)
                helper(current.right)
                print(current.data)

        helper(self.root)


    def delete(self, data):

        def helper(data, current, parent):
            while current:
                if data < current.data:
                    parent=current
                    current=current.left
                elif data > current.data:
                    parent=current
                    current=current.right
                else:



arr=[9,4,9,6,1,3,0,8,6,2]

bst=Binary()

for i in arr:
    bst.append(i)
bst.print()

a=set()
b=set()
a.add(1)
a.add(2)
b.add(1)
b.add(3)
print(a.difference(b))


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

get me a code for git push
python code
git add .
git commit -m "commit message"
git push origin branch_name
git push origin master
git push origin main
git push origin dev
git push origin feature/new-feature
exit

def display(hai):
    print("Hello")
    return hai()

@display
def hai():
    print("hai")


#decorator
def my_decorator(func):
    
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
        return wrapper
    return my_decorator

@my_decorator
def say_hello():
    print("Hello!")

say_hello()




arr=[1,2,4,5,6,7,8,9,10]

x = filter(lambda x:x%2==0, arr)
for x in x:
    print(x)


def fibinocci():
    a,b=1,2
    while a<100:
        yield a
        a,b=b,a+b

for el in fibinocci():
    print(el)


d = lambda x,y:x*y
print(d)


n=5
i=1
while i<n*2:
    j=1
    while j<n*2:
        if i==n or j==n or j-i==i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
        j+=1
    print()
    i+=1

arr = [5,4,3,2,1]
print(arr[::-1])

x='aaabbca'
n=len(x)
cnt=1
strs=''
i=0
while i<n:
    if i<n-1 and x[i] == x[i+1]:
        cnt+=1
    else:
        strs+=x[i]+str(cnt)
        cnt=1
    i+=1

print(strs)



n=[1,2,3,4,5,6,7,8,9]
target=10

n=10
i=0
k=0
while i<n/2:
    j=1
    while j+k<=n/2:
        print(j, n-(j-1))
        j+=1
    print()
    k+=1
    i+=1


nums=[1,2,3,4,5,6,7,8,9]
target=10

for x in nums:
    if target-x in nums:
        print(x, target-x)


arr = [2,20,10,4,11,6,7,22,18,26,3,6,4,8]
#output = [{asd:2,akd:[20]},{asd:10,akd:[4,11]},{asd:6,akd:[7,2,18]},{asd:26,akd:[3,6,4,8]}]
dp=[]
i=0
k=2
while i+k<len(arr):
    dx_x={'asd':arr[i], 'akd':arr[i+1:i+k]}
    dp.append(dx_x)
    k+=1
    i+=1
print(dp)

str='hhheetfyfghelohelhhheehelohlehelo'

print(str.count('helo'))

arr = [1,2,3,4,5,6]

def helper(arr, value):
    mid = len(arr)//2
    if arr[mid] == value:
        return mid
    left = arr[:mid]
    right = arr[mid:]
    if value < arr[mid]:
        return helper(left, value)
    else:
        return mid + helper(right, value)
    
x = helper(arr, 5)
arr[x]=0
print(arr)


n=10
dp=[]
i=1
while len(dp)<n:
    if i%2==0 or i%3==0 or i%5==0:
        dp.append(i)
    i+=1


n="80704505322479288"
m=len(n)
if m%2==1:
    s=n[:m//2+1]+n[:m//2][::-1]
else:
    s=n[:m//2]+n[:m//2][::-1]
print(s)
    

chalk = [5,1,5]
k = 22
sm = sum(chalk)
dx = {}
cnt=0
dy = []
ind = 0
for el in chalk:
    ind+=el
    dy.append(ind)
for idx, el,  in enumerate(dy):
    print(idx, el+(sm*cnt))


s = set()

s.add(1)
s.add(2)
print(s)
del s

class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        self.tail.next = node
        self.tail = node
    
    def print(self):
        current=self.head
        while current:
            print(current.data, end=" -> ")
            current=current.next

arr = [9,4,9,6,1,3,0,8,6,2]
ll = LinkedList()
for el in arr:
    ll.append(el)
ll.print()


class Heap:
    def __init__(self):
        self.heap=[]
        self.length=0

    def parent(self, i):
        return (i-1)//2
    
    def left_child(self, i):
        return 2*i+1

    def right_child(self, i):
        return 2*i+2
    
    def append(self, data):
        self.heap.append(data)
        self.length+=1
        self.shift_up(self.length-1)

    def shift_up(self, i):
        while i>0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i=self.parent(i)

    def shift_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left<self.length and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right<self.length and self.heap[right] < self.heap[min_index]:
            min_index = right
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            return self.shift_down(min_index)
        

    def helper(self, i, j):
        min_index=i
        left=self.left_child(i)
        right=self.right_child(i)

        if left < self.length-j and self.heap[min_index] < self.heap[left]:
            min_index=left
        if right < self.length-j and self.heap[min_index] < self.heap[right]:
            min_index=right
        if i != min_index:
            self.heap[min_index], self.heap[i] = self.heap[i], self.heap[min_index]
            return self.helper(min_index, j)

    def sort(self):
        for i in range(self.length):
            self.helper(0,i)
            self.heap[0], self.heap[self.length-i-1] = self.heap[self.length-i-1], self.heap[0]
    
    def remove(self, index):
        if index < self.length:
            self.heap[index]=self.heap[self.length-1]
            self.heap.pop(self.length-1)
            self.length-=1
            self.shift_up(index)
            self.shift_down(index)

    def print(self):
        print(self.heap)



arr=[9,4,9,6,1,3,0,8,6,2]
heap=Heap()
for i in arr:
    heap.append(i)
heap.remove(0)
heap.sort()
heap.print()


class Heap:
    def __init__(self):
        self.heap=[]
        self.length=0

    def parent(self, i):
        return (i-1)//2

    def left_child(self, i):
        return 2*i+1
    
    def right_child(self, i):
        return 2*i+2

    def shift_up(self, i):
        while i>0 and self.heap[self.parent(i)]<self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i=self.parent(i)

    def shift_down(self, i):
        min_index=i
        left=self.left_child(i)
        right=self.right_child(i)

        if left < self.length and self.heap[left] > self.heap[min_index]:
            min_index=left

        if right < self.length and self.heap[right] > self.heap[min_index]:
            min_index=right

        if i!=min_index:
            self.heap[i], self.heap[min_index]=self.heap[min_index], self.heap[i]
            return self.shift_down(min_index)

    def append(self, i):
        self.heap.append(i)
        self.length+=1
        self.shift_up(self.length-1)


    def remove(self, index):
        if index==self.length-1:
            self.heap.pop()
            self.length-=1
        elif index<self.length:
            self.heap[index]=self.heap[self.length-1]
            self.heap.pop()
            self.length-=1
            self.shift_down(index)
        
    
    def helper(self, i, j):
        min_index=i
        left=self.left_child(i)
        right=self.right_child(i)

        if left < self.length-j and self.heap[min_index] < self.heap[left]:
            min_index=left
        if right < self.length-j and self.heap[min_index] < self.heap[right]:
            min_index=right
        if i != min_index:
            self.heap[min_index], self.heap[i] = self.heap[i], self.heap[min_index]
            return self.helper(min_index, j)

    def sort(self):
        for i in range(self.length):
            self.helper(0,i)
            self.heap[0], self.heap[self.length-i-1] = self.heap[self.length-i-1], self.heap[0]

    def print(self):
        print(self.heap)


arr=[9,4,9,6,1,3,0,8,6,2]
heap=Heap()
for i in arr:
    heap.append(i)
heap.sort()
heap.print()


class HashMap:
    def __init__(self, size=None):
        self.size=size
        self.table = self.create()

    def create(self):
        return [[] for _ in range(self.size)]
    
    def set_value(self, key, value):
        hashed = hash(key)%self.size

        bucket = self.table[hashed]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if key == record_key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key,value))

    def print(self):
        for x in self.table:
            try:
                key, value = x[0]
                print(key, value)
            except:
                continue
    

hashmap = HashMap(10)
arr=[9,4,9,6,1,3,0,8,6,2]
for i, j in enumerate(arr):
    hashmap.set_value(i,j)
hashmap.print()


class HashMap:
    def __init__(self, size=0):
        self.size=size
        self.table=self.create()

    def create(self):
        return [[] for _ in range(self.size)]
    
    def append(self, key, value):
        hashed = hash(key)%self.size
        
        bucket = [key, value]

        for pair in self.table[hashed]:
            if pair[0]==key:
                pair[1]=value
                return
        self.table[hashed].append(bucket)



        print(bucket)
        
hash_map = HashMap(10)
hash_map.append(5)

def join(left, right):
    arr=[]
    i=0
    j=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1
    while i<len(left):
        arr.append(left[i])
        i+=1
    while j<len(right):
        arr.append(right[j])
        j+=1
    return arr
def merge(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    return join(merge(left), merge(right))


def quickSort(arr, start, end):
    if start>=end:
        return 
    pivot=start
    left=start+1
    right=end

    while left<=right:
        if arr[left]>arr[pivot] and arr[right]<arr[pivot]:
            arr[left], arr[right]=arr[right], arr[left]
            left+=1
            right-=1
        
        if arr[left]<=arr[pivot]:
            left+=1
        if arr[right]>=arr[pivot]:
            right-=1

    arr[pivot], arr[right]=arr[right], arr[pivot]
    quickSort(arr, start, right-1)
    quickSort(arr, right+1, end)
    return arr


arr=[9,4,9,6,1,3,0,8,6,2]
print(quickSort(arr, 0, len(arr)-1))


def quick_sort(arr, start, end):
    if start>=end:
        return
    
    pivot=start
    left=start+1
    right=end

    while left<=right:
        if arr[left]>arr[pivot] and arr[right]<arr[pivot]:
            arr[left], arr[right]=arr[right], arr[left]
            left+=1
            right-=1
        
        if arr[left]<=arr[pivot]:
            left+=1
        if arr[right]>=arr[pivot]:
            right-=1
    arr[pivot], arr[right]=arr[right], arr[pivot]
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)
    return arr

arr=[9,4,9,6,1,3,0,8,6,2]
print(quick_sort(arr, 0, len(arr)-1))

a, b = 2,5
el = lambda a,b : a*b
print(el(a,b))

arr=[9,4,9,6,1,3,0,8,6,2]

el = functools.reduce(lambda a,b:a+b, arr)
res=list(el)
print(res)