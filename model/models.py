from pydentic import BaseModel, Field
from typing import Optional, List,Dict, Any


class Metadata(BaseModel):
    Summary:List[str]=Field(default_factory=list, description="Summary of the document")
    Title:str
    Author:str
    DateCreated:str
    LastModifiedDate:str
    Pubslisher:str
    Langauge:str
    PageCount:Union[int,str]
    SentimentTone:str
    
