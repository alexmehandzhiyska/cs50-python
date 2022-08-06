import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        pattern = r'<iframe src="https?:\/\/(www\.)?youtube.com\/embed\/(?P<code>\w+)"><\/iframe>'
        match = re.search(pattern, s)
        code = match.group('code')

        result = f'https://youtu.be/{code}'
        return result
    except:
        return None

if __name__ == "__main__":
    main()