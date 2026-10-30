class Agent:
    def __init__(self, name,codename, level):
        self.name = name
        self.codename = codename
        self.level = level
    def introduce(self):
        print(F"my name is:{self.name},my codename is: {self.codename},my level is:{self.level}")

agent_2 = Agent("Shadow", "BYTE", 2)
agent_3 = Agent("Sad", "Red", 3)
agent_4 = Agent("Pixel", "Pink", 4)
agent_2.level  = 5

agent_2.introduce()
agent_3.introduce()
agent_4.introduce()

agents = [agent_2.codename, agent_3.codename, agent_4.codename]
print(agents)