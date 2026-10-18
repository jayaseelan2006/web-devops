from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>My DevOps Website</title>
        </head>
        <body>
            <h1>Hello! 👋</h1>
            <h1>Jayaseelan U</h1>
            <h2>Welcome to My DevOps Project</h2>
            <p>This website is built with Python Flask.</p>
            <p>Next: Docker → GitHub → CI/CD → AI</p>
        </body>
    </html>
    """

app.run(host="0.0.0.0", port=5000)
