import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def iparser_client(output, format_unit, path, connection):

    lines=output.splitlines()

    if connection!="":
        transferred_data=[]
        bw=[]
		
        for row in range(len(lines)):
            lines[row]=lines[row].split()
            if len(lines[row])>2:
                if '0.00-' not in lines[row][2] and lines[row][0]=='[' and lines[row][1]!='ID]' and '-' in lines[row][2]:
                    transferred_data.append(float(lines[row][4]))
                    unit_transfer=lines[row][5]
                    bw.append(float(lines[row][6]))
                    unit_bw=lines[row][7]
		
        bw_mean=np.mean(bw[:])
        total_transfer=np.sum(transferred_data[:]) 
		
        df=pd.DataFrame(list(zip(transferred_data, bw)), columns = ['Transferred data', 'Bandwith'])
		
        df.to_csv(path+"/iperf_client_data.csv", index=False)
		
        plt.figure()
        plt.plot(range(len(df.index)), bw, label = "Bandwith")
		
        plt.xlabel('Time [s]')
        plt.ylabel(unit_bw)
        plt.title('iPerf measurements from client side - UDP')
        plt.legend()
        plt.show()
		
        plt.figure()
        plt.plot(range(len(df.index)), transferred_data, label = "Transferred_data")
		
        plt.xlabel('Time [s]')
        plt.ylabel(unit_transfer)
        plt.title('iPerf measurements from client side - UDP')
        plt.legend()
        plt.show()   	
    else:
        transferred_data=[]
        bw=[]
        retr=[]
        cwnd=[]
		
        for row in range(len(lines)):
            lines[row]=lines[row].split()
            if len(lines[row])>2:
                if '0.00-' not in lines[row][2] and lines[row][0]=='[' and lines[row][1]!='ID]' and '-' in lines[row][2]:
                    transferred_data.append(float(lines[row][4]))
                    unit_transfer=lines[row][5]
                    bw.append(float(lines[row][6]))
                    unit_bw=lines[row][7]
                    cwnd.append(float(lines[row][9]))
                    unit_cwnd=lines[row][10]
                    retr.append(lines[row][8])
    		
        bw_mean=np.mean(bw[:])
        total_transfer=np.sum(transferred_data[:])
		
        df=pd.DataFrame(list(zip(transferred_data, bw, retr, cwnd)), columns = ['Transferred data', 'Bandwith', 'Retries', 'Congestion window'])
		
        df.to_csv(path+"/iperf_server_data.csv", index=False)
		
        plt.figure()
        plt.plot(range(len(df.index)), bw, label = "Bandwith")
		
        plt.xlabel('Time [s]')
        plt.ylabel(unit_bw)
        plt.title('iPerf measurements from client side - TCP')
        plt.legend()
        plt.show()
		
        plt.figure()
        plt.plot(range(len(df.index)), transferred_data, label = "Transferred_data")
		
        plt.xlabel('Time [s]')
        plt.ylabel(unit_transfer)
        plt.title('iPerf measurements from client side - TCP')
        plt.legend()
        plt.show()
		
        plt.figure()
        plt.plot(range(len(df.index)), cwnd, label = "Congestion window")
		
        plt.xlabel('Time [s]')
        plt.ylabel(unit_cwnd)
        plt.title('iPerf measurements from client side - TCP')
        plt.legend()
        plt.show()
		
        plt.figure()
        plt.plot(range(len(df.index)), retr, label = "Retries")
		
        plt.xlabel('Time [s]')
        plt.ylabel('N.')
        plt.title('iPerf measurements from client side - TCP')
        plt.legend()
        plt.show()
    
