# Cloudguard Workload and Azure Functions

![CI](https://github.com/metalstormbass/Cloudguard_Azure_FSP/workflows/CI/badge.svg?event=push)

<p align="left">
    <img src="https://img.shields.io/badge/Version-1.0.0-green" />
</p>    

This document outlines how to apply Cloudguard Workload protection to an Azure Function in a CI/CD pipeline. The feature being installed is call FSP or Function Self Protect. This is for demonstration purposes only. Here is a logical diagram of the Azure Function: <br>

![](images/function1.PNG)

This function is deployed through Github Actions. That being said, it can be deployed using and CI/CD tool. All of the instructions for the CI/CD pipeline are stored in the [build.yml](.github/actions/build.yml). From a high level this is what the build pipeline does: <br><br>

1. Configure Runner Environment <br>
2. Set up Azure Resource Group, Storage Container and Function App <br>
3. Apply Cloudguard FSP (Function Self Protect <br>


<b> Get started by forking this repository! </b>

## Prerequisites

In order to run this demo, you need the following:

[Github Account](https://github.com) <br>
[Azure Account](https://portal.azure.com) <br>
[Check Point Cloud Security Posture Management Account](https://secure.dome9.com/) <br>

<br>
To run the activity.py script, you must also have Python3.

## Setup

Ensur Azure Serverless Protection is enabled on [Check Point Cloud Security Posture Management ](https://secure.dome9.com/) <br><br>

![](images/CSPM1.PNG)

### Microsoft Azure

Create an App Registration in Azure. As this will be used multiple times, please note the following:

- Application (client) ID <br>
- Directory (tenant) ID <br>
- Secret <br>
- Subscription ID <br>

Ensure that you give this app registration "Contributor" permission. This is required for Terraform to build the environment.

## Prep the Github Environment

First go to Settings > Secrets and populate the secrets: <br>

![](images/secrets.PNG)<br>

CG_TOKEN - <b>Note: This must be in the format DOME9_API_KEY:DOME_API_SECRET</b> <br>      AZURE_SUBSCRIPTION_ID <br>
AZURE_TENANT_ID <br>
AZURE_CLIENT_ID <br>
AZURE_CLIENT_SECRET <br>
AZ_RG -  This is the name of the resource group to be created <br> 
AZ_LOCATION - Azure Region. EG: West US 2 <br>
STORAGE_NAME - Name of your storage container <br>
APP_NAME - App name. <b>This must be unique</b> <br><br>

<b>Note: Standard naming for Azure rules apply.</b><br><br>

Second, select the "Actions" tab and enable workflows.

## Run the Build

To deploy this function to Azure, modify the _build_flag and commit the changes. This kicks off the Github Action which deploys the function. Once the build is finished, you will then see it in Check Point CSPM<br>

![](images/build.PNG)

