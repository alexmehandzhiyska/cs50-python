import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r'(?P<start_hour>[0-9]{1,2}):?(?P<start_min>[0-9]{2})? (?P<start_type>[AP]M) to (?P<end_hour>[1-9]{1,2}):?(?P<end_min>[0-9]{2})? (?P<end_type>[AP]M)'

    try:
        match = re.match(pattern, s)
        start_hour = int(match.group('start_hour'))
        start_min = match.group('start_min')
        start_type = match.group('start_type')

        end_hour = int(match.group('end_hour'))
        end_min = match.group('end_min')
        end_type = match.group('end_type')

        if start_min and end_min:
            if int(start_min) == 60 or int(end_min) == 60:
                raise ValueError
        else:
            start_min = '00'
            end_min = '00'

        if start_type == 'PM':
            start_hour += 12
            start_hour = 12 if start_hour == 24 else start_hour
        else:
            start_hour = 0 if start_hour == 12 else start_hour
        
        if end_type == 'PM':
            end_hour += 12
            end_hour = 12 if end_hour == 24 else end_hour
        else:
            end_hour = 0 if end_hour == 12 else end_hour

        start_hour = f'0{start_hour}' if start_hour < 10 else start_hour
        end_hour = f'0{end_hour}' if end_hour < 10 else end_hour

        return f'{start_hour}:{start_min} to {end_hour}:{end_min}'

    except:
        raise ValueError

if __name__ == "__main__":
    main()