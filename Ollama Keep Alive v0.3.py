import ollama
import time

# Initialize the client with the default host and port
client = ollama.Client(host='http://127.0.0.1:11434')

# List available models using ollama.list()
models = ollama.list()

# Print the available models
print("Available models:")
for idx, model_info in enumerate(models['models']):
    print(f"{idx + 1}. {model_info['name']}")

# Allow the user to select a model
model_index = int(input("Select the model number you want to use: ")) - 1
selected_model = models['models'][model_index]['name']

def ask_question():
    # Make a request to the selected model
    response = client.chat(
        model=selected_model,
        messages=[
            {
                'role': 'user',
                'content': 'What is 2+2?'
            }
        ]
    )
    # Do not print the response
    pass

print("The service has started, your resource utilization should have increased to reflect the model that you've chosen.")

# Loop to ask the question every 4.5 minutes
while True:
    ask_question()
    # Wait for 4.5 minutes (270 seconds)
    time.sleep(270)


