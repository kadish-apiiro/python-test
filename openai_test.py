import os
from openai import OpenAI

def get_chat_completion(prompt_text):
    """
    Sends a prompt to an OpenAI chat completion model and returns the generated text.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # You can choose other models like "gpt-3.5-turbo", "gpt-4", etc.
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt_text}
            ],
            max_tokens=150, # Maximum number of tokens to generate in the response
            temperature=0.7 # Controls the randomness of the output. Higher values mean more random.
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"


# It is recommended to load your API key from an environment variable for security.
# For example, set OPENAI_API_KEY in your system environment.
# Alternatively, you can set it directly like: client = OpenAI(api_key="YOUR_API_KEY")
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

user_prompt = "Tell me a short, interesting fact about space."
generated_text = get_chat_completion(user_prompt)
print(f"User Prompt: {user_prompt}")
print(f"AI Response: {generated_text}")

print("\n--- Another Example ---")
user_prompt_2 = "Write a creative opening sentence for a fantasy story."
generated_text_2 = get_chat_completion(user_prompt_2)
print(f"User Prompt: {user_prompt_2}")
print(f"AI Response: {generated_text_2}")
