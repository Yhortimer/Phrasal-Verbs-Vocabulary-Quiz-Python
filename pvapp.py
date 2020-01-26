from colorama import Fore, Back, Style
import random
import time
import os
clear = lambda: os.system('cls') #on Windows System
clear()



try: input = raw_input
except: pass

#set of phrasal verbs + answer options + correct answer
mydict = {
'to give up' : ['здаватися', 'дарувати', 'підніматися', 0],
'to keep on' : ['тягнути', 'зберігати', 'продовжувати', 2],
'to pass out' : ['забути', 'знепритомніти', 'покинути', 1],
'to turn off' : ['вимкнути', 'повернути', 'ввімкнути', 0],
'to rub out' : ['вбивати', 'шахраювати', 'бакланити', 0],
'to screw up' : ['цідити', 'жмакати', 'жувати', 1],
'to pull over' : ['приїхати', 'обігнати', 'зупинити', 2],
'to pass away' : ['помирати', 'обганяти', 'відмовлятися', 0],
'to swing at' : ['напитися', 'замахуватися на когось', 'впадати у депресію', 1],
'to work out' : ['гуляти, мандрувати', 'фрілансити', 'владнати, налагоджувати', 2],
'to make up for' : ['компенсувати', 'фарбуватись', 'збиратися в останню путь', 0],
'to slug it out' : ['скорочувати, надрізати', 'битися, вести боротьбу', 'голодувати', 1],
'to point to' : ['зайняти місце', 'схопити корч', 'свідчити, вказувати на', 2],
'to rip off' : ['ошукувати, шахраювати', 'спочивати в мирі', 'різати, випускати тельбухи', 0],
'to run out (of)' : ['бігти в далечінь', 'закінчуватися, не залишитися', 'ухилятися від сплати аліментів', 1],
'to stand up to' : ['стояти на одній нозі', 'паралізувати', 'витримувати, протистояти (загрозі)', 2],
'to get over' : ['знайти рішення', 'отримувати прочухана', 'забути', 0],
'to settle for' : ['платити відсотки', 'погоджуватися на щось; приймати те що є', 'осісти на одному місці', 1],
'to track down' : ['їхати по шосе', 'бути в поганому настрої', 'розшукувати, відстежувати', 2],
'to turn on' : ['атакувати', 'обертатися', 'тікати геть', 0],
'to run away' : ['поранитися', 'втікати', 'запускати програму', 1],
'to run into' : ['потрапити у неприємності', 'тікати', 'натрапити на когось, випадково зустріти', 2],
'to put down' : ['класти, опускати', 'лягти відпочити', 'витріщатися (на когось/щось)', 0],
'to wipe out' : ['пускати пару', 'знищувати повністю, вимирати (про населення)', 'протирати ганчіркою', 1]

}
keyword_list = list(mydict.keys())
# shuffle the keywords in place
random.shuffle(keyword_list)
my_string1 = (('-----Pick the right option-----\n'))
for string in my_string1:
    time.sleep(0.05)
    print(string, end = "", flush=True)
print('You have only ' + Fore.GREEN + '10' + (Style.RESET_ALL) + ' attempts to pass the quiz\n\n\n')
print(Style.RESET_ALL)
time.sleep(1)
print (Back.GREEN + 'Press ENTER to start!\n')
print(Style.RESET_ALL)
input()
clear()
correct = 0
wrong = 0
for keyword in keyword_list:
    sf = '''\
{}\n
1) {}
2) {}
3) {}
'''
    print(sf.format(Fore.CYAN + keyword + (Style.RESET_ALL), mydict[keyword][0],
                    mydict[keyword][1],mydict[keyword][2]))
    letter = input("Enter the number of your choice (1 2 3): ").upper()


    if letter == '123'[mydict[keyword][3]]:
        print(Back.GREEN + 'CORRECT!')
        print(Style.RESET_ALL)
        correct += 1
        time.sleep(1)
        clear()
    elif correct + wrong == 10:
        clear()
        sf = "Answers given --> {} correct and {} wrong\n"
        print(sf.format(correct, wrong))
        time.sleep(1)
        print('---Push ENTER to quit---')
        input()
        quit()
    else:
        print(Back.RED + 'WRONG | THE CORRECT ANSWER SHOULD BE: ', '123'[mydict[keyword][3]])
        print(Style.RESET_ALL)
        print('Wait! Try to remember.')
        my_string1 = ('10 ==> 9 ==>  8 ==>  7 ==>  6 ==>  5 ==>  4 ==>  3 ==>  2 ==>  1 ==> GO\n')
        for string in my_string1:
            time.sleep(0.07)
            print(string, end="", flush=True)
        wrong += 1
        clear()
quit()
