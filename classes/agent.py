class Agent:
    total_agents = 0

    def __init__(self, code_name: str, clearance_level: int) -> None:
        Agent.total_agents += 1
        self.code_name = code_name
        self._clearance_level = clearance_level


    def report(self) -> None:
        print(f'Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}')


    @property
    def clearance_level(self) -> int:
        return self._clearance_level


    @clearance_level.setter
    def clearance_level(self, level) -> None:
        if 1 < level < 10:
            self._clearance_level = level
        else:
            print(f'clearance_level can be 1 < level < 10 only.')

    @staticmethod
    def get_total_agent():
        print(f'total agent: {Agent.total_agents}')


    @staticmethod
    def print_agents_report(agents: list[Agent]) -> None:
        for agent in agents:
            agent.report()