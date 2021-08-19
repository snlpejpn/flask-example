from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__, static_folder='../view', template_folder='../view/templates')

@app.route("/test")
def test():
    return "test success"