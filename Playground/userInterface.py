import tkinter as tk
from helperGPT import *

# Define colors
BG_COLOR = "#4CAF50"  # green
FG_COLOR = "#FFFFFF"  # white
HL_COLOR = "#81C784"  # lighter green



def unhighlight_label(label):
    label.config(bg=BG_COLOR)

def highlight_label(label):
    label.config(bg=HL_COLOR)

def send_message():
    global response_labels

    bot=DecompGPT()
    # Reset the response labels
    for response_label in response_labels:
        response_label.destroy()

    message = message_entry.get()

    if message.lower() == "exit":
        messages_listbox.insert(tk.END, "Chat ended.")
        message_entry.delete(0, tk.END)
        message_entry.config(state=tk.DISABLED)

    else:

        messages_listbox.insert(tk.END, "You: " + message)

        response_subQ = bot.getSubQuestions(message)
        subQuestionList = response_subQ["choices"][0]["message"]["content"].split("\n")

        for i, response in enumerate(subQuestionList):
            response_label = tk.Label(root, text="Bot: " + response, bg=BG_COLOR, fg=FG_COLOR, font=("Helvetica", 12))
            response_label.bind("<Enter>", lambda event, label=response_label: highlight_label(label))
            response_label.bind("<Leave>", lambda event, label=response_label: unhighlight_label(label))
            response_label.pack(padx=10, pady=5, fill=tk.X)
            response_labels.append(response_label)
        message_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Chat Interface")

# Set background color for the entire window
root.configure(bg=BG_COLOR)

response_labels = []

# Create a listbox to display messages
messages_listbox = tk.Listbox(root, height=25, width=200, bg=BG_COLOR, fg=FG_COLOR, font=("Helvetica", 12))
messages_listbox.pack(padx=10, pady=10)

# Create an entry widget to allow users to enter messages
message_entry = tk.Entry(root, width=200, bg=BG_COLOR, fg=FG_COLOR, font=("Helvetica", 12))
message_entry.pack(padx=10, pady=10)
message_entry.focus_set()

# Create a button to send messages
send_button = tk.Button(root, text="Send", bg=HL_COLOR, fg=FG_COLOR, font=("Helvetica", 12), command=send_message)
send_button.pack(padx=10, pady=10)

root.mainloop()
