from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox, font, scrolledtext, simpledialog, colorchooser
import time
from datetime import timedelta


FONT_SIZE=20
PADX=5
PADY=3
BORDER=2
AUTO_START=False
DEFAULT_NAME="Simple Stopwatch"
FG_COLOR="black"
BG_COLOR="white"
HL_FG_COLOR="black"
HL_BG_COLOR="green"

class ConfigWindow(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.auto_start=BooleanVar(master=self,value=auto_start.get())
        self.default_name=StringVar(master=self,value=default_name.get())
        self.fg=fg_color.get()
        self.bg=bg_color.get()
        self.hl_fg=hl_fg_color.get()
        self.hl_bg=hl_bg_color.get()
        # frames
        self.new_name_frame = Frame(master=self, borderwidth=BORDER, relief=GROOVE)
        self.new_name_frame.pack(expand=True, fill=BOTH, side=TOP)
        self.auto_start_frame = Frame(master=self, borderwidth=BORDER, relief=GROOVE)
        self.auto_start_frame.pack(expand=True, fill=BOTH, side=TOP,after=self.new_name_frame)
        self.color_frame = Frame(master=self, borderwidth=BORDER, relief=GROOVE)
        self.color_frame.pack(expand=True, fill=BOTH, side=TOP, after=self.auto_start_frame)
        self.hl_color_frame = Frame(master=self, borderwidth=BORDER, relief=GROOVE)
        self.hl_color_frame.pack(expand=True, fill=BOTH, side=TOP, after=self.color_frame)
        self.button_frame = Frame(master=self)
        self.button_frame.pack(expand=True, fill=BOTH, side=BOTTOM)
        # new_name_frame elements
        self.text_label = Label(master=self.new_name_frame, text="Name of New Stopwatch: ", padding=(PADX,0,PADX,PADY))
        self.text_label.pack(side=LEFT)
        self.default_name_label = Label(master=self.new_name_frame, textvariable=self.default_name, padding=(PADX,0,PADX,PADY), borderwidth=BORDER, relief=SUNKEN)
        self.default_name_label.pack(side=LEFT, after=self.text_label)
        self.change_button = Button(master=self.new_name_frame, text="Change", command=self._change_name)
        self.change_button.pack(side=RIGHT)
        # auto_start_frame elements
        self.auto_start_checkbox = Checkbutton(
            master=self.auto_start_frame,
            offvalue=False,
            onvalue=True,
            variable=self.auto_start,
            text="auto start the new stopwatch after it is added",
            padding=(PADX,0,PADX,PADY)
        )
        self.auto_start_checkbox.pack(side=LEFT)
        # color_frame elements
        self.color_label = Label(master=self.color_frame, text="Current Label Color", foreground=self.fg, background=self.bg, padding=(PADX,0,PADX,PADY), borderwidth=BORDER, relief=SUNKEN)
        self.color_label.pack(side=LEFT)
        self.fg_change_button = Button(master=self.color_frame, text="Change Foreground", command=self._fg_color_change)
        self.fg_change_button.pack(side=RIGHT, after=self.color_label)
        self.bg_change_button = Button(master=self.color_frame, text="Change Background", command=self._bg_color_change)
        self.bg_change_button.pack(side=RIGHT)
        # hl_color_frame elements
        self.hl_color_label = Label(master=self.hl_color_frame, text="Current Highlight Label Color", foreground=self.hl_fg, background=self.hl_bg, padding=(PADX,0,PADX,PADY), borderwidth=BORDER, relief=SUNKEN)
        self.hl_color_label.pack(side=LEFT)
        self.hl_fg_change_button = Button(master=self.hl_color_frame, text="Change Foreground", command=self._hl_fg_color_change)
        self.hl_fg_change_button.pack(side=RIGHT, after=self.hl_color_label)
        self.hl_bg_change_button = Button(master=self.hl_color_frame, text="Change Background", command=self._hl_bg_color_change)
        self.hl_bg_change_button.pack(side=RIGHT)
        # button_frame elements
        self.reset_button = Button(master=self.button_frame, text="Reset", command=self._reset)
        self.reset_button.pack(side=LEFT)
        self.apply_button = Button(master=self.button_frame, text="Apply", command=self._apply)
        self.apply_button.pack(side=RIGHT)
        self.done_button = Button(master=self.button_frame, text="Done", command=self._destroy)
        self.done_button.pack(side=RIGHT,before=self.apply_button)
    def _change_name(self):
        new_name = simpledialog.askstring(title="Change Default Name of New Stopwatch", prompt="Default Name:", initialvalue=self.default_name.get())
        if new_name:
            self.default_name.set(new_name)
    def _fg_color_change(self):
        (rgb, new_fg) = colorchooser.askcolor(initialcolor=self.fg, parent=self.color_frame, title="Choose Foreground Color")
        if new_fg:
            self.fg = new_fg
            self.color_label.config(foreground=self.fg)
    def _bg_color_change(self):
        (rgb, new_bg) = colorchooser.askcolor(initialcolor=self.bg, parent=self.color_frame, title="Choose Background Color")
        if new_bg:
            self.bg = new_bg
            self.color_label.config(background=self.bg)
    def _hl_fg_color_change(self):
        (rgb, new_hl_fg) = colorchooser.askcolor(initialcolor=self.hl_fg, parent=self.hl_color_frame, title="Choose Highlight Foreground Color")
        if new_hl_fg:
            self.hl_fg = new_hl_fg
            self.hl_color_label.config(foreground=self.hl_fg)
    def _hl_bg_color_change(self):
        (rgb, new_hl_bg) = colorchooser.askcolor(initialcolor=self.hl_bg, parent=self.hl_color_frame, title="Choose Highlight Background Color")
        if new_hl_bg:
            self.hl_bg = new_hl_bg
            self.hl_color_label.config(background=self.hl_bg)
    def _reset(self):
        self.auto_start.set(AUTO_START)
        self.default_name.set(DEFAULT_NAME)
        self.fg=FG_COLOR
        self.bg=BG_COLOR
        self.hl_fg=HL_FG_COLOR
        self.hl_bg=HL_BG_COLOR
        self.color_label.config(foreground=self.fg, background=self.bg)
        self.hl_color_label.config(foreground=self.hl_fg, background=self.hl_bg)
    def _apply(self):
        auto_start.set(self.auto_start.get())
        default_name.set(self.default_name.get())
        fg_color.set(self.fg)
        bg_color.set(self.bg)
        hl_fg_color.set(self.hl_fg)
        hl_bg_color.set(self.hl_bg)
        for watch in stop_watches:
            watch.update_color()
    def _destroy(self):
        self._apply()
        self.destroy()


class Stopwatch(Frame):
    def __init__(self, master, create_name, start):
        super().__init__(master)
        self.defaultFont=font.nametofont("TkDefaultFont")
        self.defaultFont.config(size=FONT_SIZE,weight=font.BOLD)
        self.pack(expand=True,fill=BOTH)
        self.bg=bg_color.get()
        self.fg=fg_color.get()
        self.hl_bg=hl_bg_color.get()
        self.hl_fg=hl_fg_color.get()
        self.label_name=StringVar()
        self.label_name.set(create_name)
        self.is_running=start
        # epoch
        self.start_time=DoubleVar()
        # monotonic
        self.this_time=DoubleVar()
        # this period length
        self.elapsed_time=DoubleVar()
        # sum of past periods in seconds
        self.past_time=DoubleVar()
        self.tosep = Separator(master=self, orient=HORIZONTAL)
        self.tosep.pack(expand=True,fill=BOTH,side=TOP)
        self.name_label=Label(master=self, padding=(PADX,0,PADX,PADY), foreground=self.fg, background=self.bg)
        self.name_label.config(textvariable=self.label_name)
        self.name_label.pack(expand=True,fill=BOTH,side=LEFT)
        self.name_time_sep=Separator(master=self,orient=VERTICAL)
        self.name_time_sep.pack(fill=Y, after=self.name_label,side=LEFT)
        self.time_label=Label(master=self, text="0:00:00", padding=(PADX,0,PADX,PADY), foreground=self.fg, background=self.bg)
        self.time_label.pack(after=self.name_time_sep,side=LEFT)
        self.time_button_sep=Separator(master=self,orient=VERTICAL)
        self.time_button_sep.pack(fill=Y, after=self.time_label, side=LEFT)
        self.log=[("Start","End","Length","Total")]
        self.delete_button=Button(master=self, text="Delete", command=self._delete)
        self.delete_button.pack(side=RIGHT)
        self.rename_button=Button(master=self, text="Rename", command=self._rename)
        self.rename_button.pack(after=self.delete_button,side=RIGHT)
        self.log_button=Button(master=self, text="Log", command=self._show_log)
        self.log_button.pack(after=self.rename_button,side=RIGHT)
        self.key_button=Button(master=self, text="Start", command=self._start)
        self.key_button.pack(after=self.log_button, side=RIGHT)
        if self.is_running:
            self._start()
    def update_color(self):
        self.fg=fg_color.get()
        self.bg=bg_color.get()
        self.hl_fg=hl_fg_color.get()
        self.hl_bg=hl_bg_color.get()
        if self.is_running:
            fg=self.hl_fg
            bg=self.hl_bg
        else:
            fg=self.fg
            bg=self.bg
        for widget in [self.name_label, self.time_label]:
            widget.config(foreground=fg, background=bg)
    def _print_time(self, double_value):
        return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(double_value))
    def _print_interval(self, double_value):
        return str(timedelta(seconds=int(double_value)))
    def _rename(self):
        new_name = simpledialog.askstring(
            title=f"Rename this Stopwatch: {self.label_name.get()}",
            prompt="New Name:",
            initialvalue=self.label_name.get(),
            parent=self
            )
        self.label_name.set(new_name)
    def _start(self):
        self.is_running=True
        self.start_time.set(time.time())    
        self._resume()
    def _resume(self):
        self.is_running=True
        self.update_color()
        self.this_time.set(time.monotonic())
        self.key_button.config(text="Pause",command=self._pause)
        self._update_time()
    def _pause(self):
        if self.is_running:
            self.key_button.config(text="Resume",command=self._resume)
            self.is_running=False
            self.update_color()
            self.elapsed_time.set(time.monotonic() - self.this_time.get())
            self.past_time.set(self.past_time.get() + self.elapsed_time.get())
            self.log.append(
                (
                    self._print_time(self.start_time.get()),
                    self._print_time(self.start_time.get()+self.elapsed_time.get()),
                    self._print_interval(self.elapsed_time.get()),
                    self._print_interval(self.past_time.get()),
                )
            )
    def _update_time(self):
        if self.is_running:
            self.elapsed_time.set(time.monotonic() - self.this_time.get())
            self.time_label.config(
                text=self._print_interval(
                        self.past_time.get()
                        + self.elapsed_time.get()
                    )
                )
            self.time_label.after(521, self._update_time)
    def _show_log(self):
        popup = Toplevel(master=self)
        def _destroy():
            popup.destroy()
        popup.title(f"{self.label_name.get()} logs")
        message=map(lambda x: '\t\t\t'.join(x), self.log)
        content = scrolledtext.ScrolledText(master=popup,height=50,width=100)
        for line in message:
            content.insert(END,line+"\n")
        content.config(state=DISABLED)
        content.pack(side=TOP)
        close = Button(master=popup, text="Close", command=_destroy)
        close.pack(side=BOTTOM)
    def _delete(self):
        flag = messagebox.askyesno(
            title="Deletion Warning",
            message=f"Do you want to delete {self.label_name.get()}",
            parent=self
        )
        if flag:
            stop_watches.remove(self)
            self.destroy()


