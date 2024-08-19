def send_email(message, recipient, sender='university.help@gmail.com'):
    valid_domains = ['.com', '.ru', '.net']
    if '@' not in recipient or not any(recipient.endswith(domain) for domain in valid_domains) \
            or '@' not in sender or not any(sender.endswith(domain) for domain in valid_domains):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}".')
        return

    if sender == recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


msg = input('Сообщение: ')
rec = input('Получатель: ')
message_sender = input('Отправитель (если отправитель по умолчанию нажмите "0"): ')
if message_sender == '0':
    send_email(message=msg, recipient=rec)
else:
    send_email(message=msg, recipient=rec, sender=message_sender)