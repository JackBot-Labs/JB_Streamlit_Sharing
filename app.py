import streamlit as st

# 비밀번호 하드코딩 (또는 st.secrets로 대체 가능)
CORRECT_PASSWORD = "3225"

st.title("🔐 Jack's Secure Dashboard")

# 비밀번호 입력 받기
password = st.text_input("비밀번호를 입력하세요:", type="password")

if password == CORRECT_PASSWORD:
    st.success("✅ 인증 성공! 대시보드를 시작합니다.")
    
    # 👉 여기 아래에 본문 대시보드 코드 작성
    st.write("📊 여기에 데이터/그래프/업로드 등 내용이 들어갑니다.")
    
else:
    if password:  # 입력은 했는데 틀렸을 경우
        st.error("❌ 비밀번호가 틀렸습니다.")
    else:
        st.info("🔐 비밀번호를 입력해야 대시보드를 볼 수 있습니다.")
