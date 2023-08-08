import streamlit as st

st.title("ChatApp")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Please enter your query here."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    print(st.session_state.messages)

response = f"Echo: {prompt}"  # replace this with actual request response
# Display assistant response in chat message container
with st.chat_message("assistant"):
    # TODO contact the docker container and get the autocompletion response and then
    st.markdown(response)
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})
