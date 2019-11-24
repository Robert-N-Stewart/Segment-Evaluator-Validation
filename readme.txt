Robert Stewart 

Reads two log files of cookies and segments and finds the difference between associated segments and cookies

Preconditions: log files must be in specified regex format of .*evaluated: \([[:alnum:]]*\).*\[\(.*\)\]
Postconditions: Outputs Segments with added cookies, Segments with missing cookies, Cookies in extra segments, Cookies omitted from segments, and all associated cookies and segments

Files: 
	driver.sh - Must pass path to log files. First input being the baseline.
	compareLogs.py - Assigns cookies and segments to associated dicts. And produces desired output

