from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random
import pandas as pd
import gym

df = pd.read_csv('C:\\Users\\PAVAN KUMAR REDDY\\Downloads\\3files\\HDFC.csv')
df = df.sort_values('Date')
#print(df.head())

class StockEnv(Env):    # Inherite the methods and properties from openai gym
    df = pd.read_csv('C:\\Users\\PAVAN KUMAR REDDY\\Downloads\\3files\\HDFC.csv')
    df = df.sort_values('Date')

    def __init__(self):

        self.df = df

        # Actions we can take, buy, hold, sell
        self.action_space = Discrete(3)
        self.observation_space = Box(low=0, high=1,shape=(5,1),dtype=np.float32)
        self.current_step=0

    def step(self, action):
        result=[]
        if action<1: #buy
            if (self.df.loc[self.current_step, 'Open']< self.df.loc[self.current_step, 'Price']):
                result.append(self.df.loc[self.current_step, 'Date'])

        if action>1: #sell
            if (self.df.loc[self.current_step, 'Open']> self.df.loc[self.current_step, 'Price']):
                result.append(self.df.loc[self.current_step, 'Date'])

        if(self.current_step==len(df)):
            done=True
        else:
            done=False
        self.current_step+=1
        info={}
        return self.current_step,result,done,info
    def reset(self):
        self.current_step=0
        return self.current_step
    def render(self):
        pass


env=StockEnv()
print(env.action_space)
print(env.observation_space)
done = False
while not done:
        #env.render()
        action = env.action_space.sample()
        _, result, done, info = env.step(action)
