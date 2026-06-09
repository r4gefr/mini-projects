"""
==================================================
 To-Do List — Tkinter GUI  |  Portfolio Project
 Author  : Your Name
 Version : 2.0
 Stack   : Python 3, Tkinter (stdlib only)
--------------------------------------------------
 Features:
   • Add / Toggle / Delete tasks
   • Priority levels: High | Medium | Low
   • Color-coded priority badges
   • Scrollable task list
   • Keyboard shortcut: Enter to add task
   • Clean MVC-style functions architecture
==================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ── Constants ──────────────────────────────────────────────────────────────────

PRIORITIES      = ["High", "Medium", "Low"]

PRIORITY_COLORS = {
    "High":   {"bg": "#FF4C4C", "fg": "#FFFFFF"},
    "Medium": {"bg": "#F5A623", "fg": "#FFFFFF"},
    "Low":    {"bg": "#4CAF50", "fg": "#FFFFFF"},
}

PRIORITY_ICONS  = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}

# ── Palette ────────────────────────────────────────────────────────────────────

BG_DARK      = "#1A1A2E"
BG_CARD      = "#16213E"
BG_INPUT     = "#0F3460"
ACCENT       = "#E94560"
TEXT_PRIMARY = "#EAEAEA"
TEXT_MUTED   = "#7A7A9D"
DONE_COLOR   = "#4A4A6A"
FONT_MAIN    = ("Segoe UI", 11)
FONT_BOLD    = ("Segoe UI", 11, "bold")
FONT_TITLE   = ("Segoe UI", 18, "bold")
FONT_SMALL   = ("Segoe UI", 9)
FONT_BADGE   = ("Segoe UI", 8, "bold")

# ── Data Store ─────────────────────────────────────────────────────────────────

tasks: list[dict] = []

# ── Task Logic (pure functions, no GUI dependency) ─────────────────────────────

def create_task(name: str, priority: str) -> dict:
    """Create and return a new task dictionary."""
    return {"task": name, "priority": priority, "done": False}


def toggle_task(index: int) -> None:
    """Toggle the done status of a task by index."""
    tasks[index]["done"] = not tasks[index]["done"]


def delete_task(index: int) -> None:
    """Delete a task by index."""
    tasks.pop(index)


def add_task(name: str, priority: str) -> tuple[bool, str]:
    """
    Validate and add a task.
    Returns (success: bool, message: str).
    """
    name = name.strip()
    if not name:
        return False, "Task name cannot be empty."
    if priority not in PRIORITIES:
        return False, "Invalid priority selected."
    tasks.append(create_task(name, priority))
    return True, f"Task added: {name}"

# ── GUI Rendering ──────────────────────────────────────────────────────────────

def render_task_list(frame: tk.Frame, on_toggle, on_delete) -> None:
    """
    Clear and re-render all task rows inside the given frame.
    Each row shows: index, priority badge, task name, done button, delete button.
    """
    for widget in frame.winfo_children():
        widget.destroy()

    if not tasks:
        empty_lbl = tk.Label(
            frame, text="No tasks yet. Add one above ☝",
            font=FONT_MAIN, bg=BG_CARD, fg=TEXT_MUTED, pady=20
        )
        empty_lbl.pack()
        return

    for i, task in enumerate(tasks):
        done     = task["done"]
        priority = task["priority"]
        p_colors = PRIORITY_COLORS[priority]

        # Row frame
        row = tk.Frame(frame, bg=DONE_COLOR if done else BG_INPUT,
                       pady=8, padx=12, cursor="arrow")
        row.pack(fill="x", pady=3, padx=4)

        # Index label
        idx_lbl = tk.Label(
            row, text=f"{i + 1}.",
            font=FONT_SMALL, bg=row["bg"], fg=TEXT_MUTED, width=3, anchor="w"
        )
        idx_lbl.pack(side="left")

        # Priority badge
        badge = tk.Label(
            row, text=f" {PRIORITY_ICONS[priority]} {priority} ",
            font=FONT_BADGE,
            bg=p_colors["bg"], fg=p_colors["fg"],
            padx=4, pady=2, relief="flat"
        )
        badge.pack(side="left", padx=(0, 8))

        # Task name
        name_color = TEXT_MUTED if done else TEXT_PRIMARY
        name_font  = ("Segoe UI", 11, "overstrike") if done else FONT_MAIN
        name_lbl   = tk.Label(
            row, text=task["task"],
            font=name_font, bg=row["bg"], fg=name_color, anchor="w"
        )
        name_lbl.pack(side="left", fill="x", expand=True)

        # Delete button
        del_btn = tk.Button(
            row, text="🗑",
            font=FONT_SMALL, bg=row["bg"], fg="#FF6B6B",
            relief="flat", cursor="hand2", activebackground=row["bg"],
            command=lambda idx=i: on_delete(idx)
        )
        del_btn.pack(side="right", padx=(4, 0))

        # Toggle button
        toggle_text  = "↩ Undo" if done else "✔ Done"
        toggle_color = "#7A7A9D" if done else "#4CAF50"
        tog_btn = tk.Button(
            row, text=toggle_text,
            font=FONT_BADGE, bg=row["bg"], fg=toggle_color,
            relief="flat", cursor="hand2", activebackground=row["bg"],
            command=lambda idx=i: on_toggle(idx)
        )
        tog_btn.pack(side="right", padx=4)


# ── App Class ──────────────────────────────────────────────────────────────────

class ToDoApp:
    """Main application class — owns the root window and all UI state."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self._configure_root()
        self._build_ui()

    # ── Setup ──────────────────────────────────────────────────────────────────

    def _configure_root(self) -> None:
        self.root.title("To-Do List")
        self.root.geometry("580x680")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_DARK)
        # Center window on screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth()  - 580) // 2
        y = (self.root.winfo_screenheight() - 680) // 2
        self.root.geometry(f"580x680+{x}+{y}")

    def _build_ui(self) -> None:
        """Construct every UI section."""
        self._build_header()
        self._build_input_section()
        self._build_stats_bar()
        self._build_task_list()
        self._build_footer()

    # ── Header ─────────────────────────────────────────────────────────────────

    def _build_header(self) -> None:
        header = tk.Frame(self.root, bg=BG_DARK, pady=20)
        header.pack(fill="x")

        tk.Label(
            header, text="✅  My To-Do List",
            font=FONT_TITLE, bg=BG_DARK, fg=TEXT_PRIMARY
        ).pack()
        tk.Label(
            header, text="Stay organised. Get things done.",
            font=FONT_SMALL, bg=BG_DARK, fg=TEXT_MUTED
        ).pack(pady=(2, 0))

    # ── Input Section ──────────────────────────────────────────────────────────

    def _build_input_section(self) -> None:
        card = tk.Frame(self.root, bg=BG_CARD, padx=20, pady=16)
        card.pack(fill="x", padx=20, pady=(0, 8))

        # Task entry
        tk.Label(card, text="New Task", font=FONT_BOLD,
                 bg=BG_CARD, fg=TEXT_PRIMARY).pack(anchor="w")

        self.task_entry = tk.Entry(
            card, font=FONT_MAIN,
            bg=BG_INPUT, fg=TEXT_PRIMARY, insertbackground=TEXT_PRIMARY,
            relief="flat", bd=0
        )
        self.task_entry.pack(fill="x", ipady=8, pady=(4, 10))
        self.task_entry.bind("<Return>", lambda e: self._handle_add())

        # Priority + button row
        row = tk.Frame(card, bg=BG_CARD)
        row.pack(fill="x")

        tk.Label(row, text="Priority:", font=FONT_MAIN,
                 bg=BG_CARD, fg=TEXT_PRIMARY).pack(side="left", padx=(0, 8))

        self.priority_var = tk.StringVar(value="Medium")
        priority_menu = ttk.Combobox(
            row, textvariable=self.priority_var,
            values=PRIORITIES, state="readonly",
            font=FONT_MAIN, width=10
        )
        priority_menu.pack(side="left")

        add_btn = tk.Button(
            row, text="+ Add Task",
            font=FONT_BOLD, bg=ACCENT, fg="#FFFFFF",
            relief="flat", padx=16, pady=6, cursor="hand2",
            activebackground="#C73652",
            command=self._handle_add
        )
        add_btn.pack(side="right")

        # Status message label
        self.status_var = tk.StringVar()
        self.status_lbl = tk.Label(
            card, textvariable=self.status_var,
            font=FONT_SMALL, bg=BG_CARD, fg=ACCENT
        )
        self.status_lbl.pack(anchor="w", pady=(6, 0))

    # ── Stats Bar ──────────────────────────────────────────────────────────────

    def _build_stats_bar(self) -> None:
        self.stats_frame = tk.Frame(self.root, bg=BG_DARK, padx=20)
        self.stats_frame.pack(fill="x", pady=(0, 4))
        self.stats_var = tk.StringVar()
        tk.Label(
            self.stats_frame, textvariable=self.stats_var,
            font=FONT_SMALL, bg=BG_DARK, fg=TEXT_MUTED
        ).pack(anchor="w")
        self._update_stats()

    def _update_stats(self) -> None:
        total  = len(tasks)
        done   = sum(1 for t in tasks if t["done"])
        high   = sum(1 for t in tasks if t["priority"] == "High" and not t["done"])
        self.stats_var.set(
            f"Total: {total}   ✔ Done: {done}   ⏳ Pending: {total - done}   🔴 High: {high}"
        )

    # ── Task List ──────────────────────────────────────────────────────────────

    def _build_task_list(self) -> None:
        container = tk.Frame(self.root, bg=BG_DARK, padx=20)
        container.pack(fill="both", expand=True)

        tk.Label(container, text="Tasks", font=FONT_BOLD,
                 bg=BG_DARK, fg=TEXT_PRIMARY).pack(anchor="w", pady=(0, 4))

        # Scrollable canvas
        canvas_wrapper = tk.Frame(container, bg=BG_CARD, relief="flat")
        canvas_wrapper.pack(fill="both", expand=True)

        self.canvas     = tk.Canvas(canvas_wrapper, bg=BG_CARD, highlightthickness=0)
        scrollbar       = tk.Scrollbar(canvas_wrapper, orient="vertical",
                                       command=self.canvas.yview)
        self.task_frame = tk.Frame(self.canvas, bg=BG_CARD)

        self.task_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left",  fill="both", expand=True, padx=8, pady=8)
        scrollbar.pack(side="right", fill="y")

        # Mouse-wheel scroll
        self.canvas.bind_all("<MouseWheel>",
                             lambda e: self.canvas.yview_scroll(-1*(e.delta//120), "units"))

        self._refresh_list()

    def _refresh_list(self) -> None:
        render_task_list(self.task_frame, self._handle_toggle, self._handle_delete)
        self._update_stats()

    # ── Footer ─────────────────────────────────────────────────────────────────

    def _build_footer(self) -> None:
        footer = tk.Frame(self.root, bg=BG_DARK, pady=10)
        footer.pack(fill="x")
        tk.Label(
            footer, text="Press Enter or click '+ Add Task' to add  •  Built with Python & Tkinter",
            font=FONT_SMALL, bg=BG_DARK, fg=TEXT_MUTED
        ).pack()

    # ── Event Handlers ─────────────────────────────────────────────────────────

    def _handle_add(self) -> None:
        name     = self.task_entry.get()
        priority = self.priority_var.get()
        ok, msg  = add_task(name, priority)
        self.status_var.set(msg)
        if ok:
            self.task_entry.delete(0, tk.END)
            self.task_entry.focus()
        self._refresh_list()

    def _handle_toggle(self, index: int) -> None:
        toggle_task(index)
        self._refresh_list()

    def _handle_delete(self, index: int) -> None:
        task_name = tasks[index]["task"]
        if messagebox.askyesno("Delete Task", f"Delete '{task_name}'?"):
            delete_task(index)
            self._refresh_list()

# ── Entry Point ────────────────────────────────────────────────────────────────

def main() -> None:
    root = tk.Tk()

    # Style the Combobox
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TCombobox",
                    fieldbackground=BG_INPUT,
                    background=BG_INPUT,
                    foreground=TEXT_PRIMARY,
                    selectbackground=BG_INPUT,
                    selectforeground=TEXT_PRIMARY)

    app = ToDoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()