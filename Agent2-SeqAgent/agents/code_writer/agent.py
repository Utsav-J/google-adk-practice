import os
import sys
from google.adk.agents import LlmAgent
curr_agent_dir = os.path.dirname(__file__)
agents_dir = os.path.dirname(curr_agent_dir)
repo_dir = os.path.dirname(agents_dir)
sys.path.append(repo_dir)
from google.adk.agents import LlmAgent
from utils.file_utils import load_instructions_file
from tools.file_tool import write_to_file

code_writer = LlmAgent(
    name="code_writer",
    model="gemini-2.5-flash",
    instruction=load_instructions_file("instruction.txt"),
    description=load_instructions_file("description.txt"),
    output_key="code_writer_output",
    tools=[write_to_file]
)