# 🎲 PyDice - Simple PySide6 Dice Roller

![Demo Screenshot](app/resource/assets/icon.png) 

*A lightweight, fun dice-rolling application built with Python and PySide6.*



## ✨ Features

- **Single or Double Roll**: Roll one die or two dice with a click.
- **Randomized Outcomes**: Fair 1-6 values per die.
- **Sleek GUI**: Minimalist and intuitive interface.
- **Sound Effects**: Dice roll sound for added immersion.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- [PySide6](https://pypi.org/project/PySide6/)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/AmbitiousFlowDev/PyDice.git
   cd PyDice
   ```
2. **Install dependencies:**
   ```sh
   pip install PySide6
   ```

### Running the Game

```sh
python main.py
# or
py main.py
```

## 🗂️ Project Structure

```
.
├── main.py
├── app/
│   ├── app.py
│   ├── controller/
│   │   └── DiceController.py
│   ├── resource/
│   │   ├── resources.py
│   │   ├── resources.qrc
│   │   └── assets/
│   │       ├── diceGreenAlt1.png
│   │       ├── diceGreenAlt2.png
│   │       ├── diceGreenAlt3.png
│   │       ├── diceGreenAlt4.png
│   │       ├── diceGreenAlt5.png
│   │       ├── diceGreenAlt6.png
│   │       ├── icon.png
│   │       └── roll.wav
│   ├── ui/
│   │   └── MainWindow.py
│   └── views/
│       └── MainWindow.ui
├── compile.ps1
├── run.bat
├── pysidedeploy.spec
├── README.md
├── LICENSE.md
└── .gitignore
```

## 📜 License

This project is licensed under the **GNU GPL-3.0**—see [LICENSE.md](LICENSE.md) for details.

## 🤝 Contributing

- **Issues**: Report bugs or suggest features [here](https://github.com/AmbitiousFlowDev/dice-roller/issues).
- **Pull Requests**: Welcome! Fork, improve, and submit.

## 💡 Why I Built This

A fun weekend project to explore PySide6 and share a simple, nostalgic dice game.

*Crafted with ♥ by AmbitiousFlowDev*
