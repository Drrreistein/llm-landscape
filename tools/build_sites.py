#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按自动驾驶图谱首页的实现方式，为多个行业生成同款单文件交互式站点。"""
import os, re, html, json, shutil

BASE = '/Users/a1-6/WorkBuddy/2026-10-21-16-35-12'
TPL = os.path.join(BASE, 'auto-driving-map', 'index.html')
OUT = os.path.join(BASE, 'sites')

# 复用原站的 CSS
src = open(TPL, encoding='utf-8').read()
CSS = re.search(r'<style>(.*?)</style>', src, re.S).group(1)

# ---------- 数据格式：名称|环节codes|技术codes|场景codes|报告或-|玩家模式 ----------
RAW = {}

RAW['embodied'] = """
绿的谐波|u1|WH,WR|工业制造|-|part
双环传动|u1|WH,WR|工业制造|-|part
中大力德|u1|WH,WR|工业制造|-|part
哈默纳科|u1|WH|工业制造|-|part
贝斯特|u2|WH|工业制造|-|part
恒立液压|u2|WH|工业制造|-|part
五洲新春|u2|WH|工业制造|-|part
秦川机床|u2|WH|工业制造|-|part
舍弗勒|u2|WH|工业制造|-|part
鸣志电器|u3|WH,QU|工业制造,科研教育|-|part
伟创电气|u3|WH|工业制造|-|part
步科股份|u3|WH|工业制造|-|part
江苏雷利|u3|WH|工业制造|-|part
鼎智科技|u3|WH|工业制造|-|part
柯力传感|u4|WH,WA|工业制造,仓储物流|-|part
东华测试|u4|WH|工业制造|-|part
坤维科技|u4|WH,WA|工业制造|-|part
宇立仪器|u4|WH|工业制造|-|part
蓝点触控|u4|WH,WA|工业制造|-|part
奥比中光|u5|WH,HW,WA|工业制造,商用服务,科研教育|-|part
图漾科技|u5|WH,WA|工业制造,仓储物流|-|part
舜宇光学|u5|WH|工业制造|-|part
韦尔股份|u5|WH|工业制造|-|part
梅卡曼德机器人|u5,m9|WA,SP|工业制造,仓储物流|梅卡曼德机器人-首次覆盖报告|part
兆威机电|u6|WH|工业制造|-|part
因时机器人|u6|WH|工业制造|-|part
傲意科技|u6|WH|医疗健康|-|part
灵心巧手|u6|WH|科研教育|-|part
英伟达|u7,s1|WH,HW,WA,QU,SP|科研教育,工业制造|-|part
地平线机器人|u7|WH,HW|工业制造,科研教育|地平线机器人-首次覆盖报告|part
瑞芯微|u7|WH,SP|商用服务,家庭|-|part
全志科技|u7|SP|家庭|-|part
华为昇腾|u7,s1|WH,HW|工业制造,科研教育|-|part
寒武纪|u7|WH|科研教育|-|part
黑芝麻智能|u7|HW|工业制造|-|part
宁德时代|u8|WH|工业制造|-|part
亿纬锂能|u8|WH|工业制造|-|part
旭升集团|u8|WH|工业制造|-|part
爱柯迪|u8|WH|工业制造|-|part
长光华芯|u9|WH|工业制造|-|part
源杰科技|u9|WH|工业制造|-|part
世运电路|u9|WH|工业制造|世运电路-首次覆盖报告|part
智元机器人|m1,d5|WH,HW|工业制造,仓储物流,文娱商演|-|oem
宇树科技|m1,m3,d4,d5|WH,QU|科研教育,文娱商演,特种作业|-|oem
优必选|m1,d1|WH|工业制造,商用服务|-|oem
乐聚机器人|m1,d4|WH|科研教育,文娱商演|-|oem
星动纪元|m1,d2|WH|仓储物流,工业制造|-|oem
傅利叶智能|m1,d8|WH|医疗健康,科研教育|-|oem
开普勒机器人|m1|WH|工业制造|-|oem
众擎机器人|m1,d5|WH|文娱商演|-|oem
加速进化|m1,d4|WH|科研教育|-|oem
小鹏 IRON|m1|WH|工业制造|-|oem
小米 CyberOne|m1|WH|家庭,科研教育|-|oem
Tesla Optimus|m1|WH|工业制造,家庭|-|oem
Figure AI|m1,d1|WH|工业制造,仓储物流|-|oem
Agility Robotics|m1,d2|WH|仓储物流|-|oem
1X|m1,d6|WH|家庭|-|oem
NEURA Robotics|m1|WH|工业制造|-|oem
Boston Dynamics|m1,m3|WH,QU|特种作业,工业制造|-|oem
Apptronik|m1,d1|WH|工业制造|-|oem
银河通用|m2,d3|WA|商用服务,工业制造|-|oem
星海图|m2|WA|工业制造,科研教育|-|oem
自变量机器人|m2|WA|商用服务|-|oem
逐际动力|m2|WH,QU|科研教育|-|oem
松灵机器人|m2|WA|科研教育|-|oem
云深处|m3,d7|QU|特种作业,科研教育|-|oem
亿嘉和|m3,d7|QU|特种作业|-|oem
申昊科技|m3,d7|QU|特种作业|-|oem
中信重工开诚|m3,d7|QU,SP|特种作业,矿区港口|-|oem
ANYbotics|m3,d7|QU|特种作业|-|oem
节卡机器人|m9,d1|SP|工业制造|-|oem
遨博智能|m9,d1|SP|工业制造|-|oem
极智嘉|m9,d2|SP|仓储物流|-|oem
快仓智能|m9,d2|SP|仓储物流|-|oem
Physical Intelligence|m4|WH,HW,WA|工业制造,科研教育|-|model
Skild AI|m4|WH,HW|工业制造|-|model
NVIDIA GR00T|m4,s1|WH|科研教育,工业制造|-|model
Google DeepMind|m4|WH,HW|科研教育|-|model
上海 AI Lab|m4|WH|科研教育|-|model
NVIDIA Isaac|m5,s1|WH,HW,WA,QU|科研教育,工业制造|-|model
光轮智能|m5|WH,HW|科研教育,工业制造|-|model
群核科技|m5|WH,HW|科研教育|-|model
51WORLD|m5|WH,SP|科研教育,特种作业|-|model
海天瑞声|m5|WH,HW|科研教育|海天瑞声-首次覆盖报告|model
数据堂|m5|WH|科研教育|-|model
中科创达|m6|WH,HW,SP|工业制造,商用服务|中科创达-首次覆盖报告|model
东土科技|m6|WH|工业制造|-|model
顺丰科技|d2|WA,SP|仓储物流|-|ops
中国邮政|d2|WA,SP|仓储物流|-|ops
京东物流|d2|WA,SP|仓储物流|-|ops
九识智能|d2|SP|仓储物流|-|ops
新石器|d2|SP|仓储物流|-|ops
擎朗智能|d3|WA,SP|商用服务|-|ops
普渡科技|d3|WA|商用服务|-|ops
云迹科技|d3|WA|商用服务|-|ops
猎户星空|d3|WA|商用服务|-|ops
比亚迪|d1|WH,SP|工业制造|-|ops
富士康|d1|WH,SP|工业制造|-|ops
宁德时代产线|d1|WA|工业制造|-|ops
科沃斯|d6|SP|家庭|-|ops
追觅科技|d6|WH|家庭|-|ops
易控智驾|d9|SP|矿区港口|-|ops
希迪智驾|d9|SP|矿区港口|-|ops
西井科技|d9|SP|矿区港口|-|ops
阿里云|s1|WH,HW,WA,QU,SP|科研教育,工业制造|阿里巴巴-首次覆盖报告|infra
华为云|s1|WH,HW|工业制造,科研教育|-|infra
腾讯云|s1|WH,HW|科研教育|-|infra
火山引擎|s1|WH,HW|科研教育|-|infra
中国电子技术标准化研究院|s2|WH,HW|工业制造,科研教育|-|infra
赛西实验室|s2|WH,HW|工业制造|-|infra
TÜV 莱茵|s2|WH,HW|工业制造|-|infra
北京人形机器人创新中心|s3|WH,HW|科研教育,工业制造|-|infra
上海国地中心|s3|WH|科研教育|-|infra
广东具身智能创新中心|s3|WH,HW|工业制造|-|infra
"""

