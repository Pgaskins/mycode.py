#!/usr/bin/env python3
import shutil
import os

def main():

    #called at run time
    os.chdir('/home/student/mycode.py/')
    shutil.move('raynor.obj', 'ceph_storage/')

    #program will pause while we accept input
    xname = input('What is the new name for kerrigan.obj? ') #collect string input from the user
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)#changing kerrigan name and changing location


main() # This calls our main function    


