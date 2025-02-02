from abc import ABC, abstractmethod

# Abstract Base Class for Agent Configuration
class AbstractAgentConfigurator(ABC):
    @abstractmethod
    def configure_agent(self):
        pass

# Abstract Base Class for Simulation Stages
class AbstractSimulationStage(ABC):
    @abstractmethod
    def execute_stage(self):
        pass