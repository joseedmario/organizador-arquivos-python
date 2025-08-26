import os
import shutil

# Pasta que será organizada (ex: Downloads)
pasta_origem = r"C:\Users\Edy&Jane\Downloads\teste"

# Tipos de arquivos e pastas de destino
pastas_destino = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Planilhas": [".xls", ".xlsx", ".csv"],
    "Documentos": [".doc", ".docx", ".txt"],
    "Compactados": [".zip", ".rar"],
    "Executáveis": [".exe", ".msi"],
    "Apresentações": [".ppt", ".pptx"],
    "Outros": []
}

# Criar pastas se não existirem
for pasta in pastas_destino:
    caminho = os.path.join(pasta_origem, pasta)
    if not os.path.exists(caminho):
        os.mkdir(caminho)

# Mover arquivos
for arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, arquivo)

    if os.path.isfile(caminho_arquivo):
        movido = False
        for pasta, extensoes in pastas_destino.items():
            if any(arquivo.lower().endswith(ext) for ext in extensoes):
                shutil.move(caminho_arquivo, os.path.join(pasta_origem, pasta, arquivo))
                movido = True
                break
        if not movido:
            shutil.move(caminho_arquivo, os.path.join(pasta_origem, "Outros", arquivo))

print("✅ Organização concluída!")
