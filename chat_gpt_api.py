import os
import openai

# Get the value of the environment variable 'Flex_AI_DailyTask'
api_key = os.environ.get('Flex_AI_DailyTask')

# Check if the environment variable exists
if api_key:
    openai.api_key = api_key
else:
    print("The Flex_AI_DailyTask environment variable is not set")

selected_model = "gpt-3.5-turbo"

def basic_generation(user_prompt):
    completion = openai.ChatCompletion.create(
        model=selected_model,
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response
