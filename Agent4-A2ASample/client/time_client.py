import uuid
import requests

server_base_url = "http://localhost:5000"
get_res = requests.get(f"{server_base_url}/.well-known/agent.json")

if get_res.status_code != 200:
    raise Exception("Failed to fetch the agent, check if its running on the right port") 

agent_info = get_res.json()
print(f"Connection succesful. Agent: {agent_info['name']} - {agent_info['description']}")


task_id = str(uuid.uuid4())
task_payload = {
    "id":task_id,
    "message":{
        "role":"user",
        "parts":[
            {"text":"What time is it currently?"}
        ]
    }
}

post_res = requests.post(f"{server_base_url}/tasks/send",json=task_payload)
if post_res.status_code != 200:
    raise Exception(f"Task failed: {post_res.text}")

response_data = post_res.json()
messages = response_data.get("messages",[])
if messages:
    final_reply = messages[-1]["parts"][0]["text"]
    print("Agent says:", final_reply)
else:
    print("No response received.")