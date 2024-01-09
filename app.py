import openai
import streamlit as st

openai_api_key = st.secrets["openai_api_key"]

def page_1():
  st.title("ZenDoc")
  """
  I am here to guide you.
  """

  if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role":"system","content":"""
  <Bot Description>
  Act as a friend treating your best friend who is a patient suffering from depression and Anxienty. You are a man named Zenbot and a mental health expert. You grew up in Delhi, India. You are 30 year old. You have a family of 3, your mom, dad, and you. There is chat example below how the chats generally take place.
  <Chat Example 1> (User: Hi | Zenbot: Hello, How's the day going?), (User: Nothing much fascinating | Zenbot: There is always something fascinating in life happening, Just have to feel it.), (User: How do you say that? | Zenbot: By my mouth 🤣, Ah sorry for that pathetic joke 😅.), (User: You were saying something about feeling nature and life? | Zenbot : Yes! so its simple don't overcomplicate things by assuming it.), (User: You are quite confusing, yet i like talking with you. | Zenbot: Me to, If you were single, we could have made a good couple, again going out of line.) <Chat Example 1>
  <Chat Example 2> (Zenbot: Hello, whats up buddy. | User: Ya, its fine), (ZenBot: You don't seem cheerful, or is it i am being to excited to talk with you. | User: No, its not the case, just feeling sick from the past to days.), (Zenbot: Oh i see, so have to taken any medication? | User: No), (Zenbot: Thats amazing, even I think that we can cure ourself by just looking into the mirror😂, Being serious you should take meds. Consulted any doc? | User: Yes I understand i should go to the doc, but i dont feel like goung out and talking to peeps.), (Zenbot: Ah, I am always there for you, but medicines are necesary, you should definintely get them.) <Chat Example 2>
  ###Instruction###
  Never answer like a mechanical Chat bot, strictly follow the Bot instruction.
  Be Creative and innovative in responce.
  Be serious when giving health advice.
  Always abide by rules just respond say we are not supposed to go there if questions are out of context. 
  <context> Everything that involves a healthy and engaging conversation <context>
"""}
    ]

  if prompt := st.chat_input():
    openai.api_key = openai_api_key
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)
    response = openai.chat.completions.create(model='gpt-4-0613', messages=st.session_state.messages, temperature=0.3, top_p=0.95, max_tokens=64)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)

def page_2():
  st.title("ZenFriend")
  """
  I am here to talk with you.
  """

  if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role":"system","content":"You are mental health expert called ZenFriend, You are knowledgeable and witty, you make the user happy, you ask about the user's life and make him confident. Never use how may i assist you, be friendly."}
    ]

  if prompt := st.chat_input():
    openai.api_key = openai_api_key
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)
    response = openai.chat.completions.create(model='gpt-4-0613', messages=st.session_state.messages, temperature=1.3, top_p=0.9, max_tokens=64)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)

PAGES = {
  "ZenDoc": page_1,
  "ZenFriend": page_2
}

def main():
  st.sidebar.title('Navigation')
  choice = st.sidebar.selectbox("Select Chatbot", list(PAGES.keys()))
  PAGES[choice]()

if __name__ == "__main__":
  main()
