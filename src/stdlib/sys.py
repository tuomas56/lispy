import sys

def register(state):
	for name in dir(sys):
		if not name.startswith("__"):
			wrap(getattr(sys, name), "sys.%s" % name, state)
	return state