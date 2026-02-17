# Simulação do Experimento de Fenda Dupla de Young

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Pygame](https://img.shields.io/badge/library-pygame--ce-green.svg)
![Pygame GUI](https://img.shields.io/badge/library-pygame--gui-orange.svg)
![NumPy](https://img.shields.io/badge/math-NumPy-lightblue.svg)

</div>

Uma simulação física interativa e visualmente precisa do **Experimento da Fenda Dupla de Thomas Young**, desenvolvida em Python. 

O projeto utiliza processamento vetorial com NumPy para renderizar padrões de difração e interferência da luz em tempo real, , permitindo que estudantes e entusiastas explorem os princípios da óptica ondulatória.

--- 

## 📸 O Projeto em Ação

<div align="center">
   
  <img src="https://github.com/user-attachments/assets/218168ef-de0d-403f-bd58-ea12e244d631" alt="Padrão Azul" width="920"/>

  <br>

  <br>
  
  <img src="https://github.com/user-attachments/assets/59b03368-d5db-4d7e-86ee-882f9431c70c" alt="Padrão Amarelo" width="920"/>
  
</div>

---

## ✨ Funcionalidades

* **Simulação Física:** Combina Difração de Fraunhofer (Fenda Única) com Interferência de Young (Fenda Dupla).
* **Renderização em Tempo Real:** Visualização instantânea do gráfico de intensidade com marcadores visuais que indicam as posições.
* **Controles Interativos:** Ajuste dinâmico de todos os parâmetros físicos via Sliders e Inputs:
    * **Comprimento de Onda ($\lambda$):** 380nm a 780nm (com conversão para cores RGB).
    * **Distância entre Fendas ($d$):** Ajuste em micrômetros ($\mu m$).
    * **Largura da Fenda ($a$):** Controle do envelope de difração.
    * **Distância do Anteparo ($L$):** Afaste ou aproxime a tela de projeção.
* **Zoom Dinâmico:** Ajuste da área total observada na tela em centímetros, permitindo análises macro ou micro do fenômeno.

## 🚀 Instalação e Execução

### Pré-requisitos
* Python 3.10 ou superior.

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/LucasJSM/young-experiment.git
    ```

2.  **Crie e ative um ambiente virtual (Recomendado):**
    * Windows:
        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        ```
    * Linux/Mac:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a simulação:**
    ```bash
    python main.py
    ```

## 🛠️ Tecnologias Utilizadas

* **[Python 3](https://www.python.org/):** Linguagem base.
* **[Pygame CE](https://pyga.me/):** Motor gráfico para renderização da janela e primitivas visuais.
* **[Pygame GUI](https://pygame-gui.readthedocs.io/):** Gerenciamento de interface (sliders e inputs).
* **[NumPy](https://numpy.org/):** Cálculos vetoriais de alta performance para processar a intensidade de luz em milhares de pixels simultaneamente.

## 📂 Estrutura do Projeto

O projeto segue o padrão arquitetural **MVC (Model-View-Controller)** para separar a lógica física da interface gráfica.

```text
young-experiment/
├── assets/
│   └── fonts/              # Tipografia customizada (ex: Roboto)
├── src/
│   ├── core/
│   │   └── app.py          # Gerenciador do Game Loop (Controller)
│   ├── model/
│   │   ├── experiment_state.py  # Estado global e parâmetros físicos
│   │   └── young_engine.py      # Motor matemático
│   ├── view/
│   │   ├── renderer.py     # Desenho do gráfico, anteparo e HUD
│   │   ├── ui_manager.py   # Gerenciador de Sliders e Inputs (Pygame GUI)
│   │   └── colors.py       # Conversor Espectral (Lambda -> RGB)
│   └── utils/
│       └── math_conversions.py  # Conversores de escalas e unidades
├── theme.json              # Configuração visual da interface
└── main.py
```

## 🧠 Física do Projeto
A intensidade $I$ da luz em um ponto $x$ do anteparo é calculada pela combinação de dois fenômenos ondulatórios.

A distância teórica entre dois máximos principais consecutivos é dada por:

$$\Delta y = \frac{\lambda L}{d}$$

### Interferência (Fenda Dupla):

$$I_{interf} = \cos^2\left(\frac{\pi d x}{\lambda L}\right)$$

### Difração (Fenda Única - Envelope):

$$I_{difr} = \text{sinc}^2\left(\frac{\pi a x}{\lambda L}\right)$$

Onde:
- $\lambda$: Comprimento de onda.
- $L$: Distância das fendas ao anteparo.
- $d$: Distância entre os centros das fendas.
- $a$: Largura de cada fenda.

## 👥 Autores
- Luca Zoio
- Lucas Moura

## 📄 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](https://github.com/LucasJSM/young-experiment/blob/main/LICENSE) para mais detalhes.
