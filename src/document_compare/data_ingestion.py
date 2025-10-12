import sys
from pathlib import Path
import fitz
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

class DocumentComparator:
    def  __init__(self):
        pass

    def delete_existing_files(self,file_path):
        """
        Delete existing files at specified paths.
        """
        pass

    def save_uploadded_file(self):
        """
        Save the uploaded file to the specified directory.
        """
        pass

    def read_pdf(self):
        """
        Read and extract text from a PDF file.
        """
        pass