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
                    print("Passwort wurde geknackt! Zeile: " + str(idx))
                    print("Das Passwort lautet: '" + word.decode() + "'")
                    print("Benötigte Zeit: %s Sekunden" % (time.time() - start_time))
                    return True
                except:
                    continue
    return False
  
  
# toimport = "passwörter.txt"
# zip_file = "schenkels_secret.zip"
zip_file = input('Geben sie den Namen der ZIP-Datei ein: ') + '.zip'
toimport = input('Geben sie den Namen der Passwörter Datei ein: ') + '.txt'

if not zipfile.ZipFile(zip_file):
    print("Das Passwort konnte nicht geknackt werden! Grund: Die ZIP-Datei konnte nicht gefunden werden.")

obj = zipfile.ZipFile(zip_file)
  
anzahl = len(list(open(toimport, "rb")))
  
print("Die Passwortliste beinhaltet " + str(anzahl) + " Passwörter, welche jetzt ausprobiert werden.")
  
if bruteforce(toimport, obj) == False:
    print("Das Passwort konnte nicht geknackt werden! Grund: Passwort ist nicht in der Liste.")
