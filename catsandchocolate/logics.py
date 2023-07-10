from catsandchocolate import parameters
import openai


def generate_items(param: parameters.GenerateItemsParameters):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content":
             f"「{param.title}」に関連する物品を{param.count}個生成してください。"}
        ],
        functions=[{
            "name": "generateItems",
            "description": "生成した物品を返す",
            "parameters": {
                "type": "object",
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "number",
                                    "description": "連番",
                                },
                                "name": {
                                    "type": "string",
                                    "description": "物品名"
                                }
                            }
                        }
                    }
                },
                "required": ["items"]
            }
        }],
        function_call={"name": "generateItems"})
    message = response['choices'][0]['message']  # type: ignore
    return message['function_call']['arguments']


def generate_events(param: parameters.GenerateEventsParameters):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content":
             f"「{param.title}」で発生し得るピンチのシチュエーションを{param.count}個生成してください。それぞれに10文字以内の要約を付加してください。"}
        ],
        functions=[{
            "name": "generateEvents",
            "description": "生成したイベントを返す",
            "parameters": {
                "type": "object",
                "properties": {
                    "events": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "number",
                                    "description": "連番",
                                },
                                "summary": {
                                    "type": "string",
                                    "description": "ピンチのシチュエーションを10文字以内で要約"
                                },
                                "event": {
                                    "type": "string",
                                    "description": "ピンチのシチュエーションを具体的に書く"
                                }
                            }
                        }
                    }
                },
                "required": ["events"]
            }
        }],
        function_call={"name": "generateEvents"})
    message = response['choices'][0]['message']  # type: ignore
    return message['function_call']['arguments']


def evaluate_solution(param: parameters.EvaluateSolutionParameters):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a strict judge. You strictly evaluate the adequacy of the proposed solution to the pinch point on a 100-point scale. You receive a score out of 100 wheather the solution is humorous. And then, you explain why you score these points."},
            {"role": "user", "content":
             f'''situation: {param.title}
             pinch: {param.event}
             solution: {param.solution}
             '''}
        ],
        functions=[{
            "name": "evaluateSolution",
            "description": "evaluate the solution to the pinch",
            "parameters": {
                "type": "object",
                "properties": {
                    "validity_score": {
                        "type": "number",
                        "description": "score that evaluates whether the solution to the pinch can be solved with that solution",
                    },
                    "humorous_score": {
                        "type": "number",
                        "description": "score is based on whether the solution to the pinch is humorous or not",
                    },
                    "reason": {
                        "type": "string",
                        "description": "the reason why you give the score in Japanese",
                    },
                    "tension": {
                        "type": "number",
                        "description": "Quantify whether the tension in the explanation of the reason is positive or negative."
                    }
                },
                "required": ["appropriate_score", "humorous_score", "reason", "tension"]
            }
        }],
        function_call={"name": "evaluateSolution"})
    message = response['choices'][0]['message']  # type: ignore
    return message['function_call']['arguments']


def find_solution(param: parameters.FindSolutionParameters):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": '''
             あなたは発想力豊かな発案者です。指示された所持品を、指示された種類の数だけ使用して、あなたならこのピンチをどう切り抜けますか?
             以下の条件に従って行動してください。
             
             ・指示された物品の中から、指示された種類の数だけ使用していること。指示された種類の数より使った物品の種類が多かったり、少なかったりした場合、誰かが死にます。
             ・使用を決めた物品と、ピンチの状況から当然存在する物品だけを用いて実行可能な行動であること
             ・ピンチの打開につながる行動が好ましい
             ・ユーモラスな行動であればなお良い
             ・行動プランは具体的かつ詳細に、物語仕立てで書いてください
             '''},
            {"role": "user", "content":
             f'''シチュエーション: {param.title}
             ピンチ: {param.event}
             物品: {"、".join(param.items)}
             物品の中から{param.number_to_use}つだけを用いてください。
             '''}
        ],
        functions=[{
            "name": "decidedAction",
            "description": "行動プラン",
            "parameters": {
                "type": "object",
                "properties": {
                    "used_items": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "使用する物品名"
                        },
                        "description": "行動で使用する物品",
                    },
                    "solution": {
                        "type": "string",
                        "description": "行動プランを物語仕立てで書く",
                    },
                },
                "required": ["items", "solution"]
            }
        }],
        function_call={"name": "decidedAction"})
    message = response['choices'][0]['message']  # type: ignore
    return message['function_call']['arguments']
