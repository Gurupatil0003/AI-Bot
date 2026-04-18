

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

```python
from gtts import gTTS
from IPython.display import Audio

text=input()

tts=gTTS(text=text,lang="en",tld="co.in",slow=True)
tts.save("o.mp3")
Audio("o.mp3")


```

```python

!pip install deep-translator
from deep_translator import GoogleTranslator

translated = GoogleTranslator(source='auto', target='kn').translate("hello")
print(translated)

```


```python
from gtts import gTTS
from IPython.display import Audio

text=input()

tts=gTTS(text=text,lang="en",tld="co.in",slow=True)
tts.save("o.mp3")
Audio("o.mp3")


```


```python
!pip install diffusers
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
from transformers import pipeline

# Load code generation model
generator = pipeline("text-generation", model="Salesforce/codegen-350M-mono")

# Prompt for code
prompt = "Write a Python function to check if a number is prime:\n"

# Generate code
output = generator(
    prompt,
    max_length=120,
    temperature=0.2,   # low = more accurate code
    num_return_sequences=1
)

# Print result
print(output[0]['generated_text'])

```


```python

from transformers import pipeline

generator = pipeline('text-generation', model='distilgpt2')

output = generator("I love coding because", max_length=30)

print(output[0]['generated_text'])

```

```python
from transformers import pipeline
import gradio as gr

# Load model
generator = pipeline('text-generation', model='distilgpt2')

# Function for Gradio
def generate_text(prompt):
    output = generator(prompt, max_length=10)
    return output[0]['generated_text']

# Gradio Interface
interface = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text",
    title="Simple Text Generator",
    description="Generate text using distilgpt2"
)

# Launch app
interface.launch()


```

```python



# Function for Gradio
def generate_text(prompt):
    output = generator(
        prompt,
        max_length=100,          # increase length
        temperature=0.7,         # control randomness
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.2,  # reduce repetition
        do_sample=True
    )
    return output[0]['generated_text']

# Gradio Interface
interface = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text",
    title="Simple Text Generator",
    description="Generate text using distilgpt2"
)

# Launch app
interface.launch()


```

```python
import transformers
import torch
from transformers import AutoTokenizer

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_id)

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    tokenizer=tokenizer,
    model_kwargs={"torch_dtype": torch.float32},
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a personal assistant."},
    {"role": "user", "content": "can u make plan for me tommorow"},
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

outputs = pipeline(
    prompt,
    max_new_tokens=150,
    temperature=0.7,
)

print(outputs[0]["generated_text"])



```

```python
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

# Set API key directly in Colab (simplest way)
os.environ["GOOGLE_API_KEY"] = "AIzaSyA8NQUVkhIN0iIKSIt8L28gDAkNVt6_ld4"

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

system_message = SystemMessage(
    content="""
You are a personal diet planner.

- Only answer diet, nutrition, and health questions.
- If anything else is asked, reply:
  "I only help with diet planning."
- Give simple meal plans (breakfast, lunch, dinner, snacks).
"""
)

chat_history = [system_message]

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    chat_history.append(HumanMessage(content=user_input))

    response = model.invoke(chat_history)
    chat_history.append(response)

    print("Model:", response.content)
    


```

```python
from transformers import pipeline
classifier = pipeline('sentiment-analysis')
text = "I love this product! It's amazing and works perfectly."
result = classifier(text)
print(f"Sentiment: {result}")

```

```python

text = """
Face expression is the significant device in computer apparition and a predictable knowledge discovery application in automation, personal security and moveable devices. However, the state-of-the-art machine and deep learning (DL) methods has complete this technology game altering and even better human matching part in terms of accurateness. This paper focuses on put on one of the progressive deep learning tools in face expression to achieve higher accuracy. In this paper, we focusses on Automatic Facial Expressions and Identification of different face reactions using Convolution Neural Network.  Here, we framed our own data and trained by convolution neural networks. Human behavior can be easily predicted using their facial expression, which helps marketing team, psychological team and other required team to understand the human facial expression more clearly.
Human behavior can be easily predicted using their facial expression, which helps marketing team, psychological team and other required team to understand the human facial expression more clearly. In Video feed and other feeds provide good recommendations to the users. We can provide good environment to the user of the corresponding product helps the company to improve its customer base.

"""

```

```python
image_captioner = pipeline("image-to-text")
image = r'/content/download.jfif'
cation = image_captioner(image)
print(cation)

```

```python
vqa_pipeline = pipeline('visual-question-answering') #visual q and a
image = r'/content/download.jfif'
question = input('Enter a question to ask about image: ')
result = vqa_pipeline(image, question)
print(result)

```

```python
import requests
import json

API_KEY = "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"

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("🤖 Chat started (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Chat ended")
        break

    response = requests.post(
        url,
        headers=headers,
        json={
            "model": "openrouter/free",
            "messages": [{"role": "user", "content": user_input}]
        }
    )

    result = response.json()

    if "choices" in result:
        print("\n🤖 Bot:", result["choices"][0]["message"]["content"], "\n")
    else:
        print("\n⚠️ API Error:\n", result, "\n")

```

```python
import pandas as pd
import gradio as gr
from sklearn.linear_model import LinearRegression

# Data
df = pd.read_csv("/content/Salary Data (2) (1).csv")

# Encode (simple)
df = pd.get_dummies(df)

X = df.drop("Salary", axis=1)
y = df["Salary"]

# Train model
model = LinearRegression().fit(X, y)

# Prediction function (VERY SIMPLE)
def predict(age, exp):
    return int(model.predict([[age, exp] + [0]*(X.shape[1]-2)])[0])

# UI
gr.Interface(
    fn=predict,
    inputs=["number","number"],
    outputs="text",
    title="Salary Predictor (Simple)"
).launch()

```
