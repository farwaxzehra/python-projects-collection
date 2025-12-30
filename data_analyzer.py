
print('Welcome to Personal Data Privacy Analyzer'.center(70))

mails = ['@gmail.com', '@yahoo.com', '@outlook.com', '@hotmail.com']
phone_patterns = ['123-456-7890', '948-683-2015', '888-482-556']
credit_cards = ['visa', 'mastercard', 'american express', 'discover']
card_lengths = ['13', '14', '15', '16']

found_emails = []
found_phones = []
found_cards = []

file_path = input('Enter file path to scan: ')
if not file_path:
    print('Error: Enter file path again.')
    exit()

def analyze_file(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('File not found.')
        return

    for line in lines:
        line = line.strip()

        # Email detection
        for mail in mails:
            if mail in line and line not in found_emails:
                found_emails.append(line)

        # Phone detection
        for phone in phone_patterns:
            if phone in line and line not in found_phones:
                found_phones.append(line)

        # Credit card detection
        for card in credit_cards:
            if card in line:
                for length in card_lengths:
                    if length in line and line not in found_cards:
                        found_cards.append(line)

    print('Total number of potential emails found:', len(found_emails))
    print('Total number of potential phone numbers found:', len(found_phones))
    print('Total number of potential credit card info found:', len(found_cards))

    if found_emails:
        print('\n- Emails found:')
        for email in found_emails:
            print(email)

    if found_phones:
        print('\n- Phone numbers found:')
        for phone in found_phones:
            print(phone)

    if found_cards:
        print('\n- Credit card info found:')
        for card in found_cards:
            print(card)

analyze_file(file_path)
