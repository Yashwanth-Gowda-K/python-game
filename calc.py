from tkinter import *  # Import all classes and functions from tkinter

class CalculatorApp:
    def __init__(self, root):
        self.root = root  # Reference to the main application window
        self.root.title("Calculator")  # Set the title of the window
        self.root.geometry("300x400")  # Set the dimensions of the window
        self.root.configure(bg="black")  # Set the background color to black
        
        # Create a StringVar to store the input expression
        self.expression = ""  # Initialize the expression as an empty string
        self.input_text = StringVar()  # StringVar to update the input field dynamically
        
        # Input field
        input_frame = Frame(self.root, bg="black")  # Create a frame for the input field
        input_frame.pack(side=TOP, fill=BOTH, padx=10, pady=10)  # Position and size the frame
        
        input_field = Entry(input_frame, textvariable=self.input_text, font=('Arial', 18), justify='right', bg="white", fg="black")  # Create the input field with white background
        input_field.pack(fill=BOTH, ipady=10)  # Add the input field to the frame and set padding
        
        # Button frame
        button_frame = Frame(self.root, bg="black")  # Create a frame for the buttons
        button_frame.pack(fill=BOTH, expand=True)  # Position and expand the button frame
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),  # First row of buttons
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),  # Second row of buttons
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),  # Third row of buttons
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),  # Fourth row of buttons
        ]
        
        for (text, row, col) in buttons:  # Loop through button definitions
            Button(
                button_frame, 
                text=text, 
                bg="#FFFFC5",  # Set button background to yellow
                fg="black",  # Set button text color to black
                font=('Arial', 14), 
                command=lambda t=text: self.on_button_click(t),  # Create each button with a command
                relief="flat",  # Remove default border style
                bd=0,  # Remove button border
                highlightbackground="black",  # Add black background highlight
                highlightthickness=1,  # Thickness for the border to shape button
                padx=5, pady=5  # Add internal padding for better rounded look
            ).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)  # Place buttons in the grid
        
        # Adjust grid weights
        for i in range(5):  # Loop through rows and columns
            button_frame.rowconfigure(i, weight=1)  # Adjust row weight for equal distribution
            button_frame.columnconfigure(i, weight=1)  # Adjust column weight for equal distribution
    
    def on_button_click(self, button_text):  # Handle button click events
        if button_text == "C":  # Clear button
            self.expression = ""  # Reset the expression
            self.input_text.set("")  # Clear the input field
        elif button_text == "=":  # Equals button
            try:
                result = eval(self.expression)  # Evaluate the expression
                self.input_text.set(result)  # Display the result
                self.expression = str(result)  # Update the expression with the result
            except Exception as e:  # Handle evaluation errors
                self.input_text.set("Error")  # Display error message
                self.expression = ""  # Reset the expression
        else:
            self.expression += button_text  # Append the button text to the expression
            self.input_text.set(self.expression)  # Update the input field

if __name__ == "__main__":
    root = Tk()  # Create the main application window
    app = CalculatorApp(root)  # Initialize the calculator application
    root.mainloop()  # Run the main event loop
