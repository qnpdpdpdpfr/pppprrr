import streamlit as st
import pandas as pd
import chardet
import os

# ------------------------------------------------
# 1️⃣ 파일 경로 설정
# ------------------------------------------------
# 절대 경로 예시 (스트림릿 환경에서 안정적)
FILE = "/mount/src/pppprrr/STCS_우리나라기후평년값_DD_20251118211755.csv"

# 상대 경로 예시 (프로젝트 내에 CSV가 있는 경우)
# FILE = "./STCS_우리나라기후평년값_DD_20251118211755.csv"

# 파일 존재 여부 확인
if not os.path.exists(FILE):
    st.error(f"CSV 파일이 존재하지 않습니다: {FILE}")
    st.stop()

# ------------------------------------------------
# 2️⃣ 인코딩 자동 감지
# ------------------------------------------------
with open(FILE, "rb") as f:
    raw = f.read()
detected = chardet.detect(raw)
encoding = detected["encoding"] or "utf-8"
st.write(f"Detected Encoding: **{encoding}**")

# ------------------------------------------------
# 3️⃣ CSV 읽기 (파싱 안전하게)
# ------------------------------------------------
try:
    # engine="python" + on_bad_lines="skip"로 파싱 오류 방지
    data = pd.read_csv(FILE, encoding=encoding, engine="python", on_bad_lines="skip")
except pd.errors.ParserError as e:
    st.error(f"CSV 파싱 오류 발생: {e}")
    st.stop()
except Exception as e:
    st.error(f"알 수 없는 오류 발생: {e}")
    st.stop()

# ------------------------------------------------
# 4️⃣ Streamlit UI
# ------------------------------------------------
st.title("기후평년값 대시보드")
st.write(f"파일: {FILE}")
st.dataframe(data)
