import json

# Load the repository's data from a JSON file
with open('repository_data.json', 'r') as file:
    repository_data = json.load(file)

# Define the chatbot function
def chatbot():
    # Start the conversation
    print("Hi there! What would you like to do today?")

    # Keep the conversation going until the user says 'bye'
    while True:
        user_input = input('> ')

        if user_input.lower() == 'bye':
            print("Goodbye!")
            break

        # Check if the user's input is a command to store data
        if user_input.lower().startswith('store '):
            # Get the data from the user's input
            data = user_input[6:]

            # Add the data to the repository's data
            repository_data.append(data)

            # Confirm that the data was stored successfully
            print('Data stored successfully!')
        else:
            print("I'm sorry, I didn't understand. Could you please rephrase?")

# Run the chatbot
chatbot()

# Save the updated repository data to the JSON file
with open('repository_data.json', 'w') as file:
    json.dump(repository_data, file)