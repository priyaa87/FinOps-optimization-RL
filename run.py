from env import FinOpsEnv
from agent import agent_action
from grader import grade_performance

env = FinOpsEnv(level="medium")

state = env.reset()
initial_cost = env.initial_cost

for _ in range(15):
    action = agent_action()
    state, reward, done = env.step(action)

    if done:
        break

final_cost = env.calculate_cost()

score = grade_performance(initial_cost, final_cost)

print("Final Cost:", final_cost)
print("Score:", score)