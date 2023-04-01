import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

sumatoria = []
uppercaseLetter1 = chr(random.randint(65, 90))
sumatoria.append(uppercaseLetter1)
uppercaseLetter2 = chr(random.randint(65, 90))
sumatoria.append(uppercaseLetter2)
lowercaseLetter1 = chr(random.randint(97, 122))
sumatoria.append(lowercaseLetter1)
lowercaseLetter2 = chr(random.randint(97, 122))
sumatoria.append(lowercaseLetter2)
number1 = str(random.randint(0, 9))
sumatoria.append(number1)
number2 = str(random.randint(0, 9))
sumatoria.append(number2)
specialsign1 = chr(random.randint(33, 47))
sumatoria.append(specialsign1)
specialsign2 = chr(random.randint(33, 47))
sumatoria.append(specialsign2)
password = ""
for variable in sumatoria:
    password += variable

password = shuffle(password)
print(password)