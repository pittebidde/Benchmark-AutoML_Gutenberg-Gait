import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

import sys
import joblib
import numpy as np


def main():
    model = joblib.load(sys.argv[1])
    print("READY", flush=True)

    for line in sys.stdin:
        line = line.strip()
        if line == "EXIT":
            break
        input_path, output_path = line.split("\t")
        done_path = output_path + ".done"
        err_path = output_path + ".err"
        try:
            X = np.load(input_path)
            y_pred = model.predict(X)
            np.save(output_path, np.asarray(y_pred, dtype=float))
            with open(done_path, "w") as f:
                f.write("OK")
        except Exception as e:
            with open(err_path, "w") as f:
                f.write(str(e))


if __name__ == '__main__':
    main()