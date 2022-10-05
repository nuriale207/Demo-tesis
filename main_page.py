import seaborn as sns
import streamlit as st
# For download buttons
from annotated_text import annotated_text

##PAGE SETTINGS
st.set_page_config(
    page_title="Predictor de futuros ICDs",
    page_icon="🎈",
    #layout="wide"
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



with st.form(key="form_1"):
    st.markdown("## **📌 Paste document **")

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

    submit_button = st.form_submit_button(label="✨ Predecir codigos ICD asociados")

    if submit_button:
        link = '[GitHub](http://github.com)'
        st.markdown(link, unsafe_allow_html=True)
#
if not submit_button:
    st.stop()
