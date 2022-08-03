import sys
import pyfiglet

def render_string(font_chosen):
    f = pyfiglet.Figlet(font=font_chosen)
    string = input('Input: ')
    print(f.renderText(string))

if len(sys.argv) == 3:
    if sys.argv[1] == '--font' or sys.argv[1] == '-f':
        try:
            render_string(sys.argv[2])
        except:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')
elif len(sys.argv) == 1:
    render_string()
else:
    sys.exit('Invalid usage')