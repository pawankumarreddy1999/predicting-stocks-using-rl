from gym import Env
from gym.spaces import Discrete, Box
from gym import error, spaces, utils
import numpy as np
import random
import gym
from gym.utils import seeding
import pandas as pd
import random

action_buy=0
action_sell=1
class stockEnv(gym.Env):
    def __init__(self):
        self.f = 'C:\\Users\\PAVAN KUMAR REDDY\\Downloads\\3files\\HDFC.csv'
        self.df_xy = pd.DataFrame(pd.read_csv(self.f))
        self.ACTION_LOOKUP = {0: 'buy', 1: 'sell'}

        self.action_space = spaces.Discrete(len(self.ACTION_LOOKUP))
        self.observation_space = spaces.Discrete(self.df_xy.shape[0])

        self.ob = self._get_random_initial_state()
        self.episode_over = False
        self.turns = 0
        self.sum_rewards = 0.0
        self.action = 0.0
        self.current_state_index = 0
        #print(self.df_xy.shape[0])
        self.result_sell=[]
        self.result_buy=[]
        self.result=[]

    def step(self, predicted_action_index):
        #print('predicted_action_index {}'.format(predicted_action_index))
        self.turns += 1
        self.predicted_action = self._take_action(predicted_action_index)
        #print('self.predicted_action {}'.format(self.predicted_action))
        self.reward = self._get_reward(predicted_action_index)
        #print('self.reward {}'.format(self.reward))
        #print('bef self.ob{}'.format(self.ob))
        self.ob = self._get_next_state()
        #print('after self.ob {}'.format(self.ob))
        if (self.current_state_index)==len(self.df_xy)-1:
            self.episode_over = True

        return self.ob, self.reward, self.episode_over

    def reset(self):
        """
               Reset the environment and supply a new state for initial state
               :return:
               """

        self.turns = 0
        self.ob = self._get_random_initial_state()
        self.episode_over = False
        self.sum_rewards = 0.0
        return self.ob

    def render(self, mode='human', close=False):
        pass

    def _take_action(self, action_index):
        """
                Take an action correpsonding to action_index in the current state
                :param action_index:
                :return:
                """
        assert action_index < len(self.ACTION_LOOKUP)
        self.action = action_index
        return self.action

    def _get_random_initial_state(self):
        nrand = random.randint(0, self.df_xy.shape[0])
        self.current_state_index = nrand
        return self.df_xy.iloc[nrand]

    def _get_reward(self, predicted_action):
        """
                Get reward for the action taken in the current state
                :return:
                """
        df = self.df_xy
        reward=0
        if predicted_action == action_buy:  # buy
            # print('Open: {}'.format(self.df.loc[self.current_step, 'Open']),'Price : {}'.format(self.df.loc[self.current_step, 'Price']))
            if (df.loc[self.current_state_index, 'Open'] < df.loc[self.current_state_index, 'Price']):
                self.result_buy.append(self.current_state_index)
                #self.result.append(df.loc[self.current_state_index, 'Date'])
                reward=1
            else:
                reward=0
                # print(self.df.iloc[self.current_step])
                # print('step number is: {}'.format(self.current_step),'action is: {}'.format(action),'Date: {}'.format(self.df.loc[self.current_step, 'Date']),'BUY')
        if predicted_action == action_sell:  # sell
            # print('Open: {}'.format(self.df.loc[self.current_step, 'Open']),'Price : {}'.format(self.df.loc[self.current_step, 'Price']))
            if (df.loc[self.current_state_index, 'Open'] > df.loc[self.current_state_index, 'Price']):
                self.result_sell.append(self.current_state_index)
                #self.result.append(df.loc[self.current_state_index, 'Date'])
                reward=1
            else:
                reward=0

                # print('step number is: {}'.format(self.current_step),'action is: {}'.format(action),'Date: {}'.format(self.df.loc[self.current_step, 'Date']),'SELL')
        self.sum_rewards += reward
        return self.sum_rewards,self.result_buy,self.result_sell

    def _get_next_state(self):
        """
        Get the next state from current state
        :return:
        """
        df = self.df_xy
        new_state_index = self.current_state_index + 1
        next_state = df.iloc[new_state_index]
        self.current_state_index = new_state_index
        return next_state

    def _seed(self):
        return
