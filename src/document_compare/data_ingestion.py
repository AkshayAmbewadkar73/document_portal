import sys
from pathlib import Path
import fitz
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

class DocumentIngestion:
    
    def  __init__(self,base_dir):
        self.log=CustomeLogger().get_logger(__name__)
        self.base_dir=Path(base_dir)
        self.base_dir.mkdir(parents=True,exist_ok=True)

    def delete_existing_files(self,file_path):
        """
        Delete existing files at specified paths.
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error deleting existing files:{e}")
            raise DocumentPortalException("An error occured while deleting existing files",sys)

    def save_uploadded_file(self):
        """
        Save the uploaded file to the specified directory.
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error saving uploaded file:{e}")
            raise DocumentPortalException("An error occured while saving the uploaded file",sys)

    def read_pdf(self,pdf_path):
        """
        Read and extract text from a PDF file.
        """
        try:
            with fitz.open(pdf_path) as doc:
                if doc.is_encrypted:
                    raise ValueError('Pdf is encrypted:{pdf_path.name}')
                all_text=[]
                for page_num in range(doc.page_count):
                    page=doc.load_page(page_num)
                    text=page.get_text()
                    if text.strip():
                        all_text.append(f"\n---page{page_num+1}--\n{text}")
                self.log.info(f"PDF read successfully",file=str(pdf_path),pages=len(all_text))  
                return "\n".join(all_text)      
        except Exception as e:
            self.log.error(f"Error reading PDF:{e}")
            raise DocumentPortalException("An error occured while reading the PDF",sys)