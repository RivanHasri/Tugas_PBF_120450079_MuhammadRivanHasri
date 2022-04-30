import spetools_120450079 as spt

limitPassword = 100
while True:
    opsi = input('Do you want to encrypt a password ? [Y/N] ')
    if (opsi == 'Y') or (opsi == 'y'):
        password = input('Enter your password: ')
        spt.cek_panjangPassword(password,limitPassword)
        print(password, '------->', spt.encrypted(password))
        print('')
    else:
        break