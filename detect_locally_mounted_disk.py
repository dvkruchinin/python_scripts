'''
Detect locally mounted disk (make sure it is local) with at least X MB free space, create Z files of size Y, run Z "dd"
processes which where each process will fill the selected file with Data and print time took to complete the work.
'''

import os
import sys
import psutil
import subprocess

def check_mounted_disk(disk_name):
   check_mount =  os.path.ismount(disk_name)
   return check_mount

def get_free_space(disk):
    free_space = round((psutil.disk_usage(disk).free/float(1<<20)), 2)
    X = 100000
    if free_space <= X:
        print('Need more disk space!')
        sys.exit(1)
    return free_space

def runcmd(cmd):
    process = subprocess.Popen('dd.exe --list', stdout=subprocess.PIPE)
    return process.communicate()

def main():
    volume = 'D:\\'
    Z = 5
    Y = 123123

    if check_mounted_disk(volume):
        print('Disk {} is mounted'.format(volume))
    else:
        print('Disk {} is not mounted'.format(volume))

    for i in psutil.disk_partitions():
        if i.mountpoint == volume and 'fixed' in i.opts:
            print('Disk {} is local'.format(volume))

    print('Free spcae on {}: {} MB'.format(volume, get_free_space(volume)))

    for num in range(1, Z):
        with open('dd_list' + str(num) + '.txt', 'w+') as _files:
            _files.write(runcmd('dd.exe --list'))

if __name__ == '__main__':
    sys.exit(main())



