import os
import openai

# Clearing the Screen
os.system('clear')


sqlQuery = input('Enter your query: ')


openai.api_key = "API_KEY"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=sqlQuery,
  temperature=0.3,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response);