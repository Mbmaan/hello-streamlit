import streamlit as st
st.title("My Streamlit Application")
st.write("Welcome to my Streamlit application!")
st.text("This is a simple text content.")
st.markdown("## This is a Markdown Header")
st.latex(r''' a^2 + b^2 = c^2 ''')
st.title("Additional Content")
st.header("This is a Header")
st.subheader("This is a Subheader")
st.code("for i in range(10): print(i)")


import pandas as pd

# Create a sample DataFrame
data = {
    'Column 1': [1, 2, 3],
    'Column 2': ['A', 'B', 'C']
}
df = pd.DataFrame(data)

# Display the DataFrame
st.write("Here is a sample DataFrame:")
st.dataframe(df)



