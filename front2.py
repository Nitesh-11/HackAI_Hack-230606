import json
import streamlit as st
# Set the title and a brief description
st.title("PhotoVoltaic Power Prediction")
st.write("Enter the minimum and maximum value of temperature")

# Add input fields for floating-point numbers
input1 = st.number_input("Enter the minimum value:", value=0.0, step=0.01)
input2 = st.number_input("Enter the maximum value:", value=0.0, step=0.01)




with open("database2.json", "r") as a:
    data = json.load(a)

value = data['boole']
if value == 0:
    if st.button(label="Condition"):
        # Create a message based on the input values
        message = f"There is a change in temperature"
        

        # Show the message in a dialog box
        st.info(message)
else:
    if st.button(label="Condition"):
        # Create a message based on the input values
        message = f"There is no change in temperature "
            

        # Show the message in a dialog box
        st.info(message)



with open('database.json', 'w') as f:
        a = {
        "input1": input1,
        "input2": input2
}
        json.dump(a,f)
        


# Add a button to trigger a dialog box
if st.button("Show Dialog Box"):
    # Create a message based on the input values
    message = f"You entered: Input 1 - {input1:.2f}, Input 2 - {input2:.2f}"
    

    # Show the message in a dialog box
    st.info(message)



def send():
    print(st.input1, " in the frontend file")
    
    return (input1, input2)

def check(boole):
    print(boole, " updation done here")
    with open('database2.json', 'w') as f:
        a = {
        "boole": boole
}
        json.dump(a,f)
    return