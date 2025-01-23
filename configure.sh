#!/bin/bash

# different level logger function
log_message() {
    local level="$1"
    local message="$2"
    echo -e "[$level] $message"
}

# function to check if Ollama is already installed
check_ollama_installed() {
    if command -v ollama &>/dev/null; then
        log_message "INFO" "Ollama is already installed on your system."
        return 0
    else
        log_message "INFO" "Ollama is not installed. Proceeding with installation."
        return 1
    fi
}

# validate user input
get_user_response() {
    while true; do
        echo "Do you want to proceed with the installation? (yes/no): "
        read -p user_response
        case "$user_response" in
            yes|YES|Yes)
                log_message "INFO" "User confirmed installation."
                return 0 # Exit the function and proceed
                ;;
            no|NO|No)
                log_message "INFO" "Installation aborted by the user."
                exit 0
                ;;
            *)
                log_message "ERROR" "Invalid input. Please enter 'yes' or 'no'."
                ;;
        esac
    done
}

log_message "INFO" "This script will install the Ollama tool on your system."

# check if Ollama is already installed
if check_ollama_installed; then
    log_message "SUCCESS" "No further action is required."
    exit 0
fi

get_user_response

# proceed with installation if user confirmed
log_message "INFO" "Installing Ollama..."
if curl -fsSL https://ollama.com/install.sh | sh; then
    log_message "SUCCESS" "Ollama has been successfully installed."
else
    log_message "ERROR" "Failed to install Ollama. Please check your internet connection or the installation script."
    exit 1
fi
