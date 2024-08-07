import pickle



with open("NBClassifier.pkl", "rb") as f_in:
  model = pickle.load(f_in)
  
def predict_recommendation(features):
  prediction = model.predict(features)
  return prediction