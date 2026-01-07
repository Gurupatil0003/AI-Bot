https://docs.google.com/spreadsheets/d/1nTLfdCPN1YvAIOTuDL4xiG5X5Apk8ltvpgGGbGP86AY/edit?usp=sharing


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
