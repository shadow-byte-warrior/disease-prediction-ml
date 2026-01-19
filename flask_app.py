from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load models
dt_model = pickle.load(open("dt_model.pkl","rb"))
rf_model = pickle.load(open("rf_model.pkl","rb"))
nb_model = pickle.load(open("nb_model.pkl","rb"))
symptoms = pickle.load(open("symptom_list.pkl","rb"))

def predict_disease(user_symptoms):
    input_vector = np.zeros(len(symptoms))
    for s in user_symptoms:
        if s in symptoms:
            input_vector[symptoms.index(s)] = 1

    input_vector = input_vector.reshape(1,-1)

    p1 = dt_model.predict(input_vector)[0]
    p2 = rf_model.predict(input_vector)[0]
    p3 = nb_model.predict(input_vector)[0]

    final = max(set([p1,p2,p3]), key=[p1,p2,p3].count)
    return final

@app.route("/", methods=["GET","POST"])
def home():
    prediction = ""
    if request.method == "POST":
        selected = request.form.getlist("symptoms")
        prediction = predict_disease(selected)
    return render_template("index.html", symptoms=symptoms, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
