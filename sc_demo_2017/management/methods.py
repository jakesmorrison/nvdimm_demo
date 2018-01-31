from ..models import NVDIMM
from ..models import NVME
import os,signal
import subprocess


class Methods():
    def retrieve_data(product,wrrd,var_name):
        if product=="nvdimm":
            if wrrd=="write":
                instance = NVDIMM.objects.first()
                if var_name == "iops":
                    if instance is None:
                        return 0
                    else:
                        last_nvdimm_write_iops = [int(x) for x in str(instance).split(" ")]
                        instance.delete()
                        return last_nvdimm_write_iops[2]
                elif var_name=="lat":
                    if instance is None:
                        return 0
                    else:
                        last_nvdimm_write_lat = [int(x) for x in str(instance).split(" ")]
                        instance.delete()
                        return last_nvdimm_write_lat[1]
                elif var_name=="bw":
                    if instance is None:
                        return 0
                    else:
                        last_nvdimm_write_bw = [int(x) for x in str(instance).split(" ")]
                        instance.delete()
                        return last_nvdimm_write_bw[0]

        elif product=="nvme":
            if wrrd=="write":
                instance = NVME.objects.first()
                if var_name == "iops":
                    if instance is None:
                        return 0
                    else:
                        last_nvdimm_write_iops = [int(x) for x in str(instance).split(" ")]
                        instance.delete()
                        return last_nvdimm_write_iops[2]
                elif var_name=="lat":
                    if instance is None:
                        return 0
                    else:
                        last_nvdimm_write_lat = [int(x) for x in str(instance).split(" ")]
                        instance.delete()
                        return last_nvdimm_write_lat[1]
                elif var_name=="bw":
                    if instance is None:
                        return 0
                    else:
                        last_nvdimm_write_bw = [int(x) for x in str(instance).split(" ")]
                        instance.delete()
                        return last_nvdimm_write_bw[0]

    def kill_all():
        password = "micron"
        print("Kill Processes")
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
