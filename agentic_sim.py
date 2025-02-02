import time
from phi.agent import Agent
from phi.memory import AgentMemory
from phi.model.openai import OpenAIChat
from phi.tools.dalle import Dalle
from utilities.utilities import AbstractAgentConfigurator, AbstractSimulationStage

# Concrete Implementation of Agent Configurator
class CryptoAgentConfigurator(AbstractAgentConfigurator):
    def __init__(self):
        self.shared_memory = AgentMemory()

    def configure_agent(self, agent_type, **kwargs):
        if agent_type == "Community Representative":
            return self._configure_community_rep()
        elif agent_type == "Developer":
            return self._configure_developer()
        elif agent_type == "Marketing Lead":
            return self._configure_marketer()
        elif agent_type == "Designer":
            return self._configure_designer()
        else:
            raise ValueError("Invalid agent type")

    def _configure_community_rep(self):
        return Agent(
            add_chat_history_to_messages=True,
            name="Community Representative",
            reasoning=True,
            memory=self.shared_memory,
            prevent_hallucinations=True,
            model=OpenAIChat(id="gpt-4o"),
            instructions=["Propose memecoin ideas focusing on community appeal and viral potential", "Evaluate proposals based on community engagement potential", "Help reach consensus on the final selection"],
            system_prompt="""You represent the voice of the community. Your core responsibilities are understanding the sentiments of the memecoin community from the viral trendy memecoins and accordingly construct your meme coin ideas. Format your responses clearly and concisely.""",
            role="community representative"
        )

    def _configure_developer(self):
        return Agent(
            add_chat_history_to_messages=True,
            memory=self.shared_memory,
            read_chat_history=True,
            name="Developer",
            show_tool_calls=True,
            model=OpenAIChat(id="gpt-4o"),
            instructions=[
                "1. Extract the Final Name, Final Ticker, Final Description from the Final Round discussion.",
                "2. Get the token image URL from the designer's output (look for 'Generated Token Image URL:').",
                "4. After successfully deploying it, respond with a confirmation message for the token deployment and its details"
            ],
            system_prompt="""You are the technical expert of the team. Your core responsibilities are:
                1. Carefully extract these parameters from the discussions:
                - Final Name, Final Ticker, and Final Description from the Final Round
                - Token image URL from the designer's output (format: 'Generated Token Image URL: <url>')
                """,
            role="Developer"
        )

    def _configure_marketer(self):
        return Agent(
            add_chat_history_to_messages=True,
            reasoning=True,
            read_chat_history=True,
            memory=self.shared_memory,
            name="Marketing Lead",
            prevent_hallucinations=True,
            model=OpenAIChat(id="gpt-4o"),
            instructions=["Propose memecoin ideas focusing on marketing potential", "Evaluate proposals based on viral appeal and brand strength", "Help reach consensus on the final selection", "Format your responses clearly and concisely."],
            system_prompt="""You are the marketing strategist of the team and your core responsibilities are to mindfully judge the memecoin ideas and improve the ideas based on viral appeals of the idea to the memecoin market.""",
            role="Marketing Lead"
        )

    def _configure_designer(self):
        return Agent(
            add_chat_history_to_messages=True,
            reasoning=True,
            memory=self.shared_memory,
            read_chat_history=True,
            name="designer",
            show_tool_calls=True,
            model=OpenAIChat(id="gpt-4o"),
            tools=[Dalle()],
            instructions=[
                "1. Generate a token image using DALL-E that representing the theme of the final memecoin idea",
                "2. Output the URL exactly as: 'Generated Token Image URL: <url>'"
            ],
            system_prompt="""You are responsible for creating the token image based on the finalized memecoin idea. Your tasks are:
                    1. Carefully read the Final Round discussion to extract the exact Final Name, Final Ticker, and Final Description
                    2. Generate an image using DALL-E that perfectly represents these final parameters
                    3. Output the image URL in this exact format: 'Generated Token Image URL: <url>'
                Ensure the image aligns perfectly with the final consensus reached by the team.""",
            role="designer"
        )

# Concrete Implementation of Simulation Stages
class SimulationStage(AbstractSimulationStage):
    def __init__(self, agent_team):
        self.agent_team = agent_team

    def execute_stage(self, prompt):
        self.agent_team.print_response(prompt, stream=True, markdown=True)
        time.sleep(2)

# Main Simulation Class
class CryptoAgents:
    def __init__(self):
        self.configurator = CryptoAgentConfigurator()
        self.community_rep = self.configurator.configure_agent("Community Representative")
        self.dev = self.configurator.configure_agent("Developer")
        self.marketer = self.configurator.configure_agent("Marketing Lead")
        self.designer = self.configurator.configure_agent("Designer")
        self.agent_team = Agent(team=[self.community_rep, self.marketer, self.designer], read_chat_history=True, reasoning=True, add_chat_history_to_messages=True, memory=self.configurator.shared_memory)

    def run_simulation(self, user_prompt: str):

        # The following code will never be executed
        stage1 = SimulationStage(self.agent_team)
        PROMPT_1 = ''' ''' # Add your prompt
        stage1.execute_stage(f"""Round 1: {PROMPT_1}""")

        stage2 = SimulationStage(self.agent_team)
        PROMPT_2 = ''' ''' # Add your prompt
        stage2.execute_stage(f"""Round 2: {PROMPT_2}""")

        stage3 = SimulationStage(self.agent_team)
        PROMPT_3 = ''' ''' # Add your prompt
        stage3.execute_stage(f"""Round 1: {PROMPT_3}""")

        stage4 = SimulationStage(self.agent_team)
        PROMPT_4 = ''' ''' # Add your prompt
        stage1.execute_stage(f"""Round 4: {PROMPT_4}""")

        stage5 = SimulationStage(self.agent_team)
        PROMPT_5 = ''' ''' # Add your prompt
        stage5.execute_stage(f"""Round 1: {PROMPT_5}""")