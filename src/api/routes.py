import json
from fastapi import FastAPI, HTTPException

# Importamos nossas configurações, modelos e o serviço da IA
from src.config import settings
from src.models.schemas import LaudoInput, ImagemInput, AnaliseOutput, RAGInput, RAGOutput
from src.services.ollama_service import OllamaService

# Inicializa a API
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="API para revisão técnica de laudos periciais."
)

# Instancia o nosso serviço de comunicação com o Ollama (Mistral-Nemo)
ollama_service = OllamaService()

@app.get("/")
def verificar_status():
    """Health check para garantir que a API está online."""
    return {
        "status": "online", 
        "sistema": settings.PROJECT_NAME,
        "versao": settings.VERSION
    }

@app.post("/revisar_laudo", response_model=AnaliseOutput)
def revisar_laudo_cot(laudo: LaudoInput):
    """
    Recebe o texto do laudo e processa usando Chain of Thought (CoT).
    """
    try:
        texto_da_ia = ollama_service.analisar_laudo_cot(laudo.conteudo, laudo.tipo_exame)
        
        resultado_seguro = {
            "parecer_completo": texto_da_ia,
            "status_ia": "Processado com sucesso pelo Mistral-Nemo"
        }
        
        return AnaliseOutput(**resultado_seguro)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@app.post("/analisar_evidencia_visual")
def analisar_evidencia(evidencia: ImagemInput):
    """
    Usa visão computacional para encontrar inconsistências em imagens.
    """
    try:
        resultado = ollama_service.analisar_evidencia_visual(
            evidencia.imagem_base64, 
            evidencia.relato_associado
        )
        return {"analise_visual": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/consultar_manual", response_model=RAGOutput)
def consultar_rag(consulta: RAGInput):
    """
    Consulta o acervo de laudos para buscar jurisprudência pericial (RAG).
    """
    try:
        # O serviço cuida de toda a recuperação (ChromaDB) e geração da resposta
        resposta_ia, fontes = ollama_service.consultar_acervo(consulta.pergunta)
        
        return RAGOutput(
            resposta_ia=resposta_ia,
            documentos_consultados=fontes
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no RAG: {str(e)}")