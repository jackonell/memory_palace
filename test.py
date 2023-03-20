import numpy as np
import random

def testing():
    f = open("encode.txt","r")
    data = f.readlines()
    random.shuffle(data)
    for record in data:
        rec = record.split()
        inp = input(rec[0]+" is:")
        if rec[1] == inp:
            print("well done!")
        else:
            print("oops, "+rec[1])

    print("congratulations!!")

if __name__ == "__main__":
    testing()
