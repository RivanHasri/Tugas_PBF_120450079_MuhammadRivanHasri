import spetools_120450079 as spt

while True:
    opsi = input('Do you want to decrypt a password ? [Y/N] ')
    if (opsi == 'Y') or (opsi == 'y'):
        password = input('Enter your password: ')
        print(password, '------->', spt.decrypted(password))
        print('')
    else:
        break