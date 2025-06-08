import streamlit as st
from gugugaga import GugaEncoder


@st.cache_resource(ttl="1h", max_entries=10)
def get_codec(charset: str, separator: str):
    return GugaEncoder(charset, separator)


if __name__ == "__main__":
    st.set_page_config(page_title="咕咕嘎嘎编码器", page_icon="./MyGO_icon.svg")
    st.title("灵感菇编码器")

    charset = st.text_input("请输入不重复的字符集：", value="咕嘎)
    separator = st.text_input("请输入分隔符：", value="~")
    codec = get_codec(charset, separator)

    func_type = st.sidebar.radio(
        "功能选择: ",
        ("编码", "解码"),
    )

    st.markdown("## 在输入框回车以查看输出")

    if func_type == "编码":
        raw_str = st.text_input(label="请输入需要编码的字符串", value="我喜欢你")
        st.markdown("## 编码结果：")
        st.text_area(
            label="output", label_visibility="hidden", value=codec.encode(raw_str)
        )
    else:
        raw_str = st.text_input("请输入需要解码的字符串", value="")
        st.markdown("## 解码结果：")
        st.text_area(
            label="output", label_visibility="hidden", value=codec.decode(raw_str)
        )
