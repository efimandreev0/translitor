import sys, os, time

def info():
        print('Usage:')
        print('-q <quote> translite only text in \" quote.')
        print('-t <translite> translite all text in file.')
        print('-un\"t\"/\"q\" <untranslite/unquote> reverse translite table\n and untranslite file.')
        print('exiting in 2 seconds...')
        time.sleep(2)
        sys.exit(1)
def main():
    if len(sys.argv) < 2:
        info()

    file = sys.argv[-1]
    enc = "utf-8"

    if not os.path.isfile(file):
        print("\nFile doesn't exist!")
        time.sleep(1)
        sys.exit(1)

    BRACKET_READ = False
    LETTERS = {'А': 'A','Б': 'B','В': 'V','Г': 'G', 'Д': 'D','Е': 'E','Ё': '<','Ж': 'J',
    'З': 'Z','И': 'I','Й': '#','К': 'K','Л': 'L','М': 'M','Н': 'N','О': 'O','П': 'P',
    'Р': 'R','С': 'S','Т': 'T','У': 'U','Ф': 'F','Х': 'H','Ц': 'C','Ч': 'Y','Ш': 'W',
    'Ъ': '{','Ы': 'Q','Ь': '}','Э': 'X','Ю': '[','Я': ']','а': 'a','б': 'b','в': 'v',
    'г': 'g','д': 'd','е': 'e','ё': '^','ж': 'j','з': 'z','и': 'i','й': '$','к': 'k',
    'л': 'l','м': 'm','н': 'n','о': 'o','п': 'p','р': 'r','с': 's','т': 't','у': 'u',
    'ф': 'f','х': 'h','ц': 'c','ч': 'y','ш': 'w','щ': '\'','Щ': '>','ъ': '_','ы': 'q',
    'ь': '&','э': 'x','ю': '@','я': '~','«': '…','»': '‥'}
    LETTERS_REV = {k: v for v, k in LETTERS.items()}
    if "-t" in sys.argv:
        text_file = open(file, 'r', encoding=enc, errors = ign)
        text = text_file.read()
        text_file.close()
        text_code = ''
        for symbol in text:
            if symbol in LETTERS:
                text_code += LETTERS[symbol]
                print (text_code)
            else:
                text_code += symbol
        code_file = open(file, 'w', encoding=enc, errors = ign)
        code_file.write(text_code)
        code_file.close()

    if "-unt" in sys.argv:
        text_file = open(file, 'r', encoding=enc, errors = ign)
        text = text_file.read()
        text_file.close()
        text_code = ''
        for symbol in text:
            if symbol in LETTERS_REV:
                text_code += LETTERS_REV[symbol]
                print (text_code)
            else:
                text_code += symbol
        code_file = open(file, 'w', encoding=enc, errors = ign)
        code_file.write(text_code)
        code_file.close()

    if "-q" in sys.argv:
        text_file = open(file, 'r', encoding=enc, errors = ign)
        text = text_file.read()
        text_file.close()
        text_code = ''
        need_translit = False
        need_translit_count = 0
        for i in text:
          if need_translit:
            try:
              text_code += LETTERS[i]
              print(text_code)
            except:
              text_code += i
          else:
            text_code += i    
          if i == '"':
            if need_translit_count < 1:
              need_translit = True
              need_translit_count += 1
            else:
              need_translit = False
              need_translit_count = 0
        code_file = open(file, 'w', encoding=enc, errors = ign)
        code_file.write(text_code)
        code_file.close()

    if "-unq" in sys.argv:
        text_file = open(file, 'r', encoding=enc, errors = ign)
        text = text_file.read()
        text_file.close()
        text_code = ''
        need_translit = False
        need_translit_count = 0
        for i in text:
          if need_translit:
            try:
              text_code += LETTERS_REV[i]
              print(text_code)
            except:
              text_code += i
          else:
            text_code += i    
          if i == '"':
            if need_translit_count < 1:
              need_translit = True
              need_translit_count += 1
            else:
              need_translit = False
              need_translit_count = 0
        code_file = open(file, 'w', encoding=enc, errors = ign)
        code_file.write(text_code)
        code_file.close()

    if "-h" in sys.argv:
        info()
if __name__ == '__main__':
    if "-t" in sys.argv:
        enc = input("Please enter txt-encoding: ")
        ign = input("Would you like to ignore errors?\nSend \"ignore\" to yes. \nJust send enter if no.")
        main()
    if "-unt" in sys.argv:
        enc = input("Please enter txt-encoding: ")
        ign = input("Would you like to ignore errors?\nSend \"ignore\" to yes. \nJust send enter if no.")
        main()
    if "-q" in sys.argv:
        enc = input("Please enter txt-encoding: ")
        ign = input("Would you like to ignore errors?\nSend \"ignore\" to yes. \nJust send enter if no.")
        main()
    if "-unq" in sys.argv:
        enc = input("Please enter txt-encoding: ")
        ign = input("Would you like to ignore errors?\nSend \"ignore\" to yes. \nJust send enter if no.")
        main()
    if "-h" in sys.argv:
        info()