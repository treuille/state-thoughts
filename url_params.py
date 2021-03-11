"""
# URL Params fix
"""

import streamlit as st


def example_with_callbacks():
    """
    URL Params with callbacks
    """
    # Fetch the initial state. This may be empty if the app is being used the first time
    # OR it may contain some state in the URL
    initial_app_state = st.experimental_get_query_params()
    app_state = {k: v[0] for k, v in initial_app_state.items()}

    if len(app_state.items()) > 0:
        if 'checkbox' in app_state.keys():
            if app_state['checkbox'] == 'True':
                app_state['checkbox'] = True
            else:
                app_state['checkbox'] = False

        # If the URL already contains some state then initialize session state with it
        state = st.beta_session_state(**app_state)
    else:
        # If the URL is empty, then initialize session state with some defaults
        state = st.beta_session_state(radio='Eat',
                                      checkbox=False,
                                      title='')
        st.experimental_set_query_params(**state.global_state)


    def update_checkbox_params(checkbox_value):
        state.checkbox = checkbox_value
        st.experimental_set_query_params(**state.global_state)


    def update_radio_params(radio):
        state.radio = radio
        st.experimental_set_query_params(**state.global_state)


    def update_title(title):
        state.title = title
        st.experimental_set_query_params(**state.global_state)

    st.checkbox("Are you really happy today?", key="checkbox1",
                value=state.checkbox, on_change=update_checkbox_params)

    radio_list = ['Eat', 'Sleep', 'Both']
    st.radio("What are you doing at home during quarantine?",
            radio_list,
            radio_list.index(state.radio),
            on_change=update_radio_params)

    st.text_input('Movie Title', value=state.title, on_change=update_title)



def example_with_signals():
    """
    URL Params with Signals
    """
    # Fetch the initial state. This may be empty if the app is being used the first time
    # OR it may contain some state in the URL
    initial_app_state = st.experimental_get_query_params()
    app_state = {k: v[0] for k, v in initial_app_state.items()}

    if len(app_state.items()) > 0:
        if 'checkbox' in app_state.keys():
            if app_state['checkbox'] == 'True':
                app_state['checkbox'] = True
            else:
                app_state['checkbox'] = False

        # If the URL already contains some state then initialize session state with it
        state = st.beta_session_state(**app_state)
    else:
        # If the URL is empty, then initialize session state with some defaults
        state = st.beta_session_state(radio='Eat',
                                      checkbox=False,
                                      title='')
        st.experimental_set_query_params(**state.global_state)

    # SIGNALS
    CHECKBOX = 'checkbox'
    RADIO = 'radio'
    TITLE = 'title'

    if st.signal(CHECKBOX):
        checkbox_value = st.signal_value()
        state.checkbox = checkbox_value
        st.experimental_set_query_params(**state.global_state)

    if st.signal(RADIO):
        radio = st.signal_value()
        state.radio = radio
        st.experimental_set_query_params(**state.global_state)

    if st.signal(TITLE):
        title = st.signal_value()
        state.title = title
        st.experimental_set_query_params(**state.global_state)

    st.checkbox("Are you really happy today?", key="checkbox1",
                           value=state.checkbox, signal=CHECKBOX)

    radio_list = ['Eat', 'Sleep', 'Both']
    st.radio("What are you doing at home during quarantine?",
                     radio_list,
                     radio_list.index(state.radio),
                     signal=RADIO)

    st.text_input('Movie Title', value=state.title, signal=TITLE)