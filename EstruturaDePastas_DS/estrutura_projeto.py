import os
import sys

def create_project_structure(project_path, project_name):
    # Criar diretório do projeto
    os.makedirs(project_name)

    # Criar subdiretórios
    os.makedirs(os.path.join(project_name, "0_data", "raw"))
    os.makedirs(os.path.join(project_name, "0_data", "processed"))

    os.makedirs(os.path.join(project_name, "1_scripts"))

    os.makedirs(os.path.join(project_name, "2_notebooks", "exploration"))
    os.makedirs(os.path.join(project_name, "2_notebooks", "analysis"))

    os.makedirs(os.path.join(project_name, "3_powerbi", "dashboards"))
    os.makedirs(os.path.join(project_name, "3_powerbi", "datasets"))

    os.makedirs(os.path.join(project_name, "4_docs"))

    # Criar README.md
    readme_content = f"""<div align='center'>

# {project_name} 💡

![DashBoard]()    

[![Tech](https://go-skill-icons.vercel.app/api/icons?i=figma,anaconda,py)](https://skillicons.dev)

</div>

> Resumo do Projeto: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.

## 🕋 Links do Projeto

- [Figma](https://exemplo.com/)
- [PowerBI](https://exemplo.com/)

## 🎯 Implementações/Features

-   [ ] Começando
-   [ ] Estilos Globais do Projeto
-   [ ] Estruturação/Estilização Avançada
-   [ ] Resolvendo Bugs
-   [ ] Projeto Finalizado

## 📁 Estrutura de Pasta
```
{project_name}/
│
├── 0_data/          # Dados brutos e processados
│   ├── raw/         # Dados brutos, diretamente das fontes
│   └── processed/   # Dados processados e limpos
│
├── 1_scripts/       # Scripts úteis
│
├── 2_notebooks/     # Jupyter Notebooks
│   ├── exploration/ # Notebooks para exploração inicial dos dados
│   └── analysis/    # Notebooks para análises específicas
│
├── 3_powerbi/       # Arquivos relacionados ao Power BI
│   ├── dashboards/  # Dashboards criados no Power BI
│   └── datasets/    # Conjuntos de dados usados no Power BI
│
└── 4_docs/          # Documentos de referência, artigos, etc.
```
## 🤝 Referencias e Links Complementares
- [exemplo](https://exemplo.com/)"""

    with open(
        os.path.join(project_name, "README.md"), "w", encoding="utf-8"
    ) as readme_file:
        readme_file.write(readme_content)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        project_path = sys.argv[1]
        project_name = input("Digite o nome do projeto: ")
        create_project_structure(project_path, project_name)
        print("Estrutura do projeto criada com sucesso!")
    else:
        print("Erro: Caminho do projeto não fornecido.")
    
    input("Pressione Enter para sair...")