def iparser_server(format_unit, path, connection):

    with open(path+'/iperf_server_output.txt','r+') as f:
    	lines=f.readlines()
    	f.truncate(0)
    if connection!="None":
		
    	transferred_data=[]
    	bw=[]
    	jitter=[]
    	packet_loss=[]
    	lost_n=[]
    	lost1=[]
    	lost2=[]
    	
    	for row in range(len(lines)):
        	lines[row]=lines[row].split()
        	if len(lines[row])>2:
                    if '0.00-' not in lines[row][2] and lines[row][0]=='[' and lines[row][1]!='ID]' and '-' in lines[row][2]:
                        transferred_data.append(float(lines[row][4]))
                        unit_transfer=lines[row][5]
                        bw.append(float(lines[row][6]))
                        unit_bw=lines[row][7]
                        jitter.append(float(lines[row][8]))
                        unit_jitter=lines[row][9]
                        packet_loss.append(lines[row][11]) #(n%)
                        lost_n.append(lines[row][10]) #n/m
    	
    	for i in range(len(packet_loss)):
        	packet_loss[i]=packet_loss[i][1:-2]
        	packet_loss[i]=float(packet_loss[i])
        	
        	a, b=lost_n[i].split('/')
        	lost1.append(int(a))
        	lost2.append(int(b))
        	
    	bw_mean=np.mean(bw[:])
    	total_transfer=np.sum(transferred_data[:]) 
    	jitter_mean=np.mean(jitter[:])
    	
    	a_total=np.sum(lost1[:]) 
    	b_total=np.sum(lost2[:])
    	if int(b_total)!=0:
    		packet_loss_total=int(a_total)/int(b_total)
	
    	df=pd.DataFrame(list(zip(transferred_data, bw, jitter, packet_loss)), columns = ['Transferred data', 'Bandwith', 'Jitter', 'Packet loss'])
    	
    	df.to_csv(path+"/iperf_server_data.csv", index=False)
    	
    	plt.figure()
    	plt.plot(range(len(df.index)), bw, label = "Bandwith")
  	
    	plt.xlabel('Time [s]')
    	plt.ylabel(unit_bw)
    	plt.title('iPerf measurements from server side - UDP')
    	plt.legend()
    	plt.show()
    	
    	plt.figure()
    	plt.plot(range(len(df.index)), transferred_data, label = "Transferred_data")
    	
    	plt.xlabel('Time [s]')
    	plt.ylabel(unit_transfer)
    	plt.title('iPerf measurements from server side - UDP')
    	plt.legend()
    	plt.show()
    	
    	plt.figure()
    	plt.plot(range(len(df.index)), jitter, label = "Jitter")
    	
    	plt.xlabel('Time [s]')
    	plt.ylabel(unit_jitter)
    	plt.title('iPerf measurements from server side - UDP')
    	plt.legend()
    	plt.show()
    	
    	plt.figure()
    	plt.plot(range(len(df.index)), packet_loss, label = "Packet loss")
    	
    	plt.xlabel('Time [s]')
    	plt.ylabel('%')
    	plt.title('iPerf measurements from server side - UDP')
    	plt.legend()
    	plt.show()
    else:
        transferred_data=[]
        bw=[]
        for row in range(len(lines)):
            lines[row]=lines[row].split()
            if len(lines[row])>2:
                if '0.00-' not in lines[row][2] and lines[row][0]=='[' and lines[row][1]!='ID]' and '-' in lines[row][2]:
                    transferred_data.append(float(lines[row][4]))
                    unit_transfer=lines[row][5]
                    bw.append(float(lines[row][6]))
                    unit_bw=lines[row][7]

        bw_mean=np.mean(bw[:])
        total_transfer=np.sum(transferred_data[:]) 
	
        df=pd.DataFrame(list(zip(transferred_data, bw)), columns = ['Transferred data', 'Bandwith'])
    	
        df.to_csv(path+"/iperf_server_data.csv", index=False)
    	
        plt.figure()import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import statistics
from tabulate import tabulate

