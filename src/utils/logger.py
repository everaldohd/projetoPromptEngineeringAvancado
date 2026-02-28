import logging
import os
import sys
import structlog

# Garantir que o diretório de logs existe
os.makedirs("logs", exist_ok=True)

def setup_logger():
    # Processadores compartilhados e configuração do structlog
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    # Formatter que exporta em formato JSON
    json_formatter = structlog.stdlib.ProcessorFormatter(
        processor=structlog.processors.JSONRenderer(),
    )

    # Formatter para console (output legível)
    console_formatter = structlog.stdlib.ProcessorFormatter(
        processor=structlog.dev.ConsoleRenderer(colors=False),
    )

    # Handlers puros do Python
    req_handler = logging.FileHandler("logs/requisicoes.log", encoding="utf-8")
    req_handler.setLevel(logging.INFO)
    req_handler.setFormatter(json_formatter)

    err_handler = logging.FileHandler("logs/erros.log", encoding="utf-8")
    err_handler.setLevel(logging.ERROR)
    err_handler.setFormatter(json_formatter)

    idx_handler = logging.FileHandler("logs/indexador.log", encoding="utf-8")
    idx_handler.setLevel(logging.INFO)
    idx_handler.setFormatter(json_formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)

    # Limpar handlers previstos
    logging.getLogger().handlers.clear()
    
    # Root logger envia para o console
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(console_handler)

    # Logger específico de requisições
    req_logger = logging.getLogger("requisicoes")
    req_logger.setLevel(logging.INFO)
    req_logger.addHandler(req_handler)
    req_logger.propagate = True

    # Logger específico de erros
    err_logger = logging.getLogger("erros")
    err_logger.setLevel(logging.ERROR)
    err_logger.addHandler(err_handler)
    err_logger.propagate = True

    # Logger específico do indexador
    idx_logger = logging.getLogger("indexador")
    idx_logger.setLevel(logging.INFO)
    idx_logger.addHandler(idx_handler)
    idx_logger.propagate = True

# Inicializa as configurações
setup_logger()

# Exporta os loggers prontos para uso
logger_requisicoes = structlog.get_logger("requisicoes")
logger_erros = structlog.get_logger("erros")
logger_indexador = structlog.get_logger("indexador")
