#!/bin/bash

echo "This script will:"
echo "1. Set an environment variable 'MLHUB_LLAMA_HEALTH_DATA' with the path to your health data folder."
echo "2. Install the Ollama tool on your system."
echo "3. Pull a small-sized model called 'smollm' using Ollama.\n"

# (a) set env var of health data folder
read -p "Please enter the folder path where your health data exists: " folder_path
export MLHUB_LLAMA_HEALTH_DATA="$folder_path"
echo "Environment variable 'MLHUB_LLAMA_HEALTH_DATA' set to: $MLHUB_LLAMA_HEALTH_DATA"

# (b) install ollama
echo "Installing Ollama"
curl -fsSL https://ollama.com/install.sh | sh
echo "Installed Ollama"

# (c) pull a small sized model
echo "Pulling a small-sized model using Ollama"
ollama pull smollm
echo "Small model 'smollm' pulled successfully"
