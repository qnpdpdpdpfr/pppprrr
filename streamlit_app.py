import streamlit as st
import pandas as pd
import chardet
import os

# ------------------------------------------------
# 파일 경로
# ------------------------------------------------
FILE = "/mount/src/pppprrr/STCS_우리나라기후평년값_DD_20251118211755.csv"

if not os.path.exists(FILE):
    st.error(f"CSV 파일이 존재하지 않습니다: {FILE}")
    st.stop()

# ------------------------------------------------
# 인코딩 자동 감지
# ------------------------------------------------
with open(FILE, "rb") as f:
    raw = f.read()
detected = chardet.detect(raw)
encoding = detected["encoding"] or "utf-8"
st.write(f"Detected Encoding: **{encoding}**")

# ------------------------------------------------
# CSV 읽기: 헤더 7번 줄, 데이터 8번 줄부터
# ------------------------------------------------
try:
    data = pd.read_csv(
        FILE,
        encoding=encoding,
        header=6,          # 7번째 줄을 컬럼명으로 사용
        engine="python",
        on_bad_lines="skip"
    )
except pd.errors.ParserError as e:
    st.error(f"CSV 파싱 오류 발생: {e}")
    st.stop()
except Exception as e:
    st.error(f"알 수 없는 오류 발생: {e}")
    st.stop()

# ------------------------------------------------
# Streamlit UI
# ------------------------------------------------
st.title("기후평년값 대시보드")
st.write(f"파일: {FILE}")
st.dataframe(data)
