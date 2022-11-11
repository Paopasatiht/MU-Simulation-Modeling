from gym.envs.registration import register

register(
    id='assault-v0',
    entry_point='gym_assault.envs:AssaultEnv',
)