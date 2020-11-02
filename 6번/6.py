import base64

str1 = 'nimda'

i = 0

while i < 20:
  i+=1
  str1 = str1.encode('utf-8')
  str1 = base64.b64encode(str1)
  str1 = str1.decode('utf-8')

str1 = str1.replace("1","!")
str1 = str1.replace("2","@")
str1 = str1.replace("3","$")
str1 = str1.replace("4","^")
str1 = str1.replace("5","&")
str1 = str1.replace("6","*")
str1 = str1.replace("7","(")
str1 = str1.replace("8",")")


print(str1)