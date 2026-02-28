import os
from datetime import datetime
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
    # MODEL_EMBEDDING: str = "nomic-embed-text" # Rápido mas superficial
    # MODEL_EMBEDDING: str = "mxbai-embed-large" # Intermediário
    MODEL_EMBEDDING: str = "qwen3-embedding" # Muito mais denso e inteligente, suporta mais tokens e contexto
    
    # Parâmetros da Inteligência Artificial
    # Temperatura 0.0 garante o "Estagiário Sóbrio" (Respostas determinísticas e precisas)
    TEMPERATURE: float = 0.0
    
    # Configurações da Memória (RAG / ChromaDB)
    # Gera pastas dinamicamente baseada no modelo usando pra vector search
    CHROMA_DB_DIR: str = os.getenv(
        "CHROMA_DB_DIR", 
        f"./artifacts/chroma_db_{MODEL_EMBEDDING}_{datetime.now().strftime('%Y-%m-%d')}"
    )

# Instância global das configurações para ser importada em outros arquivos
settings = Settings()