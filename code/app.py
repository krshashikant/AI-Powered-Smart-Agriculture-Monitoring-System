from flask import Flask, render_template, jsonify
import random

app = Flask(_name_)

@app.route("/")
def home():
    data = {
        "temperature": round(random.uniform(25, 35), 1),
        "humidity": round(random.uniform(45, 80), 1),
        "soil_moisture": random.randint(30, 90),
        "pump_status": random.choice(["ON", "OFF"])
    }
    return jsonify(data)

if _name_ == "_main_":
    app.run(debug=True)
