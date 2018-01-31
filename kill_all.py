import os,signal
import subprocess
import sqlite3


def kill_all():
    password = "micron"

    print("Clear DB")
    print("----------------------------")
    conn = sqlite3.connect("/home/micron/Documents/micron_apps/db.sqlite3")
    cursor = conn.cursor()
    table_names=["nvdimm","nvme","nvdimm_read","nvme_read"]
    for x in table_names:
        cursor.execute("DELETE FROM sc_demo_2017_"+x)
    conn.commit()

    print("Kill Processes")
    print("----------------------------")
    for line in os.popen("ps aux | grep start.py"):
        foo = list(filter(None,line.split(" ")))
        foo = foo[1]
        if foo:
            cmd = ("sudo kill -9 "+foo)
            p = subprocess.call('echo {} | sudo -S {}'.format(password, cmd), shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

    for line in os.popen("ps aux | grep fio"):
        foo = list(filter(None, line.split(" ")))
        foo = foo[1]
        if foo:
            cmd = ("sudo kill -9 " + foo)
            p = subprocess.call('echo {} | sudo -S {}'.format(password, cmd), shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # for line in os.popen("ps aux | grep python"):
    #     foo = list(filter(None,line.split(" ")))
    #     foo = foo[1]
    #     if foo:
    #         cmd = ("sudo kill -9 "+foo)
    #         p = subprocess.call('echo {} | sudo -S {}'.format(password, cmd), shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

kill_all()
