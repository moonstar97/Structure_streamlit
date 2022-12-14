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
    page_title="9μ‘° streamlit_page",
    page_icon="π",
    layout="wide",
) # μΉνμ΄μ§ ν­ λμμΈ μ€μ 

# νμ΄μ§ λ‘λ μ§ν μν© λ°
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

st.title("λ΄ κ±°μΉ μ±μ κ³Ό λΆμν κ³΅κ΅μ‘π¦")
st.subheader("MID PROJECT : μ΄μ€λ± μν νμ§ μ΄ν μ¬κ΅μ‘ νκ²½ λ³νμ μμΈ λΆμ")
st.markdown("νμ₯ : μ΄μ μ")
st.markdown("νμ : λ¬Έμμ΄, κ΅¬μν, μνμ€, λ¬Έμ’ν")
st.markdown("----------------------------")

st.sidebar.write("9μ‘° λ³΄κ³ μ λ§ν¬π")
st.sidebar.markdown("[9μ‘° λ³΄κ³ μ](https://www.notion.so/MiD-9f2b50c7238a4edca1fc07a2dc95f7a9)")

img = Image.open("data/title_png.png")
st.image(img, width=800, caption="λ΄ κ±°μΉ μκ°κ³Όμμ")
st.markdown("# μ¬μ© λΌμ΄λΈλ¬λ¦¬")
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

st.markdown("# νλ‘μ νΈ λ°°κ²½κ³Ό κ°μ")
st.markdown("### 1. μ΄λ±νκ΅ μν νμ§")
st.markdown("* 2011λ μμΈμ μμμΌλ‘ μ λ©΄ νμ§κ° λμμ§λ§, μλ§μ μ°¬λ° λΌλμ΄ μ‘΄μ¬νκ³  μλ€.\n"
"κ·Έλμ νκ΅μμλ μ΄λ€ λ³νκ° μμκ³  κ·Έ μμΈμ λ¬΄μμΌκΉ?\n"
"λ, μ§κΈμ μμ μ λ€μ μν λΆν λΌμλ₯Ό νκ³  μλκ°?")

st.markdown("\n")

st.markdown("### 2. νμ μ±μ·¨λμ νλ½μΈ")
st.markdown("* νμμ±μ·¨λμ μ§μμ μΈ νλ½μΈμ μκ·Ήν νμμ΄ λνλλ€.\n"
"* \"PISA\" : νμμ±μ·¨λ κ΅­μ λΉκ΅μ°κ΅¬λ‘ OECD κ°κ΅­ κ΅μ‘μ μ± μλ¦½μ κΈ°μ΄μλ£λ₯Ό μ κ³΅νκΈ° μν΄ λ§ 15μΈ νμμ λμμΌλ‘ μ½κΈ°(κΈ μ΄ν΄λ ₯), μν, κ³Όν λ₯λ ₯μ νκ°νλ νλ‘κ·Έλ¨\n"
"  * PISA testμ Reading, Math, Science κ³Όλͺ©μμ μμκ° λ¨μ΄μ§κ³  μλ μν©μ΄λ€.\n")

st.markdown("### 3.μ¬κ΅μ‘μ νλ")
st.markdown("* μ¬κ΅μ‘ μ°Έμ¬ μΈμμ μ μ  λμ΄λκ³  μμ§λ§ νμ μ±μ·¨λλ λ¨μ΄μ§κ³  μλ λ¬Έμ μν©μ λν λΆμκ³Ό ν΄κ²° λ°©μμ μ μ")

st.markdown("-----------------------")

st.markdown("# λ°μ΄ν° λΆμ λ΄μ©")
st.markdown("* μ½λ‘λ ννΈ μ λ¦¬")
