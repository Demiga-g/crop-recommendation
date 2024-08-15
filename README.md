# Crop Recommendation

## About the Project

This project takes into account the growing trend of precision agriculture; loosely defined as the farming strategy where observation and measurement are used to make informed decision that can improve agricultural production and sustainability.

Therefore, this will be a proof of concept project that shows how a predictive model can be created to help farmers identify the "right" crop to focus on based on some parameters such as the content of nitrogen, phosphorous, and potassium in the soil; temperature, humidity, pH, and rainfall.

## Supporting Files

💾 The dataset used was obtained [here](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset/data).

📒 The notebook used to train different predictive models can be accessed [here](https://www.kaggle.com/code/demiga/crop-recommendation/edit).

## Application

💻 The deployed application can be accessed [here](https://crop-to-recommend.streamlit.app/)

👀 Here is a quick look at how it works:

![crop recommender demo](https://github.com/user-attachments/assets/bb96692f-14e5-4fb1-91bb-2ee3d2a4b72a)

🔊 **Disclaimer:** *This is a proof-of-concept project and should not be taken as an expert opinion regarding the crop recommended to grow. Moreover, this is an augmented dataset that was obtained in India based on the data available and could not be reflective of other regions' crop growth conditions.*

## Project's Structure

- `.github`: contains GitHub action workflow file for continuous integration.
- `app`: the Flask application files (included just for trial purposes).
- `models`: the pre-trained models used.
- `src`: the project's predefined package
- `streamlit`: the streamlit application file(s).

# Environment Setup

Create a virtual environment with the libraries need by the application. 

For this project Python 3.10 was used if you don't have it installed you can follow the instructions provided by [pyenv](https://github.com/pyenv/pyenv) to get it.

With that done, run the commands below to create the virtual environment with `pipenv` and use the `Pipfile` file provided to install the required libraries.

```bash
pipenv --python=3.10
pipenv shell
pipenv install
```

## Creating a Pre-Commit

Pre-commit is also used in this project, therefore ensure you install it and run it.

```
pip install pre-commit
pre-commit install
```

Check the content of the pre-commit file to confirm the Python location and where the pre-commit needs to execute every time we make a commit

```bash
less .git/hooks/pre-commit
```
