import tkinter as tk


class KeyboardView(tk.Canvas):
    def __init__(self, master, unit=60, padding=5, **kwargs):
        super().__init__(master, bg="#1e1e1e", highlightthickness=0, **kwargs)

        self.unit = unit
        self.padding = padding

        # key_id → { "rect": id, "text": id }
        self.key_items = {}

    def render(self, keys):
        """keys を受け取って描画する"""
        self.delete("all")
        self.key_items.clear()

        for key in keys:
            self._draw_key(key)

    def _draw_key(self, key):
        x = key["x"] * self.unit
        y = key["y"] * self.unit
        w = key["w"] * self.unit
        h = key["h"] * self.unit

        rect = self.create_rectangle(
            x + self.padding,
            y + self.padding,
            x + w - self.padding,
            y + h - self.padding,
            fill="#2d2d2d",
            outline="#555",
            width=2,
            tags=("key", key["id"]),
        )

        text = self.create_text(
            x + w / 2,
            y + h / 2,
            text=key["label"],
            fill="white",
            font=("Segoe UI", 14),
            tags=("key", key["id"]),
        )

        self.key_items[key["id"]] = {
            "rect": rect,
            "text": text,
        }

    def set_key_color(self, key_id, fill=None, outline=None):
        """キーの色変更（後で使うため）"""
        items = self.key_items.get(key_id)
        if not items:
            return

        if fill:
            self.itemconfig(items["rect"], fill=fill)
        if outline:
            self.itemconfig(items["rect"], outline=outline)