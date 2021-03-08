import streamlit as st

def example_with_callbacks():
    """
    Callbacks using get_widget_state
    """
    s = st.beta_session_state(sum=0)
    st.write(s.sum)

    def mycallback(_):
        n1 = st.beta_widget_value("num1")
        n2 = st.beta_widget_value("num2")
        n1 = n1 if n1 is not None else 0
        n2 = n2 if n2 is not None else 0
        s.sum = n1 + n2



    st.number_input("Number 1", on_change=mycallback, key="num1")
    st.number_input("Number 2", on_change=mycallback, key="num2")
