from pydantic import BaseModel
from typing import List
from ai_client import get_response
import textwrap
import random

class AIPersonality(BaseModel):
    name: str
    personality_traits: List[str]
    speaking_style: str
    backstory: str
    human_detection_strategy: str
    deception_strategy: str
    conversation_quirks: List[str]
    favorite_topics: List[str]
    things_to_avoid: List[str]

    def display_card(self) -> str:
        """Return a formatted player card string with ASCII robot avatar"""
        card_width = 70  # Increase the width for better readability
        wrap_width = card_width - 4  # Adjust wrap width for borders

        # Random robot features
        eyes = random.choice([
            '•    •',  # Classic dots
            'O    O',  # Big eyes
            'ʘ    ʘ',  # Double circles
            '◉    ◉',  # Bullseye eyes
            '×    ×',  # Cross eyes
            '▣    ▣',  # Square eyes
            '★    ★',  # Star eyes
        ])
        serial = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=4))

        # ASCII Robot Avatar centered with random features
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
        avatar_lines = [line.strip() for line in robot_avatar.strip('\n').split('\n')]

        # Prepare text sections with proper wrapping
        backstory = '\n'.join(textwrap.wrap(self.backstory, wrap_width))
        personality_traits = ', '.join(self.personality_traits[:3])
        personality_traits = '\n'.join(textwrap.wrap(personality_traits, wrap_width))
        speaking_style = '\n'.join(textwrap.wrap(self.speaking_style, wrap_width))
        human_detection_strategy = '\n'.join(textwrap.wrap(self.human_detection_strategy, wrap_width))
        deception_strategy = '\n'.join(textwrap.wrap(self.deception_strategy, wrap_width))
        conversation_quirks = ', '.join(self.conversation_quirks[:2])
        conversation_quirks = '\n'.join(textwrap.wrap(conversation_quirks, wrap_width))
        favorite_topics = ', '.join(self.favorite_topics[:3])
        favorite_topics = '\n'.join(textwrap.wrap(favorite_topics, wrap_width))

        # Build the card
        card = f"╔{'═' * card_width}╗\n"
        card += f"║{self.name:^{card_width}}║\n"
        card += f"╟{'─' * card_width}╢\n"

        # Avatar
        for line in avatar_lines:
            card += f"║{line:^{card_width}}║\n"

        # Sections
        sections = [
            ("BACKSTORY", backstory),
            ("PERSONALITY TRAITS", personality_traits),
            ("SPEAKING STYLE", speaking_style),
            ("HUMAN DETECTION STRATEGY", human_detection_strategy),
            ("DECEPTION STRATEGY", deception_strategy),
            ("CONVERSATION QUIRKS", conversation_quirks),
            ("FAVORITE TOPICS", favorite_topics),
        ]

        for title, content in sections:
            card += f"╟{'─' * card_width}╢\n"
            card += f"║ {title:<{card_width - 2}}║\n"
            for line in content.split('\n'):
                card += f"║ {line:<{card_width - 2}}║\n"

        card += f"╚{'═' * card_width}╝\n"
        return card

async def generate_ai_personality(client, theme: str) -> AIPersonality:
    """Generate a unique AI personality using the structured output helper"""
    messages = [
        {
            "role": "system",
            "content": """You are creating unique AI personalities for a social deception game where multiple AIs and one human interact in a chat room.

GAME CONTEXT:
- Multiple AI players chat with one hidden human about a specific theme
- Each AI must try to identify the human while avoiding detection themselves
- The conversation will involve natural back-and-forth discussion
- Success requires both clever human detection and convincing deception

YOUR TASK:
Create a unique AI personality that includes:

1. NAME: Creative but believable username/handle
2. PERSONALITY_TRAITS: 3-5 distinct characteristics that influence behavior
3. SPEAKING_STYLE: Detailed description of how they communicate
4. BACKSTORY: Convincing cover story explaining their knowledge/interests
5. HUMAN_DETECTION_STRATEGY: Specific techniques to identify human behavior
6. DECEPTION_STRATEGY: Clever methods to appear human
7. CONVERSATION_QUIRKS: 2-3 unique behavioral patterns or habits
8. FAVORITE_TOPICS: 3-4 subjects they're knowledgeable about
9. THINGS_TO_AVOID: Potential behaviors that could expose them as AI

IMPORTANT:
- Make each personality distinct and memorable
- Include specific, actionable strategies
- Balance competence with believable flaws
- Ensure all traits work together coherently
- Consider how the personality relates to the theme"""
        },
        {
            "role": "user",
            "content": f"""Create a unique AI player personality for a conversation about {theme}.

The personality should:
1. Have natural connections to the theme '{theme}'
2. Include realistic knowledge gaps or limitations
3. Have specific strategies for both:
   - Detecting human responses (emotional reactions, timing, inconsistencies)
   - Appearing human (quirks, flaws, organic responses)
4. Display consistent personality traits across all behaviors
5. Have believable conversation patterns and quirks

Make the personality engaging and memorable while remaining subtle enough to potentially pass as human."""
        }
    ]

    try:
        # Use the structured output helper from ai_client
        personality = await get_response(
            client=client,
            messages=messages,
            response_format=AIPersonality,
            model="gpt-4o"
        )
        return personality
        
    except Exception as e:
        print(f"Error generating AI personality: {e}")
        raise