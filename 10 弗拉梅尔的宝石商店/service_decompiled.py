# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
# [GCC 9.3.0]
# Embedded file name: service.py
# Compiled at: 2021-05-21 16:36:16
# Size of source mod 2**32: 7123 bytes
Instruction context:
   
 L. 151        62  POP_BLOCK        
->                64  LOAD_CONST               True
                  66  RETURN_VALUE     
                68_0  COME_FROM            52  '52'
Instruction context:
   
 L. 165        38  POP_BLOCK        
                  40  POP_EXCEPT       
->                42  CALL_FINALLY         48  'to 48'
                  44  LOAD_CONST               False
                  46  RETURN_VALUE     
                48_0  COME_FROM            42  '42'
                48_1  COME_FROM_FINALLY    28  '28'
                  48  LOAD_CONST               None
                  50  STORE_FAST               'e'
                  52  DELETE_FAST              'e'
                  54  END_FINALLY      
                  56  POP_EXCEPT       
                  58  JUMP_FORWARD         62  'to 62'
                60_0  COME_FROM            20  '20'
                  60  END_FINALLY      
                62_0  COME_FROM            58  '58'
                62_1  COME_FROM            12  '12'
import os, signal
from urllib.parse import quote
import verify, comm, functools
print = functools.partial(print, flush=True)
TIMEOUT = 60
PLAYER_INIT_MONEY = 500
SALER_INIT_MONEY = 10000
DISCOUNT = 0.9
MAX_LINES = 100

class Commodity:

    def __init__(self, name, desc, price, num):
        self.name = name
        self.desc = desc
        self.price = price
        self.num = num


class Merchant:

    def __init__(self, money):
        self.money = money
        self.possession = dict()

    def gain_commodity(self, commodity, num):
        self.possession[commodity] = self.possession.get(commodity, 0) + num

    def gain_money(self, money):
        self.money += money

    def take_commodity(self, commodity, num):
        new_num = self.possession.get(commodity, 0) - num
        if new_num < 0:
            raise ValueError('no enough commodity')
        self.possession[commodity] = new_num
        if new_num == 0:
            del self.possession[commodity]

    def take_money(self, money):
        if self.money < money:
            raise ValueError('no enough money')
        self.money -= money


def load_commodities():
    global commodities
    commodities = []
    for name, data in comm.comms().items():
        commodities.append(Commodity(name, data['desc'], data['price'], 1))
    else:
        commodities.sort(key=(lambda c: c.price))


def find_commodity(name):
    for c in commodities:
        if c.name == name:
            return c


def build_saler():
    saler = Merchant(SALER_INIT_MONEY)
    for c in commodities:
        num = 1 if c.name == 'flag' else 10
        saler.gain_commodity(c.name, num)
    else:
        return saler


def build_player():
    player = Merchant(PLAYER_INIT_MONEY)
    player.gain_commodity(commodities[0].name, 1)
    return player


def _check_transaction(filename):
    global player
    global saler
    transaction = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                pass
            else:
                line = line.split()
                name, num = line[0], int(line[1])
                c = find_commodity(name)
                if c is None:
                    raise ValueError('%s: invalid name' % name)
                money = c.price * num
                if num > 0:
                    if name not in saler.possession:
                        raise ValueError('%s: not available' % name)
                    else:
                        if name == 'flag':
                            raise ValueError('%s: not for sale' % name)
                        if saler.possession[name] < num:
                            raise ValueError('%s: too much to buy' % name)
                        if player.money < money:
                            raise ValueError('%s: too expensive' % name)
                        transaction.append('buy %d %s ($%d)' % (num, name, money))
                else:
                    money = int(-money * DISCOUNT)
                    if name not in player.possession:
                        raise ValueError('%s: not available' % name)
                    if player.possession[name] < -num:
                        raise ValueError('%s: too much to sale' % name)
                    if saler.money < money:
                        raise ValueError('%s: too expensive' % name)
                    transaction.append('sale %d %s ($%d)' % (-num, name, money))

    return transaction


