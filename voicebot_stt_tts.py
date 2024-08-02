import streamlit as st
import openai
import os
from dotenv import load_dotenv

# .env 파일 경로 지정 
load_dotenv()

# Open AI API 키 설정하기
api_key = os.environ.get('open_api_key')

client = openai.OpenAI(api_key=api_key)

# 제목
st.set_page_config(page_title="음성 챗봇",layout="wide")

def main() :
    st.header("음성 챗봇 프로그램")

    # 구분선
    st.markdown("===")
    with st.expander("음성 챗봇 프로그램에 관하여", expanded=False):
        st.write (
            """
            - 음성 번역 챗봇 프로그램의 UI는 스트림릿을 활용합니다.
            - STT(Speech-To-Text)는 OpenAI의 Whisper를 활용합니다. 
            - 답변은 OpenAI의 GPT 모델을 활용합니다. 
            - TTS(Text-To-Speech)는 OpenAI의 TTS를 활용합니다.
            """
        )
        st.markdown ("")

#if __name__ == "__main__":
    #print(__name__)
# 실행 함수
    #main()

# 사이드바 생성
with st.sidebar :
    # GPT 모델을 선택하기 위한 라디오 버튼
    model = st.radio(label="GPT모델", options=["gpt-3.5-turbo", "gpt-4","gpt-4-turbo"])
    st.markdown("---")

    #리셋 버튼 생성
    if st.button(label="초기화"):
        #리셋 코드
        pass

if __name__== "__main__":
    main()