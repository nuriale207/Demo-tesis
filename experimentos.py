import streamlit as st



def main():
    st.title("streamlit Forms & Submit Demo")

    my_form = st.form(key = "form1")
    name = my_form.text_input(label = "Enter the model name")
    number = my_form.slider("Enter your age", min_value=10, max_value = 100 )
    submit = my_form.form_submit_button(label = "Submit this form")
    if submit:
        st.markdown(
            f"""
                            * Select Name : {name}
                            * Select Number : {number}
                            """
        )

    col1, col2 = st.beta_columns(2)

    with col1:

        with st.form('Form2'):
            f1_selectflavor=st.selectbox('Select flavor', ['Vanilla', 'Chocolate'], key=1)
            f1_selectintensity=st.slider(label='Select intensity', min_value=0, max_value=100, key=4)
            submitted1 = st.form_submit_button('Submit 1')
            if submitted1:
                st.markdown(
                    f"""
                    * Select Flavor : {f1_selectflavor}
                    * Select Intensity : {f1_selectintensity}
                    """
                )


    with col2:
        with st.form('Form3'):
            f2_selecttopping=st.selectbox('Select Topping', ['Almonds', 'Sprinkles'], key=2)
            f2_selectintensity=st.slider(label='Select Intensity', min_value=0, max_value=100, key=3)
            submitted2 = st.form_submit_button('Submit 2')
            if submitted2:
                st.markdown(
                    f"""
                    * Select Toppings : {f2_selecttopping}
                    * Select Intensity : {f2_selectintensity}
                    """
                )

    st.text(number)

    st.markdown("Columns inside form")

    with st.form(key='columns_in_form'):
        cols = st.beta_columns(5)
        for i, col in enumerate(cols):
            col.selectbox(f'Make a Selection', ['click', 'or click'], key=i)
        submitted = st.form_submit_button('Submit')



if __name__ == '__main__':
    main()