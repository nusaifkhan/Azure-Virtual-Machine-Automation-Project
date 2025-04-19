# Import necessary libraries for Azure authentication and virtual machine management
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

# Replace these values with your Azure subscription ID, resource group name, and virtual machine name
# SUBSCRIPTION_ID: Unique identifier for your Azure subscription
# RESOURCE_GROUP_NAME: Name of the resource group containing the virtual machine
# VM_NAME: Name of the virtual machine you want to manage
SUBSCRIPTION_ID = "your_subscription_id"
RESOURCE_GROUP_NAME = "your_resource_group_name"
VM_NAME = "your_vm_name"

# Authenticate using DefaultAzureCredential
# This supports various authentication methods (e.g., Azure CLI, environment variables)
credential = DefaultAzureCredential()

# Initialize the ComputeManagementClient
# This client allows interaction with Azure Compute services, like managing VMs
compute_client = ComputeManagementClient(credential, SUBSCRIPTION_ID)

# Function to start the specified virtual machine
def start_vm():
    print(f"Starting VM: {VM_NAME}...")
    # Send a request to start the VM asynchronously
    async_vm_start = compute_client.virtual_machines.begin_start(RESOURCE_GROUP_NAME, VM_NAME)
    # Wait for the operation to complete
    async_vm_start.wait()
    print(f"VM {VM_NAME} started successfully.")

# Function to stop the specified virtual machine
def stop_vm():
    print(f"Stopping VM: {VM_NAME}...")
    # Send a request to deallocate (stop) the VM resources asynchronously
    async_vm_deallocate = compute_client.virtual_machines.begin_deallocate(RESOURCE_GROUP_NAME, VM_NAME)
    # Wait for the operation to complete
    async_vm_deallocate.wait()
    print(f"VM {VM_NAME} stopped successfully.")

# Main script execution
if __name__ == "__main__":
    # Prompt the user to choose an action (start or stop the VM)
    action = input("Enter 'start' to start the VM or 'stop' to stop the VM: ").strip().lower()
    
    # Check the user's input and call the appropriate function
    if action == "start":
        start_vm()  # Call start_vm() if the user chooses 'start'
    elif action == "stop":
        stop_vm()  # Call stop_vm() if the user chooses 'stop'
    else:
        # Handle invalid input
        print("Invalid action. Please enter 'start' or 'stop'.")

