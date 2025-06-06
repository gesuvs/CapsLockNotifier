# 🚨 CapsLockNotifier

---

Um monitor simples e eficiente para o estado da tecla **Caps Lock** no Windows.  
Exibe uma notificação **toast personalizada** sempre que o Caps Lock é ativado ou desativado.

---

## 📌 Funcionalidades

- Monitoramento em tempo real do estado da tecla Caps Lock via **hook de teclado** do Windows (Low-Level Keyboard Hook)  
- Notificação toast personalizada, centralizada no topo da tela com estilo moderno e discreto  
- Executa em segundo plano e pode ser configurado para iniciar junto com o Windows  
- Baixo consumo de recursos, usando eventos do sistema ao invés de loops contínuos

---

## 📁 Estrutura do Projeto

CapsLockNotifier/  
│  
├── app/  
│ ├── __init__.py  
│ ├── notifier.py # Lógica do hook e notificação  
│ └── toast.py # Classe para exibir Toasts personalizados  
│  
├── __main__.py # Arquivo principal para rodar o app  
├── requirements.txt # Dependências Python  
├── README.md # Documentação do projeto  
└── dist/ # Executável gerado pelo PyInstaller

---

## 🚀 Como executar

1. Crie e ative um ambiente virtual:  
    ```bash
    python -m venv venv
    source venv/Scripts/activate   # Windows
    # ou
    source venv/bin/activate       # Linux/Mac (não testado)
    ```

2. Instale as dependências:  
    ```bash
    pip install -r requirements.txt
    ```

3. Execute o programa em modo debug:  
    ```bash
    python .
    ```

4. Para executar silenciosamente (sem console), use:  
    ```bash
    pythonw .
    ```

---

## 🛠️ Gerar Executável (.exe)

Utilize o PyInstaller para gerar o `.exe`:

```bash
pyinstaller --onefile --noconsole __main__.py -n CapsLockNotifier
```

O executável será gerado na pasta dist/.


🔧 Configurar inicialização automática no Windows
Adicione o programa no registro para iniciar junto com o Windows:

Crie um arquivo .reg com o conteúdo:

```
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run]
"CapsLockNotifier"="\"C:\\caminho\\para\\seu\\CapsLockNotifier.exe\""
```


Dê um duplo clique para importar no registro, ou use script Python para automatizar.

📚 Tecnologias e Bibliotecas
Python 3.10+

ctypes para integração com API Win32

tkinter para criar as notificações toast customizadas

PyInstaller para empacotamento do executável

🤝 Contribuições
Contribuições são muito bem-vindas!
Abra issues para bugs e features, ou envie pull requests.

📄 Licença
Projeto open-source — sinta-se livre para usar, modificar e distribuir!

👨‍💻 Autor
Guilherme Jesus