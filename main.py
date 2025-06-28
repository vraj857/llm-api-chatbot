
from openai import OpenAI
import os
from dotenv import load_dotenv


# This script uses OpenAI's API to generate responses based on user prompts.
# It requires the OpenAI Python package and a valid API key stored in a .env file  
# Make sure to install the required packages:
# pip install openai python-dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    try:
        response = OpenAI.ChatCompletion.create(                                    #specify the model and messages 
            model="ChatGPT-4",                                                      # specify the model to use
            messages=[                                                              # list of messages to send to the model
                {"role": "system", "content": "You are a helpful assistant."},      # system message to set the context
                {"role": "user", "content": prompt}                                 # user message containing the prompt
            ]
        )
        return response.choices[0].message['content'] # return the content of the first choice in the response
    except Exception as e:
        return f"An error occurred: {str(e)}"

#Call the function and process the response
def main():
    prompt = input("Enter your prompt: ")
    response = generate_response(prompt)
    print("Response from ChatGPT-4:")
    print(response) 

if __name__ == "__main__":
    main()