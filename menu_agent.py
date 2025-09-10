# from huggingface_hub import login

# login()

from smolagents import CodeAgent, tool, InferenceClientModel


@tool
def get_menu_recommendations(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
        Args:
            occasion (str): The type of occasion for the party. Allowed values are:
                            - "casual": Menu for casual party.
                            - "formal": Menu for formal party.
                            - "superhero": Menu for superhero party.
                            - "custom": Custom menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."


# Alfred, the butler, suggests a menu based on the occasion.
agent = CodeAgent(tools=[get_menu_recommendations], model=InferenceClientModel())
agent.run("Suggest a menu for a superhero-themed party.")
