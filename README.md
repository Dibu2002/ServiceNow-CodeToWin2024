**Problem Statement:**

Rapid urbanization and motorization has led to mobility issues in cities. There is a need to develop a system that analyzes real-time traffic data to optimize traffic flow, reduce congestion, and
enhance the overall efficiency of transportation networks.

**Solution:**

We propose a system that -
computes optimal green signal time based on current traffic at a signal
ensures lane with more traffic is allotted green signal for longer duration
obtains quick results at real-time
has provision to allow important vehicles like ambulance/ fire truck to pass with minimal delay
notifies nearby hospital/police station in case of accident or other anomalies
collects data to draw insights for better traffic management

**Architecture:**

1) Red Light Module:
   Calculates traffic density in terms of Units (parameter to assign importance to a vehicle based on speed & volume)
  
2) Green Light Module:
   Computes number of units crossing a line to derive **time taken per unit** to move at green light for clearing lane
   
3) Signal Switching Algorithm:
   Custom algorithm inspired by Multi-Level Feedback Queue (MLFQ) process scheduling algorithm to decide the order in which lanes become green.


**NOTE:** Please check Red_Light_Module branch for it's code.
   
   

