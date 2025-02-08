import streamlit as st

st.markdown('please fill details first to access the site.')
name = st.text_input('ENTER YOUR NAME : ')
education = st.selectbox('enter your eduction :',(12, 'graduation', 'post graduation'))
button = st.button("submit")
if button:
    st.markdown(f"""
                    Name : {name}
                    education : {education}""")


    st.title(' YOUR WELCOME ')
    st.header('SOLIDWORKS')
    st.subheader('MY DESIGNS')
    st.markdown('So, here are some of my selfmade cad software designs i.e solidworks. Please take a look to these designs.'
                'I have use solidworks of version ver109080.'
                'By using python as computer language I have designed this website to representing my projects and I am con-'
                '-ntinously working on it so I want your apologize for any conviences.')
    st.code(""" pip install streamlit
                import streamlit
                import pandas
                """)
