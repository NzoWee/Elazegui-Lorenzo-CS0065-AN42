import agentpy as ap
import random
import matplotlib.pyplot as plt


class RandomWalker(ap.Agent):

    def setup(self):
        self.path = [self.position]

    def move(self, occupied):
        x, y = self.position

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        possible_positions = []

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            if (0 <= new_x < self.model.p.grid_size[0] and
                    0 <= new_y < self.model.p.grid_size[1]):

                new_position = (new_x, new_y)

                if new_position not in occupied:
                    possible_positions.append(new_position)

        if possible_positions:
            self.position = random.choice(possible_positions)

        self.path.append(self.position)


class RandomWalkModel(ap.Model):

    def setup(self):
        self.agents = ap.AgentList(
            self,
            self.p.agents,
            RandomWalker
        )

        available_positions = [
            (x, y)
            for x in range(self.p.grid_size[0])
            for y in range(self.p.grid_size[1])
        ]

        random.shuffle(available_positions)

        for agent in self.agents:
            agent.position = available_positions.pop()
            agent.path = [agent.position]

    def step(self):
        occupied = {
            agent.position
            for agent in self.agents
        }

        agents = list(self.agents)
        random.shuffle(agents)

        for agent in agents:
            occupied.discard(agent.position)
            agent.move(occupied)
            occupied.add(agent.position)


def run_simulation(num_agents, grid_size, num_steps):

    parameters = {
        'agents': num_agents,
        'grid_size': (grid_size, grid_size),
        'steps': num_steps
    }

    model = RandomWalkModel(parameters)
    model.setup()

    for step in range(num_steps):
        model.step()

    return model


print("\n========================================")
print("SCENARIO 1")
print("========================================")

model1 = run_simulation(
    num_agents=5,
    grid_size=10,
    num_steps=20
)

print("\nFinal Positions - Scenario 1:")

for i, agent in enumerate(model1.agents):
    print(f"Agent {i + 1}: {agent.position}")


print("\n========================================")
print("SCENARIO 2")
print("========================================")

model2 = run_simulation(
    num_agents=10,
    grid_size=10,
    num_steps=20
)

print("\nFinal Positions - Scenario 2:")

for i, agent in enumerate(model2.agents):
    print(f"Agent {i + 1}: {agent.position}")


fig, axes = plt.subplots(1, 2, figsize=(14, 6))

ax = axes[0]

for i, agent in enumerate(model1.agents):

    x = [position[0] for position in agent.path]
    y = [position[1] for position in agent.path]

    ax.plot(
        x,
        y,
        marker='o',
        markersize=3,
        label=f'Agent {i + 1}'
    )

    ax.scatter(
        x[0],
        y[0],
        marker='s',
        s=80
    )

    ax.scatter(
        x[-1],
        y[-1],
        marker='X',
        s=100
    )

ax.set_title("Scenario 1: 5 Agents")
ax.set_xlim(-0.5, 9.5)
ax.set_ylim(-0.5, 9.5)
ax.set_xticks(range(10))
ax.set_yticks(range(10))
ax.grid(True)
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")


ax = axes[1]

for i, agent in enumerate(model2.agents):

    x = [position[0] for position in agent.path]
    y = [position[1] for position in agent.path]

    ax.plot(
        x,
        y,
        marker='o',
        markersize=3,
        label=f'Agent {i + 1}'
    )

    ax.scatter(
        x[0],
        y[0],
        marker='s',
        s=80
    )

    ax.scatter(
        x[-1],
        y[-1],
        marker='X',
        s=100
    )

ax.set_title("Scenario 2: 10 Agents")
ax.set_xlim(-0.5, 9.5)
ax.set_ylim(-0.5, 9.5)
ax.set_xticks(range(10))
ax.set_yticks(range(10))
ax.grid(True)
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")

plt.tight_layout()
plt.show()
