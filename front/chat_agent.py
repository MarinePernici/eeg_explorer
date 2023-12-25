import os
import time

from dotenv import load_dotenv
from langchain.agents import create_sql_agent, AgentExecutor
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SQLDatabase

load_dotenv()  # Charge les variables d'environnement depuis '.env'


db = SQLDatabase.from_uri(os.environ.get('DATABASE_URL_SPECTRE'))
gpt_llm = ChatOpenAI(model_name='gpt-4-1106-preview')
toolkit = SQLDatabaseToolkit(db=db, llm=gpt_llm)

# Create the agent
agent = create_sql_agent(
    llm=gpt_llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)


def query_database(query):
    """Run the agent

    Args:
        query (str): The query to run

    Returns:
        str: The response from the agent
    """
    with get_openai_callback() as cb:
        start = time.time()
        response = agent.run(query)
        end = time.time()
        execution_time = end - start
        total_tokens = cb.total_tokens
        prompt_tokens = cb.prompt_tokens
        completion_tokens = cb.completion_tokens
        total_cost = cb.total_cost
        print(f"Total tokens: {total_tokens}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Completion tokens: {completion_tokens}")
        print(f"Total cost: {total_cost}")

    return response, total_tokens, prompt_tokens, completion_tokens, total_cost, execution_time
