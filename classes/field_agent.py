from classes.agent import Agent


class FieldAgent(Agent):
    def __init__(self, code_name: str, clearance_level: int, region: str):
        super().__init__(code_name, clearance_level)
        self.region = region


    def report(self) -> None:
        print(f'Agent {self.code_name} from {self.region} reporting. Clearance Level: {self._clearance_level}')



