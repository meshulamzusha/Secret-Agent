from classes.agent import Agent
from classes.cyber_agent import CyberAgent
from classes.field_agent import FieldAgent
from classes.mission import Mission

if __name__ == '__main__':
    cyber = CyberAgent('rachel', 2, 'hacking')
    field = FieldAgent('kodcode', 3, 'north')

    mission1 = Mission('Incense cloud', 'aiosh')
    mission1.add_agent(field)

    mission1.brief()

    Agent.print_agents_report([cyber, field])