# Harden-Runner – Testing Detections
 
Harden-Runner is a purpose-built network filtering and runtime security monitoring platform for CI/CD runners. To learn more about Harden-Runner functionality, see [here](https://docs.stepsecurity.io/harden-runner)

This repository contains a workflow that triggers all Harden-Runner detections, which include: 

* Secrets in Build Logs 
* Secrets in Artifacts 
* Outbound Calls Blocked 
* Anomalous Outbound Network Calls 
* Suspicious Outbound Network Calls 
* Source Code Overwritten 
* HTTPS Outbound Network Calls 
* Action Uses Imposter Commit 
* Suspicious Process Events (Reverse Shell, Priviledged Container, Runner Memory Read) 

## Setting up your environment
* You can simply copy the workflow file into your own organization to test out as it is independent of anything outside of the workflow file. 
* This workflow uses a workflow_dispatch trigger, meaning it can be started manually from the Actions tab by selecting POC Detections and clicking Run workflow

## Detections not requiring a baseline
The following detections will trigger as soon as you run the workflow one time:

#### Reverse Shell (Process Event Detection) 
* Monitors for reverse shell activity. An attacker establishing a reverse shell can potentially run commands, exfiltrate data, and move laterally. 

#### Privileged Container (Process Event Detection) 
* Monitors for priviledged container scenarios. A priviledged container process can give an attacker the ability to escape the container and access host resources, exfiltrate data, and move laterally 

#### Runner Worker Memory Read (Process Event Detection) 
* Monitors for attempts to read runner.worker process memory. Compromises like TJ-Actions rely on accessing runner worker memory to extract secrets 



 

 

 

 
