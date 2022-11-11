# import gym
# from gym import error, spaces, utils
# from gym.utils import seeding
#
# class FooEnv(gym.Env):
#   metadata = {'render.modes': ['human']}
#
#   def __init__(self):
#     ...
#   def step(self, action):
#     ...
#   def reset(self):
#     ...
#   def render(self, mode='human', close=False):
#     ...

import gym

env = gym.make("ALE/Assault-v5",
               render_mode="human")
env.action_space.seed(42)

observation, info = env.reset(seed=42)

for _ in range(1000):
    observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

    if terminated or truncated:
        observation, info = env.reset()

env.close()
