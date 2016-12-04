# Anomaly-Detection of ports 

Overview:- 
This project is based on anomaly detection of ports on client machine. Code was designed using python language.

Language:- 
Python

Resources:-
Ubuntu, Windows, IDLE 3.5, py2exe, libraries. 

Summary:- 
For this project, two files are created. One file (Client_Auto_Detect) can be executed at client machine which will continuously monitor the detection of open ports and other file (Server_Auto_Detect) can be executed at server end that will recieve the alerts from client machine on detection of any new open port. 

Working:-
It is two tier architecture. Client machine will continuously scan the specified or all tcp ports on its machine. Any detection of new port will trigger an event and forward it to server which listens on specific port "5555" to receive alerts. Any new port detection will be triggered as alerts and client will forward it to server. At server end, logs will be stored at file with named as  "Storage.dat" (.dat extension as the server is ubuntu). In addition, all the subsequent logs will be appended to the existing logs on the same file.

Use cases :- 
1. Anomaly detection of ports - Sudden detection of port apart from allowed ports may be detected as anomaly behavior. 
2. Port Scanner - It can be used to detect port on the server 
3. Prevent exfiltration or exploitation - An exfiltration of critical data and exploitation of vulnerable ports can be mitigated to large extent with detection mechanism. 

Road Map or Extension:- 
I am working on the extension part of this project which will provide the administrator a privilege to take appropriate action on detection of unwanted open ports.  






