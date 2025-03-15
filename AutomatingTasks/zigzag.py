import time, sys
indent = 0
indent_increasing = True
INDENT_STOP = 10

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)

        if indent_increasing:
            indent += 1
            if indent == INDENT_STOP:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
