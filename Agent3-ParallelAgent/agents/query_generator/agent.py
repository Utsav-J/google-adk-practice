import os
import sys
curr_agent_dir = os.path.dirname(__file__)
agents_dir = os.path.dirname(curr_agent_dir)
repo_dir = os.path.dirname(agents_dir)
sys.path.append(repo_dir)
from google.adk.agents import LlmAgent
from utils.file_utils import load_txt_file

query_generator_agent = LlmAgent(
    name="query_generator_agent",
    model="gemini-2.5-flash",
    description=load_txt_file("agents/query_generator/description.txt"),
    instruction=load_txt_file("agents/query_generator/instruction.txt"),
    output_key="query_generator_agent_output"
)