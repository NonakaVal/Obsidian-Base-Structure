# Visão geral
-----------
Estrutura base para um vault Obsidian com templates, snippets, bases de notas e scripts auxiliares. Projetado para servir como esqueleto reutilizável para organização pessoal, Zettelkasten, gestão de projetos e automações (scripts Python).

Esta pasta já contém uma configuração .obsidian pronta (plugins, snippets, temas) e coleções de templates / CSS / scripts que aceleram a criação de novos vaults.

## 📁 Estrutura

```
.obsidian  
│  
├── Plugins  
├── Themes  
├── Snippets  
└── Workspaces  

X  
│  
└── Coleções adicionais, assets e consultas Dataview (opcional)  

	Assets  
	│  
	├── Hotkeys  
	├── Dataview Collections  
	├── CSS Snippets  
	└── Outros assets  
	
	Templates  
	│  
	├── Format — estruturas e moldes de formatação  
	└── Snippet — pequenos blocos reutilizáveis  
	
	Bases  
	│  
	└── Arquivos .base usados como ponto inicial para notas e boards  
	
	Scripts  
	│  
	├── processamento_audio — transcrição e processamento de áudio  
	├── ferramentas_diversas — conversões e utilidades (ipynb → md, EPUB, etc.)  
	└── organizacao_obsidian — scripts para manipular o vault  	

```


Soluções de problemas comuns
----------------------------
- Plugins não aparecem: mover a pasta `.obsidian` para o diretório do vault e reiniciar o Obsidian.
- CSS snippets não aplicam: Settings → Appearance → CSS snippets → ativar o snippet desejado.
- Templater não executa: confirmar caminho de Templates nas configurações do plugin.

Arquivos/recursos importantes 
-----------------------------
- .obsidian/ — configurações e plugins instalados.
- Templates/Format/_ base template.md — template base para novas notas.
- Scripts/organizacao_obsidian/ChanGe-Templates-Folder.py — script para reorganizar templates (ler antes de executar).
- Assets/Dataview/ — consultas e painéis prontos para usar com Dataview.