RAW['llm'] = """
英伟达|u1|FT,OW,MM|大模型训练,大模型推理|-|part
AMD|u1|FT,OW|大模型推理,大模型训练|-|part
博通|u1,u4|FT,OW|大模型训练,大模型推理|-|part
Google TPU|u1|FT,MM|大模型训练,大模型推理|-|part
AWS Trainium|u1|FT,OW|大模型训练,大模型推理|-|part
华为昇腾|u1|FT,OW|大模型训练,大模型推理|-|part
寒武纪|u1|FT,OW|大模型推理|-|part
海光信息|u1|FT,OW|大模型推理|-|part
沐曦|u1|FT,OW|大模型推理|-|part
壁仞科技|u1|FT|大模型训练|-|part
摩尔线程|u1|FT,OW|大模型训练|-|part
燧原科技|u1|OW|大模型推理|-|part
天数智芯|u1|FT,OW|大模型训练|-|part
景嘉微|u1|SM|端侧推理|-|part
Groq|u1|OW,MM|大模型推理|-|part
Cerebras|u1|FT|大模型训练|-|part
SK 海力士|u2|FT,OW,MM|大模型训练,大模型推理|-|part
三星电子|u2|FT,OW,MM|大模型训练,大模型推理|-|part
美光|u2|FT,OW|大模型训练|-|part
长鑫存储|u2|OW|大模型推理|-|part
台积电|u3|FT,OW,MM|大模型训练,大模型推理|-|part
中芯国际|u3|SM,OW|端侧推理|-|part
长电科技|u3|FT,OW|大模型训练|-|part
通富微电|u3|FT|大模型训练|-|part
中际旭创|u4|FT,OW|大模型训练,大模型推理|-|part
新易盛|u4|FT,OW|大模型训练,大模型推理|-|part
天孚通信|u4|FT,OW|大模型训练|-|part
Coherent|u4|FT|大模型训练|-|part
Lumentum|u4|FT|大模型训练|-|part
源杰科技|u4|FT,OW|大模型训练|-|part
光迅科技|u4|OW|大模型推理|-|part
戴尔|u5|FT,OW|大模型训练,大模型推理|-|part
超微电脑|u5|FT,OW|大模型训练|-|part
鸿海|u5|FT,OW|大模型训练|-|part
浪潮信息|u5|FT,OW|大模型训练,大模型推理|-|part
中科曙光|u5|FT,OW|大模型训练|-|part
联想|u5|OW|大模型推理|-|part
工业富联|u5|FT|大模型训练|-|part
英维克|u6|FT,OW|大模型训练,大模型推理|-|part
Vertiv|u6|FT,OW|大模型训练|-|part
施耐德电气|u6|FT,OW|大模型训练|-|part
伊顿|u6|FT|大模型训练|-|part
阳光电源|u6|FT,OW|大模型训练|-|part
华为数字能源|u6|FT,OW|大模型训练|-|part
海天瑞声|u7|FT,OW,MM|大模型训练|海天瑞声-首次覆盖报告|part
Scale AI|u7|FT,MM|大模型训练|-|part
Appen|u7|FT,OW|大模型训练|-|part
数据堂|u7|OW|大模型训练|-|part
OpenAI|m1|FT,MM|消费级应用,编程,科研与垂直|-|model
Anthropic|m1|FT,MM|编程,企业软件,科研与垂直|-|model
Google DeepMind|m1|FT,MM|消费级应用,科研与垂直|-|model
xAI|m1|FT,MM|消费级应用|-|model
Mistral AI|m1|FT,OW|企业软件,编程|-|model
Cohere|m1|FT|企业软件,知识库|-|model
AI21 Labs|m1|FT|企业软件|-|model
Meta Llama|m2|OW,SM|消费级应用,科研与垂直|-|model
DeepSeek|m2|OW,MM|编程,科研与垂直,消费级应用|-|model
阿里通义|m2|OW,SM,MM|企业软件,消费级应用|阿里巴巴-首次覆盖报告|model
月之暗面 Kimi|m2|OW,MM|消费级应用,编程|-|model
智谱 GLM|m2|OW,SM|企业软件,编程|-|model
MiniMax|m2|OW,MM|消费级应用,内容营销|-|model
腾讯混元|m2|OW,MM|企业软件,内容营销|-|model
小米 MiMo|m2|OW,SM|端侧推理,消费级应用|-|model
阶跃星辰|m2|OW,MM|消费级应用|-|model
百川智能|m2|OW|医疗健康,企业软件|-|model
零一万物|m2|OW,SM|企业软件|-|model
Harvey|m3|VT|科研与垂直|-|model
Hippocratic AI|m3|VT|医疗健康|-|model
BloombergGPT|m3|VT|科研与垂直|-|model
蚂蚁百灵|m3|VT,SM|金融,端侧推理|-|model
vLLM|m4|OW,MM|大模型推理,企业软件|-|tool
SGLang|m4|OW,MM|大模型推理,编程|-|tool
TensorRT-LLM|m4|FT,OW|大模型推理|-|tool
LMDeploy|m4|OW,SM|大模型推理,端侧推理|-|tool
Ollama|m4|SM,OW|端侧推理|-|tool
llama.cpp|m4|SM|端侧推理|-|tool
Triton|m5|FT,OW|大模型训练,大模型推理|-|tool
Apache TVM|m5|SM,OW|端侧推理|-|tool
XLA|m5|FT|大模型训练|-|tool
CANN|m5|FT,OW|大模型训练,大模型推理|-|tool
MXMACA|m5|OW|大模型推理|-|tool
ROCm|m5|FT,OW|大模型训练|-|tool
无问芯穹|m5,d1|FT,OW|大模型训练,大模型推理|-|tool
HAMi|m5|FT,OW|大模型训练,大模型推理|-|tool
OpenRouter|m6|FT,OW,MM|大模型推理|-|tool
Together AI|m6|OW,MM|大模型推理,大模型训练|-|tool
Fireworks AI|m6|OW,MM|大模型推理|-|tool
Pinecone|m6|VT|知识库|-|tool
Weaviate|m6|VT|知识库|-|tool
LangChain|m6|VT,MM|Agent 与工作流,知识库|-|tool
LlamaIndex|m6|VT|知识库|-|tool
LangGraph|m7|MM,VT|Agent 与工作流|-|tool
AutoGen|m7|MM|Agent 与工作流|-|tool
CrewAI|m7|MM|Agent 与工作流|-|tool
Dify|m7|VT,MM|Agent 与工作流,企业软件|-|tool
扣子 Coze|m7|VT,MM|Agent 与工作流,消费级应用|-|tool
Cursor|d1|FT,MM|编程|-|app
GitHub Copilot|d1|FT,MM|编程|-|app
Claude Code|d1|FT,MM|编程|-|app
通义灵码|d1|OW,VT|编程|-|app
CodeBuddy|d1|FT,OW|编程|-|app
Sierra|d2|FT,VT|客服与工单|-|app
Decagon|d2|FT|客服与工单|-|app
Intercom|d2|FT|客服与工单|-|app
智齿科技|d2|OW,VT|客服与工单|-|app
Glean|d3|FT,VT|知识库,企业软件|-|app
Notion AI|d3|FT|知识库,内容营销|-|app
Microsoft 365 Copilot|d7|FT|企业软件|-|app
Salesforce Agentforce|d7|FT,MM|企业软件,Agent 与工作流|-|app
ServiceNow|d7|FT|企业软件|-|app
钉钉 AI|d7|OW,VT|企业软件,Agent 与工作流|-|app
用友|d7|VT|企业软件|-|app
金蝶|d7|VT|企业软件|-|app
Jasper|d5|FT|内容营销|-|app
Copy.ai|d5|FT|内容营销|-|app
Midjourney|d5|MM|内容营销|-|app
可灵|d5|MM|内容营销|-|app
ChatGPT|d6|FT,MM|消费级应用,编程,内容营销|-|app
Claude|d6|FT,MM|消费级应用,编程|-|app
Gemini|d6|FT,MM|消费级应用|-|app
豆包|d6|OW,MM|消费级应用|-|app
腾讯元宝|d6|OW,MM|消费级应用|-|app
Perplexity|d6|FT,MM|消费级应用,科研与垂直|-|app
Character.AI|d6|VT|消费级应用|-|app
Elicit|d8|FT,VT|科研与垂直|-|app
Consensus|d8|FT|科研与垂直|-|app
Hugging Face|s1|OW,SM,MM|科研与垂直,大模型训练|-|infra
GitHub|s1|OW|编程|-|infra
AWS|s2|FT,OW,MM|大模型训练,大模型推理,公有云算力|-|infra
Microsoft Azure|s2|FT,MM|大模型训练,大模型推理|-|infra
Google Cloud|s2|FT,MM|大模型训练,大模型推理|-|infra
阿里云|s2|OW,MM|大模型训练,大模型推理|阿里巴巴-首次覆盖报告|infra
腾讯云|s2|OW,MM|大模型推理|-|infra
火山引擎|s2|OW,MM|大模型推理,公有云算力|-|infra
紫光股份|s2|FT,OW|公有云算力|紫光股份-三季报更新与评级|infra
中科创达|s2|SM,VT|端侧推理|中科创达-首次覆盖报告|infra
中国信通院|s3|FT,OW,MM|科研与垂直|-|infra
WAICO|s3|FT,OW|科研与垂直|-|infra
"""

