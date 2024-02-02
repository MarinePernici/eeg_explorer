""" 
This file contains the SQLAgent class, which is used to interact with the 
SQL database using the GPT-4 language model.
"""

import os
import time
from typing import Dict, Tuple

import requests
from dotenv import load_dotenv
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI
from langchain.utilities import SQLDatabase

import back.sql_agent_config as sql_agent_cfg

load_dotenv()

class SQLAgent:
    def __init__(self):
            """Initiate the SQLAgent class.
            
            This class is used to interact with the SQL database using the GPT-4
            language model.
            
            The class is initiated by creating an instance of the SQLDatabase class
            and the ChatOpenAI class. The SQLDatabase class is used to interact with
            the SQL database, and the ChatOpenAI class is used to interact with the
            GPT-4 language model.
            
            The class also creates an agent using the initialize_agent function
            from the langchain.agents module. The agent is used to interact with
            the SQL database using the GPT-4 language model.
            
            The class also defines the prefix and suffix of the agent's prompt.
            
            Args:
                None
                
            Returns:
                None
            """
            self.db = SQLDatabase.from_uri(os.environ.get('DATABASE_URL_SPECTRE'))
            self.gpt_llm = ChatOpenAI(model_name='gpt-4-turbo-preview')
            self.toolkit = SQLDatabaseToolkit(db=self.db, llm=self.gpt_llm)
            self.agent = initialize_agent(
                tools=self.toolkit.get_tools(),
                llm=self.gpt_llm,
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                verbose=True,
                return_intermediate_steps=True,
                agent_kwargs={
                    "prefix": self.prefix_sql(),
                    "suffix": self.suffix_sql()
                },
                handle_parsing_errors=True
            )

    @staticmethod
    def prefix_sql():
        """Return the prefix of the agent's prompt."""
        return sql_agent_cfg.prefix

    @staticmethod
    def suffix_sql():
        """Return the suffix of the agent's prompt."""
        return sql_agent_cfg.suffix
    
    def query_database(
        self, 
        query: str
    ) -> Tuple[str, int, int, int, float, float]:
        """Query the SQL database with the sql agent.
        
        Args:
            query (str): The query to be executed on the SQL database.
        
        Returns:
            Tuple[str, int, int, int, float, float]: A tuple containing the
            result of the query, the total tokens used, the prompt tokens used,
            the completion tokens used, the total cost of the query, and the
            execution time in seconds.
        """
        try:
            with get_openai_callback() as cb:
                start = time.time()
                result = self.agent(query)
                end = time.time()
                return self.format_response(result, cb, end - start)
        except Exception as e:
            print(f"Error: {e}")
            return (
                "An error occurred, please try again",
                None,
                None,
                None,
                None,
                -1.
            )

    @staticmethod
    def format_response(result, cb, execution_time):
        """Format the response from the agent and the callback.
        
        Args:
            result (str): The response from the agent.
            cb (Callback): The callback from the agent.
            execution_time (float): The execution time of the query.
            
        Returns:
            Tuple[str, int, int, int, float, float]: A tuple containing the
            result of the query, the total tokens used, the prompt tokens used,
            the completion tokens used, the total cost of the query, and the
            execution time in seconds."""
        return (
            result,
            cb.total_tokens,
            cb.prompt_tokens,
            cb.completion_tokens,
            cb.total_cost,
            execution_time
        )

