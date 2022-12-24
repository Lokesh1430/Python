# Write a program to read n number of values in the list and print min amd max values in the list?

l=[]
n=int(input())
for i in range(n):
    val=int(input('Enter the number:'))
    l.append(val)
print(l)
print('max=',max(l))
print('min=',min(l))

OUTPUT:

Enter the total numbers:5
Enter the number:10
Enter the number:5
Enter the number:20
Enter the number:80
Enter the number:6
[10, 5, 20, 80, 6]
max= 80
min= 5


