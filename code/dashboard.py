from flask import Flask, render_template
from sensor import Sensor

app = Flask(_name_)
sensor = Sensor()

@app.route("/")
def dashboard():
    data = sensor.get_sensor_data()
    return render_template("dashboard.html", data=data)

if _name_ == "_main_":
    app.run(debug=True)
