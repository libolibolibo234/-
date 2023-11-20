from flask import Flask, render_template
from disneyland import *


app = Flask(__name__)



# 首页路由
@app.route('/')
def index():
    return render_template('index.html')

# 详情页路由
@app.route('/dream')
def dream():
    return render_template('dream.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/garden')
def garden():
    return render_template('garden.html')

@app.route('/mickey')
def mickey():
    return render_template('mickey.html')

@app.route('/tomorrow')
def tomorrow():
    return render_template('tomorrow.html')

@app.route('/toyStory')
def toyStory():
    return render_template('toyStory.html')

# 任务：为treasure.html页面配置资源路径
@app.route('/treasure')
def treasure():
    return render_template('treasure.html')

app.run(port=5004)
