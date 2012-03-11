"""A simple checkers GUI written in python/ncurses
Ben Hartman 3/10/2012
"""

import curses, traceback
if __name__= '__main__':
	try:
# Initialize curses
		stdscr=curses.initscr()
# Turn off echoing of keys, and enter cbreak mode,
# where no buffering is performed on keyboard input
		curses.noecho()
		curses.cbreak()

# In keypad mode, escape sequences for special keys
# (like the cursor keys) will be interpreted and
# a special value like curses.KEY_LEFT will be returned
		stdscr.keypad(1)
		#main(stdscr)                    # Enter the main loop
# Set everything back to normal
		stdscr.keypad(0)
		curses.echo()
		curses.nocbreak()
		curses.endwin()                 # Terminate curses
	except:
# In event of error, restore terminal to sane state.
		stdscr.keypad(0)
		curses.echo()
		curses.nocbreak()
		curses.endwin()
		traceback.print_exc()           # Print the exception
