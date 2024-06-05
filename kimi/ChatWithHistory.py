from openai import OpenAI  # 假设这是你的自定义库或兼容库

client = OpenAI(
    api_key="sk-xpk3STT8JvFCH9jpJhe82DY4C5Jgfzb8zsClIywLl2kowBbT",
    base_url="https://api.moonshot.cn/v1",
)

history = [
    {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，..."}
]


def chat(query, history):
    # 将用户查询添加到历史记录中  
    history.append({"role": "user", "content": query})

    # 调用API获取响应  
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=history,
        temperature=0.3,
    )

    # 提取响应内容  
    result = completion.choices[0].message.content

    # 将AI的响应添加到历史记录中（可选，取决于你是否需要保留完整的对话历史）  
    history.append({"role": "assistant", "content": result})

    return result


# 调用chat函数并打印结果
print(chat("地球的自转周期是多少？", history))
print(chat("月球呢？", history))
