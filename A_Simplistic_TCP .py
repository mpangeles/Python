#Automatons, or Finite State Machines (FSM), are extremely useful to programmers when it comes to software design. You will be given a simplistic version of an FSM to code for a basic TCP session.

#The outcome of this exercise will be to return the correct state of the TCP FSM based on the array of events given.
#def traverse_TCP_states(events):
    state = "CLOSED"  # initial state, always
    process=["CLOSED"]
    for event in events:
        len_process=len(process)-1
        
        if event=="APP_PASSIVE_OPEN" and process[len_process]=="CLOSED":
            process.append("LISTEN")
        elif event=="APP_ACTIVE_OPEN" and process[len_process]=="CLOSED":
            process.append("SYN_SENT");  
        elif event=="RCV_SYN" and process[len_process]=="LISTEN":
            process.append("SYN_RCVD");  
        elif event=="APP_SEND" and process[len_process]=="LISTEN":
            process.append("SYN_SENT");
        elif event=="APP_CLOSE" and process[len_process]=="LISTEN":
            process.append("CLOSED");
        elif event=="APP_CLOSE" and process[len_process]=="SYN_RCVD":
            process.append("FIN_WAIT_1");
        elif event=="RCV_ACK" and process[len_process]=="SYN_RCVD":
            process.append("ESTABLISHED");
        elif event=="RCV_SYN" and process[len_process]=="SYN_SENT":
            process.append("SYN_RCVD");
        elif event=="RCV_SYN_ACK" and process[len_process]=="SYN_SENT":
            process.append("ESTABLISHED");
        elif event=="APP_CLOSE" and process[len_process]=="SYN_SENT":
            process.append("CLOSED");
        elif event=="APP_CLOSE" and process[len_process]=="ESTABLISHED":
            process.append("FIN_WAIT_1");
        elif event=="RCV_FIN" and process[len_process]=="ESTABLISHED":
            process.append("CLOSE_WAIT");
        elif event=="RCV_FIN" and process[len_process]=="FIN_WAIT_1":
            process.append("CLOSING");
        elif event=="RCV_FIN_ACK" and process[len_process]=="FIN_WAIT_1":
            process.append("TIME_WAIT");
        elif event=="RCV_ACK" and process[len_process]=="FIN_WAIT_1":
            process.append("FIN_WAIT_2");
        elif event=="RCV_ACK" and process[len_process]=="CLOSING":
            process.append("TIME_WAIT");
        elif event=="RCV_FIN" and process[len_process]=="FIN_WAIT_2":
            process.append("TIME_WAIT");
        elif event=="APP_TIMEOUT" and process[len_process]=="TIME_WAIT":
            process.append("CLOSED");
        elif event=="APP_TIMEOUT" and process[len_process]=="TIME_WAIT":
            process.append("CLOSED");
        elif event=="APP_CLOSE" and process[len_process]=="CLOSE_WAIT":
            process.append("LAST_ACK");
        elif event=="RCV_ACK" and process[len_process]=="LAST_ACK":
            process.append("CLOSED");     
        else:
            process.append("ERROR");     
      
    len_process=len(process)-1   
    return process[len_process]