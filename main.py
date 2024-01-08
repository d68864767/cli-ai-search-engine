import sys
from search_engine import search
from utils import load_config, sanitize_query

def main():
    # Load the configuration settings
    config = load_config()
    if not config:
        print("Failed to load configuration. Exiting program.")
        sys.exit(1)

    # Greet the user and provide instructions
    print("Welcome to the AI-Powered Search Engine!")
    print("Type your query and press Enter to search. Type 'exit' to quit.")

    # Main loop
    while True:
        # Get user input
        user_input = input("Search query: ").strip()

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting the search engine. Goodbye!")
            break

        # Sanitize the user input
        sanitized_query = sanitize_query(user_input)

        # Perform the search
        results = search(sanitized_query)

        # Check if there are results and display them
        if results:
            print("Search results:")
            for i, result in enumerate(results, start=1):
                print(f"{i}. {result}")
        else:
            print("No results found for your query.")

        print("\n")  # Print a newline for better readability between searches

if __name__ == "__main__":
    main()
