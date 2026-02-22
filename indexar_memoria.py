import os
import chromadb
from chromadb.utils import embedding_functions
from PyPDF2 import PdfReader
from src.config import settings

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
    # Parâmetros de 'Segurança Máxima' para destravar o projeto
    CHUNK_SIZE = 400   
    OVERLAP = 100      
    STRIDE = CHUNK_SIZE - OVERLAP 

    print(f"Iniciando indexação robusta (Modelo: {settings.MODEL_EMBEDDING})...")
    
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
            
            chunks = []
            for i in range(0, len(texto_completo), STRIDE):
                bloco = texto_completo[i : i + CHUNK_SIZE]
                if len(bloco.strip()) > 30:
                    chunks.append(bloco)
            
            if chunks:
                print(f"   -> Gerados {len(chunks)} fragmentos. Indexando...")
                for idx, chunk in enumerate(chunks):
                    # Debug: mostra o progresso para identificar o ponto de falha
                    if idx % 10 == 0:
                        print(f"      Processando fragmento {idx}/{len(chunks)}...")
                    
                    collection.upsert(
                        documents=[chunk],
                        ids=[f"{nome_arquivo}_{idx}"],
                        metadatas=[{"origem": nome_arquivo}]
                    )
                print(f"✅ Arquivo {nome_arquivo} processado com sucesso.")

    print("\n🚀 MISSÃO CUMPRIDA: O acervo de laudos está pronto para consulta!")

if __name__ == "__main__":
    criar_banco_laudos()