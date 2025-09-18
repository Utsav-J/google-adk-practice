from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

@app.get("/.well-known/agent.json")
def agent_card():
    return jsonify(
        {
            "name":"TellTime",
            "description":"Tells the current time",
            "url": "localhost:5000",
            "version":"1.0",
            "capabilities":{
                "streaming":False,
                "pushNotifications":False
            }
        }
    )

@app.post("/tasks/send")
def handle_task():
    try:
        task = request.get_json()
        task_id = task.get("id")
        user_message = task["message"]["parts"][0]["text"]
    except (KeyError, IndexError, TypeError):
        return jsonify(
            {
                "error":"Invalid data format"
            }
        ),400
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    reply_text = f"The current time is {current_time}"
    return jsonify(
        {
            "id":task_id,
            "status":{"state":"completed"},
            "messages":[
                task["message"],
                {
                    "role":"agent",
                    "parts":[{"text":reply_text}]
                }
            ]
        }
    )

if __name__ == "__main__":
    app.run(port=5000)