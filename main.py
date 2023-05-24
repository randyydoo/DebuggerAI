import os
import openai

# assign api key from env var
openai.api_key = os.environ.get(API_KEY)

def get_message(prompt): 
    messages = [{"role": "user", "content": prompt}] 
    response = openai.ChatCompletion.create(
            model = "gpt-3.5=turbo",
            messages = messages,
            temperature = 0)
    return response.choices[0].messages["content"]

