import steamlit as st
import google.generativeai as genai


st.set_page_config(page_title = "Out chatbot ", layout="centered")
st.title("Our chatbot")


st.secret["GEMINI_API_KEY"]
geneai.configure(api_key=api_key)
model=genai.GenerativeModel('gemini-1.5-flash')


if "messages" not in st.session_state.messages: 
    st.session_state.messages=[]

for message in st.session_state.messages(message["role"]):
    st.markdown(message["content"])



if prompt := st.chat_input("Κάνε μου μια ερώτησηση "):
    st.session_state.messages.append({"role":"user", "content":"prompt"})
with st.chat_message("user"):st.markdown(prompt)


st.chat_message("assistant"):response=model.generate_content(prompt)

st.markdown(response.text)

 st.session_state.messages.append({"role":"assistant", "content":response.text})
