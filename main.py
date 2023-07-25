# put your python code here
a=int(input())
b=int(input())
c=int(input())
if a==b and a==c and b==c:
  print('Равносторонний')
elif a==b or a==c or b==c:
  print('Равнобедренный')
else:
  print('Разносторонний')
  