def add_stopwatch():
    if stop_watches:
        toadd_name = simpledialog.askstring(title="Add New Stopwatch", prompt="Name:", parent=window)
        if not toadd_name:
            num_idx = 0
            current_names = map(lambda x:x.label_name.get(),stop_watches)
            toadd_name = f"{default_name.get()}"
            while (toadd_name in current_names):
                num_idx += 1
                toadd_name = f"{default_name.get()} {num_idx}"
    else:
        toadd_name = default_name.get()
    toadd = Stopwatch(master=window, create_name=toadd_name, start=auto_start.get())
    stop_watches.append(toadd)
    toadd.pack(side='top',before=section_sep)

def config_func():
    config_window = ConfigWindow(master=window)
    config_window.title("Settings")

if __name__=='__main__':
    # Create the main window
    window = Tk()
    window.title("Daily Multi-StopWatch")
    stop_watches=[]
    auto_start=BooleanVar(master=window, value=AUTO_START)
    default_name=StringVar(master=window, value=DEFAULT_NAME)
    fg_color=StringVar(value=FG_COLOR)
    bg_color=StringVar(value=BG_COLOR)
    hl_fg_color=StringVar(value=HL_FG_COLOR)
    hl_bg_color=StringVar(value=HL_BG_COLOR)
    section_sep = Separator(master=window,orient=HORIZONTAL)
    section_sep.pack(expand=True,fill=BOTH,side=TOP)
    add_button = Button(master=window, text="Add",command=add_stopwatch)
    add_button.pack(side=LEFT)
    config_button = Button(master=window, text="Config",command=config_func)
    config_button.pack(side=LEFT, after=add_button)
    add_stopwatch()
    # Run the main loop
    window.mainloop()