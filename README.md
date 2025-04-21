
# Azure Virtual Machine Automation Project

## Overview

This repository provides scripts to automate the starting and stopping of Azure Virtual Machines (VMs). The project includes:
- A **Python Script** built using the Azure SDK for Python.
- A **Bash Script** leveraging the Azure CLI for simple command-line VM management.

Both scripts help optimize resource usage and improve operational efficiency.

---

## Features

- Start and stop Azure VMs interactively.
- Separate implementations for Python and Bash.
- Secure credential management using `.env` (for Python script).
- Error handling and logging for reliable execution.

---

## Prerequisites

1. An active Azure account with necessary permissions to manage VMs.
2. Installed tools:
   - Python 3.6 or later (for Python script).
   - Azure CLI (for both Python and Bash scripts).

---

## Python Script

### **Step 1: Install Dependencies**

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux/macOS
   venv\Scripts\activate        # Windows




## Install required packages using requirements.txt:
```bash
pip install -r requirements.txt
```
### If you don't have requirements.txt, manually install the dependencies:
``bash
pip install azure-identity azure-mgmt-compute python-dotenv
``
## Step 2: Set Up Environment Variables
### Create a .env file in the root directory with the following content:
```env
SUBSCRIPTION_ID=your_subscription_id
RESOURCE_GROUP_NAME=your_resource_group_name
VM_NAME=your_vm_name
```

## The Python script will load these variables automatically using the python-dotenv package.

## Step 3: Execute the Script
### Run the Python script:
```bash
python_script.py
```

## Follow the prompt to start or stop the VM:
**Enter start to start the VM.**
**Enter stop to stop the VM.**

## Bash Script
**Step 1: Install Azure CLI**
**Install the Azure CLI for your operating system:**
**Linux:**
```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

macOS:
bash
brew install azure-cli
```
### Windows: Download and install from Azure CLI Installer.

## Authenticate to Azure:
```bash
az login
```

## Step 2: Edit the Script
**Replace the placeholders in the Bash script (azure_vm_manager.sh) with your Azure details:**
```bash
SUBSCRIPTION_ID="your_subscription_id"
RESOURCE_GROUP_NAME="your_resource_group_name"
VM_NAME="your_vm_name"
```

### Step 3: Execute the Script
**Make the script executable:**
```bash
chmod +x bash_script.sh
```

## Run the script:
```bash
./bash_script.sh
```

## Follow the prompt to start or stop the VM:
#### Enter "start" to start the VM.

#### Enter "stop" to stop the VM.

## Notes
#### Ensure you have the correct permissions to manage VMs in your Azure account.
#### For the Python script, authentication relies on DefaultAzureCredential, which works seamlessly with Azure CLI or managed identity setups.
#### Use a .env file to keep sensitive information secure and separate from the codebase.

