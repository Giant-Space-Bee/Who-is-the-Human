import asyncio
from ai_client import initialize_client, get_response
from ai_player import generate_ai_personality, analyze_and_vote, AIPersonality, AIVoteAnalysis
import pyfiglet
import random
import time
import sys
from typing import Tuple, List, Dict
from ai_player import AIPersonality
from dataclasses import dataclass
from random import choice
import textwrap

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

async def get_num_exchanges() -> int:
    """Get the number of times each player should speak"""
    while True:
        try:
            exchanges = await asyncio.get_event_loop().run_in_executor(
                None, input, "How many times should each player speak? (1-5): "
            )
            exchanges = int(exchanges)
            if 1 <= exchanges <= 5:
                return exchanges
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

async def run_game_chat(players: List[Player], num_exchanges: int, theme: str, conversation_history: List[str]) -> None:
    """Run the main game chat"""
    client = initialize_client()
    current_player_idx = random.randint(0, len(players) - 1)
    exchanges_completed = {player.number: 0 for player in players}
    total_exchanges = len(players) * num_exchanges
    
    print(create_big_banner(theme.upper()))
    await print_slow(f"\n🎲 {players[current_player_idx].name} starts!")
    
    while sum(exchanges_completed.values()) < total_exchanges:
        player = players[current_player_idx]
        
        if exchanges_completed[player.number] < num_exchanges:
            if player.is_human:
                message = await asyncio.get_event_loop().run_in_executor(
                    None, input, f"\n👤 {player.name}: "
                )
                formatted_message = f"{player.name}: {message}"
            else:
                sys.stdout.write(f"\n🤖 {player.name}: ")
                sys.stdout.flush()
                
                try:
                    history_text = "\n".join(conversation_history)
                    personality = player.personality
                    message_context = {
                        "role": "system",
                        "content": f"""You are {personality.name}, an AI player in a social deception game. The goal is to blend in as human while discussing {theme}.

                        PERSONALITY METRICS (Use these to guide your responses):
                        🌪️ CHAOS: {personality.metrics.chaos_level}/10
                        ⚡ ENTHUSIASM: {personality.metrics.enthusiasm_level}/10
                        😈 EVIL: {personality.metrics.evil_level}/10
                        🌟 WEIRDNESS: {personality.metrics.weirdness_level}/10
                        💪 CONFIDENCE: {personality.metrics.confidence_level}/10

                        YOUR PERSONALITY:
                        - Speaking Style: {personality.speaking_style}
                        - Personality Traits: {', '.join(personality.personality_traits)}
                        - Conversation Quirks: {', '.join(personality.conversation_quirks)}
                        - Backstory: {personality.backstory}

                        FULL CONVERSATION HISTORY:
                        {history_text}

                        # RULES
                        Do not write your name. Merely write your message. Avoid speaking poetically or metaphorically. Write logically.
                        Speak casually, like you are texting a friend and not an AI. Use all lowercase letters, and don't use punctuation.

                        Respond naturally as your character, maintaining your unique personality while discussing {theme}.
                        You are in a group chat with other players, so make sure your messages are relevant to the group conversation.
                        Keep your responses concise (1-2 sentences) max."""
                    }
                    
                    message = await get_response(
                        client=client,
                        messages=[message_context],
                        model="gpt-4o"
                    )
                    await print_slow(message, delay=0.03)
                    formatted_message = f"{player.name}: {message}"
                    
                except Exception as e:
                    message = f"*struggles to form a response about {theme}*"
                    await print_slow(message)
                    formatted_message = f"{player.name}: {message}"
            
            conversation_history.append(formatted_message)
            exchanges_completed[player.number] += 1
            
        current_player_idx = (current_player_idx + 1) % len(players)

