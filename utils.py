import json

def load_config(config_path='config.json'):
    """
    Load the configuration file.

    :param config_path: The path to the configuration file.
    :return: The configuration dictionary.
    """
    try:
        with open(config_path) as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        print(f"Configuration file {config_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the configuration file {config_path}.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading the configuration: {e}")
        return None

def save_config(config, config_path='config.json'):
    """
    Save the configuration dictionary to a file.

    :param config: The configuration dictionary to save.
    :param config_path: The path to the configuration file.
    """
    try:
        with open(config_path, 'w') as config_file:
            json.dump(config, config_file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving the configuration: {e}")

def sanitize_query(query):
    """
    Sanitize the user's search query to prevent potential abuse when using the OpenAI API.

    :param query: The user's search query.
    :return: The sanitized search query.
    """
    # Implement any necessary sanitization steps here.
    # This is a placeholder implementation and should be replaced with actual sanitization logic.
    sanitized = query.replace('\n', ' ').strip()
    return sanitized

# Additional utility functions can be added here as needed.
