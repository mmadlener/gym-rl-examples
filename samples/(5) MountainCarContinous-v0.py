import gym

# create environment
env = gym.make("MountainCarContinuous-v0")
# start 
observation = env.reset()

# define params
done = False
step_index = 0

while not done:
  # render 
  env.render()
  # your agent here (this takes random actions)
  action = env.action_space.sample() 
  # observate
  observation, reward, done, info = env.step(action)
  
  # print out values
  step_index += 1
  print("Step {}:".format(step_index))
  print("action: {}".format(action))
  print("observation: {}".format(observation))
  print("reward: {}".format(reward))
  print("done: {}".format(done))
  print("info: {}".format(info))

for t in range(5000):
  env.render()
  action = env.action_space.sample()
  observation, reward, done, info = env.step(action)
  
env.close()
input("Episode finished after {} steps".format(step_index + 1))