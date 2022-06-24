import os, time, random, requests
#
#            [ TeleX V0.3 ]
#
#
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[1;32m' #اخضر
A = '\033[2;34m'#ازرق داكن
C = '\033[1;35m' #وردي
B = '\033[1;36m'#سمائي
Y = '\033[1;34m' #ازرق
W ="\033[1;37m"#ابيض
#                           Welcome to teleX
generated_users = 11000     # How many generated users you want
telegram_token = '5332779790:AAF1VfauHnzQnkEs5qDolLTEzNwON4fsSHY'   # Your telegram bot token!
admin_id =  '5012751368'    # Your telegram id
#
#                                                 Coded By:
#                                                     Telegram: @Plugin
#                                                     Github:   @PluginX
#
#
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'
message = requests.get(f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={admin_id}&text= ⌔ New Start! ").json()
id_msg = str(message['result']["message_id"])
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


logo = '''
𝙩𝙝𝙚 𝙘𝙖𝙩𝙘𝙝𝙚𝙧
'''
lo2 = '''
𝙗𝙚𝙨𝙩 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙪𝙨𝙚𝙧 𝙝𝙪𝙣𝙩
'''

ins = '''
𝚒𝚗𝚜𝚝𝚊 : @𝚣𝚟.𝚊𝚊
'''
tel = '''
𝚃𝚎𝚕𝚎 : @ 𝙶_𝙳_𝙸
'''

def main():
    print(logo)
    print('''
        - [1] Check your users list
        - [2] TeleX users generate
    ''')
    inp1 = '2'
    if inp1 == '1':
        cls()
        check_own_list()
    else:
        cls()
        telex_generate()


def gen_users(data):
    GenCounter = 0
    GenList = []

    while True:
        randomUser = ''
        if data == '1':
            randomUser += random.choice(chars) + random.choice(chars) + random.choice(chars) + 'Bot'
        elif data == '2':
            randomUser += random.choice(chars) + random.choice(chars) + random.choice(
                chars) + random.choice(
                chars) + 'Bot'
        elif data == '3':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarA + VarB + VarB + random.choice(chars) + 'Bot'
        elif data == '4':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarA + VarB + VarB + VarA + 'Bot'
        elif data == '5':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarA + VarA + VarA + VarB + 'Bot'
        elif data == '6':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarA + VarA + VarA + VarA + 'Bot'
        elif data == '7':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarA + VarA + VarB + VarB + 'Bot'


        elif data == '8':
            randomUser += random.choice(chars) + random.choice(chars) + random.choice(
                chars) + random.choice(
                chars) + random.choice(chars)
        elif data == '9':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarB + VarB + VarB + VarA + random.choice(chars)
        elif data == '10':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarA + VarB + VarB + VarB + random.choice(chars)
        elif data == '11':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarB + random.choice(chars) + VarB + VarB + VarA
        elif data == '12':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarA + VarA + random.choice(chars) + VarB + VarA
        elif data == '13':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarA + VarA + VarA + random.choice(chars) + VarB
        elif data == '14':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += random.choice(chars) + VarB + VarB + VarB + VarA
        elif data == '15':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarA + VarB + VarB + VarB + VarA


        elif data == '16':
            randomUser += random.choice(chars) + random.choice(chars) + random.choice(
                chars) + random.choice(
                chars) + random.choice(chars) + random.choice(chars)

        elif data == '17':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarA + VarB + VarB + VarB + VarB + VarA

        elif data == '18':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarA + VarB + VarB + VarB + VarB + VarA

        elif data == '19':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarA + VarA + VarB + VarB + VarA + VarA

        elif data == '20':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarA + VarB + VarB + VarA + VarA + VarA

        elif data == '21':
            VarA = random.choice(chars)
            VarB = random.choice(chars)
            randomUser += VarA + VarB + VarB + VarB + VarB + random.choice(chars)

        if int(generated_users) == int(GenCounter):
            break
        else:
            GenList.append(randomUser)

        GenCounter += 1
    checker(GenList)


def check_own_list():
    list = []
    print(logo)
    file = input('    - [TeleX] What is your file name: ')
    with open(file, 'r') as users_file:
        line = users_file.readlines()
        for user in line:
            list.append(user.split('\n')[0])
    checker(list)


def telex_generate():
    print(logo)
    try:
        tests = 'ABCDEFGHIJKLMNOPQRSTUVWXYZqwertyuioplkjhgfdsazxcvbnm'
        VarA = random.choice(tests)
        VarB = random.choice(tests)
        print(f'''
        ┌ Bots Users
        ├ [1] Generated 3L Bot Users [Example: {random.choice(tests) + random.choice(tests) + random.choice(tests)}Bot]
        ├ [2] Generated Random 4L Bot Users [Example: {random.choice(tests) + random.choice(tests) + random.choice(tests) + random.choice(tests)}Bot]
        ├ [3] Generated 4L Bot Users [Example: {VarA + VarB + VarB + random.choice(tests)}Bot]
        ├ [4] Generated 4L Bot Users [Example: {VarA + VarB + VarB + VarA}Bot]
        ├ [5] Generated 4L Bot Users [Example: {VarA + VarA + VarA + VarB}Bot]
        ├ [6] Generated 4L Bot Users [Example: {VarA + VarA + VarA + VarA}Bot]
        ├ [7] Generated 4L Bot Users [Example: {VarB + VarB + VarA + VarA}Bot]

        ┌ 5L Users
        ├ [8] Generate Random 5L User [Example: {random.choice(tests) + random.choice(tests) + random.choice(tests) + random.choice(tests) + random.choice(tests)}] 
        ├ [9] Generate 5L User [Example: {VarB + VarB + VarB + VarA + random.choice(tests)}]
        ├ [10] Generate 5L User [Example: {VarA + VarB + VarB + VarB + random.choice(tests)}]
        ├ [11] Generate 5L User [Example: {VarB + random.choice(tests) + VarB + VarB + VarA}]
        ├ [12] Generate 5L User [Example: {VarA + VarA + random.choice(tests) + VarB + VarA}]
        ├ [13] Generate 5L User [Example: {VarA + VarA + VarA + random.choice(tests) + VarB}]
        ├ [14] Generate 5L User [Example: {random.choice(tests) + VarB + VarB + VarB + VarA}]
        ├ [15] Generate 5L User [Example: {VarA + random.choice(tests) + VarB + VarA + VarA}]

        ┌ 6L Users
        ├ [16] Generate Random 6L User [Example: {random.choice(tests) + random.choice(tests) + random.choice(tests) + random.choice(tests) + random.choice(tests) + random.choice(tests)}] 
        ├ [17] Generate 6L User [Example: {VarA + VarB + VarB + VarB + VarB + VarA}]
        ├ [18] Generate 6L User [Example: {VarA + VarB + VarB + VarB + VarB + VarA}]
        ├ [19] Generate 6L User [Example: {VarA + VarA + VarB + VarB + VarA + VarA}]
        ├ [20] Generate 6L User [Example: {VarA + VarB + VarB + VarA + VarA + VarA}]
        ├ [21] Generate 6L User [Example: {VarA + VarB + VarB + VarB + VarB + random.choice(tests)}]


        ''')
        inp = '1'
        if int(inp) > 21:
            cls()
            print('    - [TeleX] Wrong Chose!')
            time.sleep(2)
            main()
        else:
            cls()
            gen_users(inp)
            print('    - [TeleX] Wrong Chose!')
            time.sleep(2)
            main()
    except:
        print(' - Only Numbers!')
        time.sleep(5)
        quit()


def checker(list):
    clear_fies()
    Taken_in_channel = 0
    Taken_in_group = 0
    Taken_in_person = 0
    Taken_in_bot = 0
    taken_counter = 0
    valid_user = 0
    bad_users = 0

    session = requests.session()
    counter = 0

    for user in list:
        cls()
        print(Z+logo)
        print(Z1+lo2)
        print(F+f'''
        ┌ Stats
        ├ Checking:    [{user}]
        ├ Checked:     [{counter}]
        ├ Bad Users:   [{bad_users}]
        ├ Valid Users: [{valid_user}]
        ├ Taken Users: [{taken_counter}]

        ┌ Valid Users
        ├ [{valid_user}] Valid

        ┌ Taken Users
        ├ [{Taken_in_channel}] In channel
        ├ [{Taken_in_group}] In group
        ├ [{Taken_in_person}] In person
        ├ [{Taken_in_bot}] In bot''')
        print(C+ins)
        print(Y+tel)

        try:
            if type(int(user[0])) == int or len(user) < 5:
                bad_users += 1
                continue
        except:
            requests.post(f"""https://api.telegram.org/bot{telegram_token}/editmessagetext?chat_id={admin_id}&message_id={id_msg}&text=    
User: [ {user} ]
        ┌ Checked: [{counter}]
        ├ In channel: [{Taken_in_channel}] 
        ├ In group: [{Taken_in_group}]
        ├ In person: [{Taken_in_person}]
        ├ In bot: [{Taken_in_bot}]
        ├ Valid Users: [{valid_user}]
        ├ Taken Users: [{taken_counter}]
   """)
   
        telegram_url = f"https://t.me/{user}"
        r = session.get(telegram_url).text

        if r.find(
                'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
            valid_user += 1
            with open('valid.txt', 'a') as save_file:
                save_file.write('@' + user + '\n')

            try:
                telegram_post = f'https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={admin_id}&text=[{counter}] Valid User: @{user}'
                session.post(telegram_post)
            except:
               pass
               
        elif r.find('subscribers') >= 0:
            Taken_in_channel += 1
            taken_counter += 1
            with open('channel.txt', 'a') as c_file:
                c_file.write('@' + user + '\n')

        elif r.find('members') >= 0:
            Taken_in_group += 1
            taken_counter += 1
            with open('group.txt', 'a') as g_file:
                g_file.write('@' + user + '\n')

        else:
            if user.find('bot') >= 0 or user.find('Bot') >= 0:
                Taken_in_bot += 1
                taken_counter += 1
                with open('bot.txt', 'a') as b_file:
                    b_file.write('@' + user + '\n')
            else:
                Taken_in_person += 1
                taken_counter += 1
                with open('person.txt', 'a') as p_file:
                    p_file.write('@' + user + '\n')
        counter += 1
        time.sleep(1)


def clear_fies():
    with open('person.txt', 'w') as p_file:
        p_file.write(' - TeleX Checker - \n')
        p_file.close()
    with open('bot.txt', 'w') as b_file:
        b_file.write(' - TeleX Checker - \n')
        b_file.close()
    with open('group.txt', 'w') as g_file:
        g_file.write(' - TeleX Checker - \n')
        g_file.close()
    with open('channel.txt', 'w') as c_file:
        c_file.write(' - TeleX Checker - \n')
        c_file.close()
    with open('valid.txt', 'w') as save_file:
        save_file.write(' - TeleX Checker - \n')
        save_file.close()


def intro():
    logo1 = '''
☆*: .｡. .｡.:*☆*★,°*:.☆:*.°★* 。
                                      ( 1/3 )
         Loading ████   

        '''

    logo2 = '''
☆.。.:*・°☆.。.:*・°☆.。.:*・°☆.。.:*・°☆
                                     ( 2/3 )
         Loading ██████
        '''


    logo3 = '''
`*:;,．★ ～☆・:.,;*`*:;,．★ ～☆・:.,;*`
                                     ( 3/3 )
         Loading ████████      
        '''


    print(B+logo1)
    time.sleep(1)
    cls()

    print(C+logo2)
    time.sleep(1.5)
    cls()
    
    print(X+logo3)
    time.sleep(1.5)
    cls()



    main()


intro()