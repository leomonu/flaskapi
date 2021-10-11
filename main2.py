from flask import Flask, jsonify, request
import csv

all_articles = []

with open('Articles.csv',encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []



app = Flask(__name__)

@app.route("/get-article")
def get_article():
    articles_data = {
        "title": all_articles[0][19],
        "poster_link": all_articles[0][27],
        "release_date": all_articles[0][13] or "N/A",
        "duration": all_articles[0][15],
        "rating": all_articles[0][20],
        "overview": all_articles[0][9]
    }
    return jsonify({
        "data": articles_data,
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/disliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201