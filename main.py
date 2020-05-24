#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#28/08/2019 

#this program is writed in python 3.2

"""
Software developed by Rodrigo Galdino
(sorry me for my simple english)


I make this program for exercise my code and my code is
simple cause i study still. Sorry me cause anything


×Instagram: 'https://www.instagram.com/rgr205?r=nametag'

×Facebook: 'https://www.facebook.com/RodrigoGaldino'


I'm from Brazil...

"""

import encryptor
import os

os.system('clear')

while True:
    print('='*36)
    print('{:^36}'.format('Encryptor'))
    print('='*36)
    
    mode = str(input('Click[1] For encrypt\nClick[2] For descript\nClick[0] For exit\n: '))
    
    print()

    if (mode == '1'):
    #encrypt message
        print("\033[1;31m\nDon't use accent!!\033[m")
        
        message = input('Digit your message: ').strip().lower()   
        key = encryptor.setKey()
        save_in_text = input('Save in archive?[S/N] ').strip().lower()
        
        if 's' in save_in_text:
            save_in_text = 's'
            
        else:
            save_in_text = 'n'
            
        encryptor.encrypt(message, key, save_in_text)
        
        next = input ('Press enter >>> ')
    
    elif mode == '2':
    #descript message
        message = input('Input the message to descript: ').strip().lower()
        key = encryptor.setKey()
        save_in_text = input('Save in archive?[S/N] ').strip().lower()
        
        if 's' in save_in_text:
            save_in_text = 's'
            
        else:
            save_in_text = 'n'
            
        encryptor.descript(message, key, save_in_text)
        
        next = input ('Press enter >>> ')

    elif mode == '0':
    #close program
        break        
        quit ()
    
print ('=' * 36)
print ('\n{:<12}'.format ('THANK YOU FOR REVIEW MY PROGRAM'))
print ('=' * 36)
