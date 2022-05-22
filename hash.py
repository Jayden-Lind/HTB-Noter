from passlib.hash import sha256_crypt

with open('/usr/share/seclists/Passwords/darkweb2017-top10000.txt', 'r') as file:
    
    hash = "$5$rounds=535000$76NyOgtW18b3wIqL$HZqlzNHs1SdzbAb2V6EyAnqYNskA3K.8e1iDesL5vI2"
    
    passs = file.read()
    passwords = passs.split("\n")
    for i in passwords:
        if sha256_crypt.verify(i, hash):
            print(i + " is the answer!!")