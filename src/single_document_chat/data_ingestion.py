import uuid
from pathlib import Path
import sys
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from utils.model_loader import ModelLoader


class SingleDocIngestor:
    def __init__(self):
        try:
            self.log= CustomLogger().get_logger(__name__)
        except Exception as e:
            self.log.error("Error initializing SingleDocIngestor", error=str(e))
            raise DocumentPortalException("Failed to initialize SingleDocIngestor", sys)  

    def ingest_files(self):
        try:
            pass
        except Exception as e:
            self.log.error("Document Ingestion Failed", error=str(e))
            raise DocumentPortalException("Ingestion eror in SingleDocIngestor", sys)   


    def _create_retriever(self):
        try:
            pass
        except Exception as e:
            self.log.error("Creating retriever failed", error=str(e))
            raise DocumentPortalException("Failed to create retriever in SingleDocIngestor", sys)


