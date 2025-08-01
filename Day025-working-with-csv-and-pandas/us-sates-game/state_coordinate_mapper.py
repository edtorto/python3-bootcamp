import turtle
import pandas as pd

# load state names
csv_path = "state-names.csv"
df = pd.read_csv(csv_path)

# Add empty x and y columns if they don't exist
df['x'] = None
df['y'] = None
df.to_csv('states.csv', index=False)

# setting the turtle screen
screen = turtle.Screen()
screen.setup(600, 400)
screen.title("U.S. State Coordinate Mapper")
image = "blank-states-img.gif"
screen.addshape(image)
turtle.shape(image)

# load state with empty x and y columns
csv_path = "states.csv"
df = pd.read_csv(csv_path)
click_index = df[df['x'].isnull()].index.min()

def get_mouse_click(x, y):
    """save x and y coordinate to corresponding state names"""
    global click_index
    # If no rows left, stop collecting
    if click_index is None or click_index >= len(df):
        print("All rows have coordinates.")
        return

    # Assign to DataFrame
    df.at[click_index, 'x'] = x
    df.at[click_index, 'y'] = y

    # Save to CSV
    df.to_csv(csv_path, index=False)

    # Move to next available row
    next_unfilled = df[df['x'].isnull()].index
    click_index = next_unfilled.min() if not next_unfilled.empty else None

# collect x and y coordinates
turtle.onscreenclick(get_mouse_click)
turtle.mainloop()

# Convert x and y to integers
df['x'] = df['x'].astype(int)
df['y'] = df['y'].astype(int)

# Save back to CSV
df.to_csv("new_states.csv", index=False)