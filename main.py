palindrome = str(input("Введите слово: "))
a = palindrome[::-1]
if palindrome == a:
  print("True")
else:
  print("False"