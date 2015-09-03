from flask import render_template, redirect, request, url_for

from analysis.HtmlAnalysis import HtmlAnalysis
from app import app


#
# templates
#

@app.route('/')
def index():
    return render_template('index.html')


# analysis starting point
@app.route('/analysis/<path:url>')
def url_analysis_start(url):
    try:
        html_analysis = HtmlAnalysis(url)
        return render_template("analysis.html", html_analysis=html_analysis)
    except Exception as e:
        return "error rendering URL: '" + url + "': " + str(e)


@app.route('/analysis/links_out/<path:url>')
def links_analysis_outgoing(url):
    try:
        html_analysis = HtmlAnalysis(url)
        return render_template("outgoing_links.html", html_analysis=html_analysis)
    except Exception as e:
        return "error rendering URL: '" + url + "': " + str(e)


@app.route('/analysis/')
def empty_analysis():
    return "No URL found. Please go back and enter one."


#
# forms
#

@app.route('/url_submit', methods=['GET'])
def do_url_submit():
    url = request.values.get('url_field_val', None)
    # todo urllib.parse.quote(url)?
    return redirect(url_for('url_analysis_start', url=url))
