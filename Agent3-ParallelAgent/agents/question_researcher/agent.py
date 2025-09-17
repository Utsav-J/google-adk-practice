import os
import sys
curr_agent_dir = os.path.dirname(__file__)
agents_dir = os.path.dirname(curr_agent_dir)
repo_dir = os.path.dirname(agents_dir)
sys.path.append(repo_dir)

from google.adk.agents import LlmAgent, ParallelAgent
from google.adk.tools import google_search
from utils.file_utils import load_txt_file

base_description = load_txt_file("agents/question_researcher/description.txt")
base_instruction = load_txt_file("agents/question_researcher/instruction.txt")


question_researcher_1 = LlmAgent(
    name = "question_researcher_1",
    model = "gemini-2.5-flash",
    description=base_description,
    instruction=base_instruction,
    tools=[google_search],
    output_key="question_researcher_1_output"
)
question_researcher_2 = LlmAgent(
    name = "question_researcher_2",
    model = "gemini-2.5-flash",
    description=base_description,
    instruction=base_instruction,
    tools=[google_search],
    output_key="question_researcher_2_output"
)
question_researcher_3 = LlmAgent(
    name = "question_researcher_3",
    model = "gemini-2.5-flash",
    description=base_description,
    instruction=base_instruction,
    tools=[google_search],
    output_key="question_researcher_3_output"
)
question_researcher_4 = LlmAgent(
    name = "question_researcher_4",
    model = "gemini-2.5-flash",
    description=base_description,
    instruction=base_instruction,
    tools=[google_search],
    output_key="question_researcher_4_output"
)
question_researcher_5 = LlmAgent(
    name = "question_researcher_5",
    model = "gemini-2.5-flash",
    description=base_description,
    instruction=base_instruction,
    tools=[google_search],
    output_key="question_researcher_5_output"
)

question_researcher_parallel_agent = ParallelAgent(
    name = "question_researcher_parallel_agent",
    description="Runs five question research agents in parallel to research and answer all five questions simultaneously",
    sub_agents=[
        question_researcher_1,
        question_researcher_2,
        question_researcher_3,
        question_researcher_4,
        question_researcher_5
    ]
)

question_researcher_agent = question_researcher_parallel_agent