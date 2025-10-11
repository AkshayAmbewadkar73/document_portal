import os
from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from prompt.prompt_library import *
import sys
from model import *
from langchain_core.output_parsers import JSONOutputParser
from langchain.ouput_parsers import OutputFixingParser

class DocumentAnalyzer:
    'Analyzes documents using a pre-trained model.'
    
    def __init__(self):
        self.log=CustomLogger().get_logger(__name__)
        try:
            self.loader=ModelLoader()
            self.llm=self.loader.load_llm()
            #prepare parser
            self.parser=JSONOutputParser(pydentic_object=Metadata)
            self.fixing_parser=OutputFixingParser
            self.prompt= prompt
            self.log.info("DocumentAnalyzer initialized successfully")
            
        except Exception as e:
            self.log.error("Error initializing DocumentAnalyzer", error=str(e))
            raise DocumentPortalException("Failed to initialize DocumentAnalyzer", e) from e
        

    def analyze_document(self, document_text:str)-> dict:
        """Analyze the document text and return structured metadata and summary"""
        try:
            chain=self.prompt|self.LLM|self.parser
            self.log.info("Meta data analysis chain initialized")

            response = chain.invoke({
                "format_instructions": self.parser.get_format_instructions(),
                "document_text": document_text
            })
            self.log.info("Metadata extraction successful",key=list(response.keys()))

            return response
        except Exception as e:
            self.log.error("Metadata analysis failed"),error=str(e)
            raise DocumentPortalException("Failed to analyze document", e) from e
        