"""
Script developed by Rodrigo Galdino
(sorry me for my simple english)

×Instagram: 'https://www.instagram.com/rgr205?r=nametag'

×Facebook: 'https://www.facebook.com/RodrigoGaldino'

"""

import math

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1', '$', '2', '-', '3', '4', ' ', '5', '0']


def encrypt(word, key_encrypt=15, save_file = 's'):
#this function encrypt message and print in screen
    
    word_secret = []
    
    print()
    
    letters_list = divide(word)
    
    for c in range (0, len (letters_list)):
        for l in range (0, len (alpha)):
            if (letters_list[c] == alpha[l] or letters_list[c].upper() == alpha[l].upper()):
                key = l - key_encrypt
                word_secret.append (alpha[key].lower())
   
    
       
    print('Message encrypted with success!')
    print('=' * 36)
    print('{:^36}'.format ('Encryptor'))
    print('=' * 36)
    
    if 's' in save_file:
        try:
        #for save in system android
            directory = open('/sdcard/encrypt_message.txt', 'w')
            directory.write(toString(word_secret))
            directory.close()
        
        except:
            try:
            #for save in system Windows
                directory = open(c:\users\public\encrypt_message.txt', 'w')
                directory.write(toString(word_secret))
                directory.close()
                
            except:
                print("\033[1;31mERROR!! COULDN'T SAVE MESSAGE IN MEMORY!\033[m")
                
            else:
                print('save in C:\\users\public\encrypt_message.txt')
            
        else:
            print('Save in /sdcard/encrypt_message.txt')
       
    print()
    print('>>>',toString(word_secret), '<<<')
    print()
    print('='* 36)
    

def divide(word):
#this function divide the word in letters and keep in a list
    word_list = []
    
    for c in word:
        word_list.append(c)
    
    return word_list

    
def toString(list_word):
#this function parse the list with letters for a variable string
    word_cript = ''
    
    for c in list_word:
        word_cript = word_cript + c
    
    return word_cript
    
    
def descript(word, key_descript=15, save_file='s'):
#this function descript messages and print in screen

    word_list = []
    word_public = []
   
    letters_list = divide(word)
    
    for c in range (0, len (word)):
        for l in range (0, len (alpha)):
            key = math.ceil(l + key_descript)
            
            if key > len (alpha):
                key = key - len (alpha)
            
            elif key < len(alpha):
                key = key + len(alpha)
            
            if alpha[l] == word[c]:
                if key < len(alpha):
                    word_public.append(alpha[key])
                
                else:
                    word_public.append(alpha[key - len(alpha)])
                
    message = toString(word_public)
      
    print ('=' * 36, '{:^36}'.format ('OutPut'))
    print ('-' *36,)
    
    if 's' in save_file:
        try:
            directory = open('/sdcard/descript_message.txt', 'w')
            directory.write(toString(message))
            directory.close()
        
        except:
            try:
                directory = open('C:\\users\public\descript_message.txt', 'w')
                directory.write(toString(message))
                directory.close()
                
            except:
                print("\033[1;31mERROR!! COULDN'T SAVE MESSAGE IN MEMORY!\033[m")
            
            else:
                print('Save in C:\\users\public\descript_message.txt')
        
        else:
            print('Save in /sdcard/encrypt_message.txt')
       
    print ('\n{:^36}\n'.format (message))
    print ()
    print ('=' * 36)
    

def setKey():
#this function set the key of encrypt 
    while True:
        key = int(input('input the key that you want(min1 - max15): '))
       
        if key >= 1 and key <= 15:
            break
        
        else:
            print('\033[1;31mERROR!! Input a number arrive 1 and 15\033[m')
    
    return key
