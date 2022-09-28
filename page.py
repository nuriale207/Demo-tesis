import streamlit as st
import numpy as np
from pandas import DataFrame
# For Flair (Keybert)
import seaborn as sns
# For download buttons
import os
import json
from annotated_text import annotated_text



st.set_page_config(
    page_title="Predictor de futuros ICDs",
    page_icon="🎈",
    layout="wide"
)

def _max_width_():
    max_width_str = f"max-width: 1600px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


_max_width_()

c30, c31, c32 = st.columns([2.5, 1, 3])

with c30:
    # st.image("logo.png", width=400)
    st.title("Predictor de futuros ICDs")
    st.header("")

with st.expander("ℹ️ - About this app", expanded=True):
    st.write(
        """     
-   El predictor de futuras enfermedades se basa en el estudio de miles de historiales de pacientes previos para sugerir enfermedades que el paciente tiene riesgo de sufrir
-   Emplea un modelo de inteligencia artificial entrenado para dicho propósito utilizando evoluciones clínicas de miles de pacientes
 """
    )

    st.markdown("")

st.markdown("")
st.markdown("## **📌 Paste document **")
with st.form(key="my_form"):
    # ce, c1, ce, c2, c3 = st.columns([0.01, 1, 0.07, 5, 0.07])

    # with c1:
    #     StopWordsCheckbox = st.checkbox(
    #         "Remove stop words",
    #         help="Tick this box to remove stop words from the document (currently English only)",
    #     )

    # with c2:
    doc = st.text_area(
        "Escribe el documento aquí (maximo 500 palabras)",
        height=510,
    )

    MAX_WORDS = 500
    import re

    res = len(re.findall(r"\w+", doc))
    if res > MAX_WORDS:
        st.warning(
            "⚠️ Your text contains "
            + str(res)
            + " words."
            + " Only the first 500 words will be reviewed. Stay tuned as increased allowance is coming! 😊"
        )

        doc = doc[:MAX_WORDS]

    submit_button = st.form_submit_button(label="✨ Predecir posibles ICD y enfermedades futuras")

    # if use_MMR:
    #     mmr = True
    # else:
    #     mmr = False

    # if StopWordsCheckbox:
    #     StopWords = "english"
    # else:
    #     StopWords = None

if not submit_button:
    st.stop()
st.markdown("## Códigos ICD inferidos ##")
with st.container():
    annotated_text(
        "El paciente presenta", ("fiebre", "", "#8ef"), ("dolor abdominal", ""), "e", ("hinchazón en el abdomen", ""),
        "Posible cuadro de ", ("obstrucción intestinal", "", "#faa")
    )
    st.write("\n\n\n")


with st.container():
    annotated_text(

        ("R50", "", "#8ef"), ":Fever of other and unknown origin"
    )

    annotated_text(

        ("K56", "", "#faa"), "Paralytic ileus and intestinal obstruction without hernia"
    )

# keywords = kw_model.extract_keywords(
#     doc,
#     keyphrase_ngram_range=(min_Ngrams, max_Ngrams),
#     use_mmr=mmr,
#     stop_words=StopWords,
#     top_n=top_N,
#     diversity=Diversity,
# )
#
# st.markdown("## **🎈 Check & download results **")
#
# st.header("")
#
# cs, c1, c2, c3, cLast = st.columns([2, 1.5, 1.5, 1.5, 2])
#
# with c1:
#     CSVButton2 = st.download_button(keywords, "Data.csv", "📥 Download (.csv)")
# with c2:
#     CSVButton2 = download_button(keywords, "Data.txt", "📥 Download (.txt)")
# with c3:
#     CSVButton2 = download_button(keywords, "Data.json", "📥 Download (.json)")
#
# st.header("")

# df = (
#     DataFrame(keywords, columns=["Keyword/Keyphrase", "Relevancy"])
#         .sort_values(by="Relevancy", ascending=False)
#         .reset_index(drop=True)
# )
#
# df.index += 1

# Add styling
cmGreen = sns.light_palette("green", as_cmap=True)
cmRed = sns.light_palette("red", as_cmap=True)


c1, c2, c3 = st.columns([1, 3, 1])

format_dictionary = {
    "Relevancy": "{:.1%}",
}
