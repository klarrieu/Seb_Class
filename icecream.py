import cIce as cic
import fFree as ff

def main():
    logger = ff.logging_begin('icelog.log')
    ice = cic.Ice('rude')
    ice()
    return

if __name__ == '__main__':
    main()