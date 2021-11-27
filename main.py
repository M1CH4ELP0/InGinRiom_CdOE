def asek_pasewored(password):
    num=int(input())
    count= 1
    while password != num and count != 3:
        count += 1
        print('enter pass: ')
        num = int(input())
    if num == password:
        print('Done!')
password = int(input())
asek_pasewored(password)