from flask import render_template, redirect, request, url_for

from analysis.HtmlAnalysis import HtmlAnalysis
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analysis/')
def need_url():
    return "No URL found. Please go back and enter one."


@app.route('/analysis/<path:url>')
def analyze_url(url):
    try:
        urlAnalysis = HtmlAnalysis(url)
        return render_template("analysis.html", urlAnalysis=urlAnalysis)
    except Exception as e:
        return "error rendering URL: '" + url + "': " + str(e)


@app.route('/url_submit', methods=['GET'])
def do_url_submit():
    url = request.values.get('url_field_val', None)
    # todo urllib.parse.quote(url)?
    return redirect(url_for('analyze_url', url=url))
