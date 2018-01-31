Python Packages Needed
----------------------
Django==1.9
numpy
pandas

Anaconda 3.6
-------------
Install anaconda.
create a env called micron_apps

Demo Start Up Script (start.sh)
--------------------------------
source activate micron_apps
python /home/micron/Documents/micron_apps/kill_all.py
#service entierd restart
sudo ecmd --delete_all
sudo ecmd --pagesize 128k
sudo ecmd --create vdrive /dev/pmem0 /dev/pmem1 /dev/pmem2 /dev/pmem3 /dev/pmem4 /dev/pmem5 /dev/pmem6 /dev/pmem7 /dev/pmem8 /dev/pmem9 /dev/pmem10 /dev/pmem11stripe
sudo ecmd --create vdrive /dev/nvme0n1
sudo ecmd --create vdrive0 vdrive1
sudo ecmd --stats off t=0
python /home/micron/Documents/micron_apps/manage.py runserver


