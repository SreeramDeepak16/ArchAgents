from pydantic import BaseModel, Field
from typing import List, Optional


class AnalystState(BaseModel):
    srs: Optional[str] = None
    fr: List[str] = Field(default_factory=list)
    nfr: List[str] = Field(default_factory=list)
    asr: List[str] = Field(default_factory=list)
    dc: List[str] = Field(default_factory=list)


class ArchState(BaseModel):
    description: str
    srs: Optional[str] = None
    analyst_state: Optional[AnalystState] = None