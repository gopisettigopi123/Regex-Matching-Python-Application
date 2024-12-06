from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle regex matching
@app.route("/results", methods=["POST"])
def results():
    test_string = request.form["test_string"]
    regex = request.form["regex"]
    try:
        matches = re.findall(regex, test_string)
        error = None
    except re.error as e:
        matches = []
        error = f"Invalid regex: {e}"
    return render_template("index.html", test_string=test_string, regex=regex, matches=matches, error=error)

# Route to validate email
@app.route("/validate-email", methods=["POST"])
def validate_email():
    email = request.form["email"]
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid = re.match(regex, email) is not None
    return render_template("validate_email.html", email=email, is_valid=is_valid)

if __name__ == "__main__":
    app.run(debug=True)
