def main():
    time = input('What time is it? ')
    
    if time.startswith('0'):
        time = time[1:]
    
    time_in_hours = convert(time)
    
    if time_in_hours >= 7 and time_in_hours <= 8:
        print('breakfast time')
    elif time_in_hours >= 12 and time_in_hours <= 13:
        print('lunch time')
    elif time_in_hours >= 18 and time_in_hours <= 19:
        print('dinner time')


def convert(time):
    hours, mins = time.split(':')
    hours, mins = int(hours), int(mins)

    total_hours = hours + mins / 60
    return total_hours


if __name__ == "__main__":
    main()