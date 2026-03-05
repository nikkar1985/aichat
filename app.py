import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Our chatbot", layout="centered")
st.title("Our chatbot")

# 1. Διόρθωση στο API Key (χρήση st.secrets)
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Αρχικοποίηση του session state 
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Εμφάνιση παλαιότερων μηνυμάτων
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Λήψη ερώτησης από τον χρήστη
if prompt := st.chat_input("Κάνε μου μια ερώτηση"):
    # Προσθήκη ερώτησης στο state και εμφάνιση
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 5. Παραγωγή απάντησης από το μοντέλο
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
    
    # 6. Αποθήκευση της απάντησης στο ιστορικό 
    st.session_state.messages.append({"role": "assistant", "content": response.text})
