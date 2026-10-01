# Janelas em Python com Tkinter

O Tkinter é a biblioteca padrão do Python para a criação de interfaces gráficas (GUI). Para criar e manipular janelas de forma eficiente, existem diversos recursos de configuração, dimensionamento e controle.[^1][^2]

Este guia reúne dicas práticas para gerenciar janelas no Tkinter.

## 1. Inicialização básica

Toda aplicação Tkinter precisa de uma janela principal e do loop de eventos para permanecer aberta.[^3][^4]

```python
import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Minha Aplicação")

# Mantém a janela aberta (deve ser a última linha)
janela.mainloop()
```

## 2. Controle de tamanho e dimensões

### Definir o tamanho inicial

Use o método `geometry("larguraxaltura")`:

```python
janela.geometry("600x400")
```

### Bloquear o redimensionamento

Para impedir que o usuário altere o tamanho da janela, use `resizable()` com valores booleanos:

```python
janela.resizable(False, False)  # Trava completamente o tamanho
```

### Iniciar maximizada

Para abrir a janela ocupando a tela inteira:

```python
janela.state("zoomed")
```

### Definir limites de tamanho

Defina os tamanhos mínimo e máximo permitidos:[^5][^6][^7]

```python
janela.minsize(400, 300)
janela.maxsize(800, 600)
```

## 3. Centralizar a janela na tela

Por padrão, o Tkinter abre a janela no canto superior esquerdo. Use este cálculo para centralizá-la em qualquer monitor:

```python
largura = 500
altura = 400

# Obtém as dimensões da tela do usuário
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calcula as posições X e Y para o centro
pos_x = int((largura_tela / 2) - (largura / 2))
pos_y = int((altura_tela / 2) - (altura / 2))

# Aplica a geometria final
janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
```

## 4. Criar múltiplas janelas (pop-ups)

Para abrir uma nova janela, como uma tela de login ou configurações, use o widget `Toplevel`. Não crie uma segunda janela usando `tk.Tk()`, pois isso pode causar problemas no ciclo de eventos do programa.[^8]

```python
def abrir_nova_janela():
    nova_janela = tk.Toplevel(janela)
    nova_janela.title("Janela Secundária")
    nova_janela.geometry("300x200")


botao = tk.Button(janela, text="Abrir Subtela", command=abrir_nova_janela)
botao.pack()
```

## 5. Estética e comportamento avançado

### Mudar a cor de fundo

Use o método `configure(bg=...)`:

```python
janela.configure(bg="#2c3e50")  # Aceita nomes em inglês ou hexadecimal
```

### Alterar o ícone da janela

No Windows, o arquivo precisa estar no formato `.ico`:

```python
janela.iconbitmap("caminho_do_seu_icone.ico")
```

### Manter a janela sempre no topo

Força a janela a ficar acima dos outros programas:

```python
janela.attributes("-topmost", True)
```

### Definir a transparência

Altera a opacidade da janela. O valor `0.0` torna a janela totalmente invisível, enquanto `1.0` a mantém totalmente opaca.[^7][^9]

```python
janela.attributes("-alpha", 0.85)
```

## Alternativa: CustomTkinter

Se você deseja criar interfaces com um visual mais moderno, incluindo suporte simples a modo escuro, pesquise também sobre o [CustomTkinter][^10][^11].

## Referências

[^1]: [Tutorial no YouTube](https://www.youtube.com/watch?v=yHdZvQhSRiA)
[^2]: [Tkinter: interfaces gráficas em Python - DevMedia](https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956)
[^3]: [Tutorial no YouTube](https://www.youtube.com/watch?v=-vk1hE8KPtM)
[^4]: [Artigo da DIO](https://www.dio.me/articles/simplifique-e-interaja-transformando-programas-python-com-tkinter)
[^5]: [Tutorial no YouTube](https://www.youtube.com/watch?v=p5EmG_75fws)
[^6]: [Tutorial Tkinter - Python GUIs](https://translate.google.com/translate?u=https://www.pythonguis.com/tutorials/create-gui-tkinter/&hl=pt&sl=en&tl=pt&client=sge)
[^7]: [Tkinter Window - Python Tutorial](https://translate.google.com/translate?u=https://www.pythontutorial.net/tkinter/tkinter-window/&hl=pt&sl=en&tl=pt&client=sge)
[^8]: [Como abrir uma nova janela com um botão - GeeksforGeeks](https://www.geeksforgeeks.org/python/open-a-new-window-with-a-button-in-python-tkinter/)
[^9]: [Tutorial no YouTube](https://www.youtube.com/watch?v=1H5-vVnw5p8&t=482)
[^10]: [Tkinter no Python - Hashtag Treinamentos](https://www.hashtagtreinamentos.com/tkinter-no-python)
[^11]: [Login com CustomTkinter - Hashtag Treinamentos](https://www.hashtagtreinamentos.com/login-com-customtkinter-python)
