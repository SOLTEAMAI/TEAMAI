# SOLTEAMAI

**Your Own Custom Solana AI Agents**

Deploy autonomous AI agents to revolutionize your Solana trading and token creation. From idea generation and image creation to market analysis, token deployment, and community engagement, our intelligent agents work 24/7 to optimize your crypto operations while maintaining full compliance and security.

---

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Quick Start](#quick-start)
  - [Running the Simulation](#running-the-simulation)
  - [Example Code](#example-code)
- [Project Structure](#project-structure)
- [Concepts and Architecture](#concepts-and-architecture)
  - [Agent Collaboration](#agent-collaboration)
  - [Function Calling](#function-calling)
- [Customization and Extension](#customization-and-extension)
  - [Adding New Agents](#adding-new-agents)
  - [Integrating External APIs](#integrating-external-apis)
- [API Reference](#api-reference)
  - [Agent Classes](#agent-classes)
  - [Utility Functions](#utility-functions)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Features

- **Intelligent Token Creation**: Advanced AI and automated protocols allow agents to brainstorm token ideas and deploy them as a team.
- **Advanced AI Connections**: Real-time integrations with the latest AI models like OpenAI GPT-4 and DALL·E for idea generation and image creation.
- **Open Source AI Framework**: An open-source framework to include in your workflows, working with various endpoints like Pump.fun.
- **Agent Collaboration**: AI agents can chat with each other to discuss ideas, create images, deploy tokens, post on social media, and more.
- **Plug & Play**: Set up our AI agents in under 5 minutes. Simple, free, open-source AI products with cryptocurrency capabilities.

---

## Getting Started

### Prerequisites

- **Python 3.8 or higher**
- **Pip** (Package Installer for Python)
- **OpenAI API Key**: Required for GPT-4 and DALL·E integrations.
- **Solana Wallet**: For deploying tokens to the Solana blockchain.
- **Rust and Solana CLI**: Required for Solana development.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/SOLTEAMAI.git
   cd SOLTEAMAI
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**

   Create a `.env` file in the project root directory and add your API keys:

   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   SOLANA_PRIVATE_KEY=your_solana_private_key_here
   ```

---

## Usage

### Quick Start

To quickly get started with SOLTEAMAI, follow these steps:

1. **Start the FastAPI Server**

   ```bash
   uvicorn main:app --reload
   ```

2. **Access the Web Interface**

   Open your browser and navigate to `http://127.0.0.1:8000/`.

3. **Provide Inspiration**

   Enter a memecoin idea or any inspiration text for the AI agents to work with.

4. **Run the Simulation**

   Click on the "Run Simulation" button to start the agents' autonomous discussions and token creation process.

5. **View the Results**

   The agents will display outputs at each step, including brainstorming sessions, refined ideas, the final token image, and deployment confirmation.

### Running the Simulation

You can also run the simulation directly using the `CryptoAgents` class.

```python
from agentic_sim import CryptoAgents

# Create an instance of the CryptoAgents class
agents = CryptoAgents()

# Run the simulation with a user-provided inspiration
user_inspiration = "A memecoin inspired by space exploration and alien life."
async for output in agents.run_simulation(user_inspiration):
    print(output)
```

### Example Code

Below is an example of how you can interact with the agents programmatically.

```python
import asyncio
from agentic_sim import CryptoAgents

async def main():
    # Initialize the agents
    agents = CryptoAgents()

    # User's inspiration for the memecoin
    user_inspiration = "Create a memecoin based on the latest viral cat meme."

    # Run the simulation and print outputs
    async for output in agents.run_simulation(user_inspiration):
        print(output)

# Run the main function
asyncio.run(main())
```

---

## Project Structure

- **`agentic_sim.py`**: Contains the `CryptoAgents` class that defines all AI agents involved in the simulation.
- **`createtoken.py`**: Functions to save token images and deploy tokens on the Solana blockchain.
- **`main.py`**: The FastAPI application that serves the web interface and API endpoints.
- **`templates/`**: HTML templates for the web interface.
- **`static/`**: Static files like CSS and JavaScript.
- **`requirements.txt`**: List of required Python packages.

---

## Concepts and Architecture

### Agent Collaboration

The framework is designed around multiple AI agents, each with a specific role:

- **Community Representative**: Focuses on community appeal and viral potential.
- **Marketing Lead**: Evaluates marketing potential, viral appeal, and brand strength.
- **Designer**: Generates token images based on the final memecoin idea using DALL·E.
- **Developer**: Deploys the token on the Solana blockchain using the provided parameters.

These agents communicate and collaborate to brainstorm ideas, refine them, and execute token creation and deployment.

### Function Calling

Agents can utilize function calling capabilities to interact with external APIs and tools. For example:

- The **Designer** uses the DALL·E API to generate images.
- The **Developer** calls the `deploy_token` function to deploy the token on Solana.

---

## Customization and Extension

### Adding New Agents

You can extend the framework by adding new agents with custom roles and behaviors.

```python
from phi.agent import Agent

class AnalystAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Market Analyst",
            reasoning=True,
            memory=self.shared_memory,
            prevent_hallucinations=True,
            model=OpenAIChat(id="gpt-4"),
            instructions=["Analyze market trends for meme tokens", "Provide insights and recommendations"],
            system_prompt="You provide detailed market analysis for crypto tokens.",
            role="market analyst"
        )
```

Add the new agent to the simulation:

```python
agents = CryptoAgents()
agents.idea_gen_team.team.append(AnalystAgent())
```

### Integrating External APIs

To integrate external APIs or tools, you can define new functions and include them in an agent's tools.

```python
from phi.tools import Tool

def sentiment_analysis(text):
    # Implement your sentiment analysis logic here
    return "Positive"

# Define the tool
sentiment_tool = Tool(
    name="SentimentAnalysis",
    func=sentiment_analysis,
    description="Analyzes the sentiment of the given text."
)

# Add the tool to an agent
agents.community_rep.tools.append(sentiment_tool)
```

---

## API Reference

### Agent Classes

#### `CryptoAgents`

**Description**: Configures agentic behavior and runs the simulation.

**Initialization**:

```python
agents = CryptoAgents()
```

**Methods**:

- `run_simulation(user_prompt: str)`: Runs the simulation based on the user's input.

  **Parameters**:

  - `user_prompt (str)`: The initial inspiration or idea provided by the user.

  **Returns**:

  - An asynchronous generator yielding outputs from each step of the simulation.

**Agents**:

- `community_rep`: Represents the voice of the community.
- `marketer`: Focuses on marketing strategies.
- `designer`: Generates token images using DALL·E.
- `dev`: Deploys the token on the Solana blockchain.

### Utility Functions

#### `save_token_image(url: str)`

**Description**: Downloads an image from a given URL and saves it locally.

**Parameters**:

- `url (str)`: The URL of the image to download.

**Returns**:

- `Path`: The path to the saved image file.

**Usage**:

```python
from createtoken import save_token_image

image_path = save_token_image("https://example.com/image.png")
```

#### `deploy_token(token_image_url: str, fin_name: str, fin_ticker: str, fin_description: str, twitter_post_text: str)`

**Description**: Deploys a token on the Solana blockchain with the provided metadata.

**Parameters**:

- `token_image_url (str)`: URL of the token image.
- `fin_name (str)`: Final token name.
- `fin_ticker (str)`: Final ticker symbol.
- `fin_description (str)`: Description of the token.
- `twitter_post_text (str)`: Twitter post text promoting the token.

**Usage**:

```python
from createtoken import deploy_token

deploy_token(
    token_image_url="https://example.com/token_image.png",
    fin_name="SpaceCat",
    fin_ticker="SCAT",
    fin_description="A memecoin inspired by space-loving cats.",
    twitter_post_text="Join the #SpaceCat revolution! To the moon!"
)
```

---

## Contributing

We welcome contributions from the community. Please follow these steps:

1. **Fork the Repository**

   Click on the "Fork" button at the top right of the repository page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/yourusername/SOLTEAMAI.git
   cd SOLTEAMAI
   ```

3. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

4. **Make Changes**

   Implement your feature or bug fix.

5. **Commit Changes**

   ```bash
   git commit -am 'Add new feature'
   ```

6. **Push to Your Fork**

   ```bash
   git push origin feature/YourFeature
   ```

7. **Create a Pull Request**

   Go to the original repository and click on "New Pull Request". Provide a clear description of your changes.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- **OpenAI GPT-4**: For language understanding and generation capabilities.
- **DALL·E**: For image generation.
- **Pump.fun**: For token deployment endpoints.
- **Solana Blockchain**: The blockchain platform used for deploying tokens.