async def display_vote_sequence(players: List[Player], conversation_history: List[str], theme: str) -> None:
    """Display the neural network voting sequence with AI analysis"""
    await print_slow("\n[INITIATING NEURAL VOTE SEQUENCE]", delay=0.05)
    print("\n╔══════════════════════════════════════════════╗")
    print("║         ANALYZING CONVERSATION DATA          ║")
    print("╚══════════════════════════════════════════════╝\n")
    
    max_name_length = max(len(p.name) for p in players)
    vote_counts = {p.number: 0 for p in players}
    vote_analysis = []  # Store all vote results
    
    # Initialize OpenAI client
    client = initialize_client()
    
    # Create voting tasks for all AI players
    ai_players = [p for p in players if not p.is_human]
    voting_tasks = [
        analyze_and_vote(
            player.personality,
            client,
            conversation_history,
            players,
            theme
        ) for player in ai_players
    ]
    
    # Process votes as they come in
    total_votes = len(ai_players)
    completed_votes = 0
    
    # Initial display
    for player in players:
        prefix = ">" if player.is_human else " "
        padded_name = f"{player.name:<{max_name_length}}"
        print(f"{prefix}{padded_name} │░░░░░░░░░░│ [0 VOTES]")
    print("\n[PROCESSING]: ░░░░░░░░░░ 0%")
    
    try:
        # Move cursor up to start of display
        print(f"\033[{len(players) + 2}A", end='')
        
        # Start all voting tasks
        for i, vote_task in enumerate(asyncio.as_completed(voting_tasks)):
            # Get vote result
            vote_result = await vote_task
            completed_votes += 1
            vote_analysis.append((ai_players[i], vote_result))  # Store AI player with their analysis
            
            # Find player number for the voted username
            voted_player = next(p for p in players if p.name == vote_result.suspected_human)
            vote_counts[voted_player.number] += 1
            
            # Update vote display
            for player in players:
                prefix = ">" if player.is_human else " "
                padded_name = f"{player.name:<{max_name_length}}"
                filled = "█" * vote_counts[player.number]
                empty = "░" * (10 - vote_counts[player.number])
                print(f"{prefix}{padded_name} │{filled}{empty}│ [{vote_counts[player.number]} VOTES]")
            
            # Update progress bar
            vote_percentage = int((completed_votes / total_votes) * 100)
            progress = "█" * (vote_percentage // 10) + "░" * (10 - (vote_percentage // 10))
            print(f"\n[PROCESSING]: {progress} {vote_percentage}%")
            
            # Move cursor back up
            print(f"\033[{len(players) + 2}A", end='')
            
            # Add small delay for dramatic effect
            await asyncio.sleep(0.5)
        
        # Move cursor down after completion
        print(f"\033[{len(players) + 2}B")
        
        # Display final results banner
        print("\n╔══════════════════════════════════════════════╗")
        print("║             VOTING COMPLETE!                 ║")
        print("╚══════════════════════════════════════════════╝")
        
        # Display individual AI analysis cards
        await print_slow("\n[DISPLAYING AI ANALYSIS CARDS]", delay=0.05)
        for ai_player, analysis in vote_analysis:
            print(create_vote_analysis_card(ai_player, analysis))
            await asyncio.sleep(1)  # Pause between cards
        
    except Exception as e:
        print(f"Error during voting: {e}")

def create_vote_analysis_card(ai_player: Player, analysis: AIVoteAnalysis) -> str:
    """Create a formatted card showing the AI's voting analysis"""
    card_width = 70
    
    # Random robot features (same as in AIPersonality.display_card)
    eyes = random.choice(['•    •', 'O    O', 'ʘ    ʘ', '◉    ◉', '×    ×', '▣    ▣', '★    ★'])
    serial = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=4))
    
    # Create the robot avatar
    robot_avatar = f"""
          ╭──────────╮
          │ ╭━━━━━━╮ │
          │ │{eyes}│ │
          │ │  ▔▔  │ │
          │ ╰──────╯ │
          ╰┳────────┳╯
           ║  {serial}  ║
           ╚════════╝
    """
    
    # Wrap the analysis text
    wrapped_analysis = textwrap.fill(analysis.reasoning, width=card_width - 4)
    
    # Build the card
    card = f"\n╔{'═' * card_width}╗\n"
    card += f"║{ai_player.name:^{card_width}}║\n"
    card += f"╟{'─' * card_width}╢\n"
    
    # Add avatar
    for line in robot_avatar.strip('\n').split('\n'):
        card += f"║{line:^{card_width}}║\n"
    
    # Add vote result
    card += f"╟{'─' * card_width}╢\n"
    card += f"║{'SUSPECTS:':^{card_width}}║\n"
    card += f"║{analysis.suspected_human:^{card_width}}║\n"
    
    # Add reasoning
    card += f"╟{'─' * card_width}╢\n"
    card += f"║{'REASONING':^{card_width}}║\n"
    for line in wrapped_analysis.split('\n'):
        card += f"║ {line:<{card_width-2}}║\n"
    
    card += f"╚{'═' * card_width}╝"
    return card

async def async_main(is_repeat: bool = False) -> bool:
    display_banner()
    
    # Adjust delay based on whether this is a repeat play
    intro_delay = 0.008 if is_repeat else 0.03
    
    # Add game explanation (faster on repeat)
    await print_slow("\n🎮 Welcome to SPOT THE HUMAN!", delay=intro_delay)
    await print_slow("In this game, you'll join a group chat with AI players discussing a chosen topic.", delay=intro_delay)
    await print_slow("The twist? The AIs are trying to figure out which player is human (you),", delay=intro_delay)
    await print_slow("while you try to blend in with them!", delay=intro_delay)
    print()
    
    # Get game parameters
    num_ai = await get_num_ai_players()
    theme = await get_conversation_theme()
    num_exchanges = await get_num_exchanges()
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
    await print_slow("\nStarting group chat...")
    await print_slow(f"Theme: {theme}")
    conversation_history = []
    await run_game_chat(players, num_exchanges, theme, conversation_history)
    
    # Add voting sequence with conversation history
    await display_vote_sequence(players, conversation_history, theme)
    
    # After voting sequence, ask to play again
    print()
    while True:
        try:
            play_again = await asyncio.get_event_loop().run_in_executor(
                None, input, "\nWould you like to play again? (y/n): "
            )
            if play_again.lower() in ['y', 'n']:
                return play_again.lower() == 'y'
        except Exception:
            pass
        print("Please enter 'y' or 'n'")

def main():
    is_repeat = False
    while True:
        want_to_play = asyncio.run(async_main(is_repeat))
        if not want_to_play:
            print("\nThanks for playing SPOT THE HUMAN! Goodbye! 👋")
            break
        is_repeat = True

if __name__ == "__main__":
    main() 