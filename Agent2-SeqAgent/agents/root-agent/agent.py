import os
import sys
curr_agent_dir = os.path.dirname(__file__)
agents_dir = os.path.dirname(curr_agent_dir)
repo_dir = os.path.dirname(agents_dir)
sys.path.append(repo_dir)
from agents.designer.agent import designer
from agents.requirements_writer.agent import requirements_writer
from agents.code_writer.agent import code_writer

from google.adk.agents import SequentialAgent
root_agent = SequentialAgent(
    name="website_builder_root_agent",
    sub_agents=[requirements_writer,designer,code_writer],
    description="This is a sequential agent that executes the sub agents in the provided order"
)