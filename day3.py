"""23>count the freq of char in a string"""
# s1=input("enter string:  ")
# d1={}
# for i in s1:
#     if i in d1:
#         d1[i]=d1[i]+1
#     else:
#         d1[i]=1
# print(d1)
"""24>count the freq of vowel char in a string"""
# s1= input("pls enter your string: ")
# d1={}
# for i in s1:
#     if i in "AEIOUaeiou":
#         if i in d1:
#             d1[i]+=1
#         else:
#             d1[i]=1
# print(d1) 
"""25>find the last occured vowel in a string"""
# s1=input("enter: ")
# s2=""
# for i in s1:
#     if i in "AEIOUaeiou":
#         s2=s2+i
# print(s2[-1])
"""26>find the first occured vowel in a string"""
# s1= input("enter: ")
# s2=""
# for i in s1:
#     if i in "AEIOUaeiou":
#         s2=s2+i
# print(s2[0])
"""27>check if two strings are anagram or not
if two strings has same length and has same chars eg: 1>BAD and 2.abd"""
# s1="bad"
# s2="abd"
# count=0
# if len(s1)==len(s2):
#     for i in s1:
#         if i in s2:
#             count+=1
#     if count==len(s2):
#         print("Anagram")
#     else:
#         print("not a anagram")
# else:
#     print("not")
# =================================other way
# s1="listen"
# s2="silent"
# if len(s1)==len(s2):
#     d1={}
#     d2={}
#     for i in s1:
#         if i in d1:
#             d1[i]+=1
#         else:
#             d1[i]=1
#     for j in s2:
#         if j in d2:
#             d2[j]+=1
#         else:
#             d2[j]=1
# # print(d1,d2)
# if d1== d2:
#     print("anagram")
# else:
#     print("not a anagram")
"""28>remove duplicates from a string and store them in a string"""
# s1="Best Interview Approach (@@(Using Sorting)"
# s2=""
# for i in s1:
#     if i in s2:
#         pass
#     else:
#         s2=s2+i
# print(s2)
"""29>find the first nonrepetive char"""
# s1 = "Best Interview Approach"
# # print(range(len(s1)))
# for i in range(len(s1)):
#     count = 0
#     for j in range(len(s1)):
#         if s1[i] == s1[j]:
#             count = count + 1
#     print(s1[i],count)
#     if count == 1:
#         print(s1[i])
#         break
"""30>input hello world
    output olleh dlrow"""
# s1="hello world"
# s2 =""
# rev=""
# for i in s1:
#     if i !=" ":
#         rev=i+rev
#     else:
#         s2=s2+rev
#         rev=""
# print(s2+" "+rev)