import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk

color_bar = None  # Initialize color_bar as None

def update_button_color(event):
    selected_color = color_var.get()
    if selected_color in plt.colormaps():
        plot_button.configure(bg=selected_color)
        plot_surface()
    else:
        plot_button.configure(bg='blue')  # Default color

def plot_surface():
    global color_bar

    # Clear any previous plots and color bars
    ax.clear()
    if color_bar is not None:
        color_bar.remove()

    # Create a meshgrid of x and y values
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)

    # Define the function for the U-shaped surface
    Z = 0.5 * (X**2 + Y**2)

    # Create the 3D surface plot
    surf = ax.plot_surface(X, Y, Z, cmap=color_var.get())

    # Set labels for the axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set the title
    ax.set_title('Colorful 3D U-shaped Surface Plot')

    # Add color bar on the side
    color_bar = fig.colorbar(surf, ax=ax, pad=0.1, shrink=0.8, aspect=10)

    # Redraw the canvas
    canvas.draw()

# Create the main GUI window
root = Tk()
root.title('3D Surface Plot')

# Set the size of the GUI window
root.geometry("1920x1080")

# Create a frame for the dropdown menu
frame = Frame(root)
frame.pack(padx=10, pady=10)

# Create a label for the dropdown menu
label = Label(frame, text='Select Color:', font=("Helvetica", 16))
label.pack(side=LEFT)

# Create a variable for the selected color
color_var = StringVar()
color_var.set('plasma')

# Create the dropdown menu for selecting colors
color_dropdown = ttk.Combobox(frame, textvariable=color_var, font=("Helvetica", 16))
color_dropdown['values'] = plt.colormaps()
color_dropdown.pack(side=LEFT)

# Bind the dropdown change event to update the button color
color_dropdown.bind("<<ComboboxSelected>>", update_button_color)

# Create a Matplotlib figure and a 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the canvas to display the Matplotlib plot
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Set the size of the canvas
canvas.get_tk_widget().configure(width=1720, height=880)

# Create a button to plot the surface
plot_button = Button(root, text='Plot Surface', command=plot_surface, font=("Helvetica", 24), bg='blue', fg='white')
plot_button.pack()

color_bar = None  # Initialize color_bar as None

# Start the GUI event loop
root.mainloop()
