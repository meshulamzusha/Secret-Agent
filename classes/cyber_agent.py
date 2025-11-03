from classes.agent import Agent


class CyberAgent(Agent):
    def __init__(self, code_name: str, clearance_level: int, specialty: str):
        super().__init__(code_name, clearance_level)
        self.specialty = specialty


    def report(self) -> None:
        print(f'Agent {self.code_name} with specialty of {self.specialty} reporting. Clearance Level: {self._clearance_level}')