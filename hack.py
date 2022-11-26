# a=[2,3,4,23,4,35,42,35,9,9]
# b=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i+=1
# print(b)

# a=[2,3,4,23,4,35,42,35,9,9]
# b=[]
# i=0
# c=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         c+=1
#     i+=1
# print(b)
# print(c)


# a=[2,3,4,23,4,35,42,35,9,9]
# b=[]
# i=0
# p=1
# c=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         p=p*a[i]
#         c+=1
#     i+=1
# print(b)
# print(p)
# print(c)

# a=[[2,3,4,12],[23,34,56,66],[12,34,56,99]]
# sum=0
# c=0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         sum=sum+a[i][j]
#         c+=1
#         avf=sum/c
# print(sum)
# print(avf)
    
# a=[2,4,6,8,10]
# i=1
# b=[]
# while i<len(a):
#     c=a[-i]-a[-i-1]
#     b.append(c)
#     i+=1
# print(b)        

# a=[23,33,46,12,29,40]
# i=0
# while i<len(a):
#     if 20<a[i]<30:
#         print(a[i])
#     i+=1
    
# a=[2,34,-32,45,-45,-33]
# i=0
# nc=0
# pc=0
# while i<len(a):
#     if a[i]<0:
#         nc=nc+1
#     else:
#         pc=pc+1
#     i+=1
# print('print postitive umbers in this list',pc)
# print('print negative numbers in this list',nc)
    
# a=[23,45,78,99]
# b=a.sort()
# print('firsyt maxmumum is',a[-1])
# print('second maxmumum is',a[-2])

# a=[2,4,53,22,48,12,3,5,7,9,25,12]
# i=0
# e=[]
# o=[]
# while i<len(a):
#     if a[i]%2==0:
#         e.append(a[i])
#     else:
#         o.append(a[i])
#     i+=1
# print('even numbers',e)
# print('odd numbers',o)
# a=[2,4,53,22,48,12,3,5,7,9,25,12]
# i=0
# e=[]
# o=[]
# sume=0
# sumo=0
# while i<len(a):
#     if a[i]%2==0:
#         e.append(a[i])
#         sume=sume+a[i]
#     else:
#         o.append(a[i])
#         sumo=sumo+a[i]
#     i+=1
# print('even numbers',e)
# print('odd numbers',o)
# print(sume)
# print(sumo)

# a=['red','marroon','yellow']
# i=0
# b=[]
# while i<len(a):
#     d=a[i]
#     c=d.split()
#     b.append(c)
#     i+=1
# # print(b)
# a=['red','marroon','yellow']
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][j])
#         j+=1
#     i+=1
# print(b)

# a=[[1,2,3],[5,6,8]]
# sum=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j+=1
#     i+=1
# print(sum)
# a=[[1,2,3],[2,3]]
# prod=1
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         prod=prod*a[i][j]
#         j+=1
#     i+=1
# print(prod)

# a=[1,2,3,4,5,6]
# i=0
# b=[]
# while i<len(a):
#     c=a[i]+a[i]+1
#     b.append(c)
#     i+=1
# print(b)


# a=[1,2,3,4,5,6]
# i=0
# b=[]
# while i<len(a):
#     c=[a[i],a[i]+1]
#     b.append(c)
#     i+=1
# print(b)

# a=int(input('enter number:'))
# b=int(input('enter number:'))
# c=int(input('enter number:'))
# d=[]
# d.append(a)
# d.append(b)
# d.append(c)
# for i in range(0,3):
#     for j in range(0,3):
#         for k in range(0,3):
#             if i!=j and j!=k and k!=i:
#                 print(d[i],d[j],d[k])

# a=[1,2,3,4,5]
# i=0
# b=[]
# while i<len(a):
#     b.append(a[i])
#     i+=1
#     print(b)

# a=['red','marron','black']
# b=[]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][j])
#         j+=1
#     i+=1
# print(b)
                
    
# a=[1,1,1,2,3,4,4,4,5,6,6,6,9,78]
# b=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i+=1
# printt(b)

# a=[1,2,[],3,[],5,7,8]
# b=[]
# i=0
# while i<len(a):
#     if a[i]!=[]:
#         b.append(a[i])
#     i+=1
# print(b)

# grocery_list = ['flour','cheese','carrots']
# i=0
# while i<len(grocery_list):
#     print(i,':',grocery_list[i])
#     i+=1

# # 2) List product excluding duplicates.
# list = [6,1,3,5,6,3,1]
# p=1
# i=0
# b=[]
# while i<len(list):
#     if list[i] not in b:
#         b.append(list[i])
#         p=p*b[i]
#     i+=1
# print(b)
# print(p)
     
# ## 5. Count unique values inside a list.
# a = [1, 2, 2, 5, 8, 4, 4, 8]
# i=0
# c=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         c+=1
#     i+=1
# print(b)
# print(c)

# ##9. Find the First Maximum, Second maximum, Third maximum number from the List
# a=[23,9,89,1121,239,34]
# a.sort()
# print('1st maximum number:',a[-1])
# print('second maximum number:',a[-2])

# ##11. For example, if we give 9119 the function should return 811181, as the square of 9 is 81 and square
# #of 1 is 1.
# a='9119'
# b=''
# i=0
# while i<len(a):
#     c=int(a[i])**2
#     b=b+str(c)
#     i+=1
# print(b)
#a='2345'
# c=''
# for i in range(len(a)):
#     b=int(a[i])**2
#     c+=str(b)
# print(c)

