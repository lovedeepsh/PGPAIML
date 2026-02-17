"""
Interactive Storytelling with ChatGPT – Course-end Project 1
Simplilearn Generative AI Literacy | Purdue University

This script implements an interactive storytelling adventure using the OpenAI API
(ChatGPT). Run it and provide your choices; the AI continues the narrative.
Set your API key in environment: OPENAI_API_KEY
"""

import os

# Use OpenAI API (ChatGPT). Install: pip install openai
try:
    from openai import OpenAI
except ImportError:
    print("Install the openai package: pip install openai")
    exit(1)


def get_client():
    """Create OpenAI client using API key from environment."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Set OPENAI_API_KEY in your environment to run this script.")
        print("Example (terminal): export OPENAI_API_KEY='your-key-here'")
        return None
    return OpenAI(api_key=api_key)


SYSTEM_PROMPT = """You are a collaborative storyteller. The user is co-creating an interactive story with you.
- You are the narrator. After each of your responses, offer exactly 2-3 clear choices (numbered) for what the user's character can do next.
- Keep responses engaging but concise (a few short paragraphs per turn).
- Adapt to the user's theme, characters, and choices. Continue the story based on their input."""


def run_story(client, theme="fantasy", character_brief="a brave traveler"):
    """
    Run an interactive storytelling session.
    theme: genre (e.g. fantasy, science fiction, mystery)
    character_brief: short description of the user's character
    """
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"Start an interactive {theme} story. The main character is {character_brief}. "
            "Write a short opening scene (2-3 paragraphs) and then give me 2-3 numbered choices for what to do next.",
        },
    ]

    print("\n--- Interactive Story ---\n")
    turn = 0
    while True:
        # Get AI response
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=500,
        )
        assistant_message = response.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_message})

        print(assistant_message)
        turn += 1

        # User choice
        print("\n---")
        user_input = input("Your choice (number or describe action), or 'end' to finish: ").strip()
        if not user_input or user_input.lower() == "end":
            print("\nStory session ended.")
            break

        messages.append(
            {"role": "user", "content": user_input + "\nContinue the story and give me 2-3 choices again."}
        )


def main():
    client = get_client()
    if not client:
        return

    print("Interactive Storytelling – Project 1")
    print("Theme (e.g. fantasy, science fiction, mystery) [fantasy]: ", end="")
    theme = input().strip() or "fantasy"
    print("Your character in one short phrase (e.g. 'a brave traveler') [a brave traveler]: ", end="")
    character_brief = input().strip() or "a brave traveler"

    run_story(client, theme=theme, character_brief=character_brief)


if __name__ == "__main__":
    main()
