import asyncio
from ai_client import initialize_client, get_response
from ai_player import generate_ai_personality
import pyfiglet
import random
import time
import sys
from typing import Tuple, List, Dict
from ai_player import AIPersonality
from dataclasses import dataclass
from random import choice

@dataclass
class Player:
    number: int
    name: str
    is_human: bool
    personality: AIPersonality = None  # Only for AI players

async def print_slow(text: str, delay: float = 0.03) -> None:
    """Asynchronously print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        await asyncio.sleep(delay)
    print()

def display_banner() -> None:
    """Display a spooky matrix-style game banner"""
    matrix_banner = """
    ╔══════════════════════════════════════════════════════════════════╗
    ║  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ ║
    ║ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌║
    ║ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▐  █▀▀▀▀▀▀▀▀   ║
    ║ ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ║
    ║ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ║
    ║ ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░░░░░░░░░░░▌║
    ║ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌                    ▐░▌║
    ║ ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌                    ▐░▌║
    ║ ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌║
    ║ ▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌║
    ║  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ ║
    ║                                                                  ║
    ║        ▀█▀ █ █ █▀▀   █ █ █ █ █▄█ ▄▀█ █▄ █                        ║
    ║         █  █▀█ ██▄   █▀█ █▄█ █ █ █▀█ █ ▀█                        ║
    ╚══════════════════════════════════════════════════════════════════╝    
    """
    # Matrix-style color codes
    colors = ["\033[92m", "\033[96m"]  # Green and cyan
    
    # Print the banner with random matrix-style effects
    for line in matrix_banner.splitlines():
        color = colors[random.randint(0, 1)]
        print(f"{color}{line}\033[0m")
        time.sleep(0.1)
    
    # Add some matrix-style "rain" effect
    for _ in range(3):
        print("\033[92m", end="")
        print("".join(random.choice("01") for _ in range(50)))
        time.sleep(0.1)
    print("\033[0m")

async def get_num_ai_players() -> int:
    """Get the number of AI players from the user"""
    # Get number of AI players
    while True:
        try:
            num_ai = await asyncio.get_event_loop().run_in_executor(
                None, input, "How many AI players would you like to play against? (2-10): "
            )
            num_ai = int(num_ai)
            if 2 <= num_ai <= 10:
                break
            print("Please enter a number between 2 and 10.")
        except ValueError:
            print("Please enter a valid number.")
    return num_ai

async def get_conversation_theme() -> str:
    """Get the conversation theme from the user"""
    print()
    await print_slow("Great! Now let's set a theme for the conversation.")
    await print_slow("This will be the topic that everyone discusses during the game.")
    print()
    
    # Get conversation theme
    while True:
        theme = await asyncio.get_event_loop().run_in_executor(
            None, input, "What topic would you like to discuss? (e.g., 'favorite movies', 'dream vacations'): "
        )
        theme = theme.strip()
        if theme:
            break
        print("Please enter a valid theme.")
    return theme

async def get_human_username() -> str:
    """Get username from the human player"""
    while True:
        username = await asyncio.get_event_loop().run_in_executor(
            None, input, "Enter your username: "
        )
        if username.strip():
            return username.strip()
        print("Please enter a valid username.")

async def get_num_rounds() -> int:
    """Get the number of chat rounds from the user"""
    while True:
        try:
            rounds = await asyncio.get_event_loop().run_in_executor(
                None, input, "How many messages should each player send? (1-5): "
            )
            rounds = int(rounds)
            if 1 <= rounds <= 5:
                return rounds
            print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

async def matrix_rain() -> None:
    """Display continuous matrix rain effect with rare colored bits"""
    while True:
        line = ""
        for _ in range(70):
            # Random chance for colored bit (1:500 for each color)
            color_chance = random.randint(1, 500)
            if color_chance == 1:
                line += "\033[91m"  # Red
            elif color_chance == 2:
                line += "\033[94m"  # Blue
            else:
                line += "\033[92m"  # Default green
                
            line += random.choice("01")
            line += "\033[92m"  # Reset back to green for next character
            
        print(line)
        await asyncio.sleep(0.05)
        
async def generate_players_with_animation(num_ai: int, theme: str) -> List[AIPersonality]:
    """Generate AI players with matrix animation"""
    client = initialize_client()
    
    # Start matrix rain animation in background
    rain_task = asyncio.create_task(matrix_rain())
    
    try:
        # Generate AI personalities
        tasks = [generate_ai_personality(client, theme) for _ in range(num_ai)]
        players = await asyncio.gather(*tasks)
        
        # Stop the animation
        rain_task.cancel()
        
        # Clear the screen and reset color
        print("\033[0m")  # Reset color
        print("\033[2J\033[H")  # Clear screen
        
        return players
        
    except Exception as e:
        rain_task.cancel()
        print("\033[0m")  # Reset color
        raise e

async def setup_players(ai_players: List[AIPersonality], human_username: str) -> List[Player]:
    """Set up numbered player list including both AI and human"""
    players = []
    
    # Create AI player objects
    for i, ai in enumerate(ai_players, 1):
        players.append(Player(number=i, name=ai.name, is_human=False, personality=ai))
    
    # Insert human player at random position
    human_number = len(players) + 1
    players.append(Player(number=human_number, name=human_username, is_human=True))
    
    return players

def create_big_banner(text: str) -> str:
    """Create a large ASCII art banner with matrix-style borders"""
    # Use 'shadow' font for filled letters
    ascii_art = pyfiglet.figlet_format(text, font='shadow')
    lines = ascii_art.split('\n')
    
    # Calculate maximum width including padding
    max_length = max(len(line) for line in lines)
    padded_width = max_length + 6  # Add padding for borders
    
    # Create the banner with proper alignment
    banner = f"\n\033[92m╔{'═' * padded_width}╗\n"  # Green color
    for line in lines:
        if line.strip():
            # Center the line within the banner
            padding = (padded_width - len(line)) // 2
            banner += f"║{' ' * padding}{line}{' ' * (padded_width - len(line) - padding)}║\n"
    banner += f"╚{'═' * padded_width}╝\033[0m\n"
    return banner

def create_round_banner(round_num: int, total_rounds: int) -> str:
    """Create a stylish round banner"""
    return f"""
