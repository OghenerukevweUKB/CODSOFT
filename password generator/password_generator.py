import random

print('Welcome to your password Generator')

characters ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&8()~><.,?;:'

length = int(input('length of required passwords: '))

print('\nGenerated password: ')

passwords =''
for pwd in range(length):
    passwords += random.choice(characters)
print(passwords)    