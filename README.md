# Harden-Runner – Testing Detections
 
Harden-Runner is a purpose-built network filtering and runtime security monitoring platform for CI/CD runners. To learn more about Harden-Runner functionality, see [here](https://docs.stepsecurity.io/harden-runner)

This repository contains the workflow file `POC-detections-gh-hosted.yml` that contains several different jobs to trigger all Harden-Runner detections, which include: 

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
* You can simply copy the workflow file into your own organization to test out the detections. This workflow file uses GitHub hosted runners with Harden-Runner deployed on the jobs. For Self-Hosted scenario, please reach out to StepSecurity
* This workflow uses a workflow_dispatch trigger, meaning it can be started manually from the Actions tab by selecting POC Detections and clicking **Run workflow**
* To observe findings after running the workflow, navigate to the StepSecurity tenant -> Harden Runner -> Workflow Runs and select the run with detection events triggered

## Detections not requiring a baseline
The following detections will trigger as soon as you run the workflow one time:

#### Reverse Shell (Process Event Detection) 
* Monitors for reverse shell activity. An attacker establishing a reverse shell can potentially run commands, exfiltrate data, and move laterally. 

#### Privileged Container (Process Event Detection) 
* Monitors for priviledged container scenarios. A priviledged container process can give an attacker the ability to escape the container and access host resources, exfiltrate data, and move laterally 

#### Runner Worker Memory Read (Process Event Detection) 
* Monitors for attempts to read runner.worker process memory. Compromises like TJ-Actions rely on accessing runner worker memory to extract secrets

#### Imposter Commit (Process Event Detection)
* Monitors for Actions using tags that are pointed to malicious commits - specifically, commits that do not exist in the actions repository or are pointed to a fork. A technique that was used in tj-actions to evade detection

#### HTTPS Monitoring for Anamalous Network Calls
* Monitors for API calls that contain data-exfiltration signals - specifically, POST, PUT, or PATCH requests going outside of the organization where the workflow resides

#### Secrets in Build Logs
* Monitors build logs for potentially leaked secrets. Once the workflow is run, this can be seen in the `Controls` tab for the `handle-private-key` job

## Detections that require a baseline
Harden-Runner allows you to **monitor or block** any anomalous network calls that are made which are not established in the baseline. The baseline currently is generated after 100 job runs. In order to test this feature, a script is included to run the job 100 times

* After running the [baseline generation script](), run the workflow one more time (Actions tab -> POC Detections and before running the workflow, enter a new domain, ie `https://www.pastebin.com`)
* Observe the result in the Workflow Runs insights page under the Network Events tab



 

 

 

 
