from env.environment import EmailEnv
from models.action import Action
from tasks.task_easy import get_easy_task

env = EmailEnv()

task = get_easy_task()
obs = env.reset(task)

print("Task Loaded:", obs)

action = Action(action_type="classify", value="spam")

obs, reward, done, _ = env.step(action)

print("After Step:", obs)
print("Reward:", reward)
print("Done:", done)