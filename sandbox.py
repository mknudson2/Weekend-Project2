buttons = []
for i in range(3):
    for j in range(3):
        button = tk.Button(
            window,
            text="Select",
            width=10,
            height=5,
            command=lambda player_input=choices[i * 3 + j], btn=buttons[i * 3 + j]: play(
                player_input, btn
            ),
        )
        button.grid(row=i, column=j)
        buttons.append(button)



buttons = {}

# Create the grid of buttons
for row in range(5):
    for col in range(5):
        button_text = ['rock', 'paper', 'scissors', 'lizard', 'spock'][row]
        buttons[row] = buttons.get(row, {})
        buttons[row][col] = tk.Button(window, text=button_text, padx=20, pady=10,
                                     command=lambda r=row, c=col: on_button_click(r, c))
        buttons[row][col].grid(row=row, column=col)