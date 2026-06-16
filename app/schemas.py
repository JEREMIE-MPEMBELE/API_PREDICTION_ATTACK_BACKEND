from pydantic import BaseModel,Field

class DataInput(BaseModel):
    network_packet_size : int = Field(gt=0)
    login_attempts : int = Field(ge=0)
    session_duration : float = Field(gt=0)
    ip_reputation_score : float = Field(ge=0,lt=1)
    failed_logins : float = Field(ge=0)

class PredictionOutPut(BaseModel):
    classe : int
    score : float
 