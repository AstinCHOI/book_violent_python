
import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2] # HX
    dictFile = open('1_dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print("[+] Found Password: {0} | Crypt Word: {1}\n".format(word, cryptWord))
            return
        print("[-] Passwrod Not Found.\n")
        return

def main():
    passFile = open('1_passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip(' ') # HX9LLTdc/jiDE
            print("[*] Checking Passwrod For: " + user)
            testPass(cryptPass)

if __name__ == "__main__":
    main()