import shutil, os
from pathlib import Path
import magic
import csv
import argparse
import sys

percorsofiles = os.path.join(os.getcwd(), "files") #percorso cartella di riferimento

#estensioni file compatibili per rispettiva cartella di destinazione
estensioni = {".txt" : "documenti", ".png" : "immagini", ".jpeg" : "immagini", ".jpg" : "immagini", ".doc" : "documenti", ".odt" : "documenti", ".mp3" : "audio"}

#crea se non esiste file recap.csv
if "recap.csv" not in os.listdir(percorsofiles):

    cvsrecap = open("files/recap.csv", "w", newline ="")
    cvswrite = csv.writer(cvsrecap)
    cvswrite.writerow(["name", "type", "size(B)"])

else:
    cvsrecap = open("files/recap.csv", "a", newline ="")
    cvswrite = csv.writer(cvsrecap)

#sposta file passato come argomento nella cartella adeguata
def spostafile(nomefile):
    files = [file for file in os.listdir(percorsofiles)]

    if nomefile.file in files:
        if nomefile.file == "recap.csv":
            pass
        else:
            nome = nomefile.file.split(".")[0]
            tipo = magic.from_file(os.path.join(percorsofiles, nomefile.file), mime=True).split("/")[0]
            dimensioni = Path(os.path.join(percorsofiles, nomefile.file)).stat().st_size

            filecorpo, estensionefile = os.path.splitext(os.path.join(os.getcwd(), nomefile.file))
            print(f"name: {nome} type: {tipo} size: {dimensioni}")
            if not os.path.exists(os.path.join(percorsofiles, estensioni[estensionefile])):
                os.mkdir(os.path.join(percorsofiles, estensioni[estensionefile]))
                shutil.move(os.path.join(percorsofiles, nomefile.file),os.path.join(percorsofiles, estensioni[estensionefile]))
                cvswrite.writerow([nome, tipo, dimensioni])
                print(f"Il file: {nomefile.file} è stato spostato nel percorso: {os.path.join(percorsofiles, estensioni[estensionefile])}")
            else:
                shutil.move(os.path.join(percorsofiles, nomefile.file),os.path.join(percorsofiles, estensioni[estensionefile]))
                cvswrite.writerow([nome, tipo, dimensioni])
                print(f"Il file: {nomefile.file} è stato spostato nel percorso: {os.path.join(percorsofiles, estensioni[estensionefile])}")

        cvsrecap.close()

    else:
        print("File non presente oppure errore nella digitazione")

#metodo principale
def main():

    parser = argparse.ArgumentParser( description = "Sposta il file desiderato")    # create a parser object
    parser.add_argument("file", help = "Quale file desideri spostare?", type = str)     # specify the requested arguments
    args = parser.parse_args()     # collect values
    spostafile(args)

#metodo da eseguire nel momento che si esegue lo script
if __name__ == "__main__":
    main()
