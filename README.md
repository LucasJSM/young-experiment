# Simulação do Experimento de Fenda Dupla de Young

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Pygame](https://img.shields.io/badge/library-pygame-green.svg)

</div>

Uma simulação física interativa e visualmente precisa do **Experimento da Fenda Dupla de Young**, desenvolvida em Python. O projeto utiliza NumPy para renderizar padrões de interferência e difração de luz em tempo real, permitindo que estudantes e entusiastas explorem os princípios da óptica ondulatória.


## ✨ Funcionalidades

* **Simulação Física:** Combina Difração de Fraunhofer (Fenda Única) com Interferência de Young (Fenda Dupla).
* **Renderização em Tempo Real:** Visualização instantânea do gráfico de intensidade.
* **Controles Interativos:** Ajuste dinâmico de todos os parâmetros físicos via Sliders:
    * **Comprimento de Onda ($\lambda$):** 380nm a 780nm (com cor RGB fiel).
    * **Distância entre Fendas ($d$):** Ajuste em micrômetros ($\mu m$).
    * **Largura da Fenda ($a$):** Controle do envelope de difração.
    * **Distância do Anteparo ($L$):** Afaste ou aproxime a tela de projeção.
* **Zoom Dinâmico:** Altere o campo de visão para analisar detalhes centrais ou o padrão expandido.

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
* **[NumPy](https://numpy.org/):** Cálculos vetoriais de alta performance para processar a intensidade de luz em milhares de pixels simultaneamente.
* **[Pygame GUI](https://pygame-gui.readthedocs.io/):** Gerenciamento de interface (sliders).

## 📂 Estrutura do Projeto

O projeto segue o padrão arquitetural **MVC (Model-View-Controller)** para separar a lógica física da interface gráfica.

```text
young-experiment/
├── main.py
└── src/
    ├── core/
    │   └── app.py          # Gerenciador do Game Loop (Controller)
    ├── model/
    │   ├── experiment_state.py  # Dataclass com parâmetros físicos
    │   └── young_engine.py      # Motor matemático
    ├── view/
    │   ├── renderer.py     # Desenha o gráfico e o padrão de luz
    │   ├── ui_manager.py   # Gerencia Sliders e Inputs
    │   └── colors.py       # Conversão do Comprimento de Onda -> RGB
    └── utils/
        └── math_conversions.py # Conversões de unidades
```

## 🧠 Física do Projeto
A intensidade $I$ em um ponto $x$ da tela é calculada combinando dois fenômenos:

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
