from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt

import streamlit as st

load_dotenv()
model = ChatOpenAI()

st.header("Footballer Research Tool")

player_input = st.selectbox("Select a Player", ["-Select Player-","Manuel Neuer", "Thomas Muller", "Philip Lahm", "Miroslav Klose"])

style_input = st.selectbox("Select style of explanation", ["-Select Style-","Beginner-Friendly", "Technical", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["-Select Length-","Short (1-2 paragraphs)","Medium (3-5 paragraphs)", "Long (detailed explanation)" ])

template = load_prompt("template.json")

if st.button("Summarise"):
    if (
        player_input == "-Select Player-" or
        style_input == "-Select Style-" or
        length_input == "-Select Length-"
    ):
        st.warning("⚠️ Please select all options before summarising.")
    else:
        chain = template | model

        result = chain.invoke({
            'player_input': player_input,
            'style_input': style_input,
            'length_input': length_input
        })

        st.write(result.content)