import random as r
import string as s

turn_off = 'no'
while turn_off == 'no':

    user = int(input('длина пароля: \n'))

    set_up_digits = input('хотите добавить числа в пароль? yes/no \n')
    set_up_letters = input('хотите добавить ,буквы в пароль? yes/no \n')
    set_up_punctuation = input('хотите добавить пунктуации в пароль? yes/no \n')
    
    def sort (a,b,c):
        full = ''
        if a == 'yes':
            full += s.digits
        if b == 'yes':
            full += s.ascii_uppercase + s.ascii_lowercase
        if c == 'yes':
            full += s.punctuation
        return full
    a = ''
    for i in range(user):
        a += str(r.choice(sort(set_up_digits, set_up_letters, set_up_punctuation) ))
    print(a)
    turn_off = input('согласны на такой пароль no/yes ? \n')
print('done!')
