# https://github.com/Kautenja/gym-super-mario-bros

from nes_py.wrappers import BinarySpaceToDiscreteSpaceEnv
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

# Complete environments
# SuperMarioBros-v<version>
# SuperMarioBros2NoFrameskip-v<version>

# Individual Levels
# These environments allow a single attempt (life) to make it through a single level of the game.
# SuperMarioBros-<world>-<level>-v<version>
# where:
# <world> is a number in {1, 2, 3, 4, 5, 6, 7, 8} indicating the world
# <level> is a number in {1, 2, 3, 4} indicating the level within a world
# <version> is a number in {0, 1, 2, 3} specifying the ROM mode to use
# 0: standard ROM
# 1: downsampled ROM
# 2: pixel ROM
# 3: rectangle ROM
# NoFrameskip can be added before the first hyphen to disable frame skip

env = gym_super_mario_bros.make('SuperMarioBros2NoFrameskip-v0')
env = BinarySpaceToDiscreteSpaceEnv(env, SIMPLE_MOVEMENT)

done = True
for _ in range(5000):
    if done:
        state = env.reset()

    action = env.action_space.sample()
    state, reward, done, info = env.step(action)
    env.render()

env.close()