RAW['infra'] = """
台积电|u1|TR,IN,FT|大模型训练,大模型推理|-|part
中芯国际|u1|ED,IN|端侧推理|-|part
长电科技|u2|TR,IN|大模型训练,大模型推理|-|part
通富微电|u2|TR,IN|大模型训练|-|part
SK 海力士|u3|TR,IN,MM|大模型训练,大模型推理|-|part
三星电子|u3|TR,IN|大模型训练,大模型推理|-|part
美光|u3|TR,IN|大模型训练|-|part
长鑫存储|u3|IN|大模型推理|-|part
兆易创新|u4|IN,ED|端侧推理,工业视觉|兆易创新-首次覆盖报告|part
江波龙|u4|IN,ED|端侧推理|-|part
佰维存储|u4|IN|大模型推理|-|part
Solidigm|u4|IN|大模型推理|-|part
源杰科技|u5|TR,IN|大模型训练,大模型推理|-|part
长光华芯|u5|TR,IN|大模型训练|-|part
Lumentum|u5|TR|大模型训练|-|part
Coherent|u5|TR,IN|大模型训练|-|part
世运电路|u6|TR,IN|大模型训练,大模型推理|世运电路-首次覆盖报告|part
沪电股份|u6|TR,IN|大模型训练|-|part
生益科技|u6|TR,IN|大模型训练|-|part
胜宏科技|u6|TR,IN|大模型训练|-|part
立讯精密|u6|TR,IN|大模型训练|-|part
安费诺|u6|TR,IN|大模型训练|-|part
英维克|u7|TR,IN|大模型训练,大模型推理|-|part
Vertiv|u7|TR,IN|大模型训练,大模型推理|-|part
施耐德电气|u7|TR,IN|大模型训练|-|part
伊顿|u7|TR|大模型训练|-|part
阳光电源|u7|TR,IN|大模型训练|-|part
华为数字能源|u7|TR,IN|大模型训练,大模型推理|-|part
金盘科技|u7|TR|大模型训练|-|part
英伟达|m1|TR,IN,FT,SI,ED|大模型训练,大模型推理,科研计算,自动驾驶训练|-|part
AMD|m1|TR,IN|大模型训练,大模型推理|-|part
博通|m1,m3|TR,IN|大模型训练,大模型推理|-|part
Marvell|m1,m3|TR,IN|大模型训练|-|part
Google TPU|m1|TR,IN|大模型训练,大模型推理|-|part
AWS Trainium|m1|TR,IN|大模型训练|-|part
华为昇腾|m1|TR,IN,FT|大模型训练,大模型推理|-|part
寒武纪|m1|TR,IN|大模型推理|-|part
海光信息|m1|TR,IN|大模型推理|-|part
沐曦|m1|TR,IN|大模型推理|-|part
壁仞科技|m1|TR|大模型训练|-|part
摩尔线程|m1|TR,IN|大模型训练|-|part
燧原科技|m1|IN|大模型推理|-|part
天数智芯|m1|TR,IN|大模型训练|-|part
景嘉微|m1|ED|端侧推理|-|part
Groq|m1|IN|大模型推理|-|part
Cerebras|m1|TR|大模型训练|-|part
地平线机器人|m1|ED,IN|端侧推理,自动驾驶训练|地平线机器人-首次覆盖报告|part
中际旭创|m2|TR,IN|大模型训练,大模型推理|-|part
新易盛|m2|TR,IN|大模型训练,大模型推理|-|part
天孚通信|m2|TR,IN|大模型训练|-|part
光迅科技|m2|IN|大模型推理|-|part
华工科技|m2|TR,IN|大模型训练|-|part
Arista|m3|TR,IN|大模型训练,大模型推理|-|part
思科|m3|TR,IN|大模型训练|-|part
锐捷网络|m3|TR,IN|大模型训练|-|part
紫光股份|m3,d2|TR,IN|公有云算力,大模型训练|紫光股份-三季报更新与评级|part
戴尔|m4|TR,IN|大模型训练,大模型推理|-|part
超微电脑|m4|TR,IN|大模型训练|-|part
鸿海|m4|TR,IN|大模型训练|-|part
浪潮信息|m4|TR,IN|大模型训练,大模型推理|-|part
中科曙光|m4,d1|TR,IN,SI|大模型训练,科研计算|-|part
联想|m4|IN|大模型推理|-|part
工业富联|m4|TR,IN|大模型训练|-|part
华为|m4,m8,d1|TR,IN,FT|大模型训练,大模型推理,公有云算力|-|part
中兴通讯|m4,m8,d1|TR,IN|大模型训练,大模型推理|-|part
曙光 scaleX|m5,d1|TR,SI|大模型训练,科研计算|-|part
英维克冷板|m5|TR,IN|大模型训练,大模型推理|-|part
申菱环境|m5|TR,IN|大模型训练|-|part
高澜股份|m5|TR,IN|大模型训练|-|part
vLLM|m6|IN,MM|大模型推理|-|soft
SGLang|m6|IN,MM|大模型推理|-|soft
TensorRT-LLM|m6|IN|大模型推理|-|soft
LMDeploy|m6|IN,ED|大模型推理,端侧推理|-|soft
Ollama|m6|ED|端侧推理|-|soft
Triton|m6|TR,IN|大模型训练,大模型推理|-|soft
Apache TVM|m6|ED,IN|端侧推理|-|soft
XLA|m6|TR|大模型训练|-|soft
CANN|m6|TR,IN|大模型训练,大模型推理|-|soft
MXMACA|m6|IN|大模型推理|-|soft
ROCm|m6|TR,IN|大模型训练|-|soft
无问芯穹|m7,d1|TR,IN|大模型训练,大模型推理,企业私有化|-|soft
HAMi|m7|TR,IN|大模型训练,大模型推理|-|soft
Kubeflow|m7|TR,IN|大模型训练|-|soft
Ray|m7|TR,IN|大模型训练|-|soft
Slurm|m7|TR,SI|大模型训练,科研计算|-|soft
Volcano|m7|TR|大模型训练|-|soft
中国联通|m7,d1|TR,IN|大模型训练,公有云算力|-|soft
中国移动|m7,d1|TR,IN|大模型训练,公有云算力|-|soft
中国电信|m7,d1|TR,IN|大模型训练,公有云算力|-|soft
中科创达|m6|ED,IN|端侧推理,工业视觉|中科创达-首次覆盖报告|soft
NVIDIA GB200 NVL72|m8|TR,IN|大模型训练,大模型推理|-|soft
华为 Atlas 950|m8,d1|TR,IN|大模型训练,大模型推理|-|soft
中兴超节点|m8,d1|TR,IN|大模型训练|-|soft
天数 IXL144|m8|TR,IN|大模型训练|-|soft
登峰 8000|m8,d1|TR,SI|大模型训练,科研计算|-|soft
阿里云|d2|TR,IN,FT|大模型训练,大模型推理,公有云算力|阿里巴巴-首次覆盖报告|svc
腾讯云|d2|TR,IN|大模型推理,公有云算力|-|svc
华为云|d2|TR,IN|大模型训练,公有云算力|-|svc
火山引擎|d2|IN,TR|大模型推理,公有云算力|-|svc
AWS|d2|TR,IN|大模型训练,大模型推理|-|svc
Microsoft Azure|d2|TR,IN|大模型训练,大模型推理|-|svc
Google Cloud|d2|TR,IN|大模型训练,大模型推理|-|svc
CoreWeave|d2|TR,IN|大模型训练,公有云算力|-|svc
Oracle Cloud|d2|TR,IN|大模型训练|-|svc
海天瑞声|d3|FT,MM|大模型训练,具身智能训练|海天瑞声-首次覆盖报告|svc
OpenAI|d3|TR,FT|大模型训练|-|svc
Anthropic|d3|TR,FT|大模型训练|-|svc
DeepSeek|d3|TR,FT|大模型训练|-|svc
月之暗面|d3|TR,FT|大模型训练|-|svc
字节跳动|d4|IN,TR|大模型推理,大模型训练|-|svc
百度|d4|IN,TR|大模型推理|-|svc
腾讯|d4|IN,TR|大模型推理|-|svc
阿里巴巴|d4|IN,TR|大模型推理,公有云算力|阿里巴巴-首次覆盖报告|svc
特斯拉|d3|TR,FT|自动驾驶训练|-|svc
比亚迪|d3|TR|自动驾驶训练|-|svc
小鹏汽车|d3|TR|自动驾驶训练|-|svc
智元机器人|d3|TR,FT|具身智能训练|-|svc
宇树科技|d3|TR,FT|具身智能训练|-|svc
银河通用|d3|TR,FT|具身智能训练|-|svc
宁德时代|d5|ED,IN|工业视觉|-|svc
国家电网|s1|TR,IN|大模型训练,大模型推理|-|svc
南方电网|s1|TR,IN|大模型训练|-|svc
三峡能源|s1|TR|大模型训练|-|svc
阳光电源|s1|TR,IN|大模型训练|-|svc
中国建筑|s2|TR,IN|大模型训练|-|svc
数据港|s2|TR,IN|大模型训练,大模型推理|-|svc
润泽科技|s2|TR,IN|大模型训练|-|svc
奥飞数据|s2|TR,IN|大模型推理|-|svc
光环新网|s2|TR,IN|大模型推理|-|svc
中国信通院|s3|TR,IN,SI|科研计算,大模型训练|-|svc
中国电子技术标准化研究院|s3|TR,IN|科研计算|-|svc
Uptime Institute|s3|TR,IN|科研计算|-|svc
"""

