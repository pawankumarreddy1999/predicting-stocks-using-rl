from gym import Env
from gym.spaces import Discrete, Box
from gym import error, spaces, utils
import numpy as np
import random
import pandas as pd
import gym


class StockEnv(Env):    # Inherite the methods and properties from openai gym
    def __init__(self):
        self.f = 'C:\\Users\\PAVAN KUMAR REDDY\\Downloads\\3files\\HDFC.csv'
        self.df = pd.DataFrame(pd.read_csv(self.f))
        self.result_buy=[]
        self.result_sell=[]
        self.result=[]
        # Actions we can take, buy, hold, sell
        self.action_space = Discrete(3)
        self.observation_space = spaces.Discrete(self.df.shape[0])
        self.current_step=0
        self.done=False
    def step(self, action):
        if(self.current_step<len(self.df)):
            if action<1: #buy
                #print('Open: {}'.format(self.df.loc[self.current_step, 'Open']),'Price : {}'.format(self.df.loc[self.current_step, 'Price']))
                if (self.df.loc[self.current_step, 'Open']< self.df.loc[self.current_step, 'Price']):
                    self.result_buy.append(self.df.loc[self.current_step, 'Date'])
                    self.result.append(self.df.loc[self.current_step, 'Date'])

                    #print('step number is: {}'.format(self.current_step),'action is: {}'.format(action),'Date: {}'.format(self.df.loc[self.current_step, 'Date']),'BUY')
            if action>1: #sell
                #print('Open: {}'.format(self.df.loc[self.current_step, 'Open']),'Price : {}'.format(self.df.loc[self.current_step, 'Price']))
                if (self.df.loc[self.current_step, 'Open']> self.df.loc[self.current_step, 'Price']):
                    self.result_sell.append(self.df.loc[self.current_step, 'Date'])
                    self.result.append(self.df.loc[self.current_step, 'Date'])

                    #print('step number is: {}'.format(self.current_step),'action is: {}'.format(action),'Date: {}'.format(self.df.loc[self.current_step, 'Date']),'SELL')

        if(self.current_step==len(self.df)):
            self.done=True
        else:
            self.done=False
        self.current_step+=1
        return self.result_buy,self.result_sell,self.result, self.current_step
    def reset(self):
        self.current_step=0
        self.result=[]
        self.done=False
        return self.result,self.done
    def render(self):
        pass

