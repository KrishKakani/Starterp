import random
special_chars = ['$','@', '!', '*', '&','#','%']
random.shuffle(special_chars)
randompsd = ""
for i in range(2): # iterates loop for 2 times
    randompsd += special_chars[i]
    randompsd += chr(random.randint(65, 90))
    randompsd += chr(random.randint(97, 122))
    randompsd += str(random.randint(0, 9))
r1 = []
for i in range(len(randompsd)):
    r1.append(randompsd[i])
random.shuffle(r1)
password = ''.join(r1)
print(password)

