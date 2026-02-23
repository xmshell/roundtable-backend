from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # 允许跨域请求，这样小程序才能访问

# 定义5个不同视角的“智能体”
agents = [
    {"name": "技术极客", "perspective": "从技术实现角度分析"},
    {"name": "商业顾问", "perspective": "从商业模式和盈利角度分析"},
    {"name": "用户体验师", "perspective": "从最终用户感受角度分析"},
    {"name": "风险控制官", "perspective": "从潜在风险和挑战角度分析"},
    {"name": "创意策划", "perspective": "从创新和差异化角度分析"}
]

@app.route('/')
def hello():
    return "圆桌会议后端运行中！"

@app.route('/discuss', methods=['POST'])
def discuss():
    data = request.json
    user_question = data.get('question', '没有问题')
    
    discussion_result = []
    
    # 模拟每个智能体“思考”并回复
    for agent in agents:
        # 这里是模拟回复，后续我们可以接入真实的 API
        reply = f"基于{agent['perspective']}，关于「{user_question}」，我的看法是：\n这是一个非常有趣的方向。我们需要关注核心需求，同时保持灵活性。建议先进行小规模测试，验证可行性后再扩大范围。"
        
        discussion_result.append({
            "agent_name": agent["name"],
            "reply": reply
        })
        time.sleep(0.3) # 模拟讨论的延迟感
    
    return jsonify({
        "status": "success",
        "question": user_question,
        "discussion": discussion_result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
