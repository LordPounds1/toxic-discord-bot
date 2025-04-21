from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("toxic_classifier.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")  # если ты его сохранял отдельно

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
