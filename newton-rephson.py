import streamlit as st

st.set_page_config(page_title="뉴턴-랩슨법", page_icon="🧮")
st.title("🧮 뉴턴-랩슨법으로 \n√2의 근삿값 구하기")

x = st.number_input("양수를 입력하시오", value = None)

if st.button("계산하기"):
    cnt = 0
    if x <= 0:
        st.error("양수를 입력하시오")
    else:
        while True:
            cnt = cnt + 1
            x = 1/2 * (x + 2/x)
            if abs(x ** 2 - 2) < 0.00001:
                break
    
        st.info(f'총 실행 횟수는 {cnt}번이며, 최종 근삿값은 {x}입니다.')
