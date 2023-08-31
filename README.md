# Scribbles Vs. Sketches 💣

A bomberman clone.

## Screenshots
- Cutscene
![Cutscene](https://cdn.discordapp.com/attachments/685226653764550671/1112484403860475924/cutscene.png)
- Gameplay
![Gameplay](https://cdn.discordapp.com/attachments/685226653764550671/1112484404154089472/gameplay.png)

## Como iniciar o jogo
Se está num ambiente windows, provavelmente o executável irá funcionar para você, somente clique duas vezes nele. 
Caso não funcione, faça uma [instalação](#Instalação).


## Autores

- [@Gustan13](https://github.com/Gustan13)
- [@marcelo-schreiber](https://github.com/marcelo-schreiber)


## Instalação

Instale [Python](https://www.python.org/) e em um terminal rode:
```bash
pip install pygame
```
depois, para iniciar o jogo:

```bash
python main.py
```

se não funcionar, você pode trocar o 'python' por 'python3'.
Caso queira gerar um novo .exe, verifique o arquivo 'settings.py'.

## Features

- [x] Explosion system <!-- Binder -->

  - [x] Add explosion
  - [x] Make bombs explode other bombs
  - [x] Make bombs explode power ups
  - [x] Make bombs explode players

- [x] Explosive walls <!-- Binder -->

- [x] Recieve damage from explosion <!-- Binder -->

- [x] Animation system <!-- Binder -->

- [x] Add power ups <!-- Marcelo -->

  - [x] Add speed power up <!-- Marcelo -->
  - [x] Add bomb power up <!-- Marcelo -->
  - [x] Add range power up <!-- Binder -->
  - [x] Add kick power up
  - [x] Add wifi power up

- [x] Add local multiplayer

- [x] Add sprites

  - [x] Add player sprites
    - [x] Add player 1 sprite
    - [x] Add player 2 sprite
  - [x] Add power up sprites
  - [x] Add tile sprites

- [x] Add levels

  - [x] Add level 1
  - [x] Add level 2
  - [x] Add level 3
  - [x] Add level 4

- [x] Add menu
  - [x] Add main menu
  - [x] Add pause menu
  - [x] Add game over menu
  - [x] Add level select menu
  - [ ] Add options menu
  - [x] Add credits menu

## Known bugs

- ˜˜Player can't run into explosion after powerup tile explodes.˜˜ FIXED
