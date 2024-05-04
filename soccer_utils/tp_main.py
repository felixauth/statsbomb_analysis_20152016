from taipy import Gui
import taipy.gui.builder as tgb 
from statsbombpy import sb
from soccer import identify_goals, plot_goals



match_id = 267533
events = sb.events(match_id=match_id, split=True, flatten_attrs=False)
goals_index = identify_goals(events)
fig, ax = plot_goals(goals_index, events)

with tgb.Page() as page:
    tgb.part(content="{fig}", height="900px")

# list_to_display = [100/x for x in range(1, 100)]
# with tgb.Page() as page:
#     tgb.chart("{list_to_display}")
    
Gui(page).run(debug=True, use_reloader=True) # use_reloader=True