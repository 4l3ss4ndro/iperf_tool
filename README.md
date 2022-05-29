# iperf_tool
A tool to run iPerf3 multiple times, save its output in dataframes and plot the results.
All the files should be in both the client and the server and the settings in iperf_launcher_config.json must match.

# Server side
Run firstly iperf_server.py in the server terminal.
iperf_server_output.txt is a tmp file and must be blank. 
Stop the script with ctrl+C, graphs will be displayed and data will be saved in a csv.

# Client side
Run iperf_launcher.py in the client terminal.
Stop the script with ctrl+C, graphs will be displayed and data will be saved in a csv.
