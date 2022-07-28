def convert(message):
    return message.replace(':)', '🙂').replace(':(', '🙁')

def main():
    message = input('Enter your message: ')
    processed_message = convert(message)
    print(processed_message)

main()