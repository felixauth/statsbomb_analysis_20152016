import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np

def createPitch(field_dimen = (110,80), field_color ='green', linewidth=2, markersize=20):
    """ plot_pitch
    
    Plots a soccer pitch. All distance units converted to meters.
    
    Parameters
    -----------
        field_dimen: (length, width) of field in meters. Default is (106,68)
        field_color: color of field. options are {'green','white'}
        linewidth  : width of lines. default = 2
        markersize : size of markers (e.g. penalty spot, centre spot, posts). default = 20
        
    Returrns
    -----------
       fig,ax : figure and aixs objects (so that other data can be plotted onto the pitch)

    """
    fig,ax = plt.subplots(figsize=(12,8)) # create a figure 
    # decide what color we want the field to be. Default is green, but can also choose white
    if field_color=='green':
        ax.set_facecolor('mediumseagreen')
        lc = 'whitesmoke' # line color
        pc = 'w' # 'spot' colors
    elif field_color=='white':
        lc = 'k'
        pc = 'k'
    # ALL DIMENSIONS IN m
    border_dimen = (3,3) # include a border arround of the field of width 3m
    meters_per_yard = 0.9144 # unit conversion from yards to meters
    half_pitch_length = field_dimen[0]/2. # length of half pitch
    half_pitch_width = field_dimen[1]/2. # width of half pitch
    signs = [-1,1] 
    # Soccer field dimensions typically defined in yards, so we need to convert to meters
    goal_line_width = 8*meters_per_yard
    box_width = 20*meters_per_yard
    box_length = 6*meters_per_yard
    area_width = 44*meters_per_yard
    area_length = 18*meters_per_yard
    penalty_spot = 12*meters_per_yard
    corner_radius = 1*meters_per_yard
    D_length = 8*meters_per_yard
    D_radius = 10*meters_per_yard
    D_pos = 12*meters_per_yard
    centre_circle_radius = 10*meters_per_yard
    # plot half way line # center circle
    ax.plot([0,0],[-half_pitch_width,half_pitch_width],lc,linewidth=linewidth)
    ax.scatter(0.0,0.0,marker='o',facecolor=lc,linewidth=0,s=markersize)
    y = np.linspace(-1,1,50)*centre_circle_radius
    x = np.sqrt(centre_circle_radius**2-y**2)
    ax.plot(x,y,lc,linewidth=linewidth)
    ax.plot(-x,y,lc,linewidth=linewidth)
    for s in signs: # plots each line seperately
        # plot pitch boundary
        ax.plot([-half_pitch_length,half_pitch_length],[s*half_pitch_width,s*half_pitch_width],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length,s*half_pitch_length],[-half_pitch_width,half_pitch_width],lc,linewidth=linewidth)
        # goal posts & line
        ax.plot( [s*half_pitch_length,s*half_pitch_length],[-goal_line_width/2.,goal_line_width/2.],pc+'s',markersize=6*markersize/20.,linewidth=linewidth)
        # 6 yard box
        ax.plot([s*half_pitch_length,s*half_pitch_length-s*box_length],[box_width/2.,box_width/2.],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length,s*half_pitch_length-s*box_length],[-box_width/2.,-box_width/2.],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length-s*box_length,s*half_pitch_length-s*box_length],[-box_width/2.,box_width/2.],lc,linewidth=linewidth)
        # penalty area
        ax.plot([s*half_pitch_length,s*half_pitch_length-s*area_length],[area_width/2.,area_width/2.],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length,s*half_pitch_length-s*area_length],[-area_width/2.,-area_width/2.],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length-s*area_length,s*half_pitch_length-s*area_length],[-area_width/2.,area_width/2.],lc,linewidth=linewidth)
        # penalty spot
        ax.scatter(s*half_pitch_length-s*penalty_spot,0.0,marker='o',facecolor=lc,linewidth=0,s=markersize)
        # corner flags
        y = np.linspace(0,1,50)*corner_radius
        x = np.sqrt(corner_radius**2-y**2)
        ax.plot(s*half_pitch_length-s*x,-half_pitch_width+y,lc,linewidth=linewidth)
        ax.plot(s*half_pitch_length-s*x,half_pitch_width-y,lc,linewidth=linewidth)
        # draw the D
        y = np.linspace(-1,1,50)*D_length # D_length is the chord of the circle that defines the D
        x = np.sqrt(D_radius**2-y**2)+D_pos
        ax.plot(s*half_pitch_length-s*x,y,lc,linewidth=linewidth)
        
    # remove axis labels and ticks
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])
    # set axis limits
    xmax = field_dimen[0]/2. + border_dimen[0]
    ymax = field_dimen[1]/2. + border_dimen[1]
    ax.set_xlim([-xmax,xmax])
    ax.set_ylim([-ymax,ymax])
    ax.set_axisbelow(True)
    return fig,ax

