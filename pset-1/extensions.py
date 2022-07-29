file_name = input('File name: ').lower().strip()

try:
    extension_start_index = file_name.rfind('.')

    file_extension = file_name[extension_start_index + 1:]

    image_extensions = ['gif', 'jpg', 'jpeg', 'png']
    application_extensions = ['pdf', 'zip']
    text_extensions = ['txt']

    if file_extension in image_extensions:
        if file_extension == 'jpg':
            file_extension = 'jpeg'
        print(f'image/{file_extension}')
    elif file_extension in application_extensions:
        print(f'application/{file_extension}')
    elif file_extension in text_extensions:
        print('text/plain')
    else:
        print('application/octet-stream')
except:
    print('application/octet-stream')