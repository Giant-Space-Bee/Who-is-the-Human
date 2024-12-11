<img width="596" alt="image" src="https://github.com/user-attachments/assets/89b55303-5edd-44b5-90af-1ac5d3384a7a">

# 🎮 POOCS: The Human - Web Edition

Welcome to the next evolution of social deception! POOCS (originally "Find the Human") is a thrilling game where AI players with distinct personalities try to unmask the human among them. Now reimagined for the web, featuring real-time interaction and a beautiful terminal interface!

## 🌟 Game Overview

Dive into a world where AI personalities engage in witty banter, strategic deception, and clever detective work. As the human player, your mission is to blend in with these quirky AI characters, each equipped with:

- 🤖 **Unique Personalities**: From chaotic jokesters to analytical masterminds
- 🎭 **Detection Strategies**: Each AI has its own method of spotting human behavior
- 💭 **Conversation Styles**: Watch as AIs adapt their language to match their personality
- 🎲 **Dynamic Voting**: Real-time analysis of conversation patterns
- ⚡ **WebSocket Magic**: Instant responses and seamless interaction

## 🚀 Project Structure

```
poocs-web/
├── backend/           # FastAPI backend
│   ├── src/          # Python source code
│   │   ├── game/     # Core game logic
│   │   └── ws/       # WebSocket handlers
│   └── tests/        # Backend tests
└── frontend/         # React frontend
    ├── src/          # TypeScript source code
    ├── components/   # React components
    └── pages/        # Game interface pages
```

## 🛠️ Tech Stack

### Backend Magic
- 🚄 **FastAPI**: Lightning-fast Python web framework
- 🔌 **WebSockets**: Real-time bidirectional communication
- 🧠 **OpenAI GPT-4**: Powers our witty AI personalities
- 🐳 **Docker**: Containerized for easy deployment

### Frontend Delight
- ⚛️ **React + TypeScript**: Rock-solid web interface
- 📟 **xterm.js**: Beautiful terminal emulation
- ⚡ **Vite**: Lightning-fast build tooling
- 🎨 **Modern UI**: Sleek, responsive design

## 🎯 Features

- **Real-time Chat**: Engage in natural conversations with AI players
- **Terminal Interface**: Classic ASCII charm meets modern web tech
- **Personality Engine**: Each AI has unique traits that influence their behavior:
  - Chaos Level: Affects response unpredictability
  - Intelligence: Influences detection accuracy
  - Humor: Determines wit and joke frequency
  - Suspicion: Affects voting behavior
- **Dynamic Voting**: Watch as AIs analyze and cast their votes in real-time
- **Game History**: Track your success rate at fooling the AIs

## 🏃‍♂️ Getting Started

### Prerequisites
- 🐳 Docker and Docker Compose
- 📦 Node.js 20+ (for local development)
- 🐍 Python 3.12+ (for local development)
- 🔑 OpenAI API key

### Quick Start

1. Clone your way to fun:
```bash
git clone https://github.com/yourusername/poocs-web.git
cd poocs-web
```

2. Launch the experience:
```bash
docker compose up
```

3. Jump in:
- 🎮 Game Interface: http://localhost:3001
- 🎛️ API: http://localhost:3000
- 📚 API Docs: http://localhost:3000/docs

## 🎲 How to Play

1. **Enter the Arena**: Join a game room and meet your AI companions
2. **Blend In**: Participate in themed conversations while maintaining your cover
3. **Stay Sharp**: Watch for AI behavioral patterns and adapt your strategy
4. **Face Judgment**: Experience the tension as AIs cast their votes
5. **Victory or Learning**: Celebrate fooling the AIs or learn from their detection

## 📝 Original Game

Love terminal-based gaming? Check out the original version in the [poocs_game](./poocs_game) directory!

## 🤝 Contributing

Got ideas? We'd love to hear them! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests
- 🎨 Improve the UI/UX

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🌟 Coming Soon

- 🏆 Global Leaderboards
- 👥 Multiple Human Players
- 🎭 Custom AI Personality Creation
- 🎨 Theme Customization
- 🤖 AI Personality Marketplace
