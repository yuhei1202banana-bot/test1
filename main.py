import streamlit as st

# HTML をそのまま埋め込む
html_code = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vietnam Souvenir Shop</title>

    <style>
        body {
            margin: 0;
            font-family: "Helvetica", sans-serif;
            background: #fff8e6;
            color: #333;
        }

        header {
            background: #d35400;
            padding: 18px;
            color: #fff;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 1px;
        }

        .hero {
            width: 100%;
            height: 280px;
            background-image: url('vietnam-shop.jpg');
            background-size: cover;
            background-position: center;
        }

        .section {
            padding: 30px 20px;
            max-width: 900px;
            margin: auto;
        }

        .title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 12px;
            color: #d35400;
        }

        .products {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .product {
            background: #fff;
            border-radius: 12px;
            padding: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            text-align: center;
        }

        .product img {
            width: 100%;
            height: 130px;
            object-fit: cover;
            border-radius: 8px;
        }

        .product-name {
            margin-top: 10px;
            font-weight: bold;
        }

        .product-price {
            color: #d35400;
            margin-top: 5px;
        }

        footer {
            background: #d35400;
            color: #fff;
            padding: 18px;
            text-align: center;
            margin-top: 40px;
        }
    </style>
</head>

<body>

<header>
    Vietnam Souvenir Shop
</header>

<div class="hero"></div>

<div class="section">
    <div class="title">人気のお土産</div>

    <div class="products">
        <div class="product">
            <img src="coffee.jpg" alt="Vietnam Coffee">
            <div class="product-name">ベトナムコーヒー</div>
            <div class="product-price">150,000 VND</div>
        </div>

        <div class="product">
            <img src="ao-dai.jpg" alt="Ao Dai">
            <div class="product-name">アオザイ ミニチュア</div>
            <div class="product-price">200,000 VND</div>
        </div>

        <div class="product">
            <img src="bag.jpg" alt="Handmade Bag">
            <div class="product-name">ハンドメイドバッグ</div>
            <div class="product-price">180,000 VND</div>
        </div>

        <div class="product">
            <img src="lantern.jpg" alt="Hoi An Lantern">
            <div class="product-name">ホイアン ランタン</div>
            <div class="product-price">250,000 VND</div>
        </div>
    </div>
</div>

<div class="section">
    <div class="title">店舗情報</div>
    <p>
        住所：Hanoi Old Quarter, Vietnam<br>
        営業時間：9:00〜21:00<br>
        電話：012-3456-789
    </p>
</div>

<footer>
    © 2025 Vietnam Souvenir Shop
</footer>

</body>
</html>
"""

# Streamlit に表示
st.components.v1.html(html_code, height=2000, scrolling=True)