import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="점심 룰렛", layout="centered")

st.title("🍱 점심 메뉴 룰렛")

menu_data = {
    "한식": ["김치찌개", "된장찌개", "비빔밥", "불고기", "제제육볶음", "칼국수"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마파두부", "볶음밥"],
    "일식": ["초밥", "라멘", "우동", "돈카츠", "가츠동"],
    "양식": ["파스타", "스테이크", "피자", "햄버거", "리조또"],
    "분식": ["떡볶이", "순대", "김밥", "라면", "튀김"]
}

category = st.sidebar.selectbox("🍽️ 카테고리 선택", list(menu_data.keys()))
items = menu_data[category]

st.subheader(f"🎯 {category} 룰렛")

def render(items):
    import math

    n = len(items)
    angle = 360 / n

    colors = ["#ff9999","#66b3ff","#99ff99","#ffcc99","#c2c2f0","#ffb3e6"]

    # 룰렛 색상
    conic = ", ".join([
        f"{colors[i%len(colors)]} {i*angle}deg {(i+1)*angle}deg"
        for i in range(n)
    ])

    # 글씨 따로 배치 (핵심)
    labels = ""
    for i, item in enumerate(items):
        rot = i * angle + angle/2
        labels += f"""
        <div style="
            position:absolute;
            width:100%;
            height:100%;
            transform:rotate({rot}deg);
        ">
            <div style="
                position:absolute;
                left:50%;
                top:10px;
                transform:translateX(-50%);
                font-size:14px;
                font-weight:bold;
                white-space:nowrap;
            ">
                {item}
            </div>
        </div>
        """

    html = f"""
    <html>
    <body style="display:flex;flex-direction:column;align-items:center;">

        <div style="position:relative;">

            <!-- 화살표 -->
            <div style="
                position:absolute;
                top:-18px;
                left:50%;
                transform:translateX(-50%);
                width:0;height:0;
                border-left:12px solid transparent;
                border-right:12px solid transparent;
                border-bottom:20px solid red;
                z-index:10;
            "></div>

            <!-- 룰렛 -->
            <div id="wheel" style="
                width:340px;
                height:340px;
                border-radius:50%;
                background: conic-gradient({conic});
                border:5px solid black;
                position:relative;
                transition: transform 4s ease-out;
            ">
                {labels}
            </div>

        </div>

        <div style="margin-top:25px;">
            <button onclick="spin()" style="
                padding:10px 25px;
                font-size:16px;
                cursor:pointer;
            ">🎲 룰렛 돌리기</button>
        </div>

        <script>
            let wheel = document.getElementById("wheel");
            let current = 0;

            function spin() {{
                let deg = Math.floor(2000 + Math.random()*2000);
                current += deg;
                wheel.style.transform = "rotate(" + current + "deg)";
            }}
        </script>

    </body>
    </html>
    """

    components.html(html, height=650)

render(items)

st.markdown("---")
st.info("화살표 기준으로 멈춘 위치가 당첨입니다.")
