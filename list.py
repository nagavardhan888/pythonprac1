# list operations
# l = list(map(int,input("enter the list elements:").split()))
# app = int(input("enter the element to append: "))
# ind = int(input("enter the index to insert at: "))
# ins = int(input("enter the element to insert: "))
# rem = int(input("enter the element to remove: "))
# l.append(app)
# print("after append:",l)
# l.insert(ind,ins)
# print("after insert:",l)
# if rem in l:
#    l.remove(rem)
# print("after removal:",l)
# l.sort()
# print("After sort:",l)
# l.sort(reverse=True)
# print("After sort in descending order:",l)
# item = list(map(int,input("enter the list elements: ").split()))
# unique = []
# for i in item:
#     if i not in unique:
#         unique.append(i)
# print("unique elements:",unique)
#########student management system 
# n = int(input())
# students = list(map(int,input().split()))
# m = int(input())
# newbatch = list(map(int,input().split()))
# students.extend(newbatch)
# newaddmission = int(input())
# students.append(newaddmission)
# rollinsert = int(input())
# idx = int(input())
# students.insert(idx,rollinsert)
# R = int(input())
# countR = students.count(R)
# s = int(input())
# indexS = students.index(s)
# wrong = int(input())
# students.remove(wrong)
# students.sort()
# print("final list of students:",*students)
# print("count of roll number",R,"is:",countR)
# print("index of roll number",s,"is:",indexS)
###############2D lists##########################################
# classes,days = list(map(int,input().split()))
# mat1 = [] 
# for _ in range(classes):
#     mat1.append(list(map(int,input().split())))
# mat2 = [] 
# for _ in range(classes):
#     mat2.append(list(map(int,input().split())))
# for i in range(classes):
#     for j in range(days):
#         print(mat1[i][j]+mat2[i][j],end=" ")
#     print()

# n = int(input())
# mat = [] 
# for _ in range(n):
#     mat.append(list(map(int,input().split())))
# isupper = True
# for i in  range(n):
#     for j in range(n):
#         if i<j:
#             if mat[i][j]!=0:
#                 isupper = False
#                 break
# if isupper:
#     print("upper triangular")
# else:
#     print("not upper triangular")

# n=int(input())
# mat = []
# for _ in range(n):
#     mat.append(list(map(int,input().split())))
# for i in range(n):
#     flipped = mat[i][::-1]
#     for pixel in flipped:
#         invert = 1-pixel
#         print(invert,end=" ")
#     print()

# n = int(input())
# garden = []
# for _ in range(n):
#     garden.append(list(map(int,input().split())))
# for j in range(n):
#     for i in range(n):
#         print(garden[i][j],end=" ")
#     print()

n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int,input().split())))
print(" after transerve :")
for j in range(n):
    for i in range(n):
        print(mat[i][j],end=" ")
    print()