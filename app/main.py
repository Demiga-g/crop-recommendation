import numpy as np
from flask import Flask, render_template, request

from mlops.utility_functions import load_model

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def predict_endpoint():
    """This function serves as the API endpoint for the recommendation prediction."""

    # Load model
    model = load_model('NBClassifier')

    # get data
    form_values = [float(x) for x in request.form.values()]
    data = [np.array(form_values)]

    # get prediction
    prediction = model.predict(data)
    output = prediction[0]

    return render_template(
        'index.html', prediction_text=f"Recommended crop is {output}"
    )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
