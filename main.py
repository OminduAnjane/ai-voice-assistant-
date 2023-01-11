import openai_secret_manager
import openai

# Get the API key
secrets = openai_secret_manager.get_secret("openai")
api_key = secrets["api_key"]

# Use the API key to create an OpenAI client
openai.api_key = api_key

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

print(generate_response("Hello, How can I help you today?"))
