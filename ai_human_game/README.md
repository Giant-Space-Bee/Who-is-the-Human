# 🤖 Spot the Human

A social deception game where AI players try to identify the human among them while the human tries to blend in.

## ✨ Latest Features

- **AI-Driven Voting**: Each AI now analyzes the conversation using their unique personality and detection strategy
- **Parallel Processing**: All AI votes are processed simultaneously for faster results
- **Personality-Based Analysis**: AIs use their traits and quirks to inform their voting decisions
- **Real-time Vote Display**: Watch as each AI's analysis comes in and updates the vote count
- **Detailed Reasoning**: (Debug mode) See each AI's thought process for their vote
- **Faster Replay**: Quicker intro sequence when replaying the game
- **Improved Chat System**: AI responses now influenced by personality metrics:
  - Chaos Level (1-10): Affects response randomness
  - Enthusiasm Level (1-10): Influences energy in responses
  - Evil Level (1-10): Determines mischievousness
  - Weirdness Level (1-10): Controls quirky behavior
  - Confidence Level (1-10): Affects assertiveness

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
- **Interactive Chat**: Continuous conversation system with:
  - Random starting player
  - Personality-driven AI responses
  - Natural conversation flow
  - Visual turn indicators
  - Emoji reactions
  - Exchange tracking
- **Neural Network Voting**: End-game voting sequence with:
  - Real-time vote processing
  - AI-driven analysis of conversation
  - Visual vote tracking
  - Cyberpunk-style interface
  - Parallel vote processing

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
   - Set how many times each player should speak (1-5)
   - Enter your username

2. **Generation Phase**:
   - Watch as unique AI personalities are created
   - Each AI gets:
     - Random personality metrics
     - Custom detection strategy
     - Unique speaking style
     - Conversation quirks

3. **Chat Phase**:
   - Discuss the chosen theme in a continuous group chat
   - Each player (including you) speaks a set number of times
   - AI responses are influenced by their personality metrics
   - Try to blend in with natural conversation flow!

4. **Voting Phase**:
   - Each AI runs a detailed conversation analysis
   - Votes are processed in parallel
   - Watch real-time vote counting
   - See which AIs suspected you
   - Option to play again with faster intro!

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
