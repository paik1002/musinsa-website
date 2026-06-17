from flask import Flask, render_template


app = Flask(__name__)



# 메인
@app.route("/")
def index():

    return render_template(
        "index.html"
    )



# 쇼핑 페이지
@app.route("/shop")
def shop():

    return render_template(
        "shop.html"
    )



# 장바구니
@app.route("/cart")
def cart():

    return render_template(
        "cart.html"
    )



# 브랜드 소개
@app.route("/about")
def about():

    return render_template(
        "about.html"
    )



# 이벤트
@app.route("/event")
def event():

    return render_template(
        "event.html"
    )





if __name__ == "__main__":

    app.run(
        debug=True
    )
