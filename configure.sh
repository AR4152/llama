#!/bin/bash

echo "This script will:"
echo "1. Set an environment variable 'MLHUB_LLAMA_HEALTH_DATA' with the path to your health data folder."
echo "2. Install the Ollama tool on your system."
echo "3. Pull a small-sized model called 'smollm' using Ollama.\n"

# (a) set env var of health data folder
echo "Please enter the folder path where your health data exists."
read -p "Folder path: " folder_path
export MLHUB_LLAMA_HEALTH_DATA="$folder_path"

# Add the environment variable to shell configuration file
shell_config_file="$HOME/.bashrc"
if [[ -f $shell_config_file ]]; then
    echo "export MLHUB_LLAMA_HEALTH_DATA=\"$folder_path\"" >> "$shell_config_file"
    echo "Environment variable 'MLHUB_LLAMA_HEALTH_DATA' added to $shell_config_file. Please run source $shell_config_file to update the configuration."
else
    echo "Could not find shell configuration file. Please manually add the line below to your shell config file:"
    echo "export MLHUB_LLAMA_HEALTH_DATA=\"$folder_path\""
    sleep 10
fi

# (b) install ollama
echo "Installing Ollama"
curl -fsSL https://ollama.com/install.sh | sh
echo "Installed Ollama"

# (c) pull a small sized model
echo "Pulling a small-sized model using Ollama"
ollama pull smollm
echo "Small model 'smollm' pulled successfully"
