import os
import psutil
from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/cpu")
def cpu():
        cpuUse = psutil.cpu_percent(interval=1)
        print('cpu use:', cpuUse)
        return jsonify(
               cpuUse = cpuUse
        )
        # return 'cpu use:'+str(cpuUse)

#MemoroyUse
@app.route("/memory")
def memory():
        memoryUse = psutil.virtual_memory().percent
        print('memory use:', memoryUse)
        return jsonify(
                memoryUse = memoryUse
               )

#DiskUsageReadCount
@app.route("/diskUseReadCount")
def diskRead():
        diskUseReadCount = psutil.disk_io_counters(perdisk=False)[0]
        print('diskUse Read Count:', diskUseReadCount)
        return jsonify(
                diskUseReadCount = diskUseReadCount
                )







#DiskUsageWriteCount
# diskUseWriteCount = psutil.disk_io_counters(perdisk=False)[1]
# print('diskUse Write Count:', diskUseWriteCount)
#
# #NetworkOut
# networkSent = psutil.net_io_counters(pernic=True).get("en0")[0]
# print('Network Sent Byte:', networkSent)
# #NetworkIn
# networkIn = psutil.net_io_counters(pernic=True).get("en0")[1]
# print('Network Receive Byte:', networkIn)










if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)