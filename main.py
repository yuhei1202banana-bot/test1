import streamlit as st

# ページ設定
st.set_page_config(page_title="Aoki ren - 自己紹介", layout="wide")

# === 画像パス（相対パス） ===
img_singapore = "9EE65E4D-EB35-4FE8-88D0-A7E5DD4F8E95 (1).jpeg"
img_asakusa   = "462A7DD2-860C-4FD3-90CE-4C2D90F2CFAF.jpeg"
img_cappadocia = "A7C25E08-CB8F-4520-B7BC-6815D8155EBF.jpeg"


# === CSS ===
st.markdown("""
<style>
body {
    font-family: 'Helvetica', 'Arial', sans-serif;
}
header {
    background: #222;
    color: white;
    padding: 60px 20px;
    text-align: center;
    background-size: cover;
    background-position: center;
    border-radius: 10px;
}
.section {
    max-width: 900px;
    margin: 60px auto;
    padding: 0 20px;
}
.photo {
    width: 100%;
    border-radius: 14px;
    margin-top: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)


# === ヘッダー（背景に1枚目） ===
st.markdown(f"""
<header style="background-image: url('{img_singapore}')">
    <h1 style="font-size: 36px; text-shadow: 0 0 15px rgba(0,0,0,0.7);">
        Aoki ren
    </h1>
</header>
""", unsafe_allow_html=True)


# === セクション1 ===
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("一人旅が好きです")
st.write("""
知らない場所を歩くと、心が自由になる気がします!!  
この写真はシンガポールの Gardens by the Bay で撮ってもらった一枚。  
自分の世界を広げたいという気持ちで旅を続けています!!
""")
st.image(img_singapore, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)


# === セクション2 ===
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("人との出会いが好きです")
st.write("""
日本でも海外でも、いろんな国の人と出会ってきました。  
浅草を案内すると驚いた顔を見せてくれる人が多くて、  
「体験を共有するってすごく素敵だな」と感じました！  
観光地よりも、人と気持ちがつながる瞬間のほうが心に残ります。
""")
st.image(img_asakusa, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)


# === セクション3 ===
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("価値観が変わった瞬間")
st.write("""
トルコのカッパドキアで気球に乗った朝、  
隣の女性が景色に感動して涙を流していました。  
その姿を見て、ふと気づきました。  

**「体験をもらうだけじゃなく、自分も誰かに届けたい」**  

この経験をきっかけに、アプリ開発に興味を持ちました。  
まだ始めたばかりですが、いつか誰かの心を動かすサービスを作りたい。  
小さな一歩ですが、そんな気持ちで学び続けています。
""")
st.image(img_cappadocia, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)


# === 最後 ===
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.header("これからの目標")
st.write("""
旅で感じた “心が動く瞬間” を、今度は自分の手で作りたいと思っています。  
アプリ開発はまだ始めたばかりですが、  
誰かの毎日を少し明るくできるような体験を届けたい。  
そんな気持ちで挑戦を続けます。
""")
st.markdown("</div>", unsafe_allow_html=True)


# === フッター ===
st.markdown("""
<div style="text-align:center; margin-top:60px; color:#777;">
© 2025 Aoki ren
</div>
""", unsafe_allow_html=True)