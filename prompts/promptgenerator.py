from langchain_core.prompts import PromptTemplate

# Template
template = PromptTemplate(
    template="""
please research on the player named {player_input} with the following specifications:
Explanation Style : {style_input}
Explanation Length : {length_input}

Explain all the achievements and their statistics, ratings, best game and their best performance in club-level and international competitions.
""",
input_variables = ['player_input', 'style_input', 'length_input'],
validate_template = True
)

template.save('template.json')
