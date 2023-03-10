#%%
import openai
import requests

openai.api_key = "YOUR_API_KEY"

prompt = "Hello, how are you?"

response = requests.post("https://api.openai.com/v1/engines/davinci-codex/completions",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    },
    json={
        "prompt": prompt,
        "max_tokens": 10
    }
)

print(response.json()["choices"][0]["text"])

"""
Reference
[1] https://twoicefish-secu.tistory.com/495
"""
