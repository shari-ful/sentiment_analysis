from pydantic import BaseModel

class Analyze(BaseModel):
    text: str | None = None

    class Config:
        schema_extra = {
            "example": {
                "text": "I love to code"
            }
        }