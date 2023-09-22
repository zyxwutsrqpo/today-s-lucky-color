import streamlit as st

def main():
    today = datetime.now()
    lucky_color = get_lucky_color(today)

    st.title("今日のラッキーカラー")

    # ボタンを作成
    button = st.button("今日のラッキーカラーを表示")

    # ボタンが押されたらラッキーカラーを表示
    if button:
        st.write("今日のラッキーカラーは、" + lucky_color + "です。")

if __name__ == "__main__":
    main()    
import pytz
from datetime import datetime

def get_lucky_color(today):
    today_jst = today.astimezone(pytz.timezone("Asia/Tokyo"))
    hour = today_jst.hour

    if 6 <= hour < 12:
        return "赤"
    elif 12 <= hour < 18:
        return "黄色"
    else:
        return "青"
    
import streamlit as st

def main():
    today = datetime.now()
    lucky_color = get_lucky_color(today)

    st.title("今日のラッキーカラー")
    st.write("今日のラッキーカラーは、" + lucky_color + "です。")

if __name__ == "__main__":
    main()