# ---------- 各行业配置 ----------
SITES = {
'embodied': {
  'slug':'embodied-ai-landscape','title':'具身智能产业研究','en':'Embodied AI Research',
  'brand':'具身智能产业研究','doc':'具身智能行业观察笔记','docfile':'具身智能行业观察笔记.html',
  'tagline':'一份个人整理的行业笔记',
  'intro':'从丝杠谐波到人形整机，把这条产业链拆成 @@SEGN@@ 个环节、@@TOTAL@@ 家企业。<b>供应链图谱含全链条</b>；<b>本体形态</b>、<b>应用场景</b>、<b>玩家模式</b>三个视图只收录整机、模型软件与场景运营方。点击带绿点的公司名，直达调研报告。',
  'seg':'23','tech':'5','scene':'8',
  'tabs':['供应链图谱','按本体形态','按应用场景','按玩家模式'],
  'scope2':'口径：仅含<b>整机厂商、具身模型与软件、场景运营方</b>。上游减速器、丝杠、电机、传感器等零部件与支撑层不参与此视图——同一颗谐波减速器会同时装进人形、轮式和四足本体，按形态归类会失真。一家企业可横跨多列，取决于其产品线覆盖。',
  'scope3':'口径：仅含<b>整机厂商、具身模型与软件、场景运营方</b>。零部件企业不按场景归类——同一家电机厂会同时服务工业、物流与家庭。一家企业可覆盖多个场景，标记数字即为其跨环节数量。',
  'scope4':'口径：行是<b>玩家模式</b>（卖什么、担什么责），列是<b>本体形态</b>。同一家企业可在同一行内横跨多列。<b>形态拆五列，拆的不是等级、是物理载体</b>：双足赌通用场景，轮式与专用机赌成本效率，两者客户与账期完全不同。零部件与供应商不参与模式矩阵，理由见页脚。',
  'note4':'<b>两个值得注意的空格</b>：零部件供应商 × 家庭场景基本为空（家庭对价格与可靠性最苛刻，零件厂不直接面对终端）；场景运营方 × 人形双足仍稀薄（真正在工厂常态化跑的，目前多为轮式或专用机）。',
  'about':'企业按“主营业环节”归类，横跨多个环节的公司（如宇树、英伟达、华为）会在多处出现，用“多环节”标记。本体形态按“该企业主力产品载体”标注；应用场景按“已落地的场景”标注，同样可跨多个场景。<b>“按本体形态”“按应用场景”“按玩家模式”三个视图只收录整机、模型软件与场景运营方</b>——上游零部件与支撑层不参与，因为它们一套产品同时服务全部形态与场景。归类为编辑判断，非官方口径。',
  'layers':[('01','上游','减速器 · 丝杠 · 电机 · 传感器 · 灵巧手 · 芯片'),('02','中游','整机 · 本体 · 具身大模型 · 仿真数据'),('03','下游','工业 · 物流 · 商用 · 家庭 · 特种')],
  'supportdesc':'云算力 · 测试认证 · 创新中心',
  'SEG':{
   'u1':['上游','谐波 / RV 减速器'],'u2':['上游','行星滚柱丝杠'],'u3':['上游','电机与执行器'],
   'u4':['上游','力 / 触觉传感器'],'u5':['上游','3D 视觉与惯导'],'u6':['上游','灵巧手'],
   'u7':['上游','端侧 AI 芯片'],'u8':['上游','电池与轻量化'],'u9':['上游','光芯片 / PCB'],
   'm1':['中游','人形整机'],'m2':['中游','轮式双臂本体'],'m3':['中游','四足与特种本体'],
   'm4':['中游','具身大模型'],'m5':['中游','仿真 · 数据 · 工具链'],
   'm6':['中游','控制器与 OS'],'m9':['中游','专用 / 协作机器人'],
   'd1':['下游','工业制造'],'d2':['下游','仓储物流'],'d3':['下游','商用服务'],
   'd4':['下游','科研教育'],'d5':['下游','文娱商演'],'d6':['下游','家庭'],
   'd7':['下游','特种作业'],'d8':['下游','医疗健康'],'d9':['下游','矿区港口'],
   's1':['支撑层','云与训练算力'],'s2':['支撑层','测试认证与标准'],'s3':['支撑层','场景开放与创新中心']
  },
  'SUPPORT':['s1','s2','s3'],
  'APP_SEGS':['m1','m2','m3','m4','m5','m6','m9','d1','d2','d3','d4','d5','d6','d7','d8','d9'],
  'TECH':[['WH','人形双足','赌通用场景 · 最难'],['HW','人形轮式','上半身人形 · 稳定优先'],['WA','轮式双臂','不为像人 · 为干活'],['QU','四足','巡检安防 · 商业化较早'],['SP','专用机器人','分拣搬运 · 已在赚钱']],
  'TSHORT':{'WH':'人形双足','HW':'人形轮式','WA':'轮式双臂','QU':'四足','SP':'专用'},
  'SCENE':[['工业制造','真需求，但还在验证期'],['仓储物流','目前最像真生意'],['商用服务','酒店零售，任务清晰'],['科研教育','当前最大出货去向'],['文娱商演','有现金流，天花板低'],['家庭','泛化与安全未到位'],['特种作业','巡检安防，四足先行'],['医疗健康','高价值但小众']],
  'MODES':[['oem','整机厂商','卖本体 · 担交付责任','#1b4a75'],['part','零部件供应商','卖零件 · 不面对终端','#8a6416'],['model','模型与软件','卖智能 · 按授权或项目','#5f6b7a'],['ops','场景运营方','卖结果 · 按工时或运力','#a8271f'],['infra','基础设施与支撑','卖算力 · 认证与场景','#2f6f5e']],
  'BLANKS':[],
},
'llm': {
  'slug':'llm-landscape','title':'大语言模型产业研究','en':'LLM Research',
  'brand':'大语言模型产业研究','doc':'大语言模型行业观察笔记','docfile':'大语言模型行业观察笔记.html',
  'tagline':'一份个人整理的行业笔记',
  'intro':'从 HBM 到 Agent 应用，把这条产业链拆成 @@SEGN@@ 个环节、@@TOTAL@@ 家企业。<b>供应链图谱含全链条</b>；<b>模型层级</b>、<b>应用场景</b>、<b>玩家模式</b>三个视图只收录模型、工具与应用厂商。点击带绿点的公司名，直达调研报告。',
  'seg':'23','tech':'5','scene':'8',
  'tabs':['供应链图谱','按模型层级','按应用场景','按玩家模式'],
  'scope2':'口径：仅含<b>基础模型、推理框架与中间层、应用厂商</b>。上游芯片、HBM、光模块、服务器与云基础设施不参与此视图——同一张 GPU 既跑训练也跑推理，按模型层级归类会失真。一家企业可横跨多列，取决于其产品线覆盖。',
  'scope3':'口径：仅含<b>基础模型、推理框架与中间层、应用厂商</b>。算力与硬件企业不按场景归类——同一颗芯片同时服务编程、客服与科研。一家企业可覆盖多个场景，标记数字即为其跨环节数量。',
  'scope4':'口径：行是<b>玩家模式</b>（卖什么、怎么收费），列是<b>模型层级</b>。<b>拆五列不是按参数量，是按商业形态</b>：前沿闭源卖 API 与订阅，开源权重卖生态与私有化，垂直专用卖结果，端侧小模型卖设备，推理/多模态卖能力溢价。硬件与基础设施不参与模式矩阵，理由见页脚。',
  'note4':'<b>两个值得注意的空格</b>：模型厂商 × 端侧小模型基本由开源阵营占据（闭源前沿厂商很少单独做端侧）；应用厂商 × 前沿闭源高度密集，说明应用层目前仍高度依赖少数几家 API，切换成本与议价权都不在自己手里。',
  'about':'企业按“主营业环节”归类，横跨多个环节的公司（如英伟达、阿里、华为）会在多处出现，用“多环节”标记。模型层级按“该企业主力产品形态”标注；应用场景按“已落地的场景”标注，同样可跨多个场景。<b>“按模型层级”“按应用场景”“按玩家模式”三个视图只收录模型、工具与应用厂商</b>——上游算力与基础设施不参与，因为它们一套硬件同时服务全部模型与场景。归类为编辑判断，非官方口径。',
  'layers':[('01','上游','芯片 · HBM · 光互联 · 服务器 · 电力冷却 · 数据'),('02','中游','基础模型 · 推理引擎 · 编译算子 · 中间层 · Agent'),('03','下游','编程 · 客服 · 知识库 · 内容 · 企业软件 · 消费级')],
  'supportdesc':'开源社区 · 云与数据中心 · 评测合规',
  'SEG':{
   'u1':['上游','AI 芯片 / 加速器'],'u2':['上游','HBM 与 DRAM'],'u3':['上游','晶圆代工与封装'],
   'u4':['上游','光模块与光芯片'],'u5':['上游','服务器与整机'],'u6':['上游','电力与冷却'],
   'u7':['上游','训练数据与标注'],
   'm1':['中游','前沿闭源模型'],'m2':['中游','开源权重模型'],'m3':['中游','垂直 / 端侧模型'],
   'm4':['中游','推理引擎'],'m5':['中游','编译与算子库'],'m6':['中游','中间层与工具'],
   'm7':['中游','Agent 框架'],
   'd1':['下游','编程'],'d2':['下游','客服与工单'],'d3':['下游','知识库与 RAG'],
   'd4':['下游','Agent 与工作流'],'d5':['下游','内容与营销'],'d6':['下游','消费级应用'],
   'd7':['下游','企业软件'],'d8':['下游','科研与垂直行业'],
   's1':['支撑层','开源社区与生态'],'s2':['支撑层','云与数据中心'],'s3':['支撑层','评测与合规']
  },
  'SUPPORT':['s1','s2','s3'],
  'APP_SEGS':['m1','m2','m3','m4','m5','m6','m7','d1','d2','d3','d4','d5','d6','d7','d8'],
  'TECH':[['FT','前沿闭源','卖 API 与订阅 · 最贵'],['OW','开源权重','卖生态与私有化'],['VT','垂直专用','卖结果 · 按任务收费'],['SM','端侧小模型','卖设备 · 低功耗'],['MM','推理 / 多模态','卖能力溢价']],
  'TSHORT':{'FT':'前沿闭源','OW':'开源权重','VT':'垂直专用','SM':'端侧小模型','MM':'推理/多模态'},
  'SCENE':[['编程','第一个跑通的场景'],['企业软件','续约率是验证点'],['知识库','项目多，难量化'],['Agent 与工作流','演示多，可靠性待解'],['内容营销','便宜，效果难归因'],['消费级应用','用户多，ARPU 低'],['科研与垂直','高价值但小众'],['客服与工单','ROI 好算，已规模化']],
  'MODES':[['model','基础模型厂商','卖 token / 订阅','#1b4a75'],['tool','工具与中间层','卖框架 / 服务','#8a6416'],['app','应用厂商','卖席位 / 结果','#a8271f'],['infra','云与算力','卖卡时 / 算力','#5f6b7a'],['part','算力与硬件','卖芯片 / 设备','#2f6f5e']],
  'BLANKS':[],
},
'infra': {
  'slug':'ai-infrastructure-landscape','title':'AI 基础设施产业研究','en':'AI Infra Research',
  'brand':'AI 基础设施产业研究','doc':'AI 基础设施行业观察笔记','docfile':'AI基础设施行业观察笔记.html',
  'tagline':'一份个人整理的行业笔记',
  'intro':'从晶圆封装到液冷供电，把这条产业链拆成 @@SEGN@@ 个环节、@@TOTAL@@ 家企业。<b>供应链图谱含全链条</b>；<b>负载类型</b>、<b>应用场景</b>、<b>玩家模式</b>三个视图覆盖芯片器件、整机集群、软件调度与基础设施服务。点击带绿点的公司名，直达调研报告。',
  'seg':'24','tech':'5','scene':'8',
  'tabs':['供应链图谱','按负载类型','按应用场景','按玩家模式'],
  'scope2':'口径：按<b>算力负载</b>而非按产品规格归类。同一台服务器既能训练也能推理，一家企业可横跨多列，取决于其产品实际服务的负载。列里的数字是有该负载相关产品的企业数，不代表收入结构。',
  'scope3':'口径：按<b>最终算力用途</b>归类。上游器件与中游硬件也会出现在场景中，因为同一批 GPU 和光模块会流向训练、推理、科研等不同用途——这与自动驾驶图谱不同：那里技术等级由整车定义，这里的负载由任务定义，硬件必须参与才看得清全貌。',
  'scope4':'口径：行是<b>玩家模式</b>（卖什么），列是<b>负载类型</b>。<b>拆五列不是等级，是任务</b>：训练看互联与峰值算力，推理看内存带宽与每瓦 token，端侧看功耗，科研看双精度与稳定性。同一家企业的不同产品线会落在不同列。',
  'note4':'<b>两个值得注意的空格</b>：软件与调度 × 边缘推理相对稀薄（端侧多由芯片厂自带工具链闭环）；基础设施服务 × 仿真与科学计算主要靠国家队与超算中心，商业云厂商参与有限。',
  'about':'企业按“主营业环节”归类，横跨多个环节的公司（如英伟达、华为、阿里）会在多处出现，用“多环节”标记。负载类型按“该企业产品实际服务的算力任务”标注；应用场景按“最终算力用途”标注。<b>与自动驾驶图谱的口径差异</b>：那里零部件不进技术等级视图，因为 L2/L4 由整车责任定义；这里硬件必须进负载与场景视图，因为训练/推理的差别恰恰落在芯片、HBM、光模块与液冷上。归类为编辑判断，非官方口径。',
  'layers':[('01','上游','晶圆 · 封装 · HBM · 存储 · 光芯片 · PCB · 电力'),('02','中游','AI 芯片 · 光模块 · 交换 · 服务器 · 液冷 · 框架调度 · 超节点'),('03','下游','智算集群 · 云算力 · 训练 · 推理 · 行业应用')],
  'supportdesc':'电网与绿电 · 数据中心建设 · 标准测试',
  'SEG':{
   'u1':['上游','晶圆代工'],'u2':['上游','先进封装 CoWoS'],'u3':['上游','HBM 与 DRAM'],
   'u4':['上游','企业级存储 / SSD'],'u5':['上游','光芯片与器件'],'u6':['上游','PCB 与铜连接'],
   'u7':['上游','电力与散热设备'],
   'm1':['中游','AI 芯片 GPU / ASIC'],'m2':['中游','光模块'],'m3':['中游','交换芯片与网络'],
   'm4':['中游','服务器整机'],'m5':['中游','液冷系统'],'m6':['中游','推理框架与编译'],
   'm7':['中游','集群调度'],'m8':['中游','超节点整机'],
   'd1':['下游','智算集群'],'d2':['下游','云与算力租赁'],'d3':['下游','模型训练'],
   'd4':['下游','模型推理'],'d5':['下游','行业 AI 应用'],
   's1':['支撑层','电网与绿电'],'s2':['支撑层','数据中心建设'],'s3':['支撑层','标准与测试']
  },
  'SUPPORT':['s1','s2','s3'],
  'APP_SEGS':['m1','m2','m3','m4','m5','m6','m7','m8','d1','d2','d3','d4','d5'],
  'TECH':[['TR','训练','看互联与峰值算力'],['IN','推理','看每瓦 token 产出'],['FT','微调 / 后训练','中等规模，迭代快'],['SI','仿真与科学计算','双精度与稳定性'],['ED','边缘推理','功耗与成本优先']],
  'TSHORT':{'TR':'训练','IN':'推理','FT':'微调','SI':'仿真/HPC','ED':'边缘推理'},
  'SCENE':[['大模型训练','万卡集群，资本密集'],['大模型推理','已占算力支出 55%–70%'],['公有云算力','按卡时出租'],['企业私有化','信创与数据合规驱动'],['科研计算','超算与国家队主导'],['自动驾驶训练','车企与方案商自建'],['具身智能训练','仿真 + 真机数据'],['工业视觉','端侧与边缘推理']],
  'MODES':[['part','芯片与器件厂','卖硅 · 毛利最高','#1b4a75'],['soft','软件与调度','卖利用率 · 开源为主','#8a6416'],['svc','基础设施服务','卖算力与电','#a8271f'],['infra','整机与集群','卖机柜与交付','#5f6b7a']],
  'BLANKS':[],
}
}

