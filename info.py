import psutil

#CPUUtilization average
cpuUse = psutil.cpu_percent(interval=1)
print('cpu use:', cpuUse)

#MemoroyUse
memoryUse = psutil.virtual_memory().percent
print('memory use:', memoryUse)

#DiskUsageReadCount
diskUseReadCount = psutil.disk_io_counters(perdisk=False)[0]
print('diskUse Read Count:', diskUseReadCount)
#DiskUsageWriteCount
diskUseWriteCount = psutil.disk_io_counters(perdisk=False)[1]
print('diskUse Write Count:', diskUseWriteCount)

#NetworkOut
networkSent = psutil.net_io_counters(pernic=True).get("en0")[0]
print('Network Sent Byte:', networkSent)
#NetworkIn
networkIn = psutil.net_io_counters(pernic=True).get("en0")[1]
print('Network Receive Byte:', networkIn)



















