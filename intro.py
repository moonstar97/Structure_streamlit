import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import time
from PIL import Image

st.set_page_config(
    page_title="9조 streamlit_page",
    page_icon="🖍",
    layout="wide",
) # 웹페이지 탭 디자인 설정

# 페이지 로드 진행 상황 바
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

st.title("내 거친 성적과 불안한 공교육💦")
st.subheader("MID PROJECT : 초중등 시험 폐지 이후 사교육 환경 변화와 원인 분석")
st.markdown("팀장 : 이정은")
st.markdown("팀원 : 문영운, 구자현, 안혜윤, 문종현")
st.markdown("----------------------------")

st.sidebar.write("9조 보고서 링크📌")
st.sidebar.markdown("[9조 보고서](https://www.notion.so/MiD-9f2b50c7238a4edca1fc07a2dc95f7a9)")

img = Image.open("data/title_png.png")
st.image(img, width=800, caption="내 거친 생각과아악")
st.markdown("# 사용 라이브러리")
with st.echo():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import plotly.express as px
    import plotly.graph_objects as go
    import streamlit as st
    import time
    from PIL import Image



st.markdown("---------------------")

st.markdown("# 프로젝트 배경과 개요")
st.markdown("### 1. 초등학교 시험 폐지")
st.markdown("* 2011년 서울을 시작으로 전면 폐지가 되었지만, 수많은 찬반 논란이 존재하고 있다.\n"
"그동안 학교에서는 어떤 변화가 있었고 그 원인은 무엇일까?\n"
"또, 지금에 와서 왜 다시 시험 부활 논의를 하고 있는가?")

st.markdown("\n")

st.markdown("### 2. 학업 성취도의 하락세")
st.markdown("* 학업성취도의 지속적인 하락세와 양극화 현상이 나타난다.\n"
"* \"PISA\" : 학업성취도 국제비교연구로 OECD 각국 교육정책 수립의 기초자료를 제공하기 위해 만 15세 학생을 대상으로 읽기(글 이해력), 수학, 과학 능력을 평가하는 프로그램\n"
"  * PISA test의 Reading, Math, Science 과목에서 순위가 떨어지고 있는 상황이다.\n")

st.markdown("### 3.사교육의 확대")
st.markdown("* 사교육 참여 인원은 점점 늘어나고 있지만 학업 성취도는 떨어지고 있는 문제상황에 대한 분석과 해결 방안을 제시")

st.markdown("-----------------------")

st.markdown("# 데이터 분석 내용")
st.markdown("* 코로나 파트 정리")
