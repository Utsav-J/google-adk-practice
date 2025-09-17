import os
import sys
curr_agent_dir = os.path.dirname(__file__)
agents_dir = os.path.dirname(curr_agent_dir)
repo_dir = os.path.dirname(agents_dir)
sys.path.append(repo_dir)
from google.adk.agents import SequentialAgent
from utils.file_utils import load_txt_file

from agents.question_generator.agent import question_generator_agent
from agents.question_researcher.agent import question_researcher_agent
from agents.query_generator.agent import query_generator_agent
from agents.requirements_writer.agent import requirements_writer
from agents.designer.agent import designer
from agents.code_writer.agent import code_writer

root_agent = SequentialAgent(
    name="root_agent",
    description="This is a sequential agent that executes the sub agents in the provided order",
    sub_agents=[
        question_generator_agent,
        question_researcher_agent,
        query_generator_agent,
        requirements_writer,
        designer,
        code_writer
    ]
)