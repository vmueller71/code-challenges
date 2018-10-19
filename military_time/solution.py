"""
Convert a time string of the format hh:mm:ssAM or hh:mm:ssPM (07:02:57AM or 10:12:09PM)
into military time (24h).
Special rules apply:
midnight: 12:00:00AM (12h) => 00:00:00 (24h)
noon: 12:00:00PM (12h) => 12:00:00 (24h)

examples:
militaryTime("09:12:41AM") returns "09:12:41"
militaryTime("04:31:51PM") returns "16:31:51"
"""


def militaryTime(s):
    if s[:2] == '12':
        if s[-2:] == "AM":
            return '00' + s[2:-2]
        else:
            return s[:-2]
    elif s[-2:] == "AM":
        return s[:-2]
    else:
        return str(int(s[:2]) + 12) + s[2:-2]
    