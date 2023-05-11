import numpy as np
import pickle
import streamlit as st
import os


#loading the saved model
loaded_model=pickle.load(open("C:/Users/kakul/OneDrive/Desktop/streamlit/Heartdisease_model.sav",'rb'))


img = '''
<style>
.stApp {
    background-image: url("https://media.istockphoto.com/id/1359314170/photo/heart-attack-and-heart-disease-3d-illustration.jpg?b=1&s=170667a&w=0&k=20&c=fK2a-mCQ-dJA6066LnfQlN8awak_ZI6BsdKsmcQfCn8=");
    background-size: cover;
    background-position: top center;
    background-repeat: no-repeat;
    background-attachment: local;
    background-blur;
}
</style>
'''
st.markdown(img, unsafe_allow_html=True)

#creating a function for prediction

def heartdisease_prediction(input_data):
    
    #changing the input data to numpy array
    input_data_as_numpy_array=np.array(input_data,dtype=float)
    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0]==1):
        return "The person has Defective Heart"
    else:
        return "The person has Healthy Heart"


def main():

    

    #giving title
    st.title("Heart Disease Prediction Web App")

    #getting the input data from the user
   

    age=st.text_input("Enter the Age")

    sex=st.text_input("Enter the Sex")

    cp=st.text_input("Enter the Chest Pain Type")

    trestbps=st.text_input("Enter the Resting blood pressure Value (in mm Hg)")

    chol=st.text_input("Enter the Serum Cholestral level(in mg/dl)")

    fbs=st.text_input("Enter the fasting blood sugar level(in mg/dl)")

    restecg=st.text_input("Enter the resting electrocardiographic results")

    thalach=st.text_input("Enter the Maximum heart rate achieved Value")

    exang=st.text_input("Enter the Exercise Induced Agina experiencing")

    oldpeak=st.text_input("Enter the ST depression induced by exercise relative to rest")

    slope=st.text_input("Enter the slope of the peak exercise ST segment")

    ca=st.text_input("Enter the number of major vessels")

    thal=st.text_input("Enter the Thalassemia Value ")

    #code for prediction

    Report=''

    #creating button for prediction

    if st.button("Heart Disease Test Results"):

        Report=heartdisease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    
    st.success(Report)




if __name__ =='__main__':
    main()
    
