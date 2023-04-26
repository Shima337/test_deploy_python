from flask import Flask, render_template, request, Response, jsonify
import time, json
from flask_cors import CORS
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)

CORS(app)


 

def translate_content(content):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"перуведи на русский эту статью. Не сокращай ее:  {content} -- Качественный перевод статьи:"}
        ]
    )
    result = completion.choices[0].message
    print(result)

    return result

@app.route('/test', methods=['GET'])
def test():
    return "HELLO WORLD2"

@app.route('/translate', methods=['POST'])
def translate2():
    print('im here translate')
    if request.method == 'POST':
        to_translate = request.get_data().decode('utf-8')
        print(to_translate)
        result = translate_content(to_translate)
        parsed_result = json.dumps(result.to_dict())
        print("translated:  ", parsed_result)
        return parsed_result, 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=5000, debug=True)