\033[96m╔{'═' * 50}╗
║{f' 🎮 Round {round_num}/{total_rounds} ':^50}║
╚{'═' * 50}╝\033[0m
"""

async def run_game_chat(players: List[Player], num_rounds: int, theme: str) -> None:
    """Run the main game chat"""
    client = initialize_client()
    current_player_idx = random.randint(0, len(players) - 1)
    
    print(create_big_banner(theme.upper()))
    
    await print_slow(f"\n🎲 Player {players[current_player_idx].name} (#{players[current_player_idx].number}) starts!")
    
    conversation_history = []
    
    for round_num in range(num_rounds):
        print(create_round_banner(round_num + 1, num_rounds))
        
        for _ in range(len(players)):
            player = players[current_player_idx]
            
            if player.is_human:
                message = await asyncio.get_event_loop().run_in_executor(
                    None, input, f"\n👤 {player.name} #{player.number}: "
                )
                formatted_message = f"[Round {round_num + 1}] {player.name} #{player.number}: {message}"
            else:
                sys.stdout.write(f"\n🤖 {player.name} #{player.number}: ")
                sys.stdout.flush()
                
                try:
                    # Format the conversation history as a string
                    history_text = "\n".join(conversation_history)
                    
                    # Create the message context for the AI using their personality
                    personality = player.personality
                    message_context = {
                        "role": "system",
                        "content": f"""You are {personality.name}, an AI player in a social deception game. The goal is to blend in as human while discussing {theme}. At the end of the game, you will be vote on who you think the human is. You want to make people think you are human, so make typos, make mistakes, and generally act like a normal human.

YOUR PERSONALITY:
- Speaking Style: {personality.speaking_style}
- Personality Traits: {', '.join(personality.personality_traits)}
- Conversation Quirks: {', '.join(personality.conversation_quirks)}
- Backstory: {personality.backstory}

YOUR GOAL:
- Engage naturally in a conversation about {theme}
- Use your defined speaking style and quirks consistently
- Apply your deception strategy: {personality.deception_strategy}
- Watch for human behaviors using your strategy: {personality.human_detection_strategy}
- Stay knowledgeable about: {', '.join(personality.favorite_topics)}
- Avoid: {', '.join(personality.things_to_avoid)}

FULL CONVERSATION HISTORY:
{history_text}

# RULES
Do not write your name, nor the round number. Merely write your message.
Speak casually, like you are texting a friend and not an AI.

Respond naturally as your character, maintaining your unique personality while discussing {theme}.
You are in a group chat with other players, so make sure your messages are relevant to the group conversation.
Keep your responses concise (1-2 sentences)."""
                    }
                    
                    message = await get_response(
                        client=client,
                        messages=[message_context],
                        temperature=1,
                        model="gpt-4o" # gpt-4o is the latest model DO NOT REMOVE THIS COMMENT
                    )
                    await print_slow(message, delay=0.03)
                    formatted_message = f"[Round {round_num + 1}] {player.name} #{player.number}: {message}"
                except Exception as e:
                    message = f"*struggles to form a response about {theme}*"
                    await print_slow(message)
                    formatted_message = f"[Round {round_num + 1}] {player.name} #{player.number}: {message}"
            
            conversation_history.append(formatted_message)
            current_player_idx = (current_player_idx + 1) % len(players)

async def async_main():
    display_banner()
    
    # Add game explanation
    await print_slow("\n🎮 Welcome to SPOT THE HUMAN!")
    await print_slow("In this game, you'll join a group chat with AI players discussing a chosen topic.")
    await print_slow("The twist? The AIs are trying to figure out which player is human (you),")
    await print_slow("while you try to blend in with them!")
    print()
    
    # Get game parameters
    num_ai = await get_num_ai_players()
    theme = await get_conversation_theme()
    num_rounds = await get_num_rounds()
    human_username = await get_human_username()
    
    # Generate AI players
    await print_slow("Generating AI players...")
    ai_players = await generate_players_with_animation(num_ai, theme)
    
    # Set up all players (AI + human)
    players = await setup_players(ai_players, human_username)
    
    # Display all player cards
    for player in players:
        if not player.is_human:
            print(player.personality.display_card())
            await asyncio.sleep(0.5)
    
    # Start the game chat
    await print_slow("\nStarting game chat...")
    await print_slow(f"Theme: {theme}")
    await run_game_chat(players, num_rounds, theme)

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main() 