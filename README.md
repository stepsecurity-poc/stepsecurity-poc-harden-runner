# Harden-Runner POC Detections
 
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

This workflow uses a workflow_dispatch trigger, meaning the workflows can be triggered manually from the Actions tab by selecting the workflow and clicking **Run workflow**
## Prerequisites
* Ensure you have installed the [StepSecurity GitHub App](https://github.com/apps/stepsecurity-actions-security) and have access to your StepSecurity dashboard
  
## Environment setup and information 
* You can fork this repository or simply copy the workflow files into your own organization for testing. The workflow files use GitHub hosted runners with Harden-Runner deployed on the jobs. For Self-Hosted scenario, please [reach out to StepSecurity](https://www.stepsecurity.io/contact).
* This workflow uses a workflow_dispatch trigger, meaning the workflows can be triggered manually from the Actions tab by selecting the workflow and clicking **Run workflow**
* Most detections do not require a baseline to be established and will be triggered upon running the [POC Detections workflow](https://github.com/step-security-poc/stepsecurity-poc-harden-runner/blob/main/.github/workflows/POC-detections-gh-hosted.yml) file one time
* To detect and block *anomalous network calls*, a baseline is required to be established. For testing purposes, it is recommended to reduce the minimum number of runs from the default (100) to 1
  * This can be done under your dashboard: `Admin Console -> Settings -> Anomaly Detection` - set this as '1' and **save changes**

## Triggering detections not requiring a baseline
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
* Monitors build logs for potentially leaked secrets. Once the workflow is run, the leaked build log secret can be seen in the `Controls` tab for the `handle-private-key` job

## Triggering detections requiring a baseline
After a baseline is established, Harden Runner can **audit or block** any new, anomalous network calls that are outside of the baseline. The baseline is [configurable](https://docs.stepsecurity.io/admin-console/settings/anomaly-detection#configuration) by number of job runs required, or by number of days elapsed. You can find this in your tenant dashboard under `Admin Console -> Settings -> Anomaly Detection`. While the default is 100, it is recommended to lower this for easier testing purpose. 

* Run the workflow based on the number of runs set above to generate a baseline. You can verify the baseline is stable under the `Harden-Runner -> Baseline` tab
* Run the workflow one more time, this time entering a new domain. (`Actions tab -> POC Detections` and before running the workflow, enter a new domain, ie `https://www.pastebin.com`)
* Since this new domain is now outside of the baseline, it will trigger an anomalous network call - to observe the anomalous network call, navigate to the workflow runs insights page under the Network Events tab
* Block Policy - [this section is currently being updated]

##Additional advanced testing scenarios

For self-hosted ARC (Actions Runner Controller) deployments, StepSecurity supports lockdown mode - allowing you to also block some process events (reverse shell, priviledged container, runner worker memory read)
