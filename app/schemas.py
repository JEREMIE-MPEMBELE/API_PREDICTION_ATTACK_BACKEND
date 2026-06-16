from pydantic import BaseModel, Field

class DataInput(BaseModel):
    network_packet_size: int = Field(ge=0, description="Taille des paquets réseau")
    login_attempts: int = Field(ge=0, description="Nombre de tentatives de connexion")
    session_duration: float = Field(ge=0, description="Durée de la session (secondes)")
    ip_reputation_score: float = Field(ge=0, le=1, description="Score de réputation IP (0-1)")
    failed_logins: float = Field(ge=0, description="Taux d'échec de connexion")

class PredictionOutPut(BaseModel):
    classe: int
    score: float