# ---------- 生成 ----------
def parse(raw):
    rows=[]
    for line in raw.strip().split('\n'):
        line=line.strip()
        if not line or line.startswith('#'): continue
        p=line.split('|')
        assert len(p)==6, f'bad row: {line}'
        name,segs,tech,scene,rep,mode=p
        rows.append([name, [x for x in segs.split(',') if x], [x for x in tech.split(',') if x],
                     [x for x in scene.split(',') if x], None if rep=='-' else rep, mode])
    return rows

def jsval(x):
    return json.dumps(x, ensure_ascii=False)

# 少数原始数据里的笔误/跨行业代码，映射到本行业已定义的维度
TECH_FIX = {
  'embodied': {'WR':'HW'},
  'llm': {},
  'infra': {'MM':'IN'},
}
SCENE_FIX = {
  'embodied': {'矿区港口':'特种作业'},
  'llm': {'大模型训练':'科研与垂直','大模型推理':'企业软件','公有云算力':'企业软件',
          '端侧推理':'消费级应用','金融':'科研与垂直','医疗健康':'科研与垂直'},
  'infra': {'端侧推理':'工业视觉'},
}

def normalize(C, key):
    tf, sf = TECH_FIX[key], SCENE_FIX[key]
    for c in C:
        t = [tf.get(x,x) for x in c[2]]
        c[2] = list(dict.fromkeys(t))          # 去重且保序
        s = [sf.get(x,x) for x in c[3]]
        c[3] = list(dict.fromkeys(s))
    return C

