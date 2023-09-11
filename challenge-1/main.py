>>> def recur_factorial(n):
  if n==1:
    return n
else:
return n*recur_factorial(n-1)
>>>#take input from the user
>>>num=int(input("Enter a numbe:"))
Enter a number:6
>>> if num<0:
  print("sorry, faactorial does not exist for negative numbers")
elif num ==0 :
  print("the factorial of 0 is 1")
  else :
  print (" the factorial of",num,"is",recur_factorial(num))