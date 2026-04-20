# #########Calculating Plant Growth Stages
# n = int(input("enter the number of days: "))
# n1=0;
# n2 =1;
# print(n1,n2,end=" ")
# for i in range(2,n+1):
#     n = n1+n2
#     n1=n2
#     n2=n
#     print(n,end=" ")
########## coding marathon 
# n = int(input("number of participants: "))
# k = int(input("number of top participants: "))
# marks =  list(map(int, input("enter the marks of participants: ").split()))
# marks.sort(reverse=True)
# res = sum(marks[:k])
# print(res)
# ##############armstrong number
# n = int(input("enter the number:"))
# d1 = n//100
# d2 = (n//10)%10
# d3 =n%10
# res = d1**3 +d2**3+d3**3
# if res ==  n:
#     print("Arm strong number")
# else:
#     print("Not an armstrong number")
######################## 5 th page  donee ################################################
# ##########pattern printing - number pyramid 
# n = int(input("enter the number of rows:"))
# num=1;
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=1
#     print()
###########factorial 
# n = int(input("enter the number: "))
# fact =1 
# for i in range(1,n+1):
#     fact = fact*i
# print(fact)
##########reverse number
# n = int(input("enter the number: "))
# rev =0
# while n>0:
#     digit = n%10 
#     rev = rev*10+digit 
#     n = n//10 
# print(rev)
#########prime number
# n = int(input("enter the number:"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("not a prime number")
#             break
#     else:
#         print("prime number")
# else:
#     print("not a prime number")
#############list 1-D
# n = list(map(int, input("Enter elements : ").split()))
# app = int(input("Element to append: "))
# n.append(app)
# print("After append:", n)
# index = int(input("Index to insert at: "))
# element = int(input("Element to insert: "))
# if index <= len(n):
#     n.insert(index, element)
#     print("After insert:", n)
# else:
#     print("Index out of range!")
#     rem = int(input("Element to remove "))
# rem = int(input("Element to remove: "))
# if rem in n:
#     n.remove(rem)
#     print("After removal:", n)
# else:
#     print("Element not found")

# n.sort()
# print("Sorted (Asc):", n)
# n.sort(reverse=True)
# print("Sorted (Desc):", n)
###############student record system 
# 1. Get the number of marks (though we'll use len() for extra safety)
# n = int(input())
# t = tuple(map(int,input().split()))
# i = int(input())
# print(max(t))
# print(min(t))
# print(t.index(i))
# print(t[0:3])
###############city wheather tracking 
# week1 = tuple(map(int,input("Enter temperatures for week 1: ").split()))
# week2 = tuple(map(int,input("Enter temperatures for week 2: ").split()))
# searchtemp = int(input("Enter temperature to search: "))
# month = week1+week2
# print("Max temperature:", max(month))
# print("Min temperature:", min(month))
# week1avg=  sum(week1)/len(week1)
# print("Average temperature for week 1:", week1avg)
# week2avg = sum(week2)/len(week2)
# print("Average temperature for week 2:", week2avg)
# dayindex = month.index(searchtemp)
# print(f"Temperature {searchtemp} found on day {dayindex+1}")
###########university course management system
# n = int(input())
# courses = tuple(map(int,input("Enter course codes: ").split()))
# remove = input("Enter course code to remove: ")
# check =input("Enter course code to check: ")
# new = input().split()
# courselist = list(courses)
# if remove in courselist:
#     courselist.remove(remove)
#     print("After removal:", courselist)
# courselist.extend(new)
# final = tuple(courselist)
# print("Final course list:", final)
# print(len(final))
# print(check in final)
#########ATM currency breakdown
# atm = tuple(map(int,input("enter the amount: ").split()))
# num500,num200,num100 = atm
# total = num500*500 + num200*200 +num100*100 
# print("Total amount:", total)
##########student info extraction   
# t = tuple(input().split())
# name,age,grade = t
# print("Name:", name)
# print("Age:", age)      
# print("Grade:", grade)
#############product data management
# data = input().split()
# id = data[0]
# name = data[1]
# price = data[2]
# ratings = list(map(int,data[3:]))
# ratings = list(ratings) 
# avgrating = sum(ratings)/len(ratings)
# print("Product ID:", id)
# print("Product Name:", name)
# print("Price:", price)
# print("Average Rating:", avgrating)
#########employee records 
# data =  tuple(input("Enter the details:").split())
# name,department,basic,bonus,tax = data 
# print("Employee Name:", name)
# print("Department:", department)
# netsalary = int(basic)+int(bonus)-int(tax)
# print("Net Salary:", netsalary)