# # ##16. Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeri
# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b=[]
# i=0
# while i<len(a):
#     c=a[-i]-a[-i]+1
#     b.append(c)
#     i+=1
# print(b)

# #24. Remove duplicates from a list.
# a = [1,2,3,1,2,2]
# b=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i+=1
# print(b)
        
# a=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8] 
# b=[]
# k=3
# for i in a:
#     c=a.count(i)
#     if c>=3 and i not in b:
#         b.append(i)
# print(str(b))

# #27. Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.
# a=int(input('enter number:'))
# b=int(input('enter number:'))
# c=int(input('enter number:'))
# d=[]
# d.append(a)
# d.append(b)
# d.append(c)
# for i in range(0,3):
#     for j in range(0,3):
#         for k in range(0,3):
#             if i!=j and j!=k and k!=i:
#                 print(d[i],d[j],d[k])

# # 28. The task is to perform the operation of removing all the occurrences of a given item/element present in
# # a list.
# a=[1 ,1, 2, 3, 4, 5, 1, 2]
# i=0
# b=[]
# while i<len(a):
#     if a[i]!=1:
#         b.append(a[i])
#     i+=1
# print(b)

# # 29. Remove empty List from List
# a=[5, 6, [], 3, [], [], 9]
# b=[]
# i=0

# while i<len(a):
#     if a[i]!=[]:
#         b.append(a[i])
#     i+=1
# print(b)

# 30. Given a list of numbers, write a Python program to count positive and negative numbers in a List.
# # Example:
# a = [-12, 14, 95, 3]
# pc=0
# nc=0
# i=0
# while i<len(a):
#     if a[i]>0:
#         pc+=1
#     else:
#         nc+=1
#     i+=1
# print('postivie numbers in list:',pc)
# print('negative numbers in list:',nc)

# # 32. Given start and end of a range, write a Python program to print all positive numbers in given range.
# # Example:
# a=int(input('enter star :'))
# b=int(input('enter end:'))
# for i in range(a,b):
#     if i>0:
#         print(i)

# # 33. Find the sum of number digits in List.
# a=[12,34,89,123,45]
# b=[]
# for i in a:
#     sum=0
#     for digit in str(i):
#         sum=sum+int(digit)
#     b.append(sum)
# print(b)    

# # 34. Write a Python program to remove all the values except integer values from a given
# # array of mixed values.
# # Original list: [34.67, 12, -94.89, 'Python', 0, 'C#'
# a=[34.67, 12, -94.89, 'Python', 0, 'C#']
# b=[]
# i=0
# while i<len(a):
#     if a[i]==(int):
#         b.append(a[i])
#         i+=1
#     else:
#         b.append(a)
# print(b)

# # 37. Write a Python program to pair up the consecutive elements of a given list.
# # Original lists:
# a=[1, 2, 3, 4, 5, 6]
# b=[]
# i=0
# while i<len(a):
#     c=[a[i],a[i]+1]
#     b.append(c)
#     i+=1
# print(b)
        
# # 40. Write a Python program to sum two or more lists, the lengths of the lists may be
# # # different.
# a= [[1, 2, 4], [2, 4, 4], [1, 2]]
# b=[]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         j=j+i
#         j+=1
#     i+=1



#     b.append(a[i][j])
# print(b)

    

# for i in(len(a):


# # a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# # a.insert(9,20)
# # print(a)
# a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# # i=0
# # b=[]

# #45. Write a Python program to remove the last N number of elements from a given list.
# #Original lists:
# a=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# #Remove the last 3 elements from the said list:
# del a[-4:-1]
# print(a)

# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
# Remove the last 5 elements from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]
# Remove the last 1 element from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]
# 46. Write a Python program to concatenate el


# 46. Write a Python program to concatenate element-wise three given lists.
# # Original lists:
# a=['0', '1', '2', '3', '4']
# b=['red', 'green', 'black', 'blue', 'white']
# c=['100', '200', '300', '400', '500']
# d=a+b+c
# print(d)

# Concatenate element-wise three said lists:
# ['0red100', '1green200', '2black300', '3blue400', '4white500']

    
    

# # Sum said lists with different lengths:
# # [4, 8, 8]
# # Original list:
# # [[1], [2, 4, 4], [1, 2], [4]]
# # Sum said lists with different lengths:
    
# # 47. Write a Python program to convert a given list of strings into list of lists.
# # Original list of strings:
# a=['Red', 'Maroon', 'Yellow', 'Olive']
# b=[]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][j])
#         j+=1
#     i+=1
# # print(b)
# # Convert the said list of strings into list of lists:

# n=int(input('enter number:'))
# for i in range(0,n):
#     if n%5==0:
#         print('divisible')
#     else:
#         print('not divisible')
# a=[1,1,2,3,4,4,5,6]
# b=[]
# i=0
# while i<len(a):
#     b=a.count('1')
#     b.append(a[i])
#     i+=1
# print(b)

a=['hari','pallu','teja']
i=0
while i<len(a):
    i+=1
    if a=='pallu':
        break
print(a)
# for i in range(len(a)):,y
#     if i=='pallu':
#         break
# print(a)