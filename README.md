# 🤖 Automação com Python (PyAutoGUI)

Este projeto tem como objetivo **automatizar tarefas repetitivas** do dia a dia em um sistema web.  
A automação abre o navegador, realiza o login no sistema da empresa e cadastra automaticamente todos os produtos listados no arquivo **`produtos.csv`**.  

Com isso, elimina-se a necessidade de inserir os dados manualmente, tornando o processo **mais rápido, eficiente e menos propenso a erros humanos**.

---

## 🚀 Tecnologias
- Python 3  
- PyAutoGUI  
- Pandas
- CSV

---

## 🧠 Aprendizados

- **Uso do PyAutoGUI** para automatizar cliques, digitação e navegação em sistemas.
- **Leitura e manipulação de arquivos CSV** com Pandas
- **Controle de fluxo e sincronização com delays**
- **Aplicação prática de automação em cenários reais**, reduzindo tarefas manuais e repetitivas.

---

## 📊 Estrutura do CSV
codigo,marca,tipo,categoria,preco_unitario,custo,obs

MOLO000192,Logitech,Mouse,2,19.95,5.00,Conferir estoque

MOMU000111,Multilaser,Teclado,1,11.99,3.40,

CEAP000101,Apple,Celular,1,1099.00,329.70,

---

## ⚙️ Como Executar
1. Clone este Repositório.
   ```bash
   git clone https://github.com/marcosviniciusribeiiro/python-automacao.git

2. Instale as dependências.
   ```bash
   pip install pyautogui pandas
3. Ajuste o tempo de pausa do pyautogui.PAUSE se necessário, conforme a velocidade do seu sistema. 
4. Execute o script principal.
   ```bash
   python main.py

#### ⚠️ Observação: Este projeto foi desenvolvido com propósito de estudo. Para adaptá-lo ao seu sistema, será necessário ajustar as coordenadas dos cliques e o fluxo da automação.
