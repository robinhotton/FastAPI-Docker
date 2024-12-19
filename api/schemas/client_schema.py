from pydantic import BaseModel
from typing import Optional


class ClientBase(BaseModel):
    nom: str
    prenom: str
    genre: Optional[str] = None
    adresse: str
    complement_adresse: Optional[str] = None
    tel: Optional[str] = None
    email: Optional[str] = None
    newsletter: Optional[int] = 0


class ClientPost(ClientBase):
    pass


class ClientPatch(ClientBase):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    adresse: Optional[str] = None


class ClientInDB(ClientBase):
    codcli: int
    
    class Config:
        from_attributes = True