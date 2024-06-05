from openai import OpenAI

client = OpenAI(
    api_key="sk-xpk3STT8JvFCH9jpJhe82DY4C5Jgfzb8zsClIywLl2kowBbT",
    base_url="https://api.moonshot.cn/v1",
)

completion = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[
        {"role": "system",
         "content": "你是我的个人助手"},
        {"role": "user", "content": "1+1等于多少？"}
    ],
    temperature=0.3,
)

print(completion.choices[0].message.content)