HTML_SKEL = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>@@TITLE@@</title>
<style>@@CSS@@</style>
</head>
<body>

<header class="top">
  <div class="top-in">
    <div class="brand"><span class="mark"></span>@@BRAND@@<small>@@EN@@</small></div>
    <label class="search">
      <svg width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="7" cy="7" r="4.5"/><path d="M10.5 10.5L14 14"/></svg>
      <input id="q" type="search" placeholder="搜索企业 / 环节…" autocomplete="off">
    </label>
    <a class="top-link" href="#about">关于</a>
  </div>
</header>

<div class="hero">
  <h1>@@TITLE@@</h1>
  <div class="docs">
    <a class="doc-link" href="reports/@@DOCFILE@@">
      <span class="dl-t">@@DOC@@</span>
      <span class="dl-s">@@TAGLINE@@</span>
      <span class="dl-a">阅读 ↗</span>
    </a>
  </div>
  <p>@@INTRO@@</p>
  <div class="stats">
    <div><b id="s1">0</b>覆盖企业</div>
    <div><b id="s2">0<i> 家</i></b>已出调研报告</div>
    <div><b>@@SEGCOUNT@@</b>产业链环节</div>
    <div><b>@@TECHCOUNT@@</b>@@TAB2@@</div>
    <div><b>@@SCENECOUNT@@</b>@@TAB3@@</div>
  </div>
