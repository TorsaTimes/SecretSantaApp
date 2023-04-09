# Wichtel-Bot

## 1. Option Wichtel-Bot mit Whatsapp

Dieser Bot zieht für dich eine Liste von Wichtel-Geschenken. Er verwendet die Python-Bibliotheken `random`, `time`, `twilio` und `dotenv`.
Das Programm ist ein Wichtel-Zufallsgenerator, der eine Gruppe von Personen zufällig zu Paaren zusammenführt, wobei jede Person eine andere Person in der Gruppe als Wichtel zieht. Das Programm nutzt die Python-Bibliotheken "random" und "time" für die Zufallsgenerierung und einen Timer, "twilio" für die Versendung von WhatsApp-Nachrichten und "dotenv" für das Einlesen von Konfigurationsdaten aus einer .env-Datei.

Das Programm liest WhatsApp-Nummern und Namen aus einer Liste und verwendet diese, um zufällige Paare zu generieren, die dann über WhatsApp benachrichtigt werden. Wenn das Programm ausgeführt wird, generiert es eine Liste von Tupeln, die jedes Paar von Personen darstellen, die einander als Wichtel zugelost wurden. Die Tupel werden dann verwendet, um Nachrichten an die entsprechenden Telefonnummern über den Twilio-Dienst zu senden.

## Einrichtung

1. Erstelle einen [Twilio-Account](https://www.twilio.com/) und generiere eine WhatsApp-Nummer, um Nachrichten zu senden.
2. Installiere die erforderlichen Bibliotheken, indem du den Befehl `pip install -r requirements.txt` in der Befehlszeile ausführst.
3. Erstelle eine `.env`-Datei im selben Verzeichnis wie `wichtel.py` und füge die folgenden Informationen hinzu:

ACCOUNT_SID=your_account_sid_here
AUTH_TOKEN=your_auth_token_here
TWILIO_SANDBOX_TESTING_NUMBER=your_twilio_sandbox_testing_number_here

4. Füge die WhatsApp-Nummern und Namen der Personen, die am Wichteln teilnehmen, in die Listen `nr_list` und `name_list` in der Datei `wichtel.py` ein.

## Verwendung

Führe `python wichtel.py` in der Befehlszeile aus und der Bot wird automatisch Wichtelgeschenke ziehen und eine WhatsApp-Nachricht mit den entsprechenden Zuweisungen senden.

## Anmerkungen

- Wenn das Timeout von 5 Minuten erreicht ist, wird die Zuordnung zurückgesetzt und der Bot beginnt erneut.
- Die Zuweisungen werden auf der Konsole ausgegeben und in der Liste `final_nr_tuple_list` gespeichert, die aus WhatsApp-Nummer und Namen besteht.
- Der Bot kann mit anderen Nachrichten-APIs als Twilio erweitert werden, solange die API Python-Unterstützung bietet.


## 2. Option Wichtel-Bot mit SMTP


Dieses Python-Programm führt ein Wichtelziehen durch und sendet jedem Teilnehmer per E-Mail eine Nachricht mit dem Namen der Person, die er oder sie bewichteln soll.

## Voraussetzungen

Das Programm erfordert die folgenden Module, die installiert werden müssen:

- os
- smtplib
- email.message
- imghdr
- random

Zusätzlich müssen Sie über eine gültige Gmail-E-Mail-Adresse und ein entsprechendes Passwort verfügen, um die E-Mails zu senden. Sie müssen diese Informationen als Umgebungsvariablen mit den Namen `EMAIL_USER` und `EMAIL_PASS` in Ihrem Betriebssystem hinterlegen.

## Funktionsweise

Das Programm verwendet zwei Dictionaries `wichtelNames` und `wichtelEmails`, um die Namen und E-Mail-Adressen der Teilnehmer zu speichern. Beim Start des Programms wird eine Schleife ausgeführt, die zufällig Namen und E-Mail-Adressen auswählt und sicherstellt, dass jede Person jemanden anderen bewichtelt. Wenn ein Paar ausgewählt wird, wird eine E-Mail-Nachricht mit dem Namen des Bewichtelten und dem Namen des Schenkenden an die E-Mail-Adresse des Bewichtelten gesendet.

Das Programm verwendet auch eine Bilddatei `christmas.gif`, die an jede E-Mail-Nachricht angehängt wird.

## Verwendung

1. Stellen Sie sicher, dass alle erforderlichen Module installiert sind.
2. Legen Sie die Umgebungsvariablen `EMAIL_USER` und `EMAIL_PASS` fest.
3. Fügen Sie die Namen und E-Mail-Adressen der Teilnehmer in die Dictionaries `wichtelNames` und `wichtelEmails` ein.
4. Starten Sie das Programm, indem Sie die Python-Datei ausführen.


## Contributing

Pull-Requests sind willkommen. Für größere Änderungen erstellen Sie bitte zuerst ein Issue, um zu diskutieren, was Sie ändern möchten.

## Lizenz

[MIT](https://choosealicense.com/licenses/mit/)
