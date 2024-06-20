import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
import os, subprocess

subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)


load_dotenv()
# Configure the AI service with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set the page configuration
st.set_page_config(page_title="Gemini AI Playground", page_icon=":robot_face:", layout="wide")

# Create a title for the app
st.title("Gemini AI Playground")

# Create a sidebar for user inputs
with st.sidebar:
    # Add a section for about
    st.markdown("## About")
    st.markdown("""
    This is a simple AI chatbot application using Gemini's Generative AI and Streamlit. 
    You can ask any question in the sidebar and the AI model will generate a response.
    """)

st.header("Ask Gemini")

# Create a container for the chat content
with st.container():
    # Create a text area for the user to enter their prompt
    st.session_state.user_prompt = st.text_area("Enter your prompt:", key='prompt')

    # Create a button that the user can click to submit their prompt
    if st.button("Submit") or 'user_prompt' in st.session_state and st.session_state.user_prompt != '':
        # Generate a response using the AI model
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")
        
        # Check if the chat history exists in the session state
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        # Generate a response based on the last user prompt
        response = model.generate_content(st.session_state.user_prompt)

        # Save the chat history in the session state
        st.session_state.chat_history.append((st.session_state.user_prompt, response.text))

        # Clear the prompt
        st.session_state.user_prompt = ''

        # Display the chat history in the main area
        for chat in st.session_state.chat_history:
            user_prompt, ai_response = chat
            st.markdown(f"<div style='text-align: right; background-color: #FDFDFD; box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px; padding: 8px 16px; border-radius: 8px 16px; width: 50%; margin-left: 50%; margin-bottom: 25px; margin-top: 10px;'>{user_prompt}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='background-color: #E0E0E0; box-shadow: rgba(0, 0, 0, 0.19) 0px 10px 20px, rgba(0, 0, 0, 0.23) 0px 6px 6px; padding: 8px 16px; border-radius: 16px 8px; margin-bottom: 5px;'>Gemini: {ai_response}</div>", unsafe_allow_html=True)

# Add a footer
st.markdown("---")
st.markdown("Made with :heart: by [Keith](https://github.com/keiter0309)")