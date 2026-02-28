import sys
import os

from fastapi.testclient import TestClient
from src.api.routes import app

client = TestClient(app, raise_server_exceptions=False)

def run_tests():
    # 1. Testar requisição normal
    print("--- Testando requisição normal (GET /) ---")
    response = client.get("/")
    print("Status normal:", response.status_code)
    
    # 2. Testar metrics
    print("--- Testando Prometheus (GET /metrics) ---")
    response_metrics = client.get("/metrics")
    print("Status metrics:", response_metrics.status_code)

    # 3. Testar erro (forçadamente no RAG sem serviço de BD configurado/rodando)
    print("--- Testando erro 500 ---")
    response_erro = client.post("/consultar_manual", json={"pergunta": "teste para log de erro"})
    print("Status erro:", response_erro.status_code)
    
    print("\n--- Conteúdo logs/requisicoes.log ---")
    if os.path.exists("logs/requisicoes.log"):
        with open("logs/requisicoes.log", "r", encoding="utf-8") as f:
            print(f.read())
            
    print("\n--- Conteúdo logs/erros.log ---")
    if os.path.exists("logs/erros.log"):
        with open("logs/erros.log", "r", encoding="utf-8") as f:
            print(f.read())

if __name__ == "__main__":
    run_tests()
