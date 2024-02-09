""" 
This file contains the SQLAgent class, which is used to interact with a
SQL database using a large language model and is built with Langchain tools.
"""

import time
# import logging

from langchain.agents import initialize_agent
from langchain.callbacks import get_openai_callback

import back.sql_agent_config as sql_agent_cfg


class SQLAgent:
    """The SQLAgent class is used to interact with the SQL database
    using a llm.
    """
    def __init__(
        self,
        database=sql_agent_cfg.database,
        llm_model=sql_agent_cfg.llm_model,
        tools=sql_agent_cfg.tools,
        agent_type=sql_agent_cfg.agent_type,
        prompt_template=sql_agent_cfg.prompt_template
    ):
        """ Initialize the SQLAgent class with the llm, the database,
        the tools, the agent_type and the prompt template.
        """
        self.database = database
        self.llm_model = llm_model
        self.tools = tools
        self.agent_type = agent_type
        self.prefix = prompt_template["prefix"]
        self.suffix = prompt_template["suffix"]
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm_model,
            agent=self.agent_type,
            verbose=True,
            return_intermediate_steps=True,
            agent_kwargs={
                "prefix": self.prefix,
                "suffix": self.suffix
            },
            handle_parsing_errors=True
        )

    def query_database(self, query: str) -> tuple:
        """Query the SQL database with the sql agent.

        Args:
            query (str): The query to be executed on the SQL database.

        Returns:
            Tuple[str, int, int, int, float, float]: A tuple containing the
            result of the query, the total tokens used, the prompt tokens used,
            the completion tokens used, the total cost of the query, and the
            execution time in seconds.
        """
        # logging.info(f"Querying the database with the query: {query}")
        try:
            with get_openai_callback() as cb:
                start = time.time()
                result = self.agent(query)
                end = time.time()
                execution_time = end - start
                return (
                    result,
                    cb.total_tokens,
                    cb.prompt_tokens,
                    cb.completion_tokens,
                    cb.total_cost,
                    execution_time
                )
            # logging.info(f"Query successful")
        except Exception as e:
            print(f"Error: {e}")
            # logging.error(f"An error occured during the query: {e}")
            return (
                "An error occurred, please try again",
                None, None, None, None, -1
            )