</div>

<div class="tabs">
  <button class="tab on" data-v="chain">@@TAB1@@</button>
  <button class="tab" data-v="tech">@@TAB2@@</button>
  <button class="tab" data-v="scene">@@TAB3@@</button>
  <button class="tab" data-v="mode">@@TAB4@@</button>
  <div class="legend">
    <span><i class="dot"></i>有调研报告</span>
    <span><i class="dot g"></i>暂无报告</span>
  </div>
</div>

<main class="wrap">

  <section class="view on" id="v-chain">
    <div class="chain">
@@LAYERS@@
    </div>
    <div class="support">
      <div class="support-h"><span class="n">04</span><span class="t">支撑层</span><span class="d">@@SUPPORTDESC@@</span></div>
      <div class="support-grid" id="sup"></div>
    </div>
  </section>

  <section class="view" id="v-tech">
    <p class="scope">@@SCOPE2@@</p>
    <div class="grid5" id="techGrid"></div>
  </section>

  <section class="view" id="v-scene">
    <p class="scope">@@SCOPE3@@</p>
    <div class="grid4" id="sceneGrid"></div>
  </section>

  <section class="view" id="v-mode">
    <p class="scope">@@SCOPE4@@</p>
    <div class="matrix" id="modeGrid"></div>
    <p class="scope" style="margin-top:14px;border-left-color:#E24B4A;">@@NOTE4@@</p>
  </section>

  <div class="empty" id="empty">没有匹配的企业，换个关键词试试。</div>
</main>

<footer class="foot" id="about">
  <hr class="rule">
  <p><b>关于这张图。</b>@@ABOUT@@</p>
  <p><b>数据与免责。</b>企业名单基于公开信息整理，用于行业结构展示，不构成任何投资建议；覆盖不代表推荐。报告内容以原稿为准，数据截止各报告标注日期。</p>
</footer>

<script>
const SEG = @@SEG@@;
const TECH = @@TECH@@;
const SCENE = @@SCENE@@;
const SC = @@SC@@;
const TSHORT = @@TSHORT@@;
const APP_SEGS = @@APP_SEGS@@;
const SUPPORT_SEGS = @@SUPPORT@@;
const MODES = @@MODES@@;
const BLANKS = @@BLANKS@@;
const C = @@CDATA@@;

const byReport = (a,b)=> (b[4]?1:0)-(a[4]?1:0);
const isApp = c => c[1].some(s=>APP_SEGS.includes(s));
const modeOf = c => c[5] || null;
const $ = s => document.querySelector(s);
const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const reportCount = C.filter(x=>x[4]).length;
$('#s1').textContent = C.length;
$('#s2').innerHTML = reportCount + '<i> 家</i>';

function chip(c){
  const [n,segs,tech,scene,r] = c;
  const multi = segs.length>1 ? ' multi' : '';
  const badge = segs.length>1 ? `<span class="mc" title="横跨 ${segs.length} 个环节">${segs.length}</span>` : '';
  const inner = esc(n) + badge + (r ? '<span class="ar">↗</span>' : '');
  if(r) return `<a class="chip r${multi}" href="reports/${encodeURIComponent(r)}.html" title="${esc(n)} · 查看调研报告" data-n="${esc(n)}">${inner}</a>`;
  return `<span class="chip${multi}" data-n="${esc(n)}" title="${esc(n)}（暂无调研报告）">${esc(n)}</span>`;
}

const up = [], mid = [], down = [], sup = [];
Object.keys(SEG).forEach(k=>{
  const [layer,name] = SEG[k];
  const list = C.filter(c=>c[1].includes(k)).sort(byReport);
  if(!list.length) return;
  const h = `<div class="seg" data-seg="${k}">
    <div class="seg-h"><span class="st">${name}</span><span class="cnt">${list.length}</span></div>
    <div class="chips">${list.map(chip).join('')}</div>
  </div>`;
  if(SUPPORT_SEGS.includes(k)) sup.push(h);
  else if(layer==='上游') up.push(h);
  else if(layer==='中游') mid.push(h);
  else down.push(h);
});
$('#up').innerHTML = up.join('');
$('#mid').innerHTML = mid.join('');
$('#down').innerHTML = down.join('');
$('#sup').innerHTML = sup.join('');

