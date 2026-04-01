notes = [
    {'title': 'Einkauf', 'text': 'Milch, Brot, Eier'},
    {'title': 'Arbeit', 'text': 'Backendcall um 11'}
]


def show_notes():
    print("\nAktuelle Liste:....................\n")
    for note in notes:
        print(f'Titel: {note["title"]}, Text: {note["text"]}')
    print("\n...................................\n")


def add_note():
    title = input('Bitte geben Sie den Titel des neuen Eintrags an: ')
    text = input(f'Welchen Text soll ich unter "{title}" speichern? ')
    notes.append({'title': title, 'text': text})


def delete_note():
    title = input('Bitte den Titel des zu löschenden Eintrags eingeben: ')

    for i, note in enumerate(notes):
        if note.get('title') == title:
            index = i
    try:
        del notes[index]
    except Exception as ex:
        print(
            f'Der Eintrag mit dem Titel "{title}" existiert nicht.\nEs wurden keine Änderungen vorgenommen.')


def update_note():
    title = input('\nBitte den Titel des zu ändernden Eintrags eingeben: ')

    for i, note in enumerate(notes):
        if note.get('title') == title:
            text = note.get('text')
            neuerTitel = input(
                '\nGeben Sie bitte den neuen Titel ein (Return für keine Änderung): ')
            neuerText = input(
                'Geben Sie bitte den neuen Text ein (Return für keine Änderung): ')
            index = i

            if neuerTitel != '':
                title = neuerTitel
            if neuerText != '':
                text = neuerText
    try:
        notes[index] = {'title': title, 'text': text}
    except Exception as ex:
        print(
            f'\nDer Eintrag mit dem Titel "{title}" existiert nicht. Es wurden keine Änderungen vorgenommen.')

# Programmablauf************************


schleife = True

show_notes()

while schleife:
    print('<****************************************>\n\nFolgende Funktionen stehen zur Wahl: h_inzufügen, v_erändern und l_öschen eines Eintrages.\n(jede andere Eingabe zeigt die aktuelle Liste an und beendet das Programm anschließend)')
    choice = input('\nAuswahl (mit Enter bestätigen): h/v/l >')
    match choice:

        case "h":
            add_note()

        case "l":
            delete_note()

        case "v":
            update_note()

        case _:
            schleife = False
    show_notes()
