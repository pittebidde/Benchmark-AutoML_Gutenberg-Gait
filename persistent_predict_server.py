# Imports
import sys
import joblib
import numpy as np


def main():
    model = joblib.load(sys.argv[1]) # Load the model from the specified path
    print("Loading model READY")

    for line in sys.stdin: # Read input lines from standard input
        if line.strip() == "EXIT":
            break
        input_path, output_path = line.strip().split("\t") # Split the input line into input and output paths
        X = np.load(input_path)
        y_pred = model.predict(X)
        np.save(output_path, np.asarray(y_pred, dtype=float)) # Vorhersagen als float speichern (bool/int-Labels werden zu 0.0/1.0/2.0)



if __name__ == '__main__':
    main()