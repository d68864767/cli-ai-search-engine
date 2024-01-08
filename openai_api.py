import openai
import json

# Load the configuration file
with open('config.json') as config_file:
    config = json.load(config_file)

# Extract the OpenAI API key and API settings from the configuration
OPENAI_API_KEY = config['openai_api_key']
API_SETTINGS = config['api_settings']

# Initialize OpenAI API client
openai.api_key = OPENAI_API_KEY

def query_openai(prompt, engine=API_SETTINGS['engine'], temperature=API_SETTINGS['temperature'], max_tokens=API_SETTINGS['max_tokens']):
    """
    This function sends a query to the OpenAI API and returns the response.

    :param prompt: The user's query to be sent to the OpenAI API.
    :param engine: The engine to use for the OpenAI API.
    :param temperature: Controls randomness in the generation. Lower is more deterministic.
    :param max_tokens: The maximum number of tokens to generate in the response.
    :return: The text of the response from the OpenAI API.
    """
    try:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        print(f"An error occurred while querying the OpenAI API: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
# result = query_openai("What is the capital of France?")
# print(result)
