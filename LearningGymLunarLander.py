import gymnasium as gym
#create the env
#making the environment
env=gym.make('LunarLander-v3', render_mode='human')
#make() used to create an environment,env, which you interact with
#render_modes= how env is visualized. rgb_array or human 



#once youve initalized the environment, you have to reset it to get your first observation and info
observations, info=env.reset()


#you want to loop agent-observation work until the end of the episode: 
episode_over=False
while not episode_over:
    #action must be chosen from action space
    action=env.action_space.sample()
    #.sample() means that its chosen randomly for now
    observations, rewards, terminated, truncated, info=env.step(action)
    #.step() function used to execute the action chosen from action space
    #observations are given to the agent
    #rewards are recieved from environment based on action taken
    #terminated- at some stage : example: the robot has crashed, baby has learnt walking : the environment has been terminated;
    #   you want to end the episode here 
    #truncated- if you want to end the episode after certain number of steps
    #STOP THE EPISODE IF TERMINATED OR TRUNCATED=TRUE
    episode_over=terminated or truncated

env.close()