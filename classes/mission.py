class Mission:
    def __init__(self, mission_name: str, target_location: str):
        self.mission_name = mission_name
        self.target_location = target_location
        self.agent = None


    def add_agent(self, agent) -> None:
        self.agent = agent


    def brief(self) -> None:
        print(f'Mission: {self.mission_name} Target: {self.target_location} Agent: {self.agent.code_name}')