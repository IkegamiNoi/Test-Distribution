if __name__ == "__main__":
    root = tk.Tk()
    root.title("KeyboardView Test")

    keys = [
        {"id": "ESC", "label": "Esc", "x": 0, "y": 0, "w": 1, "h": 1},
        {"id": "1", "label": "1", "x": 1, "y": 0, "w": 1, "h": 1},
        {"id": "2", "label": "2", "x": 2, "y": 0, "w": 1, "h": 1},
        {"id": "TAB", "label": "Tab", "x": 0, "y": 1, "w": 1.5, "h": 1},
        {"id": "A", "label": "A", "x": 1.5, "y": 1, "w": 1, "h": 1},
        {"id": "ENTER", "label": "Enter", "x": 10, "y": 2, "w": 2, "h": 1},
    ]

    view = KeyboardView(root, unit=60)
    view.pack(fill="both", expand=True)

    view.render(keys)

    root.mainloop()