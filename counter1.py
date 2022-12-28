# pip install rich pyfiglet
import pyfiglet
from rich import print
import getopt
import sys
import time
import os
import numpy
import pygame


def makeSound(freak):
    sampleRate = 44100
    freq = 440 * (int(freak) / 2)

    pygame.mixer.init(44100,-16,2,512)
    arr = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * freq * x / sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
    arr2 = numpy.c_[arr,arr]
    sound = pygame.sndarray.make_sound(arr2)
    sound.play(-1)
    pygame.time.delay(1000)
    sound.stop()


def printBig(word, colour):
    title = pyfiglet.figlet_format(str(word), font='xsansb')
    print(f'[{colour}]{title}[/{colour}]')


def setLoop(side, setCount, colour):
    baseCount=1
    repCount=1


    while repCount <= REPS:
        while baseCount <= DURATION:
            os.system('clear')
            printBig("SET: " + str(setCount) + " REP: " + str(repCount), "blue")
            printBig(side + "UP: " + str(baseCount), colour)
            makeSound(baseCount)
            baseCount = baseCount + 1

        while baseCount > 1:
            baseCount = baseCount - 1
            os.system('clear')
            printBig("SET: " + str(setCount) + " REP: " + str(repCount), "blue")
            printBig(side + "DOWN: " + str(baseCount), colour)
            makeSound(baseCount)

        repCount = repCount + 1
    

def checkOptions(argv):
    global setCount
    global REPS
    global SETS
    global DURATION

    REPS = None
    SETS = None
    DURATION = 5

    try:
        opts, args = getopt.gnu_getopt(argv,"h:r:s:d:",["reps=","sets="])
    except gnu_getopt.GetoptError:
        print(f'$0 -r <REPS> -s <SETS>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('$0 -r <REPS> -s <SETS> -d <DURATION> (optional)')
            sys.exit()
        elif opt in ("-d", "--duration"):
            DURATION = int(arg)
        elif opt in ("-r", "--reps"):
            REPS = int(arg)
        elif opt in ("-s", "--sets"):
            SETS = int(arg)

    if REPS is not None or SETS is not None:
        printBig("REPS: " + str(REPS), "blue")
        printBig("SETS: " + str(SETS), "red")
        
        setCount=1

        while setCount <= SETS:
            printBig("START SET: " + str(setCount), "blue")
            time.sleep(2)
            os.system('clear')
            setLoop("LEFT\n", setCount, "red")
            os.system('clear')
            printBig("SWITCH LEG", "orange")
            time.sleep(2)
            setLoop("RIGHT\n", setCount, "green")
            os.system('clear')

            setCount = setCount + 1

        printBig("WELL DONE.\n" + str(REPS) + " REPS - " + str(SETS) + " SETS\n" + str(REPS * SETS) + "LIFTS PER LEG", "blue")


if __name__ == "__main__":
   checkOptions(sys.argv[1:])