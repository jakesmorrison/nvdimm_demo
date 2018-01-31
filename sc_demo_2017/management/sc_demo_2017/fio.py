import subprocess
import pandas as pd
import sqlite3
import sys
password = "micron"


class myfio():
    def __init__(self, file_name,device):
        print(test)
        self.file_name = file_name
        self.device = device
        self.run_fio()
        self.write_to_db()

    def run_fio(self):

        cd = {
            'direct': 1,
            'sync': 1,
            'randrepeat': 0,
            'ioengine': 'libaio',
            'runtime': 100,
            'size': '12G',
            'group_reporting': 1,
            'ramp_time': 10,
            'rw': 'randread',
            'bs': '4k',
            'rwmixread': 100,
            'filename': '/dev/eba',
            'numjobs': 16,
            'iodepth': 16,
            'loops': 100,
            'write_bw_log': self.file_name,
            'write_iops_log':  self.file_name,
            'write_lat_log': self.file_name,
            'log_avg_msec': 900
        }

        f = open("my_fio.fio",'w')
        start = "[global]\n"
        end = "[finish-test]"
        f.write(start)
        for key, val in cd.items():
            f.write(""+key+"="+str(val)+"\n")
        f.write(end)
        f.close()

        # Run command
        cmd = "sudo fio my_fio.fio"
        p = subprocess.call('echo {} | sudo -S {}'.format(password, cmd), shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)


    def write_to_db(self):
        fname = self.file_name.replace('.fio','')
        df_bw = pd.read_csv(fname+"_bw.log", header=None, usecols=[1, 1])
        df_iops = pd.read_csv(fname+"_iops.log", header=None, usecols=[1, 1])
        df_lat = pd.read_csv(fname+"_lat.log", header=None, usecols=[1, 1])

        result = pd.concat([df_bw, df_lat, df_iops], axis=1, join_axes=[df_bw.index])
        result.columns = ["bw", "lat", "iops"]
        result["bw"] = result["bw"].apply(lambda x: x*16)
        result["iops"] = result["iops"].apply(lambda x: x*16)

        # Write to DB
        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()
        for index, row in result.iterrows():
            cursor.execute("insert into sc_demo_2017_"+self.device+" (bw, lat, iops) values (?, ?, ?)",(int(row["bw"]), int(row["lat"]), int(row["iops"])))
        conn.commit()

        # #Deleting Old Files
        # cmd = "sudo rm enmotus*"
        # p = subprocess.call('echo {} | sudo -S {}'.format(password, cmd), shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)


# myfio("enmotus_eba","nvdimm")
