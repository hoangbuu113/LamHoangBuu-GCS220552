import tkinter as tk


def configure_fonts():
    """
    Configures the default font settings for the Tkinter application.
    """
    default_font = ("Helvetica", 10)

    # Configure default fonts for various Tkinter widgets
    tk.Label.configure(font=default_font)
    tk.Button.configure(font=default_font)
    tk.Entry.configure(font=default_font)
    tk.Text.configure(font=default_font)
    tk.scrolledtext.ScrolledText.configure(font=default_font)
    tk.Toplevel.configure(font=default_font)
