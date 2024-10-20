import json


def load_secrets(file_name):
    """Loads secrets from a JSON file."""

    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the secrets file
    secrets_path = os.path.join(current_dir, file_name)

    # Check if the file exists
    if os.path.isfile(secrets_path):
        with open(secrets_path, 'r') as file:
            secrets_data = json.load(file)
        return {key: str(value) for key, value in secrets_data.items()}
    else:
        print(f"Error: Secrets file '{secrets_path}' not found.")
        return None  # Or handle the error appropriately
