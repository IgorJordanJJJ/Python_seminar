import json

# Load the chatbot's data from a JSON file
with open('chatbot_data.json', 'r') as file:
    chatbot_data = json.load(file)

# Define the chatbot function
def chatbot():
    # Start the conversation
    print(chatbot_data['greetings'][0])

    # Keep the conversation going until the user says 'bye'
    while True:
        user_input = input('> ')

        if user_input.lower() == 'bye':
            print(chatbot_data['farewells'][0])
            break

        # Check if the user's input matches any of the chatbot's responses
        for key in chatbot_data['responses']:
            if user_input.lower() in key:
                print(chatbot_data['responses'][key])
                break
        else:
            print(chatbot_data['fallback'][0])

# Run the chatbot
chatbot()

# Save the updated chatbot data to the JSON file
with open('chatbot_data.json', 'w') as file:
    json.dump(chatbot_data, file)







