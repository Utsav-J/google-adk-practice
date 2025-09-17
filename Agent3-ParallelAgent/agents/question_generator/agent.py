import os
import sys
curr_agent_dir = os.path.dirname(__file__)
agents_dir = os.path.dirname(curr_agent_dir)
repo_dir = os.path.dirname(agents_dir)
sys.path.append(repo_dir)
from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from utils.file_utils import load_txt_file

question_generator_agent = LlmAgent(
    name="question_generator_agent",
    description=load_txt_file("description.txt"),
    instruction=load_txt_file("instruction.txt"),
    tools=[google_search],
    output_key="question_generator_output"
)
