import zipfile
import time
  
def bruteforce(toimport, obj):
    global start_time
    start_time = time.time()

    idx = 0

    with open(toimport, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print("Password has been cracked! Line: " + str(idx))
                    print("The password is: '" + word.decode() + "'")
                    print("Time needed: %s seconds" % (time.time() - start_time))
                    return True
                except:
                    continue
    return False
  
  
# toimport = "passwords.txt"
# zip_file = "secret.zip"
zip_file = input('Enter the name of the ZIP file: ') + '.zip'
toimport = input('Enter the name of the passwords file: ') + '.txt'

if not zipfile.ZipFile(zip_file):
    print("The password could not be cracked! Reason: The ZIP file could not be found.")

obj = zipfile.ZipFile(zip_file)
  
length = len(list(open(toimport, "rb")))
  
print("The password list contains " + str(length) + " passwords, which will be tried now.")
  
if bruteforce(toimport, obj) == False:
    print("The password could not be cracked! Reason: Password is not in the list.")
