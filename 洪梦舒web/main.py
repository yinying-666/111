# 导入网页框架Flask，用来做网站
from flask import Flask

# 创建网站实例
app = Flask(__name__)

# 网站首页路由：访问域名首页就会执行这里的代码
@app.route('/')
def index():
    # 返回一段HTML代码，就是浏览器打开看到的网页页面
    return '''
    <html>
        <head>
            <meta charset="utf-8">
            <title>结课作业Web项目</title>
            <style>
                body{text-align:center;margin-top:100px;font-family:微软雅黑;}
                h1{color:#2563eb;}
            </style>
        </head>
        <body>
            <h1>我的Railway结课作业网页</h1>
            <p>部署成功！此页面可公网访问</p>
        </body>
    </html>
    '''

# 本地运行用，Railway线上会用Procfile的命令启动，这行不影响部署
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
