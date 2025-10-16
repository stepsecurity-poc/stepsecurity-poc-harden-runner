# Harden-Runner – Testing Detections
 
Harden-Runner is a purpose-built network filtering and runtime security monitoring platform for CI/CD runners. To learn more about Harden-Runner functionality, see [here](https://docs.stepsecurity.io/harden-runner)

This repository contains a workflow to trigger all Harden-Runner detections, which include: 

* Secrets in Build Logs 
* Secrets in Artifacts 
* Outbound Calls Blocked 
* Anomalous Outbound Network Calls 
* Suspicious Outbound Network Calls 
* Source Code Overwritten 
* HTTPS Outbound Network Calls 
* Action Uses Imposter Commit 
* Suspicious Process Events (Reverse Shell, Priviledged Container, Runner Memory Read) 

 

## Triggering Non-baseline depedendent Detections 

#### Reverse Shell (Process Event Detection) 
Monitors for reverse shell activity. An attacker establishing a reverse shell can potentially run commands, exfiltrate data, and move laterally. 

> **How to test it:**  
> Trigger [workflow name] and observe the [job name]'s activity under the **Network Events** tab.  
> This workflow contains a request …

#### Privileged Container (Process Event Detection) 
Monitors for reverse shell activity. An attacker establishing a reverse shell can potentially run commands, exfiltrate data, and move laterally. 

> **How to test it:**  
> Trigger [workflow name] and observe the [job name]'s activity under the **Network Events** tab.  
> This workflow contains a request …

#### HTTPS Outbound Network Calls
Monitors HTTPS calls for malicious activity. A detection will trigger if an API call is exfiltrating data (PUT, POST, PATCH) to outside of the Organization that the workflow is running in 

> **How to test it:**  
> Trigger [workflow name] and observe the [job name]'s activity under the **Network Events** tab.  
> This workflow contains a request …

How to test it: Trigger [workflow name] and observe the [job name]'s activity under the Network Events tab. This workflow contains a request …. 

 

 

 

 
