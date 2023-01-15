import sys, os, time, json

def info():
        print('Usage:')
        print('-q <quote> translite only text in \" quote.')
        print('-t <translite> translite all text in file.')
        print('-un(-t/-q) <untranslite/unquote> reverse translite table and untranslite file.')
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
    with open("table.json", encoding="utf-8") as json_file:  
        LETTERS = json.load(json_file)
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
    if len(sys.argv) < 2:
        info()
    if "-t" in sys.argv:
        main()
    if "-unt" in sys.argv:
        main()
    if "-q" in sys.argv:
        main()
    if "-unq" in sys.argv:
        main()
    if "-h" in sys.argv:
        info()