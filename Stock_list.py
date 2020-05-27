import os
import subprocess
import platform
import csv
import psutil
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
result_list = []
public_ip = 'curl ifconfig.io'
pub_ip = subprocess.Popen(public_ip, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc_pub = pub_ip.wait()
out,err = pub_ip.communicate()
o=out.strip()
print (out,type(out))
if rc_pub == 0:
    result_list.append(o)
else:
    result_list.append('Nil')
print (result_list)

internal_ip="ifconfig | grep inet | awk 'NR==1{print $2}'"
int_ip = subprocess.Popen(internal_ip, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc_int = int_ip.wait()
out,err = int_ip.communicate()
o=out.strip() 
if rc_pub == 0:
    result_list.append(o)
else:
    result_list.append('Nil')
print (result_list)


os_d_a = platform.platform()
os_details= os_d_a.split('with-')[1]
result_list += [os_details]
print (os_details,type(os_details))

arch = platform.machine()
result_list += [arch]
print (arch,type(arch))

release = platform.release()
result_list += [release]
print (release,type(release))

core = (psutil.cpu_count(logical=True))
result_list += [core]

print (result_list)
svmem = psutil.virtual_memory()
memory = get_size(svmem.total)
result_list += [memory]
print (result_list)
#print(f"Available: {get_size(svmem.total)}")
#partitions = psutil.disk_partitions()
#for partition in partitions:
#    print(f"=== Device: {partition.device} ===")
#    print(f"  Mountpoint: {partition.mountpoint}")
#    print(f"  File system type: {partition.fstype}")
#    try:
#        partition_usage = psutil.disk_usage(partition.mountpoint)
#    except PermissionError:
#        # this can be catched due to the disk that
#        # isn't ready
#        continue
#    print(f"  Total Size: {get_size(partition_usage.total)}")
#    if "/" == partition.mountpoint:
#        continue
swap = psutil.swap_memory()
swap_memory = get_size(swap.total)
result_list += [swap_memory]
print (result_list)
#print(f"Total: {get_size(swap.total)}")

fo= open('stock.csv','w')
csv_writer = csv.writer(fo,delimiter='\n')
csv_writer.writerows([result_list])
fo.close()
