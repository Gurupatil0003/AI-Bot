

https://docs.google.com/spreadsheets/d/1nTLfdCPN1YvAIOTuDL4xiG5X5Apk8ltvpgGGbGP86AY/edit?usp=sharing


```python
import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Set up API key
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

# Initialize model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

print("Chat started. Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    response = model.invoke(user_input)
    print("Model:", response.content + "\n")


```
```python

#model insallation 
!pip install git+https://github.com/huggingface/diffusers 

```

```python
from os import pipe 
from diffusers import StableDiffusionPipeline 
import torch 
m_id = "sd-legacy/stable-diffusion-v1-5" 
pipe=StableDiffusionPipeline.from_pretrained(m_id) 
pipe=pipe.to("cuda") #cpu 

prompt = "an astronut riding a horse in the moon" 
image =pipe(prompt).images[0] 
display(image) 


```
```python

A simple Python chatbot built with Flask and LangChain that uses Google’s Gemini model to generate AI responses through a clean interface.

```

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

print("🤖 Gemini AI Bot (Terminal Mode)")
print("Type 'exit' to quit\n")

while True:
    user_msg = input("You: ")

    if user_msg.lower() in ["exit", "quit"]:
        print("👋 Exiting AI Bot. Bye!")
        break

    response = model.invoke(user_msg)
    print("AI:", response.content)
    print("-" * 50)


```

```python
from flask import Flask, render_template, request
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Initialize model once
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

@app.route("/", methods=["GET", "POST"])
def AI_bot():
    reply = ""

    if request.method == "POST":
        user_msg = request.form.get("msg")
        reply = model.invoke(user_msg).content

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run()


```

```python

<!DOCTYPE html>
<html>
<head>
    <title>Gemini AI Bot</title>

    <style>
        body {
            background-color: #0f172a;
            font-family: Arial, sans-serif;
        }

        .container {
            width: 600px;
            margin: 60px auto;
            background: #020617;
            padding: 20px;
            border-radius: 10px;
            color: white;
        }

        form {
            display: flex;
            gap: 10px;
        }

        input {
            flex: 1;
            padding: 8px;
            border-radius: 5px;
            border: none;
        }

        button {
            padding: 8px 14px;
            border-radius: 5px;
            border: none;
            background: #22c55e;
            cursor: pointer;
        }

        .reply {
            margin-top: 15px;
            background: #1e293b;
            padding: 15px;
            border-radius: 5px;
        }

        .ai-text {
            white-space: pre-wrap;  /* ⭐ KEY LINE */
            line-height: 1.6;
        }
    </style>
</head>

<body>

<div class="container">
    <h2>🤖 Gemini AI Bot</h2>

    <form method="POST">
        <input type="text" name="msg" placeholder="Ask something..." required>
        <button type="submit">Ask</button>
    </form>

    {% if reply %}
    <div class="reply">
        <h4>AI Reply:</h4>
        <p class="ai-text">{{ reply }}</p>
    </div>
    {% endif %}
</div>

</body>
</html>


```

```python
GOOGLE_API_KEY=


```
