import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsbombpy import sb
import warnings
from pitch import sb_pitch

def identify_goals(events: pd.DataFrame) -> list:
    """
    Returns the index of the goals in the shots dataframe from events.
    
    Parameters
    -----------
        events: dataframe with all the events of a match
        
    Returrns
    -----------
       list of index
    
    """
    shots = events["shots"]["shot"]
    goals_index = []
    for index_shot, shot in enumerate(shots):
        outcome = shot["outcome"]
        if outcome["name"] == "Goal":
            goals_index.append(index_shot)
            
    return goals_index

def plot_goals(goals_index: list, events: pd.DataFrame):
    """
    Plot the goals of match on the pitch.
    
    Parameters
    -----------
        goals_index: index of the goals in the 'shots' events dataframe
        events: dataframe with all the events of a match
        
    Returrns
    -----------
       list of index
    
    """
    fig, ax = sb_pitch()
    goals_shots = events["shots"].loc[goals_index,["possession_team","period","timestamp","location","shot"]]
    for _, goal in goals_shots.iterrows():
        ax.plot(goal["location"][0],goal["location"][1], 'ro', markersize=6)
        ax.plot(goal["shot"]["end_location"][0],goal["shot"]["end_location"][1], 'ro', markersize=6)
    
    return fig,ax

if __name__ == "__main__":
    
    warnings.filterwarnings('ignore')
    
    match_id = 267533
    events = sb.events(match_id=match_id, split=True, flatten_attrs=False)
    goals_index = identify_goals(events)
    plot_goals(goals_index, events)
    # print(goals_index)
