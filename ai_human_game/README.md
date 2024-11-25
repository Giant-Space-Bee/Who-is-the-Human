# 🤖 Spot the Human

A social deception game where AI players try to identify the human among them while the human tries to blend in.

## 🎮 Game Overview

"Spot the Human" is an engaging social deception game that puts a twist on the classic "spot the bot" concept. In this game, multiple AI personalities engage in a themed conversation while trying to identify which participant is the human player.

## ✨ Features

- **Dynamic AI Personalities**: Each AI player has unique traits, quirks, and strategies
- **Custom Themes**: Choose any conversation topic for the game
- **Async Generation**: AI profiles are generated in parallel with Matrix-style animation
- **Visual Elements**:
  - Matrix-style loading animations
  - Colorful round banners
  - AI thinking indicators
  - Custom ASCII robot avatars
  - Themed game banners
  - Player cards with personality details
- **Interactive Chat**: Turn-based conversation system with:
  - Random starting player
  - Personality-driven AI responses
  - Conversation history tracking
  - Visual turn indicators
  - Emoji reactions

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai_human_game.git
cd ai_human_game
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'  # On Windows: set OPENAI_API_KEY=your-api-key-here
```

### Running the Game

```bash
python src/main.py
```

## 🎯 How to Play

1. **Setup**:
   - Choose the number of AI players (2-10)
   - Select a conversation theme
   - Choose number of chat rounds (1-5)
   - Enter your username

2. **Generation Phase**:
   - Watch the Matrix-style animation while AI personalities are created
   - Each AI gets unique traits, strategies, and conversation styles
   - Review each AI's personality card

3. **Chat Phase**:
   - Random player starts the conversation
   - Take turns discussing the chosen theme
   - AI players respond based on their personalities
   - Try to blend in or spot the human!

## 🤖 AI Personalities

Each AI player features:
- Unique personality traits
- Custom speaking style
- Specific strategies for human detection
- Deception tactics
- Conversation quirks
- Favorite topics
- Things they avoid

## 🎨 Visual Design

The game features:
- Matrix-style banner
- Typewriter text effects
- Custom ASCII robot avatars
- Formatted player cards
- Color-coded elements

## 🛠️ Technical Details

- Built with Python 3.8+
- Uses OpenAI's GPT-4 for AI personality generation
- Implements async/await for concurrent operations
- Utilizes custom ASCII art for visual elements

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🙏 Acknowledgments

- OpenAI for the GPT-4 API
- The Python community for async support
- ASCII art community for inspiration

## 📬 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/ai_human_game](https://github.com/yourusername/ai_human_game)
