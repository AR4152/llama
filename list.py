# MLHub toolkit for llama - list
# ml list llama

# ----------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------

import click
from util import get_installed_models_raw

@click.command()

# -----------------------------------------------------------------------
# Command line argument and options
# -----------------------------------------------------------------------

def cli():
    """Lists installed models in Ollama."""
    cli_output = get_installed_models_raw()
    if len(cli_output.split("\n")) < 2:
        print("No models are installed.")
        return
    print(cli_output)
    
if __name__ == "__main__":
    cli(prog_name="list")
