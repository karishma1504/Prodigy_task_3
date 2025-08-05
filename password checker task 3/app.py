from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def check_password_strength(password):
    suggestions = []
    strength = 0

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Add at least 8 characters")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add an uppercase letter")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add a lowercase letter")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        suggestions.append("Add a digit")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        suggestions.append("Add a special character")

    if strength <= 2:
        verdict = "Weak"
    elif strength == 3 or strength == 4:
        verdict = "Moderate"
    else:
        verdict = "Strong"

    return verdict, suggestions, strength

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data.get("password", "")
    verdict, suggestions, strength = check_password_strength(password)
    return jsonify({
        "verdict": verdict,
        "suggestions": suggestions,
        "strength": strength
    })

if __name__ == "__main__":
    app.run(debug=True)
