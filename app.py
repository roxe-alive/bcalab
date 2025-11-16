from flask import Flask, send_file

app =  Flask(__name__)

pdf_link = "IMG-20250608-WA0002.jpg"

@app.route("/")
def home():
    return send_file(pdf_link)

@app.route("/health")
def health_check():
    return "OK", 200


if __name__ == "__main__":
    app.run()