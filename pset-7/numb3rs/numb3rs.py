def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        num_1, num_2, num_3, num_4 = map(int, ip.split('.'))
        
        num_1_valid = num_1 >= 0 and num_1 <= 255
        num_2_valid = num_2 >= 0 and num_2 <= 255
        num_3_valid = num_3 >= 0 and num_3 <= 255
        num_4_valid = num_4 >= 0 and num_4 <= 255

        return num_1_valid and num_2_valid and num_3_valid and num_4_valid
    except:
        return False


if __name__ == "__main__":
    main()