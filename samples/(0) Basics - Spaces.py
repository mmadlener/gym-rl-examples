import gym

# create environment
print("Create 'CartPole-v0' environment")
env = gym.make('CartPole-v0')

# show spaces of cart pole
print(env.action_space) #[Output: ] Discrete(2) - non-negative possible values, above 0 or 1
print(env.observation_space) # [Output: ] Box(4,) - represent n-dim array

# create new environment
env = gym.make('MountainCarContinuous-v0')
print("Create 'MountainCarContinuous-v0' environment")

# show spaces of cart pole
print(env.action_space) #[Output: ] Box(1,)
print(env.observation_space) #[Output: ] Box(2,)

input("")