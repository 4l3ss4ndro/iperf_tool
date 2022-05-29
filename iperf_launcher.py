import time
import json
import sys
import subprocess
import pathlib
from iparser import iparser_client


def iperf_launcher(ip_address, set_time, connection, interval, max_bw, port, format_unit, interval_output, packets_n, path):
    
    cmd='iperf3'
    
    if packets_n=='None':
        packets_n=''
    else:
        packets_n=' -k '+packets_n
        
    if port=='None':
        port=''
    else:
        port=' -p '+port
   
    if connection=='None':
        connection=''
    else:
        connection=' -'+connection
        
    input_params='-c '+ip_address+connection+' -b '+max_bw+' -t '+set_time+' -f '+format_unit+' -i '+interval_output+packets_n+port
    output=''
    
    print(cmd+' '+input_params)
    
    while(True):
        try:
            output=output+(subprocess.getoutput(cmd+' '+input_params))
            print('Run finished.')        
            time.sleep(int(interval))
            print('Starting new run...')
        except KeyboardInterrupt:   
            iparser_client(output, format_unit, path, connection)
            sys.exit()
            
if __name__ == '__main__': 

    path=str(pathlib.Path(__file__).parent.resolve())
    with open(path+'/iperf_launcher_config.json','r') as f:

        f_data=json.load(f)
                
        ip_address=f_data["ip_address"]
        set_time=f_data["set_time"]
        connection=f_data["connection_type"]        
        interval=f_data["interval_between_commands"]
        max_bw=f_data["max_bandwith"]
        port=f_data["port_number"]
        format_unit=f_data["format"]
        interval_output=f_data["interval"]
        packets_n=f_data["number_of_packets_to_send"]      

    iperf_launcher(ip_address, set_time, connection, interval, max_bw, port, format_unit, interval_output, packets_n, path)
        
