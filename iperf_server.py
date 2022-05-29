import time
import json
import sys
import subprocess
import os
import pathlib
from iparser import iparser_server


def iperf_server(port, format_unit, interval_output, path, connection):
    
    cmd='iperf3'
           
    if port=='None':
        port=''
    else:
        port=' -p '+port
        
    input_params='-s '+'-f '+format_unit+' -i '+interval_output+port+' >> '+path+'/iperf_server_output.txt'
    
    print(cmd+' '+input_params)
    
    os.system(cmd+' '+input_params)

    while(True):   
        if(KeyboardInterrupt):   
            iparser_server(format_unit, path, connection)
            sys.exit()
        
if __name__ == '__main__':
 
    path=str(pathlib.Path(__file__).parent.resolve())
    
    with open(path+'/iperf_launcher_config.json','r') as f:
    
        f_data=json.load(f)
        
        port=f_data["port_number"]
        format_unit=f_data["format"]
        interval_output=f_data["interval"]
        connection=f_data["connection_type"]
        
    iperf_server(port, format_unit, interval_output, path, connection)
