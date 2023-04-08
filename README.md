README
Wichtel-Generator
Dieses Programm generiert Wichtel-Paare für eine Gruppe von vier Personen. Jeder Teilnehmer bekommt per WhatsApp die Person zugelost, für die er oder sie ein Geschenk kaufen soll.

Wie funktioniert das Programm?
Das Programm besteht aus zwei Dateien: wichtel_logic.py und main.py.

In wichtel_logic.py wird eine Liste von Telefonnummern und Namen angelegt. Die Funktion get_wichtel_tuple_list() generiert dann zufällige Paare von Telefonnummern und Namen, die der final_nr_tuple_list hinzugefügt werden. set_wichtel_tuple_list() ordnet dann jeder Telefonnummer den entsprechenden Namen zu.

In main.py wird schließlich das Hauptprogramm ausgeführt. Es ruft die Funktionen aus wichtel_logic.py auf und verschickt die Wichtel-Paare per WhatsApp. Dazu benötigt man die Twilio-API.

Wie wird das Programm ausgeführt?
Um das Programm auszuführen, müssen Sie main.py ausführen. Achten Sie darauf, dass Sie alle notwendigen Module installiert haben. Sie können das Programm auch manuell anpassen, um mehr oder weniger Teilnehmer einzubeziehen.

Folgender Codeausschnitt zeigt, wie das Programm ausgeführt wird:

python
Copy code
import wichtel_logic


def main():
    wichtel_logic.set_wichtel_tuple_list(wichtel_logic.get_wichtel_tuple_list())
    wichtel_logic.send_wichtel_msg()


if __name__ == "__main__":
    main()
Ausgabe
Die Ausgabe des Programms erfolgt über die Konsole. Die Ausgabe zeigt die gezogenen Paare von Telefonnummern und Namen an, sowie die verschickten WhatsApp-Nachrichten. Folgender Codeausschnitt zeigt die Ausgabe:

python
Copy code
Sending message to: WHATSAPPNUMBER
Message sent to: WHATSAPPNUMBER

Sending message to: WHATSAPPNUMBER
Message sent to: WHATSAPPNUMBER

Sending message to: WHATSAPPNUMBER
Message sent to: WHATSAPPNUMBER

Sending message to: WHATSAPPNUMBER
Message sent to: WHATSAPPNUMBER
Autor
Dieses Programm wurde von [Name des Autors] entwickelt.
