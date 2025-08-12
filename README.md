# mypythonrepo

Um ambiente Python com Jupyter para desenvolvimento, automação e experimentos.

Um repositório onde concentrei alguns trabalhos em Python. Entre eles um trabalho com Selenium para automatizar login na plataforma GitLab e alguns notebooks em Jupyter para estudo de Equações Diferenciais.

---

## Índice

- [Sobre](#sobre)
- [Recursos](#recursos)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Uso](#uso)
- [Scripts Disponíveis](#scripts-disponíveis)
- [Testes Selenium](#testes-selenium)
- [Executáveis](#executáveis)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

---

## Sobre

Este repositório fornece um ambiente Python completo, com suporte a Jupyter Notebook, scripts utilitários e exemplos de automação usando Selenium. Foi pensado para quem quer prototipar rapidamente projetos em Python, testar automações web e empacotar scripts como executáveis.

---

## Recursos

- Ambiente virtual já configurado em `myenv/`
- Integração com Jupyter Notebook
- Pasta de scripts para tarefas diversas
- Exemplos de automação em `selenium/`
- Gerador de executáveis em `executables/`

---

## Pré-requisitos

- Python 3.7 ou superior
- Git
- pip (gerenciador de pacotes Python)
- Navegador compatível com Selenium (Chrome, Firefox etc.)

---

## Instalação

1. Clone o repositório  
   ```bash
   git clone https://github.com/marcio-loiola/mypythonrepo.git
   cd mypythonrepo
   ```

2. Ative o ambiente virtual  
   - Linux/macOS  
     ```bash
     source myenv/bin/activate
     ```  
   - Windows  
     ```powershell
     myenv\Scripts\activate
     ```

3. Instale dependências adicionais (caso necessário)  
   ```bash
   pip install -r requirements.txt
   ```

4. Registre o kernel do ambiente no Jupyter  
   ```bash
   pip install ipykernel
   python -m ipykernel install --user --name=mypythonenv
   ```

---

## Estrutura do Projeto

- **myenv/**  
  Ambiente virtual com pacotes instalados

- **executables/**  
  Scripts empacotados como executáveis

- **scripts/**  
  Ferramentas e utilitários em Python

- **selenium/**  
  Exemplos de automação web usando Selenium

---

## Uso

### Jupyter Notebook

1. Certifique-se de que o ambiente `mypythonenv` esteja ativo  
2. Inicie o servidor  
   ```bash
   jupyter notebook
   ```  
3. Crie ou abra arquivos `.ipynb` na raiz do projeto

### Executar Scripts

Dentro do ambiente virtual, rode qualquer script com:  
```bash
python scripts/<nome_do_script>.py
```

---

## Scripts Disponíveis

- `scripts/data_cleaning.py`
- `scripts/report_generator.py`
- `scripts/api_client.py`

_(Adicione a lista completa conforme seu projeto cresce)_

---

## Testes Selenium

1. Certifique-se de ter o driver apropriado instalado (ChromeDriver, GeckoDriver etc.)  
2. Ative o ambiente virtual  
3. Execute o teste  
   ```bash
   python selenium/<nome_do_teste>.py
   ```

---

## Executáveis

Os executáveis gerados via ferramentas como PyInstaller estão em `executables/`. Para criar novos:

1. Instale o PyInstaller  
   ```bash
   pip install pyinstaller
   ```
2. Empacote um script  
   ```bash
   pyinstaller --onefile scripts/<nome_do_script>.py
   ```
3. O binário ficará em `dist/`

---

## Contribuindo

1. Fork deste repositório  
2. Crie uma branch com sua feature  
3. Faça commits claros e concisos  
4. Abra um pull request descrevendo suas mudanças

---

## Licença

Este projeto está sob a [MIT License](LICENSE).
