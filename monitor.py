import os
import time

while True:

    if os.path.exists("titanic_model.pkl"):
        print("Model File Exists")
    else:
        print("Model File Missing")

    time.sleep(10)