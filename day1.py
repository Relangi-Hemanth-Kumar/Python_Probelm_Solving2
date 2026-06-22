"""1>revese a string"""
# s="hello python class"
# s1=""
# for i in s:
#     s1=i+s1
# print(s1)
"""2>palindrome string"""
# s1 = "madam"
# rev =""
# temp= s1
# for i in s1:
#     rev=i+rev
# print(rev)
# if rev == temp:
#     print("palindrome")
# else:
#     print("not a palindrome")
"""3>count the vowels in a string"""
# s1="elephant"
# v=["a","e","i","o","u"]
# V=["A","E","I","O","U"]
# count=0
# for i in s1:
#     if i in v or i in V:
#         count=count+1
# print(count)
"""4>count consonants in a string"""
# s1=input("enter string:  ")
# v=["a","e","i","o","u"]
# V=["A","E","I","O","U"]
# count=0
# for i in s1:
#     if i not in "aeiouAEIOU":
#         count+=1
# print(count)
"""5>count the digits in a string"""
# s1="madam"
# count=0
# for i in s1:
#     count+=1
# print(count)
"""6>special char in string"""
# char = ord(input("enter your sp character: "))
# if char>=32 and char<=126:
#     print("special char")
# else:
#     print("not a special char")
"""7>count upper case letters in a string"""
# s1="hello PYthon"
# count=0
# for i in s1:
#     if ord(i)>=65 and ord(i)<=90:
#         # print("upper case")
#         count+=1
#     # else:
#         # print("lowercase")
# print(count)
"""8>count lowercase char in a string"""
# s1="hello PYthon"
# count=0
# for i in s1:
#     if ord(i)>=97 and ord(i)<=122:
#         # print("upper case")
#         count+=1
# print(count)
"""9>print lowercase letters in a string"""
# s1="hello PYthon"
# count=0
# for i in s1:
#     if ord(i)>=97 and ord(i)<=122:
#         print(i,end="")
"""10>print upper case in string"""
# s1="hello PYthon"
# count=0
# for i in s1:
#     if ord(i)>=65 and ord(i)<=90:
#         print(i,end="")
"""11>convert lowercase to uppercase"""
# s="apple BALL CAT Dog"
# res=""
# for i in s:
#     if 97<=ord(i)<=120:
#         res=res+chr(ord(i)-32)
#     else:
#         res= res+i
# print(res)
"""12>convert uppercase to lowercase"""
# s="apple BALL CAT Dog"
# res=""
# for i in s:
#     if 65<=ord(i)<=90:
#         res=res+chr(ord(i)+32)
#     else:
#         res= res+i
# print(res)