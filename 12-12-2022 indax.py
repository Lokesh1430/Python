# Write a program to read n number of values in the list and display 0, 2, and 4 index values?

n=int(input('Enter the total number:'))
l=list(map(int,input('Enter the number:').split()))
print(l)
print(l[0])
print(l[2])
print(l[4])


OUTPUT:
  
Enter the total number:5
Enter the number:50 40 80 70 20
[50, 40, 80, 70, 20]
50
80
20


