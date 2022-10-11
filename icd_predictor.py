import time

import pandas as pd
import streamlit as st
# For download buttons
from annotated_text import annotated_text

import functions

##PAGE SETTINGS
st.set_page_config(
    page_title="Future admissions analyzer ",
    page_icon="⚕️",
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
st.title("Future admissions analyzer")
st.header("")

with st.expander("ℹ️ - About this app", expanded=True):
#     st.write(
#         """
# -   El predictor de futuras enfermedades se basa en el estudio de miles de historiales de pacientes previos para sugerir enfermedades que el paciente tiene riesgo de sufrir
# -   Emplea un modelo de inteligencia artificial entrenado para dicho propósito utilizando evoluciones clínicas de miles de pacientes
#  """
#     )
    st.write(
            """     
    -   The predictor of future diseases is based on the study of thousands of previous patient histories to suggest diseases that the patient is at risk of suffering.    
    -  It employs an artificial intelligence model trained for this purpose using clinical evolutions of thousands of patients.
     """
        )


    st.markdown("")

st.markdown("")

# st.write("#### Ejemplos ####")

# option = st.selectbox("",
#     ('', 'Ejemplo 1', 'Ejemplo 2', "Ejemplo 3"))
option = st.selectbox("Examples",
    ('', 'Example 1'))

# placeholder_form = st.empty()
with st.form(key="form_1"):
    st.markdown("## Write document ##")

    ejemplo=""
    if str(option)== "Example 1":
        ejemplo= functions.get_ejemplo_1()
    else:
        ejemplo=option

    print(option)
    print(ejemplo)
    # doc = st.text_area(
    #     "Escribe el documento aquí (maximo 500 palabras)",
    #     height=510, value=ejemplo
    # )
    doc = st.text_area(
        "Write the document here",
        height=510, value=ejemplo
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

    submit_button = st.form_submit_button(label="⚙️ Analyze the document")

#
if not submit_button:
    st.stop()

# placeholder_form.empty()


# st.markdown("### Registro clínico ###")
st.markdown("### Marked document ###")
# annotated_text(
#     "El paciente presenta", ("fiebre", "", "#8ef"), "dolor abdominal e hinchazón en el abdomen. ",
#     "Posible cuadro de ", ("obstrucción intestinal", "", "#faa")
# )
functions.get_ejemplo_1_marked()
st.write("\n\n\n")

with st.expander("Predicted ICD codes", expanded=False):
    if str(option)== "Example 1":
        functions.get_ejemplo_1_marked_ICD()

    # annotated_text(
    #
    #     ("R50", "", "#8ef"), ":Fever of other and unknown origin"
    # )
    #
    # annotated_text(
    #
    #     ("K56", "", "#faa"), "Paralytic ileus and intestinal obstruction without hernia"
    # )


st.write("\n\n")
st.write("#### Inferred ICD timeline ####")

time.sleep(3)
plot=functions.timeline_chart(functions.get_ejemplo_1_cronology())

st.pyplot(plot)

st.write("#### Posible future diagnoses ####")

df_futuro=functions.get_ejemplo_1_future()
# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

st.table(df_futuro)

