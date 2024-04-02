import pandas as pd
import matplotlib.pyplot as plt
from create_vertex import create_graph_and_apply_coloring  # Import the function from create_vertex.py

def create_schedule_dataframe(G, colors):
    # Define the available time slots
    time_slots = [
        "8:00 - 9:30", "9:45 - 11:15", "11:30 - 13:00",
        "13:30 - 15:00", "15:15 - 16:45", "17:00 - 18:30", "18:45 - 20:15"
    ]
    
    # Collect all unique groups from the graph, preserving the order they appear
    groups = list({node[0] for node in G.nodes()})
    
    # Create an empty DataFrame where index is time slots and columns are groups
    df = pd.DataFrame(index=time_slots, columns=groups).fillna('')
    
    # Assign courses to the DataFrame using colors to map to times and groups
    for node, color in colors.items():
        group, course, _, teacher, _, _, _ = node  # Unpack the node tuple
        day_index = color // len(time_slots)  # Assuming colors map to specific days and times
        time_index = color % len(time_slots)
        time_slot = time_slots[time_index]
        
        # Create the course detail string
        course_details = f"{course}\n{teacher}"
        
        # Add the course to the DataFrame
        if df.at[time_slot, group] == '':  # If the cell is empty, add course details
            df.at[time_slot, group] = course_details
        else:  # If the cell already has details, append the new details
            df.at[time_slot, group] += f"\n{course_details}"
    
    return df

def save_schedule_image(df, image_path='schedule.png'):
    fig, ax = plt.subplots(figsize=(12, 9))  # Adjust to fit your table size
    ax.axis('off')
    
    # Create table
    table = ax.table(cellText=df.values, colLabels=df.columns, rowLabels=df.index, loc='center', cellLoc='center')
    
    # Apply a style to the table, similar to the uploaded image
    table.auto_set_font_size(False)
    table.set_fontsize(5)
    table.scale(3, 3)  # Adjust scale to fit your table size
    
    # Style and save the table image
    plt.savefig(image_path, bbox_inches='tight', dpi=300)
    plt.close(fig)

if __name__ == "__main__":
    json_file = "file_1.json"
    G, colors = create_graph_and_apply_coloring(json_file)
    df = create_schedule_dataframe(G, colors)
    save_schedule_image(df, 'schedule.png')
