import sys
from dotenv import load_dotenv
import pandas as pd
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from prompt.prompt_library import PROMPT_REGISTRY
from utils.model_loader import ModelLoader
from langchain_core.output_parsers.json import JsonOutputParser
from langchain.output_parsers import OutputFixingParser

class DocumentComparatorLLM:
    def __init__(self):
        load_dotenv()
        self.log=CustomLogger().get_logger(__name__)
        self.loader=ModelLoader()
        self.llm=self.loader.load_llm()
        self.parser=JsonOutputParser(pydantic_object=SummaryResponse)
        self.fixing_parser=OutputFixingParser.from_llm(parser=self.parser,llm=self.llm)
        self.prompt=PROMPT_REGISTRY["document_comparison"]
        self.chain=self.prompt|self.llm|self.fixing_parser
        self.log.info("DocumentComparatorLLM initialized successfully")
    def compare_documents(self):
        """
        Compare two documents and returns a structured comparison.
        """
        try:
            pass
        except Exception as e:
            self.log.error("Error in compare_documents:{e}", error=str(e))
            raise DocumentPortalException("An error occured while comparing document", sys) from e
    def _format_response(self):
        """
        Format the LLM response into a structured format.
        """
        try:
            pass
        except Exception as e:
            self.log.error("Error formatting response into Dataframe", error=str(e))
            raise DocumentPortalException("Error formatting response", sys) from e