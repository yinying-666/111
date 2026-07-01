from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 学生信息接口固定地址
API_URL = "https://ehall.qtc.edu.cn/xsf/sys/jbxwapp/sys/emappagelog/config/getStuBaseInfo.do"

# 首页跳转登录页面
@app.route('/')
def login_page():
    return render_template("login.html")

# 提交表单查询校园接口
@app.route('/query', methods=["POST"])
def query_info():
    # 获取页面输入的CAS凭证（你复制的MOD_AUTH_CAS那段）
    cas_str = request.form.get("cas_token")
    headers = {
        "Cookie": cas_str,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        res = requests.get(API_URL, headers=headers, timeout=10)
        return f"""
        <h2>✅ API调用成功，你的学生信息</h2>
        <pre style="white-space:pre-wrap;">{res.text}</pre>
        <a href="/">返回登录页</a>
        """
    except Exception as err:
        return f"""
        <h2>❌ 查询失败</h2>
        <p>原因：{err}</p>
        <p>1.必须连接校园WiFi；2.密钥已过期需重新复制</p>
        <a href="/">返回重新输入</a>
        """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
