import urllib.request

from flask import render_template, redirect, request, url_for

from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analysis/<path:url>')
def analyze_url(url):
    try:
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        req = urllib.request.Request(url, headers={'User-Agent': user_agent})   # some sites like foxnews.com require spoofing
        httpResponse = urllib.request.urlopen(req)
        # todo use httpResponse :-)
        return render_template("analysis.html", url=url)
    except Exception as e:
        return "error rendering URL: '" + url + "': " + str(e)


@app.route('/url_submit', methods=['GET'])
def do_url_submit():
    url = request.values.get('url_field_val', None)
    # todo urllib.parse.quote(url)?
    return redirect(url_for('analyze_url', url=url))
