# MLHub toolkit for llama - pull
# ml pull llama <model_name>

# ----------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------

import click
from util import pull_model

@click.command()
@click.argument("model_name", required=True)

# -----------------------------------------------------------------------
# Command line argument and options
# -----------------------------------------------------------------------

def cli(model_name: str):
    """
    Pull/Download specified model using Ollama.
    Wrapper for 'ollama pull' command.
    """
    if pull_model(model_name):
        print(f"Model '{model_name}' pulled successfully.")
    else:
        print(f"Error pulling model '{model_name}'")
    
if __name__ == "__main__":
    cli(prog_name="pull")
