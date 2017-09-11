#!/usr/bin/python
# -*- coding: utf-8 -*-

def cprint(text, color):

    if text:
        decorate = {
        'gray' : "\033[1;30;90m", 
        'red' : "\033[1;31;91m", 
        'green' : "\033[1;32;92m",
        'yellow' : "\033[1;33;93m",
        'blue' : "\033[1;34;94m",
        'magenta' : "\033[1;35;95m",
        'cyan' : "\033[1;36;96m",
        'white' : "\033[1;36;97m",
        }

        # print decorate['red']
        if color:        
            print  "{color}{message}{background}".format(message=text, color=decorate[color], background="\033[0;37;40m")
        else:
            print  text
    else:
        print  ""
