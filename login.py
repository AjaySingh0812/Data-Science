uname = 'Admin'
pwd = 'admin123'
attempt = 0
while True:
    attempt += 1
    print(f'Attempt {attempt} of 3')
    username = input('Enter username:')
    password = input('enter password:')
    if attempt ==3:
        print('too many attempts')
        break
    if username != uname:
        print(' Invalid username')
    if  password!= pwd:
        print('Invalid Password')
    if username == uname and password == pwd:
        print('Login Sucessfull')  
        break

