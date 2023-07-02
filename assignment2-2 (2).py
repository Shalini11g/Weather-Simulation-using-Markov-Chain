import numpy as np
'''Weather Simulation class is being created to implement all the required methods'''


class WeatherSimulation:
    '''The constructor is being created to take the values transition_probabilities and holding_times'''
    def __init__(self,transition_probabilities,holding_times):
        '''transition_probabilities is a dictionary used to store the transitions probabilities with each state'''
        self.transition_probabilities=transition_probabilities
        '''holding_times is a dictionary used to store holdong time of each state'''
        self.holding_times=holding_times
        self.holding_time = 0
        self.states = 'sunny'

        for state in transition_probabilities.values():
            probablility=0
            for probab in state.values():
                probablility+=probab
            if probablility!=1:
                raise(RuntimeError("sum of probablities is not 1"))    


    def get_states(self):
        '''get_states is a method used to return all the states'''
        return list(self.transition_probabilities.keys())

    def current_state(self):
        '''current_state is a method used to return current state'''
        return self.states

    def set_state(self,new_state):
        '''set_state method is used to set the new state to current state'''
        self.states=new_state

    def next_state(self):
        '''next_state is a method to select the next state
        from a current state based on the probabilities'''
        if self.holding_time <=0:
            self.states = np.random.choice(self.get_states(), p=list(self.transition_probabilities[self.states].values()))
            self.holding_time = self.holding_times[self.states]
        self.holding_time = self.holding_time-1

    def current_state_remaining_hours(self):
        '''current_state_remaining_hours is a method to return the current state remaining time '''
        return self.holding_time

    
    def iterable(self):
        '''iterable is a generator method that gives the current state and moves to the next state'''
        while(1):
            yield self.states
            self.next_state()
 
    def simulate(self,hours=1000):
        '''simulate runs the simulation for hours and returns the percentages that each value shows'''
        state_values = {}
        for x in self.transition_probabilities.keys():
            state_values[x]=0
        for _ in range(hours):
            state_values[self.current_state()] = state_values[self.current_state()]+1
            self.next_state()
        sequence = list(state_values.values())
        percentages=[]
        for i in range(len(sequence)):
            percentages.append(sequence[i]*100/hours)
        return percentages
    