import colorama
import hashlib

colorama.init(autoreset=True)

style = '''\033[31m
      _    _           _       _______ ____   ____  _
     | |  | |         | |     |__   __/ __ \ / __ \| |
     | |__| | __ _ ___| |__      | | | |  | | |  | | |___
     |  __  |/ _` / __| '_ \     | | | |  | | |  | | / __|  
     | |  | | (_| \__ \ | | |    | | | |__| | |__| | \__ \  - Author: @V9x
     |_|  |_|\__,_|___/_| |_|    |_|  \____/ \____/|_|___/
    '''
print(style)
print("\033[31m=============================================")
print("\033[32m[1]-Hash Checker "
      "\n[2]-Hash Length "
      "\n[3]-Hash Type "
      "\n[4]-MD5 Encrypt "
      "\n[5]-MD5 Decrypt "
      "\n[6]-SHA1 Encrypt "
      "\n[7]-SHA1 Decrypt "
      "\n[8]-SHA256 Encrypt "
      "\n[9]-SHA256 Decrypt"
      "\n[0]-Exit")
print("\033[31m=============================================")

while True:
    choose = input("\033[32mPlease Choose an Option > ")

    if choose == '1' or choose.lower() == "hash checker":
        print("\033[31m-This Option Hash Checker")
        hash1 = input("\033[32m[-]Enter The Hash[1] > ")
        hash2 = input("\033[32m[-]Enter The Hash[2] > ")
        if hash1 == hash2:
            print("\033[32m[-]The Hash Is Clean \n")
        else:
            print("\033[31m[-]The Hash Is Virus \n")

    elif choose == '2':
        print("\033[31m[-]This Option Hash Length")
        Length = input("\033[32m[-]Enter Your Hash > ")
        print("\033[32mLength Hash Is > " + str(len(Length)) + "\n")

    elif choose == '3':
        print("\033[31mThis Option Hash Type")
        HashType = input("\033[32m[-]Enter Your Hash > ")
        length = len(HashType)
        if length == 32:
            print("\033[32m[-]The Hash Is [MD5] \n")
        elif length == 40:
            print("\033[32m[-]The Hash Is [SHA1] \n")
        elif length == 64:
            print("\033[32m[-]The Hash Is [SHA256] \n")
        else:
            print("\033[31m[-]Invalid Hash Type \n")

    elif choose == '4':
        print("\033[31mThis Option MD5 Encrypt")
        word = input("\033[32m[-]Enter Your Text > ")
        md5 = hashlib.md5(word.encode())
        print("\033[31mMD5 Hash > " + md5.hexdigest() + "\n")

    elif choose == '5':
        print("\033[32m-This Option MD5 Decrypt")
        hash_Encrypt = input("\033[32m[-]Enter Your Hash > ")
        file = input("\033[32mWrite File Name > ")
        try:
            with open(file, mode='r') as f:
                for line in f:
                    line = line.strip()
                    if hashlib.md5(line.encode()).hexdigest() == hash_Encrypt:
                        print("\033[31m[-] Password Found > " + line + "\n")
        except FileNotFoundError:
            print("\033[31m[-] File not found\n")

    elif choose == '6':
        print("\033[32m-This Option SHA1 Encrypt")
        word = input("\033[32m[-]Enter Your Text > ")
        sha1 = hashlib.sha1(word.encode())
        print("\033[31mSHA1 Hash > " + sha1.hexdigest() + "\n")

    elif choose == '7':
        print("\033[32m-This Option SHA1 Decrypt")
        hash_Encrypt = input("\033[32m[-]Enter Your Hash > ")
        file = input("\033[32mWrite File Name > ")
        try:
            with open(file, mode='r') as f:
                for line in f:
                    line = line.strip()
                    if hashlib.sha1(line.encode()).hexdigest() == hash_Encrypt:
                        print("\033[31m[-] Password Found > " + line + "\n")
        except FileNotFoundError:
            print("\033[31m[-] File not found\n")

    elif choose == '8':
        print("\033[32m-This Option SHA256 Encrypt")
        word = input("\033[32m[-]Enter Your Text > ")
        sha256 = hashlib.sha256(word.encode())
        print("\033[31mSHA256 Hash > " + sha256.hexdigest() + "\n")

    elif choose == '9':
        print("\033[32m-This Option SHA256 Decrypt")
        hash_Encrypt = input("\033[32m[-]Enter Your Hash > ")
        file = input("\033[32mWrite File Name > ")
        try:
            with open(file, mode='r') as f:
                for line in f:
                    line = line.strip()
                    if hashlib.sha256(line.encode()).hexdigest() == hash_Encrypt:
                        print("\033[31m[-] Password Found > " + line + "\n")
        except FileNotFoundError:
            print("\033[31m[-] File not found\n")

    elif choose == '0':
        exit()
