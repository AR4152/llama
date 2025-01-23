import subprocess

def get_installed_models_raw():
    """Fetch the raw output of installed models using the Ollama CLI."""
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr.strip()}"
    except FileNotFoundError:
        return "Error: Ollama CLI is not installed or not in PATH."

def get_installed_models():
    """Fetch the list of installed models using the Ollama CLI."""
    return parse_installed_models(get_installed_models_raw())

def parse_installed_models(output):
    """Parse the output of 'ollama list' to extract model names."""
    lines = output.strip().split("\n")
    
    models = []
    for line in lines[1:]:
        parts = line.split()
        if len(parts) >= 2:
            model_name = parts[0]
            models.append(model_name)
    
    return models

def is_model_installed(model_name):
    """Check if a specific model is installed."""
    installed_models = get_installed_models_raw()
    return model_name in installed_models

def pull_model(model_name):
    """Run subprocess to download the specified model."""
    try:
        result = subprocess.run(["ollama", "pull", model_name], text=True)
        if result.returncode == 0:
            return True
        else:
            print(f"Error pulling model '{model_name}':", result.stderr)
            return False
    except FileNotFoundError:
        print("Ollama is not installed or not in PATH.")
        return False
