#Notes Manager
Notes_stored = "notes.txt"

def add_note(note):
    with open(Notes_stored, 'a') as file:
        file.write(note + '\n')
        print('Note added.')
        
def view_notes():
    with open(Notes_stored, 'r') as file:
        lines = file.readlines()
        if len(lines) == 0:
            print('No notes found.')
        else:
            for n, line in enumerate(lines,start=1):
                print(f"{n}. {line.strip()}")

def clear_notes():
    with open(Notes_stored, 'w'):
        pass
    print('All notes cleared.')
    
def main_notes():
    print('Notes Manager'.center(50))
    while True:
        command = input('Enter a command (add, view, clear, exit): ').lower()
        if command == 'add':
            note = input('Enter your note: ')
            add_note(note)
        elif command == 'view':
            view_notes()
        elif command == 'clear':
            clear_notes()
        elif command == 'exit':
            print('Exiting Notes Manager. Goodbye!')
            break
        else:
            print('Invalid command. Please try again.')
            
main_notes()