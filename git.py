import json
import os

with open("info.json", "r", encoding="utf-8") as f:
    info = json.load(f)

version = info["versão"]
beta_status = info["beta"]
detalhes = input("Detalhes da versão (Opcional): ").strip()

# Criar nova branch
print(f"Criando branch v{version}...")
os.system(f'git checkout -b v{version}')

# Adicionar alterações
os.system('git add .')

# Criar mensagem de commit
commit_message = f'Versão {version}'
if detalhes:
    commit_message += f' - {detalhes}'

# Fazer commit
os.system(f'git commit -m "{commit_message}"')

# Enviar branch
os.system(f'git push origin v{version}')

# Definir tag beta/alpha
tag_suffix = "beta" if beta_status == 1 else "alpha"
tag_name = f"v{version}-{tag_suffix}"

# Adicionar tag
os.system(f'git tag {tag_name}')
os.system(f'git push origin {tag_name}')

print(f"Versão {version} enviada com a tag {tag_name}!")