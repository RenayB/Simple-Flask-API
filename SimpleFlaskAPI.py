from flask import Flask , request , jsonify

app = Flask(__name__)

#root , endpoint
@app.route("/")
def home():
    return "Home"

#GET routes
@app.route("/get-user/<user_id>") # <- path parameter , used in url with given id
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200

#POST routes
@app.route("/create-user", methods=["POST"]) #test using postman software
def create_user():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)
