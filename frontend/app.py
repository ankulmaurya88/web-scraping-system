from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            # Run the main scraper
            try:
                result = subprocess.run(["python3", "main.py", url], capture_output=True, text=True)
                output = result.stdout + "\n" + result.stderr
            except Exception as e:
                output = f"Error: {e}"
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
