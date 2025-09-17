import os
import sys
from google.adk.agents import LlmAgent
curr_agent_dir = os.path.dirname(__file__)
agents_dir = os.path.dirname(curr_agent_dir)
repo_dir = os.path.dirname(agents_dir)
sys.path.append(repo_dir)
from google.adk.agents import LlmAgent
from utils.file_utils import load_txt_file

requirements_writer = LlmAgent(
    name="requirements_writer",
    model="gemini-2.5-flash",
    instruction=load_txt_file("agents/requirements_writer/instructions.txt"),
    description=load_txt_file("agents/requirements_writer/description.txt"),
    output_key="requirements_writer_output"
)