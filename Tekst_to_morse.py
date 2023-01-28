# Программа для кодироания текта на русском языке в шифр Морзе
# обозначаем каждую букву, цифру, знак препинания согласно азбуке Морзе
# затем выводим на экран сам шифр 
import winsound as sound
import time
frequency=800
def Rus_to_morse():
    text = []
    text = str(input('Введите текст: ')).lower()
    morse = []
    for element in text:
        if element=='а':
            morse_code=('.-')
            print('.-')
            morse.append(morse_code)
        elif element=='б':
            morse_code=('-...')
            print('-...')
            morse.append(morse_code)
        elif element=='в':
            morse_code=['.','-','-']
            print('.--')
            morse.append(morse_code)
        elif element=='г':
            morse_code=('--.')
            print('--.')
            morse.append(morse_code)
        elif element=='д':
            morse_code=('-..')
            print('-..')
            morse.append(morse_code)
        elif element =='е':
            morse_code=['.']
            print('.')
            morse.append(morse_code)
        elif element=='ё':
            morse_code=('.')
            print('.')
            morse.append(morse_code)
        elif element=='ж':
            morse_code=('...-')
            print('...-')
            morse.append(morse_code)
        elif element=='з':
            morse_code=('--..')
            print('--..')
            morse.append(morse_code)
        elif element=='и':
            morse_code=['.','.']
            print('..')
            morse.append(morse_code)
        elif element=='й':
            morse_code=('.---')
            print('.---')
            morse.append(morse_code)
        elif element=='к':
            morse_code=('-.-')
            print('-.-')
            morse.append(morse_code)
        elif element=='л':
            morse_code=('.-..')
            print('.-..')
            morse.append(morse_code)
        elif element=='м':
            morse_code=('--')
            print('--')
            morse.append(morse_code)
        elif element=='н':
            morse_code=('-.')
            print('-.')
            morse.append(morse_code)
        elif element=='о':
            morse_code=('---')
            print('---')
            morse.append(morse_code)
        elif element=='п':
            morse_code=['.','-','-','.']
            print('.--.')
            morse.append(morse_code)
        elif element=='р':
            morse_code=['.','-','.']
            print('.-.')
            morse.append(morse_code)
        elif element=='с':
            morse_code=('...')
            print('...')
            morse.append(morse_code)
        elif element=='т':
            morse_code=['-']
            print('-')
            morse.append(morse_code)
        elif element=='у':
            morse_code=('..-')
            print('..-')
            morse.append(morse_code)
        elif element=='ф':
            morse_code=('..-.')
            print('..-.')
            morse.append(morse_code)
        elif element=='х':
            morse_code=('....')
            print('....')
            morse.append(morse_code)
        elif element=='ц':
            morse_code=('-.-.')
            print('-.-.')
            morse.append(morse_code)
        elif element=='ч':
            morse_code=('---.')
            print('---.')
            morse.append(morse_code)
        elif element=='ш':
            morse_code=('----')
            print('----')
            morse.append(morse_code)
        elif element=='щ':
            morse_code=('--.-')
            print('--.-')
            morse.append(morse_code)
        elif element=='ъ':
            morse_code=('--.--')
            print('--.--')
            morse.append(morse_code)
        elif element=='ы':
            morse_code=('-.--')
            print('-.--')
            morse.append(morse_code)
        elif element=='ь':
            morse_code=('-..-')
            print('-..-')
            morse.append(morse_code)
        elif element=='ю':
            morse_code=('..--')
            print('..--')
            morse.append(morse_code)
        elif element=='я':
            morse_code=('.-.-')
            print('.-.-')
            morse.append(morse_code)
        elif element=='1':
            morse_code=('.----')
            print('.----')
            morse.append(morse_code)
        elif element=='2':
            morse_code=('..---')
            print('..---')
            morse.append(morse_code)
        elif element=='3':
            morse_code=('...--')
            print('...--')
            morse.append(morse_code)
        elif element=='4':
            morse_code=('....-')
            print('....-')
            morse.append(morse_code)
        elif element=='5':
            morse_code=('.....')
            print('.....')
            morse.append(morse_code)
        elif element=='6':
            morse_code=('-....')
            print('-....')
            morse.append(morse_code)
        elif element=='7':
            morse_code=('--...')
            print('--...')
            morse.append(morse_code)
        elif element=='8':
            morse_code=('---..')
            print('---..')
            morse.append(morse_code)
        elif element=='9':
            morse_code=('----.')
            print('----.')
            morse.append(morse_code)
        elif element=='0':
            morse_code=('-----')
            print('-----')
            morse.append(morse_code)
        elif element=='.':
            morse_code=('......')
            print('......')
            morse.append(morse_code)
        elif element==',':
            morse_code=('.-.-.-')
            print('.-.-.-')
            morse.append(morse_code)
        elif element==':':
            morse_code=('---...')
            print('---...')
            morse.append(morse_code)
        elif element==';':
            morse_code=('-.-.-')
            print('-.-.-')
            morse.append(morse_code)
        elif element=='?':
            morse_code=('..--..')
            print('..--..')
            morse.append(morse_code)
        elif element=='!':
            morse_code=('--..--')
            print('--..--')
            morse.append(morse_code)
    
    n = len(morse) 
    n = int(n)
    i = 0
    k = 0
    while i < n:
        k = len(morse[i])
        j=0
        while j < k:
           if morse[i][j]=='.':
               sound.Beep(frequency, 100)
               j = j + 1
           elif morse[i][j]=='-':
                 sound.Beep(frequency, 600)
                 j = j + 1 
        i = i + 1   
        time.sleep(0.5)    
Rus_to_morse()    
    