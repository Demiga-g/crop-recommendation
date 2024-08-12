import os
import pickle


def load_model(model_prefix="model_"):
    """
    Load the latest model from the specified directory with a given prefix.

    Parameters:
    model_prefix (str): The prefix of the model files to be loaded. Default is "model_".

    Returns:
    model: The loaded model object.

    Raises:
    FileNotFoundError: If no model files are found with the given prefix in the specified directory.
    """

    # get models path
    model_dir = os.path.join(os.path.dirname(__file__), '../..', 'models')
    model_files = [
        f
        for f in os.listdir(model_dir)
        if f.startswith(model_prefix) and f.endswith('.pkl')
    ]

    if not model_files:
        raise FileNotFoundError(
            f"No model files found starting with '{model_prefix}' in {model_dir}"
        )

    # Assuming the latest model is the last one alphabetically
    selected_model = model_files[-1]
    model_path = os.path.join(model_dir, selected_model)
    with open(model_path, 'rb') as f_in:
        model = pickle.load(f_in)
    return model
