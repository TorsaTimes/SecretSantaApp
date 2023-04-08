import os
import smtplib
from email.message import EmailMessage
import imghdr
import random

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

wichtelNames = {1: "NAME",
                2: "NAME",
                3: "NAME"}

wichtelEmails = {1: "EMAIL",
                 2: "EMAIL",
                 3: "EMAIL"}

Playing = True

listName = []
listEmail = []

maxAnzahl = 9
minAnzahl = 1

while Playing:

    wichtelNamenZahl: int = random.randint(minAnzahl, maxAnzahl)
    wichtelEmailZahl: int = random.randint(minAnzahl, maxAnzahl)

    if wichtelNamenZahl != wichtelEmailZahl:

        if not ((wichtelNamenZahl in listName)):
            # print("Es wurde der namen " + str(wichtelNamenZahl) + " gezogen" + " if abfrage ergebnis = " + str(wichtelNamenZahl in listName))

            if not ((wichtelEmailZahl) in listEmail):
                # print("Die Email " + str(wichtelEmailZahl) + " hat den namen " + str(wichtelNamenZahl) + " gezogen")
                # print("Die Email " + wichtelEmails[wichtelEmailZahl] + " hat den namen " + wichtelNames[wichtelNamenZahl] + " gezogen")

                name = wichtelNames[wichtelNamenZahl]
                nameEmail = wichtelNames[wichtelEmailZahl]
                msg = EmailMessage()
                msg['Subject'] = 'Wichtel Ergebniss - HOHOHO'
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = wichtelEmails[wichtelEmailZahl]
                msg.set_content(nameEmail + ' hat ' + name + ' gewichtelt')

                with open('christmas.gif', 'rb') as f:
                    file_data = f.read()
                    file_type = imghdr.what(f.name)
                    file_name = f.name
                msg.add_attachment(file_data, maintype='image',
                                   subtype=file_type, filename=file_name)

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

                    smtp.send_message(msg)

                listEmail.insert(wichtelEmailZahl, wichtelEmailZahl)
                listName.insert(wichtelNamenZahl, wichtelNamenZahl)

    else:
        print("Neu ziehen")
        if len(listName) == maxAnzahl and len(listEmail) == maxAnzahl:
            quit()
        else:
            print(str(len(listName)) + " laenge der NamenListe " +
                  str(len(listEmail)) + " EmailList laenge")