$('#techGrid').innerHTML = TECH.map(([k,t,s])=>{
  const list = C.filter(c=>isApp(c) && c[2].includes(k)).sort(byReport);
  return `<div><div class="col-h"><div class="t">${t}<span class="cc">${list.length}</span></div><div class="s">${s}</div></div>
    <div class="colbox" data-tech="${k}">${list.map(chip).join('')}</div></div>`;
}).join('');

$('#sceneGrid').innerHTML = SCENE.map(([k,d],i)=>{
  const list = C.filter(c=>isApp(c) && c[3].includes(k)).sort(byReport);
  return `<div class="scene${i===0?' wide':''}" data-scene="${k}"><h3>${k}<span class="cc">${list.length}</span></h3><div class="m">${d}</div>
    <div>${list.map(chip).join('')}</div></div>`;
}).join('');

let mhtml = '<div class="mrow"><div class="mhead"></div>' +
  TECH.map(([k,t,s])=>`<div class="mhead"><div class="ht">${TSHORT[k]}<span class="cc">${C.filter(c=>modeOf(c)&&c[2].includes(k)).length}</span></div><div class="hs">${s}</div></div>`).join('') + '</div>';
MODES.forEach(([mk,mt,ms,col])=>{
  mhtml += `<div class="mrow"><div class="mlab"><div class="mt" style="color:${col}">${mt}</div><div class="ms">${ms}</div></div>`;
  TECH.forEach(([k])=>{
    const blank = BLANKS.find(b=>b[0]===mk && b[1]===k);
    let inner;
    if(blank){
      inner = `<div class="mblank"><b>${blank[2]}</b>${blank[3]}</div>`;
    } else {
      const list = C.filter(c=>modeOf(c)===mk && c[2].includes(k)).sort(byReport);
      inner = list.length ? list.map(chip).join('') : '<span class="mnone">—</span>';
    }
    mhtml += `<div class="mcell">${inner}</div>`;
  });
  mhtml += '</div>';
});
$('#modeGrid').innerHTML = mhtml;

document.querySelectorAll('.tab').forEach(b=>{
  b.onclick = ()=>{
    document.querySelectorAll('.tab').forEach(x=>x.classList.remove('on'));
    b.classList.add('on');
    document.querySelectorAll('.view').forEach(v=>v.classList.remove('on'));
    $('#v-'+b.dataset.v).classList.add('on');
  };
});

if(['#tech','#scene','#chain','#mode'].includes(location.hash)){
  const k = location.hash.slice(1);
  const b = document.querySelector('.tab[data-v="'+k+'"]');
  if(b) b.click();
}

const q = $('#q');
q.addEventListener('input', ()=>{
  const v = q.value.trim().toLowerCase();
  let shown = 0;
  document.querySelectorAll('.chip').forEach(el=>{
    const hit = !v || el.dataset.n.toLowerCase().includes(v);
    el.classList.toggle('hide', !hit);
    if(hit) shown++;
  });
  document.querySelectorAll('.seg, .scene').forEach(el=>{
    const any = [...el.querySelectorAll('.chip')].some(c=>!c.classList.contains('hide'));
    el.classList.toggle('hide', !any);
  });
  document.querySelectorAll('.colbox').forEach(el=>{
    const box = el.closest('div').parentElement;
    const any = [...el.querySelectorAll('.chip')].some(c=>!c.classList.contains('hide'));
    if(box) box.style.opacity = any ? 1 : .35;
  });
  $('#empty').style.display = (v && shown===0) ? 'block' : 'none';
});
</script>
</body>
</html>
'''

def build(key, cfg):
    C = normalize(parse(RAW[key]), key)
    segn = len(cfg['SEG'])
    layers = '\n'.join(
      f'''      <div class="layer">
        <div class="layer-h"><span class="n">{n}</span><span class="t">{t}</span><span class="d">{d}</span></div>
        <div id="{i}"></div>
      </div>''' for (n,t,d),i in zip(cfg['layers'],['up','mid','down']))
    rep = {
      '@@TITLE@@':cfg['title'],'@@BRAND@@':cfg['brand'],'@@EN@@':cfg['en'],
      '@@DOC@@':cfg['doc'],'@@DOCFILE@@':cfg['docfile'],'@@TAGLINE@@':cfg['tagline'],
      '@@INTRO@@':cfg['intro'].replace('@@SEGN@@',str(segn)).replace('@@TOTAL@@',f'<span id="total">{len(C)}</span>'),
      '@@SEGCOUNT@@':str(segn),'@@TECHCOUNT@@':str(len(cfg['TECH'])),'@@SCENECOUNT@@':str(len(cfg['SCENE'])),
      '@@TAB1@@':cfg['tabs'][0],'@@TAB2@@':cfg['tabs'][1],'@@TAB3@@':cfg['tabs'][2],'@@TAB4@@':cfg['tabs'][3],
      '@@LAYERS@@':layers,'@@SUPPORTDESC@@':cfg['supportdesc'],
      '@@SCOPE2@@':cfg['scope2'],'@@SCOPE3@@':cfg['scope3'],'@@SCOPE4@@':cfg['scope4'],
      '@@NOTE4@@':cfg['note4'],'@@ABOUT@@':cfg['about'],
      '@@CSS@@':CSS,
      '@@SEG@@':jsval(cfg['SEG']),'@@TECH@@':jsval(cfg['TECH']),
      '@@SCENE@@':jsval(cfg['SCENE']),
      '@@SC@@':jsval({k:k for k,_ in cfg['SCENE']}),
      '@@TSHORT@@':jsval(cfg['TSHORT']),'@@APP_SEGS@@':jsval(cfg['APP_SEGS']),
      '@@SUPPORT@@':jsval(cfg['SUPPORT']),'@@MODES@@':jsval(cfg['MODES']),
      '@@BLANKS@@':jsval(cfg['BLANKS']),'@@CDATA@@':jsval(C),
    }
    out = HTML_SKEL
    for k,v in rep.items():
        out = out.replace(k,v)
    # intro 里的 total span 需要 JS 同步（保持和原站一致）
    out = out.replace("$('#s1').textContent = C.length;", "$('#total').textContent = C.length;\n$('#s1').textContent = C.length;")
    return out, C

def main():
    os.makedirs(OUT, exist_ok=True)
    for key,cfg in SITES.items():
        d = os.path.join(OUT, cfg['slug'])
        os.makedirs(os.path.join(d,'reports','md'), exist_ok=True)
        os.makedirs(os.path.join(d,'tools'), exist_ok=True)
        text, C = build(key,cfg)
        open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(text)
        # 报告链接清单
        reps = sorted({c[4] for c in C if c[4]})
        print(f"{cfg['slug']}: {len(C)} 家企业 / {len(cfg['SEG'])} 环节 / {len(reps)} 份研报")
        for r in reps: print('   -',r)
        open(os.path.join(d,'.reports.json'),'w',encoding='utf-8').write(json.dumps(reps,ensure_ascii=False,indent=1))
    print('done')

if __name__=='__main__':
    main()
