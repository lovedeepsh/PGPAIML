# Interactive Storytelling with ChatGPT – Course-end Project 1

Simplilearn Generative AI Literacy | Purdue University

## Contents

| File | Description |
|------|-------------|
| `generative_ai_literacy_project1` | Project problem statement and steps |
| **`interactive_storytelling.py`** | **Code for submission** – runnable script that uses OpenAI API for interactive storytelling |
| `interactive_storytelling_guide.ipynb` | Guide with example prompts and checklist (optional) |
| `requirements.txt` | Python dependencies |
| `README.md` | This file |

## Objective

Use ChatGPT to co-create an interactive story: define theme and characters, drive the plot with your inputs, explore branching paths, and bring the narrative to a conclusion.

## Code for submission

**Submit the file `interactive_storytelling.py`** when the portal asks for code. It implements the interactive storytelling project using the OpenAI API (ChatGPT).

## How to run the code

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your OpenAI API key** (get one at https://platform.openai.com):
   ```bash
   export OPENAI_API_KEY='your-key-here'
   ```

3. **Run the script:**
   ```bash
   python interactive_storytelling.py
   ```

4. Enter theme (e.g. fantasy, mystery) and character when prompted, then type your choices each turn. Type `end` to finish.

## How to complete the project (for submission)

1. Read the problem statement in `generative_ai_literacy_project1`.
2. Run `interactive_storytelling.py` (or use ChatGPT manually) to build your story.
3. **Submit** `interactive_storytelling.py` as your **code**. Optionally submit your story transcript or summary as well.

## What the code does

1. Asks for story theme and character.
2. Calls the OpenAI API to generate an opening scene and 2–3 choices.
3. You type your choice (or describe an action); the script sends it to the API and prints the next part of the story and new choices.
4. Repeats until you type `end`.
