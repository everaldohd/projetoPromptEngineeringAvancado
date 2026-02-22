from pydantic import BaseModel, Field
from typing import List, Optional

# ==========================================
# Entradas (Inputs) - O que o usuário envia
# ==========================================

class LaudoInput(BaseModel):
    """Esquema para o endpoint de Texto e CoT."""
    conteudo: str = Field(
        ..., 
        description="Texto completo do laudo pericial ou do relato da dinâmica da ocorrência."
    )
    tipo_exame: str = Field(
        default="Local de Crime", 
        description="Área da perícia (ex: Balística, Informática, Local de Morte Violenta)."
    )

class ImagemInput(BaseModel):
    """Esquema para o endpoint de Visão Computacional (Moondream)."""
    imagem_base64: str = Field(
        ..., 
        description="String base64 da fotografia do vestígio."
    )
    relato_associado: str = Field(
        ..., 
        description="O trecho do laudo que descreve o que deveria estar nesta imagem."
    )

class RAGInput(BaseModel):
    """Entrada para consulta ao acervo de laudos."""
    pergunta: str = Field(..., description="Dúvida técnica ou busca por casos similares no acervo.")

# ==========================================
# Saídas (Outputs) - O que a API devolve
# ==========================================

class AnaliseOutput(BaseModel):
    """Esquema padronizado de resposta montado pelo nosso backend."""
    parecer_completo: str = Field(
        ..., 
        description="Análise detalhada do Perito Revisor em texto livre."
    )
    status_ia: str = Field(
        default="Revisão Concluída", 
        description="Status do processamento."
    )


class RAGOutput(BaseModel):
    """Resposta estruturada da consulta ao acervo com fontes."""
    resposta_ia: str = Field(..., description="Resposta processada pela IA com base nos documentos.")
    documentos_consultados: List[str] = Field(..., description="Lista dos nomes dos arquivos PDF de onde a informação foi extraída.")