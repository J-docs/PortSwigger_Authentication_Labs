#Wriring username
with open('users_list.txt', 'w') as f:
    for i in range(150):
        if i %3:
            f.write("carlos\n")
        else:
            f.write("wiener\n")

print("[**] completed writing username to file 'userlist.txt'")

#for Password
with open('password.txt','r') as r:
    lines = r.readlines()

file = open('password_list.txt','w')

i = 0
for line in lines:
    if i % 3:
        file.write(line.strip('\n')+'\n')
    else:
        file.write('peter\n')
        file.write(line.strip('\n')+'\n')
        i = i+1

    i = i+1

print("[**] completed writing passwords to file 'passwordList.txt'")
        
