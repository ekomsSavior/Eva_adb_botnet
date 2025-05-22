import curses
import json
import time
import os
from glob import glob

STATE_FILES = glob("bots/*/jeangrey_state.json")

def load_states():
    states = []
    for filepath in glob("bots/*/jeangrey_state.json"):
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                states.append(data)
        except:
            continue
    return states

def draw_dashboard(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    while True:
        stdscr.erase()
        stdscr.border(0)
        stdscr.addstr(1, 2, "EVA LIVE BOT DASHBOARD", curses.A_BOLD)
        stdscr.addstr(2, 2, "ID".ljust(15) + "IP".ljust(18) + "Tags".ljust(30) + "Last Seen")
        bots = load_states()
        for idx, bot in enumerate(bots):
            stdscr.addstr(4 + idx, 2, f"{bot.get('bot_id', '-')[:14].ljust(15)}{bot.get('ip', '-')[:17].ljust(18)}{','.join(bot.get('tags', []))[:29].ljust(30)}{bot.get('last_seen', '-')}")
        stdscr.addstr(curses.LINES - 2, 2, "[Ctrl+C to exit] Refreshing every 3s...")
        stdscr.refresh()
        time.sleep(3)

def main():
    curses.wrapper(draw_dashboard)

if __name__ == "__main__":
    main()
