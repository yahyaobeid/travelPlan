# openai_utils.py
import json
import openai

# Set your OpenAI API key here
openai.api_key = "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"

def create_completion(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2000
        )
        
        response_text = response['choices'][0]['text'].strip()
        
        # Check if the response is valid JSON
        if not response_text.startswith('{'):
            raise ValueError("Invalid JSON response")
        
        return json.loads(response_text)
    except Exception as e:
        print("Error fetching completion:", str(e))
        return None

# import requests

# def send_api_request(destination, duration, preferences, food, interests):
#     # Your OpenAI API endpoint
#     api_endpoint = 'https://api.openai.com/v1/engines/davinci-codex/completions'

#     # Set your OpenAI API key
#     api_key = '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'

#     # Set the headers with your API key
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {api_key}',
#     }

#     # Prepare the data to be sent in the request body as a JSON object
#     data = {
#         'destination': destination,
#         'duration': duration,
#         'preferences': preferences,
#         'food': food,
#         'interests': interests,
#     }

#     try:
#         # Send the POST request to the OpenAI server
#         response = requests.post(api_endpoint, headers=headers, json=data)

#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             return response.json()  # If successful, return the JSON response
#         else:
#             print(f'Error: {response.status_code} - {response.text}')
#             return None

#     except requests.exceptions.RequestException as e:
#         print(f'Error: {e}')
#         return None