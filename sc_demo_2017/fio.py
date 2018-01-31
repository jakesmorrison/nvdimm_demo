import subprocess
import pandas as pd
import sqlite3
import sys
import os,signal
password = "micron"


class myfio():
    def __init__(self):
        print("start " + sys.argv[2] +" "+sys.argv[4]+" "+sys.argv[5])
        self.file_name = sys.argv[1]
        self.device = sys.argv[2]
        self.drive_name = sys.argv[3]
        self.rw = sys.argv[4]
        self.bs = sys.argv[5]

        self.rwmixread = 100
        self.rwmixwrite = 100

        if self.rw == "write":
            self.rwmixread = "0"
            self.rwmixwrite = "100"
        elif self.rw == "read":
            self.rwmixread = "100"
            self.rwmixwrite = "0"

        self.run_fio()

    def run_fio(self):
        cd = {
            'direct': 1,
            'randrepeat': 0,
            'ioengine': 'libaio',
            'runtime': 10,
            'size': '12G',
            'group_reporting': 1,
            'ramp_time': 0,
            'rw': 'rand'+self.rw,
            'bs': self.bs,
            'rwmixread': self.rwmixread,
            'rwmixwrite': self.rwmixwrite,
            'filename': self.drive_name,
            'numjobs': 16,
            'iodepth': 16,
            'loops': 100,
            'write_bw_log': self.file_name,
            'write_iops_log':  self.file_name,
            'write_lat_log': self.file_name,
            'log_avg_msec': 1000
        }

        fio_file_name = "/home/micron/Documents/micron_apps/sc_demo_2017/my_fio_"+self.device+".fio"
        f = open(fio_file_name,'w')
        start = "[global]\n"
        end = "[finish-test]"
        f.write(start)
        for key, val in cd.items():
            f.write(""+key+"="+str(val)+"\n")
        f.write(end)
        f.close()

        # Run command
        cmd = "sudo fio "+fio_file_name
        p = subprocess.call('echo {} | sudo -S {}'.format(password, cmd), shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

        self.write_to_db()

    def write_to_db(self):
        fname = self.file_name.replace('.fio','')
        df_bw = pd.read_csv(fname+"_bw.log", header=None, usecols=[1, 1])
        df_iops = pd.read_csv(fname+"_iops.log", header=None, usecols=[1, 1])
        df_lat = pd.read_csv(fname+"_lat.log", header=None, usecols=[1, 1])

        result = pd.concat([df_bw, df_lat, df_iops], axis=1, join_axes=[df_bw.index])
        result.columns = ["bw", "lat", "iops"]
        result["bw"] = result["bw"].apply(lambda x: x)
        result["iops"] = result["iops"].apply(lambda x: x)
        result = result.reset_index()

        # Write to DB
        conn = sqlite3.connect("/home/micron/Documents/micron_apps/db.sqlite3")
        cursor = conn.cursor()
        iops_sum = 0
        bw_sum = 0
        lat_sum = 0
        for index, row in result.iterrows():
            index = index +1
            if index%4==0:
                cursor.execute("insert into sc_demo_2017_"+self.device+" (bw, lat, iops) values (?, ?, ?)",(bw_sum*4, int(lat_sum/4), iops_sum*4))
                iops_sum = 0
                bw_sum = 0
                lat_sum = 0
            iops_sum = iops_sum + int(row["iops"])
            bw_sum = bw_sum + int(row["bw"])
            lat_sum = lat_sum + int(row["lat"])

        conn.commit()

        print("finished " +self.device)
        #Deleting Old Files
        cmd = "sudo rm enmotus*"
        p = subprocess.call('echo {} | sudo -S {}'.format(password, cmd), shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

myfio()
