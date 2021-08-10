import os
import sys

model_name = sys.argv[1]


os.system("python ../3_Feature_Selection/Selection.py")
os.system(f"python ../4_Model/randomforest.py {model_name}")
os.system(f"python ../5_New_Prediction/prediction.py {model_name}")