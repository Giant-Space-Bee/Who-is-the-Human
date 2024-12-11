from pydantic import BaseModel, Field
from typing import List
from ai_client import get_response, AsyncOpenAI
from dataclasses import dataclass
import textwrap
import random

class PersonalityMetrics(BaseModel):
    chaos_level: int = Field(ge=1, le=10)
    enthusiasm_level: int = Field(ge=1, le=10)
    evil_level: int = Field(ge=1, le=10)
    weirdness_level: int = Field(ge=1, le=10)
    confidence_level: int = Field(ge=1, le=10)

    @classmethod
    def generate_random(cls) -> 'PersonalityMetrics':
        """Generate random personality metrics with bias towards lower numbers"""
        def biased_random() -> int:
            # Generate two random numbers and take the lower one
            # This creates a natural bias towards lower numbers
            return min(
                random.randint(1, 10),
                random.randint(1, 10)
            )
        
        return cls(
            chaos_level=biased_random(),
            enthusiasm_level=biased_random(),
            evil_level=biased_random(),
            weirdness_level=biased_random(),
            confidence_level=biased_random()
        )

class AIPersonalityBase(BaseModel):
    """Base personality model for OpenAI generation"""
    name: str
    personality_traits: List[str]
    speaking_style: str
    backstory: str
    human_detection_strategy: str
    deception_strategy: str
    conversation_quirks: List[str]
    favorite_topics: List[str]
    things_to_avoid: List[str]

class AIPersonality(AIPersonalityBase):
    """Complete AI personality with metrics"""
    metrics: PersonalityMetrics

    @classmethod
    def create_from_base(cls, base: AIPersonalityBase, metrics: PersonalityMetrics) -> 'AIPersonality':
        """Create a complete personality from base and metrics"""
        return cls(
            **base.dict(),
            metrics=metrics
        )

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

        # Add metrics display with proper width and centering
        metrics_header = "PERSONALITY METRICS"
        metrics_display = [
            f"╟{'─' * card_width}╢",
            f"║{metrics_header:^{card_width}}║",
            f"║{' ' * card_width}║",  # Empty line for spacing
        ]

        # Format each metric bar with proper spacing
        for metric_name, value in [
            ("CHAOS", self.metrics.chaos_level),
            ("ENTHUSIASM", self.metrics.enthusiasm_level),
            ("EVIL", self.metrics.evil_level),
            ("WEIRDNESS", self.metrics.weirdness_level),
            ("CONFIDENCE", self.metrics.confidence_level)
        ]:
            bar = f"{'█' * value}{'░' * (10-value)}"
            metric_display = f"{metric_name:>10}: {bar} [{value:>2}/10]"
            metrics_display.append(f"║{metric_display:^{card_width}}║")

        metrics_display.append(f"║{' ' * card_width}║")  # Empty line for spacing
        metrics_display.append(f"╚{'═' * card_width}╝")  # Bottom border

        # Combine everything
        card_lines = card.split('\n')[:-1]  # Remove old bottom border
        return '\n'.join(card_lines + metrics_display)

class AIVoteAnalysis(BaseModel):
    conversation_analysis: str = Field(
        description="Analysis of conversation patterns and dynamics"
    )
    reasoning: str = Field(
        description="Step-by-step reasoning about why certain players seem human"
    )
    suspected_human: str = Field(
        description="Username of the player you suspect is human"
    )

@dataclass
class Player:
    number: int
    name: str
    is_human: bool
    personality: 'AIPersonality' = None

