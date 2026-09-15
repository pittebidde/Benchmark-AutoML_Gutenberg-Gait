import sys
import json
import numpy as np
import pandas as pd
from autogluon.tabular import TabularPredictor


def main():
    with open(sys.argv[2]) as f: # Load the feature names from the specified JSON file
        feature_names = json.load(f)

    predictor = TabularPredictor.load(sys.argv[1]) # Load the model from the specified path
    print("Loading model READY")

    for line in sys.stdin:
        if line.strip() == "EXIT":
            break
        input_path, output_path = line.strip().split("\t") # Split the input line into input and output paths
        X = np.load(input_path)
        df = pd.DataFrame(X, columns=feature_names) # AutoGluon needs input as Dataframe
        y_pred = predictor.predict(df) 
        np.save(output_path, np.asarray(y_pred.values, dtype=float)) # Vorhersagen als float speichern (bool/int-Labels werden zu 0.0/1.0/2.0)


if __name__ == '__main__':
    main()