def iparser_client(output, format_unit, path, connection):

    lines=output.splitlines()

    if connection!="":
        transferred_data=[]
        bw=[]
		
        for row in range(len(lines)):
            lines[row]=lines[row].split()
            if len(lines[row])>2:
                if '0.00-' not in lines[row][2] and lines[row][0]=='[' and lines[row][1]!='ID]' and '-' in lines[row][2]:
                    transferred_data.append(float(lines[row][4]))
                    unit_transfer=lines[row][5]
                    bw.append(float(lines[row][6]))
                    unit_bw=lines[row][7]
		
        bw_mean=np.mean(bw[:])
        total_transfer=np.sum(transferred_data[:]) 
		
        df=pd.DataFrame(list(zip(transferred_data, bw)), columns = ['Transferred data', 'Bandwith'])
		
        df.to_csv(path+"/iperf_client_data.csv", index=False)
        
        #mean
        tr_data_mean = statistics.mean(transferred_data)
        bw_mean = statistics.mean(bw)
        #variance
        tr_data_variance = statistics.variance(transferred_data)
        bw_variance = statistics.variance(bw)
        #st dev
        tr_data_stdev = statistics.stdev(transferred_data)
        bw_stdev = statistics.stdev(bw)
        
        data_to_print = [['transferred_data', tr_data_mean, tr_data_variance, tr_data_stdev],
                         ['bandwith', bw_mean, bw_variance, bw_stdev]]
        
        print (tabulate(data_to_print, headers=["Metric", "Mean", "Variance", "Std deviation"]))
		
        plt.figure()
        plt.plot(range(len(df.index)), bw, label = "Bandwith")
		
        plt.xlabel('Time [s]')
        plt.ylabel(unit_bw)
        plt.title('iPerf measurements from client side - UDP')
        plt.legend()
        plt.show()
		
        plt.figure()
        plt.plot(range(len(df.index)), transferred_data, label = "Transferred_data")
		
        plt.xlabel('Time [s]')
        plt.ylabel(unit_transfer)
        plt.title('iPerf measurements from client side - UDP')
        plt.legend()
        plt.show()   	
    else:
        transferred_data=[]
        bw=[]
        retr=[]
        cwnd=[]
		
        for row in range(len(lines)):
            lines[row]=lines[row].split()
            if len(lines[row])>2:
                if '0.00-' not in lines[row][2] and lines[row][0]=='[' and lines[row][1]!='ID]' and '-' in lines[row][2]:
                    transferred_data.append(float(lines[row][4]))
                    unit_transfer=lines[row][5]
                    bw.append(float(lines[row][6]))
                    unit_bw=lines[row][7]
                    cwnd.append(float(lines[row][9]))
                    unit_cwnd=lines[row][10]
                    retr.append(lines[row][8])
    		
        bw_mean=np.mean(bw[:])
        total_transfer=np.sum(transferred_data[:])
		
        df=pd.DataFrame(list(zip(transferred_data, bw, retr, cwnd)), columns = ['Transferred data', 'Bandwith', 'Retries', 'Congestion window'])
		
        df.to_csv(path+"/iperf_server_data.csv", index=False)
        
        #mean
        tr_data_mean = statistics.mean(transferred_data)
        bw_mean = statistics.mean(bw)
        retr_mean = statistics.mean(retr)
        cwnd_mean = statistics.mean(cwnd)
        #variance
        tr_data_variance = statistics.variance(transferred_data)
        bw_variance = statistics.variance(bw)
        retr_variance = statistics.variance(retr)
        cwnd_variance = statistics.variance(cwnd)
        #st dev
        tr_data_stdev = statistics.stdev(transferred_data)
        bw_stdev = statistics.stdev(bw)
        retr_stdev = statistics.stdev(retr)
        cwnd_stdev = statistics.stdev(cwnd)
        
        data_to_print = [['transferred_data', tr_data_mean, tr_data_variance, tr_data_stdev],
                         ['bandwith', bw_mean, bw_variance, bw_stdev],
                         ['retries', retr_mean, retr_variance, retr_stdev],
                         ['cwnd', cwnd_mean, cwnd_variance, cwnd_stdev]]
        
        print (tabulate(data_to_print, headers=["Metric", "Mean", "Variance", "Std deviation"]))
		
        plt.figure()
        plt.plot(range(len(df.index)), bw, label = "Bandwith")
		
        plt.xlabel('Time [s]')
        plt.ylabel(unit_bw)
        plt.title('iPerf measurements from client side - TCP')
        plt.legend()
        plt.show()
		
        plt.figure()
        plt.plot(range(len(df.index)), transferred_data, label = "Transferred_data")
		
        plt.xlabel('Time [s]')
        plt.ylabel(unit_transfer)
        plt.title('iPerf measurements from client side - TCP')
        plt.legend()
        plt.show()
		
        plt.figure()
        plt.plot(range(len(df.index)), cwnd, label = "Congestion window")
		
        plt.xlabel('Time [s]')
        plt.ylabel(unit_cwnd)
        plt.title('iPerf measurements from client side - TCP')
        plt.legend()
        plt.show()
		
        plt.figure()
        plt.plot(range(len(df.index)), retr, label = "Retries")
		
        plt.xlabel('Time [s]')
        plt.ylabel('N.')
        plt.title('iPerf measurements from server side - TCP')
        plt.legend()
        plt.show()
    
