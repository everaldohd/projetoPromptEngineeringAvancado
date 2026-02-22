import os
from pydantic import BaseModel

class Settings(BaseModel):
    """Configurações globais da API Operação IntelliDoc."""
    
    # Informações da API
    PROJECT_NAME: str = "IntelliDoc - Revisor Pericial"
    VERSION: str = "1.0.0"
    
    # Configurações do Ollama (Cozinha)
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    MODEL_TEXT: str = os.getenv("MODEL_TEXT", "mistral-nemo")
    MODEL_VISION: str = os.getenv("MODEL_VISION", "moondream")
    MODEL_EMBEDDING: str = "nomic-embed-text" #mxbai-embed-large
    
    # Parâmetros da Inteligência Artificial
    # Temperatura 0.0 garante o "Estagiário Sóbrio" (Respostas determinísticas e precisas)
    TEMPERATURE: float = 0.0
    
    # Configurações da Memória (RAG / ChromaDB)
    CHROMA_DB_DIR: str = os.getenv("CHROMA_DB_DIR", "./artifacts/chroma_db")

# Instância global das configurações para ser importada em outros arquivos
settings = Settings()