import streamlit as st
import nltk
import torch
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

chatbot = pipeline("text-generation", model = "distilgpt2")
 
def Healthcare_chatbot(user_input):
    user_input_lower = user_input.lower()

    if "symptom" in user_input_lower or "feel" in user_input_lower:
        return check_symptoms(user_input_lower)
    if any(emergency in user_input_lower for emergency in ["emergency", "chest pain", "can't breathe", "severe bleeding"]):
        return " This sounds like an emergency. Please contact emergency services or visit a hospital immediately."
    elif "tip" in user_input_lower or "health" in user_input_lower:
        return get_health_tips()
    elif "mental" in user_input_lower or "stress" in user_input_lower:
        return mental_health_tips()
    elif "book" in user_input_lower or "appointment" in user_input_lower:
        return "Sure, I can help you book an appointment. Please provide your name and preferred date."
    else:
        response = chatbot(user_input,max_length=500, num_return_sequences=1) 
        
    return response[0]['generated_text']

def check_symptoms(text):
    if "fever" in text:
        return "You may have a viral infection. Stay hydrated and monitor your temperature regularly."
    elif "cough" in text:
        return "It could be a common cold or allergy. If it persists more than a week, consult a doctor."
    elif "headache" in text:
        return "You might need rest, hydration, and low screen time. Consider seeing a doctor if it continues."
    else:
        return "That symptom isn't recognized right now. Please consult a healthcare professional for detailed advice."
    

def get_health_tips():
    tips= ["Stay hydrated: Drink at least 2 liters of water daily.",
        "Get 7–8 hours of sleep every night.",
        "Exercise at least 3 times a week.",
        "Eat a balanced diet rich in fruits and vegetables.",
        "Avoid processed foods and too much sugar."]
    
    return "Here are some general health tips:\n" + "\n".join(["- " + tip for tip in tips])

def mental_health_tips():
    tips = [
        "Take 5-minute breaks during work to reset your mind.",
        "Practice meditation or breathing exercises daily.",
        "Talk to someone you trust about your feelings.",
        "Avoid information overload from social media.",
        "Seek help from a therapist if you feel persistently low."
    ]
    
    return "Here are a few mental wellness tips:\n" + "\n".join(["- " + tip for tip in tips])

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("how can i help you?")
    if st.button("submit"):
        if user_input:
            st.write("user : ",user_input)
            with st.spinner("processing your request...,please wait........."):
                response = Healthcare_chatbot(user_input)
            st.write("assistant : ",response)
        else:
            st.write("Please enter a message")
main()