def iparser_server(format_unit, path, connection):

    with open(path+'/iperf_server_output.txt','r+') as f:
    	lines=f.readlines()
    	f.truncate(0)
    if connection!="None":
		
        transferred_data=[]
        bw=[]
        jitter=[]
        packet_loss=[]
        lost_n=[]
        lost1=[]
        lost2=[]
    	
        for row in range(len(lines)):
            lines[row]=lines[row].split()
            if len(lines[row])>2:
                    if '0.00-' not in lines[row][2] and lines[row][0]=='[' and lines[row][1]!='ID]' and '-' in lines[row][2]:
                        transferred_data.append(float(lines[row][4]))
                        unit_transfer=lines[row][5]
                        bw.append(float(lines[row][6]))
                        unit_bw=lines[row][7]
                        jitter.append(float(lines[row][8]))
                        unit_jitter=lines[row][9]
                        packet_loss.append(lines[row][11]) #(n%)
                        lost_n.append(lines[row][10]) #n/m
    	
        for i in range(len(packet_loss)):
        	packet_loss[i]=packet_loss[i][1:-2]
        	packet_loss[i]=float(packet_loss[i])
        	
        	a, b=lost_n[i].split('/')
        	lost1.append(int(a))
        	lost2.append(int(b))
        	
        bw_mean=np.mean(bw[:])
        total_transfer=np.sum(transferred_data[:]) 
        jitter_mean=np.mean(jitter[:])
   	
        a_total=np.sum(lost1[:]) 
        b_total=np.sum(lost2[:])
        if int(b_total)!=0:
        		packet_loss_total=int(a_total)/int(b_total)
	
        df=pd.DataFrame(list(zip(transferred_data, bw, jitter, packet_loss)), columns = ['Transferred data', 'Bandwith', 'Jitter', 'Packet loss'])
    	
        df.to_csv(path+"/iperf_server_data.csv", index=False)
        
        #mean
        tr_data_mean = statistics.mean(transferred_data)
        bw_mean = statistics.mean(bw)
        jitter_mean = statistics.mean(jitter)
        packet_loss_mean = statistics.mean(packet_loss)
        #variance
        tr_data_variance = statistics.variance(transferred_data)
        bw_variance = statistics.variance(bw)
        jitter_variance = statistics.variance(jitter)
        packet_loss_variance = statistics.variance(packet_loss)
        #st dev
        tr_data_stdev = statistics.stdev(transferred_data)
        bw_stdev = statistics.stdev(bw)
        jitter_stdev = statistics.stdev(jitter)
        packet_loss_stdev = statistics.stdev(packet_loss)
        
        data_to_print = [['transferred_data', tr_data_mean, tr_data_variance, tr_data_stdev],
                         ['bandwith', bw_mean, bw_variance, bw_stdev],
                         ['jitter', jitter_mean, jitter_variance, jitter_stdev],
                         ['packet_loss', packet_loss_mean, packet_loss_variance, packet_loss_stdev]]
        
        print (tabulate(data_to_print, headers=["Metric", "Mean", "Variance", "Std deviation"]))
    	
        plt.figure()
        plt.plot(range(len(df.index)), bw, label = "Bandwith")
          	
        plt.xlabel('Time [s]')
        plt.ylabel(unit_bw)
        plt.title('iPerf measurements from server side - UDP')
        plt.legend()
        plt.show()
    	
        plt.figure()
        plt.plot(range(len(df.index)), transferred_data, label = "Transferred_data")
           	
        plt.xlabel('Time [s]')
        plt.ylabel(unit_transfer)
        plt.title('iPerf measurements from server side - UDP')
        plt.legend()
        plt.show()
           	
        plt.figure()
        plt.plot(range(len(df.index)), jitter, label = "Jitter")
           	
        plt.xlabel('Time [s]')
        plt.ylabel(unit_jitter)
        plt.title('iPerf measurements from server side - UDP')
        plt.legend()
        plt.show()
           	
        plt.figure()
        plt.plot(range(len(df.index)), packet_loss, label = "Packet loss")
           	
        plt.xlabel('Time [s]')
        plt.ylabel('%')
        plt.title('iPerf measurements from server side - UDP')
        plt.legend()
        plt.show()
    else:
        transferred_data=[]
        bw=[]
        for row in range(len(lines)):
            lines[row]=lines[row].split()
            if len(lines[row])>2:
                if '0.00-' not in lines[row][2] and lines[row][0]=='[' and lines[row][1]!='ID]' and '-' in lines[row][2]:
                    transferred_data.append(float(lines[row][4]))
                    unit_transfer=lines[row][5]
                    bw.append(float(lines[row][6]))
                    unit_bw=lines[row][7]

        bw_mean=np.mean(bw[:])
        total_transfer=np.sum(transferred_data[:]) 
	
        df=pd.DataFrame(list(zip(transferred_data, bw)), columns = ['Transferred data', 'Bandwith'])
    	
        #mean
        tr_data_mean = statistics.mean(transferred_data)
        bw_mean = statistics.mean(bw)
        #variance
        tr_data_variance = statistics.variance(transferred_data)
        bw_variance = statistics.variance(bw)
        #st dev
        tr_data_stdev = statistics.stdev(transferred_data)
        bw_stdev = statistics.stdev(bw)
        
        data_to_print = [['transferred_data', tr_data_mean, tr_data_variance, tr_data_stdev],
                         ['bandwith', bw_mean, bw_variance, bw_stdev]]
        
        print (tabulate(data_to_print, headers=["Metric", "Mean", "Variance", "Std deviation"]))
        
        df.to_csv(path+"/iperf_server_data.csv", index=False)
    	
        plt.figure()
        plt.plot(range(len(df.index)), bw, label = "Bandwith")
  	
        plt.xlabel('Time [s]')
        plt.ylabel(unit_bw)
        plt.title('iPerf measurements from server side - TCP')
        plt.legend()
        plt.show()

        plt.figure()
        plt.plot(range(len(df.index)), transferred_data, label = "Transferred_data")
    	
        plt.xlabel('Time [s]')
        plt.ylabel(unit_transfer)
        plt.title('iPerf measurements from server side - TCP')
        plt.legend()
        plt.show()
    


        plt.plot(range(len(df.index)), bw, label = "Bandwith")
  	
        plt.xlabel('Time [s]')
        plt.ylabel(unit_bw)
        plt.title('iPerf measurements from server side - TCP')
        plt.legend()
        plt.show()

        plt.figure()
        plt.plot(range(len(df.index)), transferred_data, label = "Transferred_data")
    	
        plt.xlabel('Time [s]')
        plt.ylabel(unit_transfer)
        plt.title('iPerf measurements from server side - TCP')
        plt.legend()
        plt.show()
    

