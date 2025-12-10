from flask import Flask,render_template,request
from langchain_google_genai  import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def AI_bot():
    if request.method=="POST":
        user_msg=request.form.get("msg")
        model=ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            api_key=os.getenv("GOOGLE_API_KEY")
        )
        reply=model.invoke(user_msg).content
    return render_template("index.html",reply=reply)

# debug mode running on 8000 port
if __name__=="__main__":
    app.run(debug=True)