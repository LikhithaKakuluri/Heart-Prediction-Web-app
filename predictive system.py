import numpy as np
import pickle

loaded_model=pickle.load(open("C:/Users/kakul/OneDrive/Desktop/streamlit/Heartdisease_model.sav",'rb'))
input_data=(56,1,1,120,236,0,1,178,0,0.8,2,0,2)
input_data_as_numpy_array=np.array(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if (prediction[0]==1):
    print("The person has Defective Heart")
else:
    print("The person has Healthy Heart")