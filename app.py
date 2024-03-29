from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/movie")
def movie():
    datalist = []
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template("movie.html", movies=datalist)


@app.route("/score")
def score():
    score = [] # 评分
    count = [] # 每个评分对应的电影数量
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    sql = '''
            SELECT score, count(id)
            FROM movie250
            GROUP BY score
          '''
    data = cur.execute(sql)
    for item in data:
        score.append(str(item[0]))
        count.append(item[1])
    cur.close()
    conn.close()
    return render_template("score.html", score=score, count=count)


@app.route("/cloud")
def cloud():
    return render_template("cloud.html")


@app.route("/team")
def team():
    return render_template("team.html")


if __name__ == "__main__":
    app.run(debug=True)