def _perform_transaction(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                pass
            else:
                line = line.split()
                name, num = line[0], int(line[1])
                c = find_commodity(name)
                money = c.price * num
                if num > 0:
                    player.take_money(money)
                    player.gain_commodity(name, num)
                    saler.gain_money(money)
                    saler.take_commodity(name, num)
                else:
                    money = int(-money * DISCOUNT)
                    player.gain_money(money)
                    player.take_commodity(name, -num)
                    saler.take_money(money)
                    saler.gain_commodity(name, -num)


def check_transaction--- This code section failed: ---

 L. 144         0  SETUP_FINALLY        86  'to 86'

 L. 145         2  LOAD_GLOBAL              _check_transaction
                4  LOAD_FAST                'filename'
                6  CALL_FUNCTION_1       1  ''
                8  STORE_FAST               'transaction'

 L. 146        10  LOAD_GLOBAL              print
               12  LOAD_STR                 'You are going to:'
               14  CALL_FUNCTION_1       1  ''
               16  POP_TOP          

 L. 147        18  LOAD_GLOBAL              print
               20  LOAD_STR                 '\n'
               22  LOAD_METHOD              join
               24  LOAD_FAST                'transaction'
               26  CALL_METHOD_1         1  ''
               28  CALL_FUNCTION_1       1  ''
               30  POP_TOP          

 L. 148        32  LOAD_GLOBAL              print
               34  LOAD_STR                 "Type 'y' to confirm: "
               36  LOAD_STR                 ''
               38  LOAD_CONST               ('end',)
               40  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               42  POP_TOP          

 L. 149        44  LOAD_GLOBAL              input
               46  CALL_FUNCTION_0       0  ''
               48  LOAD_STR                 'y'
               50  COMPARE_OP               ==
               52  POP_JUMP_IF_FALSE    68  'to 68'

 L. 150        54  LOAD_GLOBAL              print
               56  LOAD_STR                 'confirmed'
               58  CALL_FUNCTION_1       1  ''
               60  POP_TOP          

 L. 151        62  POP_BLOCK        
               64  LOAD_CONST               True
               66  RETURN_VALUE     
             68_0  COME_FROM            52  '52'

 L. 153        68  LOAD_GLOBAL              print
               70  LOAD_STR                 'cancelled'
               72  CALL_FUNCTION_1       1  ''
               74  POP_TOP          

 L. 154        76  POP_BLOCK        
               78  LOAD_CONST               False
               80  RETURN_VALUE     
               82  POP_BLOCK        
               84  JUMP_FORWARD        134  'to 134'
             86_0  COME_FROM_FINALLY     0  '0'

 L. 155        86  DUP_TOP          
               88  LOAD_GLOBAL              Exception
               90  COMPARE_OP               exception-match
               92  POP_JUMP_IF_FALSE   132  'to 132'
               94  POP_TOP          
               96  STORE_FAST               'e'
               98  POP_TOP          
              100  SETUP_FINALLY       120  'to 120'

 L. 156       102  LOAD_GLOBAL              print
              104  LOAD_FAST                'e'
              106  CALL_FUNCTION_1       1  ''
              108  POP_TOP          

 L. 157       110  POP_BLOCK        
              112  POP_EXCEPT       
              114  CALL_FINALLY        120  'to 120'
              116  LOAD_CONST               False
              118  RETURN_VALUE     
            120_0  COME_FROM           114  '114'
            120_1  COME_FROM_FINALLY   100  '100'
              120  LOAD_CONST               None
              122  STORE_FAST               'e'
              124  DELETE_FAST              'e'
              126  END_FINALLY      
              128  POP_EXCEPT       
              130  JUMP_FORWARD        134  'to 134'
            132_0  COME_FROM            92  '92'
              132  END_FINALLY      
            134_0  COME_FROM           130  '130'
            134_1  COME_FROM            84  '84'

Parse error at or near `LOAD_CONST' instruction at offset 64


def perform_transaction--- This code section failed: ---

 L. 161         0  SETUP_FINALLY        14  'to 14'

 L. 162         2  LOAD_GLOBAL              _perform_transaction
                4  LOAD_FAST                'filename'
                6  CALL_FUNCTION_1       1  ''
                8  POP_TOP          
               10  POP_BLOCK        
               12  JUMP_FORWARD         62  'to 62'
             14_0  COME_FROM_FINALLY     0  '0'

 L. 163        14  DUP_TOP          
               16  LOAD_GLOBAL              Exception
               18  COMPARE_OP               exception-match
               20  POP_JUMP_IF_FALSE    60  'to 60'
               22  POP_TOP          
               24  STORE_FAST               'e'
               26  POP_TOP          
               28  SETUP_FINALLY        48  'to 48'

 L. 164        30  LOAD_GLOBAL              print
               32  LOAD_FAST                'e'
               34  CALL_FUNCTION_1       1  ''
               36  POP_TOP          

 L. 165        38  POP_BLOCK        
               40  POP_EXCEPT       
               42  CALL_FINALLY         48  'to 48'
               44  LOAD_CONST               False
               46  RETURN_VALUE     
             48_0  COME_FROM            42  '42'
             48_1  COME_FROM_FINALLY    28  '28'
               48  LOAD_CONST               None
               50  STORE_FAST               'e'
               52  DELETE_FAST              'e'
               54  END_FINALLY      
               56  POP_EXCEPT       
               58  JUMP_FORWARD         62  'to 62'
             60_0  COME_FROM            20  '20'
               60  END_FINALLY      
             62_0  COME_FROM            58  '58'
             62_1  COME_FROM            12  '12'

 L. 166        62  LOAD_CONST               True
               64  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `CALL_FINALLY' instruction at offset 42


def banner():
    print('Welcome to the store.')
    print('What do you want to do?')
    print("Type 'help' for help.")


if __name__ == '__main__':
    signal.alarm(TIMEOUT)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    token = input('token: ')
    if verify.validate(token) is None:
        print('wrong token')
        exit()
    comm.set_token(token)
    load_commodities()
    saler = build_saler()
    player = build_player()
    banner()
    while True:
        while True:
            try:
                cmd = input('\n> ')
            except EOFError:
                print('bye')
                break
            else:
                if cmd == 'help':
                    print('help: show help message')
                    print('inspect: show your possessions')
                    print('list: show commodities in the store')
                    print('trade: start a transaction')
                    print()
                    print('an example for trade:')
                    print('jade 1 (buy 1 jade)')
                    print('citrine -1 (sale 1 citrine)')
                    print('END (trade ends)')

        if cmd == 'inspect':
            print('You have $%d, and' % player.money)
            if len(player.possession) == 0:
                print('nothing')
            else:
                for name, num in player.possession.items():
                    c = find_commodity(name)
                    print('%s ($%d * %d): %s' % (name, c.price, num, c.desc))

        else:
            if cmd == 'list':
                print('Saler have $%d, and' % saler.money)
                for name, num in saler.possession.items():
                    c = find_commodity(name)
                    print('%s ($%d * %d)' % (name, c.price, num))

            else:
                if cmd == 'trade':
                    filename = os.path.join('/tmp', quote((token[:5] + token[-5:]), safe='') + '.txt')
                    f = open(filename, 'w')
                    for _ in range(MAX_LINES):
                        line = input()
                        if line == 'END':
                            break
                        else:
                            f.write(line + '\n')
                    else:
                        f.close()

                    if not check_transaction(filename):
                        pass
                    else:
                        if perform_transaction(filename):
                            print('transaction completed')
                        else:
                            print('transaction failed')
                        print('command error')
                        exit()
