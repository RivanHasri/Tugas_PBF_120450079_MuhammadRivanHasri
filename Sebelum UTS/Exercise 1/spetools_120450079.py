# Author : Muhammad Rivan Hasri
# NIM : 120450079
# Affiliation : Sains Data ITERA
# Date : 13 March 2022
# Description : Program to solve simple encryption and decryption password problem

# Encrypted Password
def cek_panjangPassword(password,limit):
    return False if (len(password) > limit) and (len(password) < 0) else True

def transformasi(password):
    return [ord(char) for char in password]

def valEncrypt(password):
    newPassword = ''
    for char in password:
        val1 = chr((char // 26) + 80)
        val2 = chr((char % 26) + 80)
        if val1 < val2:
            val3 = '+'
        else:
            val3 = '-'
        newPassword += val1 + val2 + val3
    return newPassword

def encrypted(password):
    return valEncrypt(transformasi(password))

# Decrypted Password
def valDecrypt(password):
    split = [password[i:i+3] for i in range(0,len(password),3)]
    hasilDecryp = ''
    for s in split:
        char = ((s[0] - 80) * 26) + (s[1] - 80)
        hasilDecryp += chr(char)
    return hasilDecryp

def decrypted(password):
    return valDecrypt(transformasi(password))