def calculate_adj_position(position: list, field_dimen: list) -> list[float, float]:
    """ 
    
    Calculate the position on a zero-centered axis as the pitch center is (0,0)
    
    Parameters
    -----------
        position: position from Statsbomb data
        field_dimen: (length, width) of field in meters. Default is (106,68)
        
    Returns
    -----------
       position adjusted, centered around 0

    """
    
    x_adjust = position[0] - field_dimen[0] / 2
    y_adjust = position[1] - field_dimen[1] / 2
    
    return [x_adjust, y_adjust]

def sb_pitch(pitch_dim: tuple = (120, 80)):
    """
    See Statsbomb pitch dimension on page 23 of the PDF events documentation
    """

    # Storing pitch length and width
    pitch_length = pitch_dim[0]
    pitch_width = pitch_dim[1]

    # Creating plot
    fig, ax = plt.subplots(figsize=(12,8))
    
    # Plotting the soccer pitch
    ax.set_xlim(-10, pitch_length + 10)
    ax.set_ylim(-10, pitch_width + 10)

    # Inverting axis as per Sb documentation
    plt.gca().invert_yaxis()
    
    # Plotting the pitch boundaries
    ax.plot([0, 0], [0, pitch_width], color='black')  # left goal-line
    ax.plot([pitch_length, pitch_length], [0, pitch_width], color='black')  # right goal-line
    ax.plot([0, pitch_length], [0, 0], color='black')  # top boundary
    ax.plot([0, pitch_length], [pitch_width, pitch_width], color='black')  # bottom boundary

    # Plotting penalty areas
    ax.plot([0, 18], [18, 18], color='black')  # left penalty area horizontal line
    ax.plot([0, 18], [62, 62], color='black')  # left penalty area horizontal line
    ax.plot([102, 120], [18, 18], color='black')  # right penalty area horizontal line
    ax.plot([102, 120], [62, 62], color='black')  # right penalty area horizontal line
    ax.plot([18, 18], [18, 62], color='black')  # left penalty area vertical line
    ax.plot([102, 102], [18, 62], color='black')  # right penalty area vertical line
    ax.plot([0, 6], [30, 30], color='black')  # left small penalty area horizontal line
    ax.plot([0, 6], [50, 50], color='black')  # left small penalty area horizontal line
    ax.plot([114, 120], [30, 30], color='black')  # right small penalty area horizontal line
    ax.plot([114, 120], [50, 50], color='black')  # right small penalty area horizontal line
    ax.plot([6, 6], [30, 50], color='black')  # left small penalty area vertical line
    ax.plot([114, 114], [30, 50], color='black')  # right small penalty area vertical line
    
    # Plotting goals post
    ax.plot([0, -4], [36, 36], color='black') # left
    ax.plot([0, -4], [44, 44], color='black') # left
    ax.plot([-4, -4], [36, 44], color='black') # left
    ax.plot([120, 124], [36, 36], color='black') # right
    ax.plot([120, 124], [44, 44], color='black') # right
    ax.plot([124, 124], [36, 44], color='black') # right
    
    # Plotting center circle
    center_circle = patches.Circle((60, 40), 10, edgecolor='black', facecolor='none')
    ax.add_patch(center_circle)

    # Plotting arc
    arc_left = patches.Arc((13, 40), height=16.2, width=16.2, angle=0,
                    theta1=310, theta2=50, color="black")
    ax.add_patch(arc_left)
    arc_right = patches.Arc((107, 40), height=16.2, width=16.2, angle=0,
                    theta1=130, theta2=230, color="black")
    ax.add_patch(arc_right)

    # Plotting penalty spots
    ax.plot(12, 40, 'ko', markersize=2)  # left penalty spot
    ax.plot(108, 40, 'ko', markersize=2)  # right penalty spot

    # Plotting center spot
    ax.plot(60, 40, 'ko', markersize=2)  # center spot

    # Adding half-way line
    ax.plot([60, 60], [0, 80], color='black')

    # Set aspect to equal, so the pitch is not distorted
    ax.set_aspect('equal', adjustable='box')

    # Remove axis
    plt.axis('off')
    
    # # Show plot
    # plt.show()
    
    return fig, ax
