import subprocess
import sqlite3
from multiprocessing import Process
import os
import sys
from tqdm import tqdm
from time import sleep
password = "micron"

def start_app(rw, bs):
    print("Remove Data Files")
    print("----------------------------")
    cmd = "sudo rm enmotus*"
    p = subprocess.call('echo {} | sudo -S {}'.format(password, cmd), shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

    cmd = "sudo rm my_fio_*"
    p = subprocess.call('echo {} | sudo -S {}'.format(password, cmd), shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

    print("Clear DB")
    print("----------------------------")
    conn = sqlite3.connect("/home/micron/Documents/micron_apps/db.sqlite3")
    cursor = conn.cursor()
    table_names=["nvdimm","nvme","nvdimm_read","nvme_read"]
    for x in table_names:
        cursor.execute("DELETE FROM sc_demo_2017_"+x)
    conn.commit()

    print("Start FIO")
    print("----------------------------")
    cmd = "source activate micron_apps"
    p = subprocess.call(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print("Start NVDIMM Test")
    print("----------------------------")
    cmd = "python /home/micron/Documents/micron_apps/sc_demo_2017/fio.py enmotus_eba nvdimm /dev/eba "+str(rw)+" "+str(bs)+" &"
    os.system(cmd)
    print("Start NVME Test")
    print("----------------------------")
    cmd = "python /home/micron/Documents/micron_apps/sc_demo_2017/fio.py enmotus_nvme nvme /dev/nvme0n1 "+str(rw)+" "+str(bs)
    os.system(cmd)

    # sleep(3)
    # print("Wait 2 Minutes")
    # print("----------------------------")
    # for x in tqdm(range(0,125)):
    #     sleep(1)
    # print("Wait 2 minutes Finished")


    print("Open Browser")
    print("----------------------------")

    print("Start FIO Loop")
    print("----------------------------")
    c=1
    while True:
        print(c)
        c=c+1
        cmd = "python /home/micron/Documents/micron_apps/sc_demo_2017/fio.py enmotus_eba nvdimm /dev/eba "+str(rw)+" "+str(bs)+" "
        os.system(cmd)
        cmd = "python /home/micron/Documents/micron_apps/sc_demo_2017/fio.py enmotus_nvme nvme /dev/nvme0n1 " + str(rw) + " "+str(bs)
        os.system(cmd)


if sys.argv[1] == "read_100":
    start_app("read","4k")
elif sys.argv[1] == "write_0":
    start_app("write","4k")
elif sys.argv[1] == "fio_read_128":
    start_app("read","128k")
elif sys.argv[1] == "fio_write_128":
    start_app("write","128k")