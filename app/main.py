from flask import Flask, jsonify, request, render_template
from collections import OrderedDict

app = Flask(__name__)


# Route สำหรับเสิร์ฟ HTML
@app.route("/post_form", methods=["GET"])
def post_form():
    return render_template("post_with_js.html")


# Route สำหรับ root URL
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the root of the Flask API!"})


# Route สำหรับ API
@app.route("/api", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Flask API!"})


# Route สำหรับรับค่าผ่าน POST
@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.get_json()  # รับข้อมูล JSON จาก body ของ request
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # ใช้ OrderedDict เพื่อรักษาลำดับของ key-value
    ordered_data = OrderedDict((key, data[key]) for key in data)
    return jsonify({"received": ordered_data})  # ส่งข้อมูลกลับไปในรูปแบบ JSON


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
