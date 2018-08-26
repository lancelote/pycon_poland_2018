# ~~ May the Witchers be with you. Always.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import sys

print('~~ May the Witchers be with you. Always.')

started = False
filtered = False

with open(__file__) as f:
    print('~'*30)
    for line in f:
        if 'import os' in line:
            started = True
        elif not started:
            continue

        if line == '#end-of-filter\n':
            filtered = False

        elif filtered:
            continue

        print(line, end='')
        if 'class Challenge:\n' in line:
            filtered = True
            print('# [ filtered ]')
    print('~'*30)
BaseException

def disconnect_code():
    print(
        'I am closin\' the', __file__, 'file so it aint too eazy; you know, for your own fun.\n'
    )
    os.close(100)


LOL_NO = "I won't give you flag like this"
LOL_MEH = "Meh, you need a bit more here"

print("Flags have a format of FLAG{[A-Za-z0-9_]+}")


class Challenge:
    pass
    # [ filtered ]


#end-of-filter


def run():
    assert __file__ == '/proc/self/fd/100'  # Disconnect3d's magic

    disconnect_code()

    print('\n\n\nOkay. Now you can show off your skills. gl hf')

    while True:
        msg = input('msg: ')[:300]  # you don't need that many, but feel free...

        print(eval(msg))            # YOLO. gl hf


if __name__ == '__main__':
    run()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Flags have a format of FLAG{[A-Za-z0-9_]+}
# I am closin' the /proc/self/fd/100 file so it aint too eazy; you know, for your own fun.

# Okay. Now you can show off your skills. gl hf
# msg:
