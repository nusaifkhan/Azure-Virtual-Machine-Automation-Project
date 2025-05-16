#!/bin/bash

# Replace with your Azure subscription ID, resource group, and VM name
SUBSCRIPTION_ID="your_subscription_id"
RESOURCE_GROUP_NAME="your_resource_group_name"
VM_NAME="your_vm_name"

# Function to start the VM
start_vm() {
  echo "Starting VM: $VM_NAME..."
  az vm start --subscription "$SUBSCRIPTION_ID" --resource-group "$RESOURCE_GROUP_NAME" --name "$VM_NAME"
  if [ $? -eq 0 ]; then
    echo "VM $VM_NAME started successfully."
  else
    echo "Failed to start VM $VM_NAME."
  fi
}

# Function to stop the VM
stop_vm() {
  echo "Stopping VM: $VM_NAME..."
  az vm deallocate --subscription "$SUBSCRIPTION_ID" --resource-group "$RESOURCE_GROUP_NAME" --name "$VM_NAME"
  if [ $? -eq 0 ]; then
    echo "VM $VM_NAME stopped successfully."
  else
    echo "Failed to stop VM $VM_NAME."
  fi
}

# Main script
echo "Enter 'start' to start the VM or 'stop' to stop the VM:"
read -r action

case $action in
  start)
    start_vm
    ;;
  stop)
    stop_vm
    ;;
  *)
    echo "Invalid action. Please enter 'start' or 'stop'."
    ;;
esac