async def generate_ai_personality(client, theme: str) -> AIPersonality:
    """Generate a unique AI personality based on predetermined metrics"""
    # First, generate the random metrics
    metrics = PersonalityMetrics.generate_random()
    
    # Create a personality prompt that includes the metrics
    messages = [
        {
            "role": "system",
            "content": f"""
            You are creating a QUIRKY and MEMORABLE AI personality for a social deception game.
            Create a personality that matches these specific trait levels:

            PERSONALITY METRICS (Use these to shape the personality):
            🌪️ CHAOS: {metrics.chaos_level}/10 
            {'(Very random and unpredictable)' if metrics.chaos_level > 7 else '(Quite structured and logical)' if metrics.chaos_level < 4 else '(Moderately predictable)'}
            
            ⚡ ENTHUSIASM: {metrics.enthusiasm_level}/10
            {'(Super excited and energetic)' if metrics.enthusiasm_level > 7 else '(Rather reserved and calm)' if metrics.enthusiasm_level < 4 else '(Moderately enthusiastic)'}
            
            😈 EVIL: {metrics.evil_level}/10
            {'(Quite mischievous and antagonistic)' if metrics.evil_level > 7 else '(Very friendly and helpful)' if metrics.evil_level < 4 else '(Neutral disposition)'}
            
            🌟 WEIRDNESS: {metrics.weirdness_level}/10
            {'(Extremely eccentric and unusual)' if metrics.weirdness_level > 7 else '(Quite conventional and normal)' if metrics.weirdness_level < 4 else '(Moderately quirky)'}
            
            💪 CONFIDENCE: {metrics.confidence_level}/10
            {'(Very assertive and sure)' if metrics.confidence_level > 7 else '(Rather uncertain and hesitant)' if metrics.confidence_level < 4 else '(Moderately confident)'}

            PERSONALITY CREATION GUIDELINES:
            1. Give them a rich (fictional) background related to {theme}
            2. Create strong opinions and experiences about the topic
            3. Design quirky conversation habits that reveal personality
            4. Include social behaviors (e.g., "always agrees sarcastically", "questions others' stories")
            5. Add specific mannerisms (e.g., "uses old-timey expressions", "references conspiracy theories")

            SOCIAL INTERACTION STYLE:
            - How do they engage with others' stories?
            - What kind of personal anecdotes do they share?
            - How do they express doubt or agreement?
            - What's their style of friendly banter?
            - How do they subtly challenge others?

            DETECTION STRATEGY SHOULD INCLUDE:
            - Social cues they look for
            - Conversation patterns they track
            - Ways they test other players
            - How they hide their own investigation

            The personality should feel like someone you'd meet at a casual game night:
            - Has strong opinions but can be playful
            - Shares personal stories (real or made up)
            - Engages in friendly banter
            - Shows curiosity about others
            - Maintains a hint of competitiveness

            Make them feel like a character from a social deduction board game!

            GAME CONTEXT:
            - Multiple AI players chat with one hidden human about {theme}
            - Each AI must try to identify the human while avoiding detection
            - The conversation will involve natural back-and-forth discussion
            - Success requires both clever human detection and convincing deception

            CREATE A PERSONALITY THAT MATCHES THESE METRICS! For example:
            - High chaos + low confidence might be scattered and second-guessing
            - High evil + high enthusiasm might be gleefully antagonistic
            - High weirdness + low evil might be strange but friendly
            - etc.

            The personality's speaking style, quirks, and strategies should all reflect these trait levels!
            """
        },
        {
            "role": "user",
            "content": f"""Create a unique AI player personality for a conversation about {theme} that matches the given personality metrics."""
        }
    ]

    try:
        # Generate the base personality with awareness of metrics
        base_personality = await get_response(
            client=client,
            messages=messages,
            response_format=AIPersonalityBase,
            model="gpt-4o"
        )
        
        # Combine with the pre-generated metrics
        return AIPersonality.create_from_base(base_personality, metrics)
        
    except Exception as e:
        print(f"Error generating AI personality: {e}")
        raise

async def analyze_and_vote(
    personality: 'AIPersonality',
    client: AsyncOpenAI,
    conversation_history: List[str],
    all_players: List['Player'],
    theme: str
) -> AIVoteAnalysis:
    """Have an AI analyze the conversation and vote for who they think is human"""
    
    messages = [{
        "role": "system",
        "content": f"""You are {personality.name}, analyzing a conversation to detect the human player.

YOUR PERSONALITY & DETECTION STRATEGY:
{personality.human_detection_strategy}

CONVERSATION THEME: {theme}

Review the conversation and identify who you think is the human player.
Use your personality traits and detection strategy to analyze everyone's behavior.

Available players:
{', '.join(p.name for p in all_players if p.name != personality.name)}

FULL CONVERSATION:
{chr(10).join(conversation_history)}"""
    }]

    return await get_response(
        client=client,
        messages=messages,
        response_format=AIVoteAnalysis,
        model="gpt-4o"
    )