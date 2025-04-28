import streamlit as st
import pandas as pd
import numpy as np
import time

# ============================================
# ページ設定
# ============================================
st.set_page_config(page_title="Streamlit デモ", layout="wide")

# ============================================
# ヘッダー カード
# ============================================
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("🌟 Streamlit 初心者向けデモ")
        st.caption("コメントを解除しながら、直感的にStreamlitの機能を体験しましょう！")
    with col2:
        st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=150)

# ============================================
# サイドバー
# ============================================
st.sidebar.title("📝 デモガイド")
st.sidebar.info("""
このデモでは、**コメントアウトされたコード**を一つずつ解除しながら、
Streamlitの魅力を体験できます！
""")

# ➡️ 追加：サイドバーの簡易フィードバックフォーム
with st.sidebar.expander("📣 フィードバック"):
    feedback = st.text_input("お気に入り機能を教えて！")
    if st.button("送信する"):
        st.success(f"フィードバックを受け付けました：『{feedback}』")

# ============================================
# ライト・ダークテーマ切り替え（お試し版）
# ============================================
if 'theme' not in st.session_state:
    st.session_state.theme = 'ライト'
theme = st.radio("テーマ選択", ["ライト", "ダーク"], index=0 if st.session_state.theme == 'ライト' else 1, horizontal=True)
st.session_state.theme = theme

if theme == 'ダーク':
    st.markdown("""
    <style>
    body { background-color: #0E1117; color: white; }
    </style>
    """, unsafe_allow_html=True)

# ============================================
# UI要素 基本編
# ============================================
with st.expander("🛠️ 基本的なUI要素（テキスト入力・ボタンなど）", expanded=True):
    st.subheader("🔤 テキスト入力")
    name = st.text_input("あなたの名前は？", placeholder="ゲスト")
    st.success(f"こんにちは、{name}さん！")

    st.divider()

    st.subheader("🖱️ ボタン")
    if st.button("クリックしてみてください"):
        st.success("ボタンがクリックされました！🎉")

    st.divider()

    st.subheader("✅ チェックボックス")
    if st.checkbox("チェックを入れると...？"):
        st.info("🎁 隠しコンテンツを発見！")

    st.divider()

    st.subheader("🎚️ スライダー")
    age = st.slider("年齢を選んでください", 0, 100, 25)
    st.write(f"あなたの年齢: **{age}歳**")

    st.divider()

    st.subheader("🔽 セレクトボックス")
    language = st.selectbox("好きなプログラミング言語は？", ["Python", "JavaScript", "Java", "C++", "Go", "Rust"])
    st.write(f"あなたが選んだのは **{language}** です。")

# ============================================
# レイアウト編
# ============================================
with st.expander("📐 レイアウトと配置（カラム・タブなど）"):
    st.subheader("📑 カラムレイアウト")
    col1, col2 = st.columns(2)
    with col1:
        st.info("これは左側のカラムです")
    with col2:
        st.success("これは右側のカラムです")

    st.divider()

    st.subheader("🗂️ タブレイアウト")
    tab1, tab2 = st.tabs(["第1タブ", "第2タブ"])
    with tab1:
        st.write("👉 これは第1タブの内容です")
    with tab2:
        st.write("👉 これは第2タブの内容です")

# ============================================
# データ表示編
# ============================================
with st.expander("📊 データ表示（表・グラフ）"):
    st.subheader("🧮 データフレーム (編集可能)")
    df = pd.DataFrame({
        '名前': ['田中', '鈴木', '佐藤', '高橋', '伊藤'],
        '年齢': [25, 30, 22, 28, 33],
        '都市': ['東京', '大阪', '福岡', '札幌', '名古屋']
    })
    st.data_editor(df, use_container_width=True)

    st.divider()

    st.subheader("📈 ラインチャート")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
    st.line_chart(chart_data)

# ============================================
# インタラクティブ機能編
# ============================================
with st.expander("🎯 インタラクティブ機能（プログレスバー・アップロード）"):
    st.subheader("📈 プログレスバー")
    progress = st.progress(0)
    if st.button("進捗をスタート！"):
        for i in range(101):
            time.sleep(0.01)
            progress.progress(i)
        st.balloons()

    st.divider()

    st.subheader("📂 ファイルアップロード")
    uploaded_file = st.file_uploader("ファイルをアップロードしてください", type=["csv", "txt"])
    if uploaded_file is not None:
        st.success("ファイルがアップロードされました！")
        st.write(f"ファイル名: {uploaded_file.name}")
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)

# ============================================
# 使い方ガイド + 最後のアンケート
# ============================================
st.divider()
st.subheader("🧭 使い方ガイド")
st.markdown("""
1. コードのコメント（#で始まる行）を探してください
2. コメントを解除して保存
3. ブラウザでリロードして変化を確認！
""")
st.code("""
# 例：
# if st.button("クリックしてください"):
#     st.success("クリックされました！")

# コメント解除後
if st.button("クリックしてください"):
    st.success("クリックされました！")
""")

st.divider()

# ➡️ 追加：最後の小さなアンケート
st.subheader("📝 本日の体験はいかがでしたか？")
experience = st.radio(
    "満足度を教えてください",
    ["とても良かった", "まあまあ良かった", "普通", "あまり良くなかった"],
    horizontal=True
)
if st.button("結果を送信"):
    st.success(f"あなたの回答：{experience}　ありがとうございました！")
