#!/usr/bin/python3

import subprocess 

subprocess.run("newman run https://www.getpostman.com/collections/88c4dde55656d4e451ab -r cli,json", stdout=subprocess.PIPE, universal_newlines=True, shell=True)
