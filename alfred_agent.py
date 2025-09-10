from smolagents import (
    CodeAgent,
    DuckDuckGoSearchTool,
    FinalAnswerTool,
    InferenceClientModel,
    Tool,
    tool,
    VisitWebpageTool,
)


@tool
def budget_calculator(guest_count: int, theme: str) -> str:
    """
    Calculates estimated party budget.

    Args:
        guest_count: Number of guests
        theme: Party theme for specific calculations
    """
    base_cost_per_person = 100
    theme_multipliers = {
        "casual": 0.8,
        "formal": 1.5,
        "villain masquerade": 2.0,
        "classic heroes": 2.0,
    }
    multiplier = theme_multipliers.get(theme.lower(), 1.0)
    total = guest_count * base_cost_per_person * multiplier

    return f"Estimated budget for {guest_count} guests: ${total:,.2f}"


@tool
def suggest_playlist(theme: str) -> str:
    """
    Suggests a themed playlist for parties.

    Args:
        theme: The party theme or mood
    """
    playlists = {
        "villain masquerade": [
            "Bad Guy - Billie Eilish",
            "Sweet Dreams - Eurythmics",
            "Imperial March - Star Wars",
            "Smooth Criminal - Michael Jackson",
            "Sympathy for the Devil - Rolling Stones",
        ],
        "classic heroes": [
            "Heroes - David Bowie",
            "Holding Out for a Hero - Bonnie Tyler",
            "Superman Theme - John Williams",
            "Fight Song - Rachel Platten",
        ],
    }
    return "\n".join(playlists.get(theme.lower(), ["No playlist found for this theme"]))


@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion: The type of occasion for the party.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."


@tool
def catering_service_tool(query: str) -> str:
    """
    This tool returns the highest-rated catering service in Gotham City.

    Args:
        query: A search term for finding catering services.
    """
    # Example list of catering services and their ratings
    services = {
        "Gotham Catering Co.": 4.9,
        "Wayne Manor Catering": 4.8,
        "Gotham City Events": 4.7,
    }

    # Find the highest rated catering service (simulating search query filtering)
    best_service = max(services, key=services.get)

    return best_service


class SuperheroPartyThemeTool(Tool):
    name = "superhero_party_theme_generator"
    description = """
    This tool suggests creative superhero-themed party ideas based on a category.
    It returns a unique party theme idea."""

    inputs = {
        "category": {
            "type": "string",
            "description": "The type of superhero party (e.g., 'classic heroes', 'villain masquerade', 'futuristic Gotham').",
        }
    }

    output_type = "string"

    def forward(self, category: str):
        themes = {
            "classic heroes": "Justice League Gala: Guests come dressed as their favorite DC heroes with themed cocktails like 'The Kryptonite Punch'.",
            "villain masquerade": "Gotham Rogues' Ball: A mysterious masquerade where guests dress as classic Batman villains.",
            "futuristic Gotham": "Neo-Gotham Night: A cyberpunk-style party inspired by Batman Beyond, with neon decorations and futuristic gadgets.",
        }

        return themes.get(
            category.lower(),
            "Themed party idea not found. Try 'classic heroes', 'villain masquerade', or 'futuristic Gotham'.",
        )


# Alfred, the butler, preparing the menu for the party
agent = CodeAgent(
    tools=[
        DuckDuckGoSearchTool(),
        VisitWebpageTool(),
        suggest_menu,
        suggest_playlist,  # New tool
        budget_calculator,  # New tool
        catering_service_tool,
        SuperheroPartyThemeTool(),
        FinalAnswerTool(),
    ],
    model=InferenceClientModel(),
    max_steps=10,
    verbosity_level=2,
)

# agent.run("Give me the best playlist for a party at the Wayne's mansion. The party idea is a 'villain masquerade' theme")
try:
    result = agent.run(
        "Give me the best playlist for a party at the Wayne's mansion. The party idea is a 'villain masquerade' theme"
    )
    print(result)
except Exception as e:
    print(f"I apologize, Master Wayne. There seems to be an error: {str(e)}")
