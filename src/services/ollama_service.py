import json
import chromadb
from chromadb.utils import embedding_functions
from openai import OpenAI
from src.config import settings

# Instancia o cliente apontando para o Ollama local
client = OpenAI(
    base_url=f"{settings.OLLAMA_BASE_URL}/v1",
    api_key='ollama' # Chave dummy obrigatória
)

class OllamaService:
    def __init__(self):
        self.modelo_texto = settings.MODEL_TEXT
        self.modelo_visao = settings.MODEL_VISION
        self.temperatura = settings.TEMPERATURE
        
        # --- CONFIGURAÇÃO DA MEMÓRIA (CHROMADB) ---
        self.chroma_client = chromadb.PersistentClient(path=settings.CHROMA_DB_DIR)
        self.ollama_ef = embedding_functions.OllamaEmbeddingFunction(
            url=f"{settings.OLLAMA_BASE_URL}/api/embeddings",
            model_name=settings.MODEL_EMBEDDING
        )

    def analisar_laudo_cot(self, conteudo: str, tipo_exame: str) -> str:
        """
        Analisa o texto do laudo pericial usando Chain of Thought (CoT).
        Retorna o texto bruto da IA.
        """
        prompt_sistema = f"""
        Você é um Perito Criminal Revisor Sênior da PCDF.
        Sua missão é fazer o controle de qualidade técnico e lógico de laudos periciais da área de {tipo_exame}.
        
        REGRAS DE ANÁLISE (Chain of Thought):
        Pense passo a passo antes de concluir:
        1. Fatos: Quais são os vestígios materiais e a dinâmica relatada no texto?
        2. Coerência Física/Lógica: A dinâmica narrada é possível dadas as leis da física e a natureza dos vestígios?
        
        FORMATO DE SAÍDA:
        PARECER TÉCNICO: [Seu raciocínio detalhado]
        VEREDITO: [CONSISTENTE ou INCONSISTENTE]
        """

        print(f"\n[OllamaService] Iniciando revisão do laudo ({self.modelo_texto})...")
        
        response = client.chat.completions.create(
            model=self.modelo_texto,
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": f"LAUDO A SER REVISADO:\n{conteudo}"}
            ],
            temperature=self.temperatura
            # Removemos o response_format! A IA agora cospe texto livre.
        )
        
        return response.choices[0].message.content

    def analisar_evidencia_visual(self, imagem_b64: str, relato_associado: str) -> str:
        """
        Usa o modelo de visão para cruzar a foto do vestígio com o texto do laudo.
        """
        prompt_visao = f"""
        Você é um perito criminal de laboratório.
        O laudo descreve o vestígio da seguinte forma: "{relato_associado}".
        
        Analise a imagem enviada. O que você vê na imagem confirma ou contradiz a descrição do laudo?
        Seja direto, técnico e aponte apenas os fatos visuais.
        """

        print(f"\n[OllamaService] Iniciando análise visual ({self.modelo_visao})...")

        response = client.chat.completions.create(
            model=self.modelo_visao,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt_visao},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{imagem_b64}"}}
                    ]
                }
            ],
            temperature=self.temperatura
        )
        
        return response.choices[0].message.content

    def consultar_acervo(self, pergunta: str) -> tuple[str, list[str]]:
        """
        Consulta o acervo de laudos para buscar jurisprudência pericial (RAG).
        Retorna uma tupla contendo (resposta_da_ia, lista_de_fontes).
        """
        # Acessa a coleção que criamos no script de indexação
        collection = self.chroma_client.get_collection(name="acervo_laudos", embedding_function=self.ollama_ef)
        
        # Recupera os 4 fragmentos mais parecidos matematicamente
        resultados = collection.query(
            query_texts=[pergunta],
            n_results=4
        )
        
        contexto_recuperado = "\n---\n".join(resultados["documents"][0])
        fontes = list(set([m["origem"] for m in resultados["metadatas"][0]]))
        
        prompt_rag = f"""
        Você é um Perito Sênior consultando o acervo de laudos da PCDF.
        Baseie sua resposta ESTRITAMENTE nos fragmentos de laudos fornecidos abaixo.
        Se não encontrar a resposta, informe que o acervo não possui casos similares.

        FRAGMENTOS DO ACERVO:
        {contexto_recuperado}

        PERGUNTA: {pergunta}
        """
        
        # O modelo lê os fragmentos e formula a resposta fundamentada
        resposta_ia = self.analisar_laudo_cot(prompt_rag, "Consulta ao Acervo")
        
        return resposta_ia, fontes