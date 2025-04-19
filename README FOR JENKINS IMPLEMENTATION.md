# Azure Virtual Machine Start/Stop Automation with Jenkins

## Overview

This project automates the start/stop operations of Azure Virtual Machines (VMs) using a Jenkins pipeline. The pipeline supports user selection of either a Python script (using Azure SDK) or a Bash script (using Azure CLI) to perform the operations. This integration showcases automation and highlights DevOps best practices.

---

## Features

- Automated management of Azure Virtual Machines.
- User interaction within the pipeline to select the desired script (Python or Bash).
- Error handling and robust logging mechanisms.
- Demonstrates best practices in Jenkins pipeline integration.

---

## Prerequisites

1. **Jenkins Installed**:
   - Make sure Jenkins is installed and running. You can download it [here](https://www.jenkins.io/).
   - Ensure required plugins are installed:
     - **Pipeline Plugin**
     - **Git Plugin**
     - **SSH Agent Plugin** (if required for remote execution)

2. **Azure CLI Installed**:
   - Install the Azure CLI from [here](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).
   - Authenticate your Azure account:
     ```bash
     az login
     ```

3. **Python Installed**:
   - Ensure Python 3.6+ is installed. Install it from [python.org](https://www.python.org/).

4. **Scripts**:
   - Clone or download the repository containing your Python and Bash scripts.

---

## Pipeline Implementation

### **Step 1: Add Your Scripts to a Git Repository**
1. Push your Python (`azure_vm_manager.py`) and Bash (`azure_vm_manager.sh`) scripts to a GitHub (or other Git) repository.
2. Include the following files:
   - `azure_vm_manager.py` (Python script)
   - `azure_vm_manager.sh` (Bash script)
   - `requirements.txt` (Python dependencies)

---

### **Step 2: Create the Jenkins Pipeline**

#### **Create a New Pipeline Job**:
1. Open the Jenkins dashboard and click **New Item**.
2. Select **Pipeline** and give it a name (e.g., `Azure VM Manager`).
3. Click **OK** to proceed.

#### **Pipeline Configuration**:
1. Under **Pipeline** -> **Definition**, choose **Pipeline script**.
2. Paste the following `Jenkinsfile`:

```groovy
pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-repository.git'
            }
        }
        stage('User Choice') {
            steps {
                script {
                    // Ask the user which script to run
                    def userInput = input(
                        message: 'Choose which script to execute:',
                        parameters: [
                            choice(name: 'SCRIPT', choices: 'Python\nBash', description: 'Select Python or Bash')
                        ]
                    )
                    // Save user input in an environment variable
                    env.USER_CHOICE = userInput
                }
            }
        }
        stage('Execute Script') {
            steps {
                script {
                    // Execute based on user input
                    if (env.USER_CHOICE == 'Python') {
                        sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                        python azure_vm_manager.py
                        '''
                    } else if (env.USER_CHOICE == 'Bash') {
                        sh '''
                        chmod +x azure_vm_manager.sh
                        ./azure_vm_manager.sh
                        '''
                    } else {
                        echo "Invalid choice. No script executed."
                    }
                }
            }
        }
    }
}

```

## Step 3: Configure Jenkins Environment
### Install Python on the Jenkins Server: Ensure Python is installed on the Jenkins server. For Linux:
```bash
sudo apt install python3 python3-venv python3-pip
```

### Install Required Python Dependencies: Ensure the requirements.txt file is present in the repository and used during the pipeline's Python execution stage.

### Azure CLI Setup: Install Azure CLI on the Jenkins server and authenticate using:
```bash
az login
```

### Permissions: Ensure Jenkins has access to execute the scripts and sufficient Azure permissions to manage VMs.

##### Running the Pipeline in Production

###### Trigger the Pipeline:

### Go to the Jenkins dashboard, select the pipeline, and click Build Now.
##### Interactive Script Selection:
##### During execution, Jenkins will prompt you to select either the Python or Bash script.

## Monitor the Logs:
#### View real-time logs in Jenkins to monitor progress and capture any errors.

### Validate:
##### Ensure that the chosen script starts or stops the Azure Virtual Machine as expected.

## Best Practices for Production
##### Non-Interactive Mode: For production pipelines, avoid interactive steps like input. Instead, pass parameters (e.g., SCRIPT=Python) to the pipeline.
##### Error Handling: Ensure robust error handling in both the pipeline and scripts to gracefully handle failures.
##### Credentials Management: Use tools like Jenkins Credentials or Azure Key Vault to securely store sensitive data.
##### Scalability: Consider integrating this automation with  Infrastructure as Code (IaC) tools (e.g., Terraform), or Kubernetes for scalability.

## Contributing
#### Contributions are welcome! Feel free to open issues or submit pull requests for improvements.
