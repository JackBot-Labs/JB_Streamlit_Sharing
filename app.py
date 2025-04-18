
import streamlit as st
import pandas as pd

st.title("📊 Jack's Streamlit 공유 예제")

uploaded_file = st.file_uploader("📂 엑셀 파일을 업로드하세요", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("✅ 업로드된 데이터:")
    st.dataframe(df)

    st.line_chart(df.select_dtypes(include='number'))

else:
    st.info("👆 엑셀 파일을 업로드하면 차트를 볼 수 있어요.")
