from django.shortcuts import render
import random
import subprocess
from django.http import JsonResponse
import json
from .management import methods
import os
import numpy as np

counter = 0

# Create your views here.
def demo_dashboard(request):
    context={
    }
    return render(request,"sc_demo_2017/demo_dashboard.html",context)

def get_data(request):
    global counter
    counter = counter+1
    val_nvdimm_write_iops = methods.Methods.retrieve_data("nvdimm","write","iops")
    val_nvme_write_iops = methods.Methods.retrieve_data("nvme","write","iops")
    val_nvdimm_write_lat = methods.Methods.retrieve_data("nvdimm","write","lat")
    val_nvme_write_lat = methods.Methods.retrieve_data("nvme","write","lat")
    val_nvdimm_write_bw = methods.Methods.retrieve_data("nvdimm","write","bw")
    val_nvme_write_bw = methods.Methods.retrieve_data("nvme","write","bw")

    context={
        'nvdimm_iops': [counter, val_nvdimm_write_iops],
        'nvme_iops': [counter, val_nvme_write_iops],
        'nvdimm_lat': val_nvdimm_write_lat,
        'nvme_lat': val_nvme_write_lat,
        'nvdimm_bw': ("%.2f" % (val_nvdimm_write_bw/1000000)),
        'nvme_bw': ("%.2f" % (val_nvme_write_bw/1000000)),

    }
    return JsonResponse(json.loads(json.dumps(context)))

def new_fio(request):
    params = request.GET
    foo = params["fio"]
    methods.Methods.kill_all()
    if foo == "fio_read":
        cmd = "python /home/micron/Documents/micron_apps/sc_demo_2017/start.py read_100 &"
        os.system(cmd)
    elif foo == "fio_write":
        cmd = "python /home/micron/Documents/micron_apps/sc_demo_2017/start.py write_0 &"
        os.system(cmd)
    elif foo == "fio_read_128":
        cmd = "python /home/micron/Documents/micron_apps/sc_demo_2017/start.py fio_read_128 &"
        os.system(cmd)
    elif foo == "fio_write_128":
        cmd = "python /home/micron/Documents/micron_apps/sc_demo_2017/start.py fio_write_128 &"
        os.system(cmd)


    context={}
    return JsonResponse(json.loads(json.dumps(context)))


def get_data_2(request):
    print()
    data_ssd_arr = 20 * [np.random.randint(5,7)]
    data_nvme_arr = 20 * [np.random.randint(8,11)]
    data_nvdimm_arr = 20 * [np.random.randint(12,15)]
    all_data = data_ssd_arr + data_nvme_arr + data_nvdimm_arr

    global counter
    if counter > 59:
        counter = 0
    new_val = all_data[counter]
    counter = counter + 1

    context = {
        'val': [counter, new_val]
    }

    return JsonResponse(json.loads(json.dumps(context)))