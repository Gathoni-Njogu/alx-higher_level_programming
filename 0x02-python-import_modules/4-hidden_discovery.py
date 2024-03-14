#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    all_fxn = dir()
    for i in range(0, len(all_fxn)):
        if all_fxn[i][:2] != "__":
            print("{:s}".format(all_fxn[i]))
