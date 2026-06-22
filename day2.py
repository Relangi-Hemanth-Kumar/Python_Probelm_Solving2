"""13> split a string at spaces"""
# s1="hello python world"
# s2=""
# s3=[]
# for i in s1:
#     if i !=" ":
#         s2=s2+i
#     else:
#         s3=s3+[s2]
#         s2=""
# print(s3)
# type(s2)
"""get s2 in a list format"""
"""14> len of string without len()"""
# s1="hello python world"
# count=0
# for i in s1:
#     count+=1
# print(count)
"""15> replace the spaces with hipen(-)"""
# s1="hello python world"
# s2=""
# for i in s1:
#     if i ==" ":
#        s2=s2+"-"
#     else:
#         s2=s2+i
# print(s2)
"""16> count the vowels and print the vowels at even index"""
# s1="hello python worldae"
# count=0
# for i in range(len(s1)):
#     if s1[i] in "aeiouAEIOU":
#         count+=1
#         if i%2==0:
#             print(s1[i])
# print("vowels:",count)
"""17>count the vowels and print the vowels at odd index"""
# s1="hello python worldae"
# count=0
# for i in range(len(s1)):
#     if s1[i] in "aeiouAEIOU":
#         count+=1
#         if i%2!=0:
#             print(s1[i])
# print("vowels:",count)
"""18>count the consonants and print the consonants at odd index"""
# s1="hello python world"
# count=0
# for i in range(len(s1)):
#     if s1[i] not in "aeiouAEIOU":
#         count=count+1
#         if i%2!=0:
#             print(s1[i])
# print(count)
"""19>count the consonants and print the consonants at even index"""
# s1="hello python world"
# count=0
# for i in range(len(s1)):
#     if s1[i] not in "aeiouAEIOU":
#         count=count+1
#         if i%2==0:
#             print(s1[i])
# print(count)
"""20>check the even index vowels and find if they are palindrome or not"""
# s1="hello python waaorld"
# v=""
# for i in range(len(s1)):
#     if i%2==0:
#         if s1[i] in "aeiouAEIOU":
#             v=v+s1[i]
# # print(v)
# v1=""
# for i in v:
#     v1=i+v1
# # print(v1)
# if v==v1:
#     print("palindrome")
# else:
#     print("not a palindrome")
"""22 > input : hello python world
        output: world python hello"""
# text = "hello python world"
# word = ""
# result = ""
# for i in range(len(text)-1, -1, -1):
#     if text[i] == " ":
#         result += word + " "
#         word = ""
#     else:
#         word = text[i] + word
# result += word
# print(result)
"""22 > input : hello python world
        output: world python hello"""
# s1="hello python world"
# s2=""
# for i in s1:
#     if i not in " ":
#         s2=s2+i
# print(s2)