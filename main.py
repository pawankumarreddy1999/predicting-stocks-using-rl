import gym
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import A2C,PPO2
import numpy as np
import stock_env


env=gym.make('stock1-v0')
''''
while True:
    #print(env.action_space)
    #print(env.observation_space)
    action = env.action_space.sample()
    #print(action)
    ob,result,done,info= env.step(action)
    #print(result)
    if done:
        break
#print("BUY",result_buy)
print(result)



#env_maker = lambda: gym.make('stock1-v0')
#env = DummyVecEnv([env_maker])
'''



model = PPO2('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=100)
#model=PPO2.load('ppo2_stock')
print(model)
obs = env.reset()
count=5
print(obs)
while True:
    action, _states = model.predict(obs)
    #print(action)
    obs, rewards, dones = env.step(action[4])
    #count-=1
    if dones:
        break
print(" Reward is:{}".format(rewards[0]))
print("Results for buy: {}".format(rewards[1]))
print("Results for sell {}".format(rewards[2]))
