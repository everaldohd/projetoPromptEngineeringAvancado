import os
import re
import chromadb
from chromadb.utils import embedding_functions
from PyPDF2 import PdfReader
from src.config import settings
from src.services.ollama_service import OllamaService

def extrair_texto_pdf(caminho_pdf):
    texto = ""
    try:
        leitor = PdfReader(caminho_pdf)
        for pagina in leitor.pages:
            conteudo = pagina.extract_text()
            if conteudo:
                # Limpeza agressiva: remove tudo que não for texto útil
                texto += " ".join(conteudo.split()) + " "
    except Exception as e:
        print(f"Erro ao ler {caminho_pdf}: {e}")
    return texto

def criar_banco_laudos():
    # Limite de tamanho aproximado para o agrupamento de frases
    MAX_CHUNK_SIZE = 400

    print(f"Iniciando indexação robusta (Modelo: {settings.MODEL_EMBEDDING})...")
    
    ollama_service = OllamaService()
    chroma_client = chromadb.PersistentClient(path=settings.CHROMA_DB_DIR)
    
    # Voltamos para o Nomic, que é o padrão de ouro para RAG leve
    ollama_ef = embedding_functions.OllamaEmbeddingFunction(
        url=f"{settings.OLLAMA_BASE_URL}/api/embeddings",
        model_name=settings.MODEL_EMBEDDING
    )
    
    # Força a criação de uma coleção limpa
    try:
        chroma_client.delete_collection("acervo_laudos")
    except:
        pass
    collection = chroma_client.create_collection(name="acervo_laudos", embedding_function=ollama_ef)
    
    pasta_laudos = "artifacts/Laudos_Modelo"
    
    for nome_arquivo in os.listdir(pasta_laudos):
        if nome_arquivo.lower().endswith('.pdf'):
            caminho_completo = os.path.join(pasta_laudos, nome_arquivo)
            print(f"\n📂 Analisando arquivo: {nome_arquivo}")
            
            texto_completo = extrair_texto_pdf(caminho_completo)
            
            # Separa o texto em frases com base no ponto final
            # O regex (?<=\.)\s+ divide o texto nos espaços logo após um ponto
            frases = re.split(r'(?<=\.)\s+', texto_completo)
            
            chunks = []
            chunk_atual = ""
            
            for frase in frases:
                # Se a frase sozinha é maior que o max, ou se juntando vai caber
                if not chunk_atual or len(chunk_atual) + len(frase) <= MAX_CHUNK_SIZE:
                    chunk_atual += frase + " "
                else:
                    # O chunk atual atingiu o tamanho, podemos salvá-lo
                    if chunk_atual.strip():
                        chunks.append(chunk_atual.strip())
                    chunk_atual = frase + " "
            
            # Salvar eventuais sobras no último chunk
            if chunk_atual.strip():
                chunks.append(chunk_atual.strip())
            
            if chunks:
                print(f"   -> Gerados {len(chunks)} fragmentos. Indexando...")
                for idx, chunk in enumerate(chunks):
                    # Debug: mostra o progresso para identificar o ponto de falha
                    if idx % 10 == 0:
                        print(f"      Processando fragmento {idx}/{len(chunks)}...")
                    
                    try:
                        collection.upsert(
                            documents=[chunk],
                            ids=[f"{nome_arquivo}_{idx}"],
                            metadatas=[{"origem": nome_arquivo}]
                        )
                    except Exception as e:
                        # Se o erro for de contexto excedido (400 Bad Request / exceeds context length)
                        if "exceeds" in str(e).lower() or "context" in str(e).lower() or "400" in str(e):
                            print(f"      [!] Fragmento {idx} excedeu tokens. Resumindo...")
                            chunk_resumido = ollama_service.resumir_texto(chunk)
                            try:
                                collection.upsert(
                                    documents=[chunk_resumido],
                                    ids=[f"{nome_arquivo}_{idx}"],
                                    metadatas=[{"origem": nome_arquivo}]
                                )
                            except Exception as e2:
                                print(f"      [!] Falha ao indexar resumo. Truncando... Erro: {e2}")
                                collection.upsert(
                                    documents=[chunk_resumido[:2000]],
                                    ids=[f"{nome_arquivo}_{idx}"],
                                    metadatas=[{"origem": nome_arquivo}]
                                )
                        else:
                            print(f"      [X] Erro desconhecido no fragmento {idx}: {e}")
                print(f"✅ Arquivo {nome_arquivo} processado com sucesso.")

    print("\n🚀 MISSÃO CUMPRIDA: O acervo de laudos está pronto para consulta!")

if __name__ == "__main__":
    criar_banco_laudos()