import gym

env=gym.make('stock-v0')
while not env.done:

    #print(env.action_space)
    #print(env.observation_space)
    action = env.action_space.sample()
    result,step = env.step(action)
    print(result)
    if env.done:
        break
