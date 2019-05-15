import gym

# create environment
env = gym.make("CartPole-v1")

# define episodes
episodes = 100

for e in range(episodes):
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

  print("Episode finished after {} steps".format(step_index + 1))

print('Did not solve after {} episodes '.format(e))

if e == episodes - 1:
  input('Did not solve after {} episodes '.format(episodes))