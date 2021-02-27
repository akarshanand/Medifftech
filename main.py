def singlechar():
    print('Single Character case')
    return -1


def palindrome_check():
    b = a[::-1]
    if b == a:
        print('Palindrome')
        return 1
    else:
        print('Not palindrome')
        return 0


a = input('Enter the string value: ')

size = len(a)


if size == 1:
    singlechar()
else:
    palindrome_check()




