import json
import streamlit as st
from streamlit_lottie import st_lottie
col1, col2 = st.columns(2)
with col1:

    st.markdown("""## Binary Search by Sudhanshu""")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)



with col1:
    lottie_now = load_lottiefile("file/code.json")
st_lottie(
    lottie_now,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    height=400,
    key=None,

)
st.success("Enter the element of list separated by spaces")
Sudhuu = [int(x) for x in st.text_input(
    " ").split()]
Sudhuu.sort()

st.success("Enter that element you want to search")
x = int(st.text_input(""))


low = 0
high = len(Sudhuu) - 1
while low <= high:
    mid = (low + high) // 2
    if Sudhuu[mid] == x:
        st.success("Element found at Possition")
        st.warning(mid+1)
        break
    elif Sudhuu[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
else:
    st.success("Element not found in the list")
