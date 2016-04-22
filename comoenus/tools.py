from datetime import datetime


def login(username, password):
    pass


def time_ago(timestamp):
    seconds = int((
            datetime.utcnow()-timestamp
        ).total_seconds())
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    weeks = days / 7
    months = days / 30
    years = days / 365

    time_ago = None

    #seconds
    if seconds < 60:
        if seconds <= 1:
            time_ago = "a second ago"
        else:
            time_ago = "%s seconds ago" % seconds
    #minutes
    elif seconds >= 60:
        if seconds == 60:
            time_ago = "%s minute ago" % minutes
        elif seconds > 60 and seconds < 3600:
            time_ago = "%s minutes ago" % minutes

        #hours
        elif minutes >= 60:
            if hours == 1:
                time_ago = "%s hour ago" % hours
            elif hours > 1 and hours < 24:
                time_ago = "%s hours ago" % hours

            #days
            elif hours >= 24:
                if days == 1:
                    time_ago = "%s day ago" % days
                elif days > 1 and days < 7:
                    time_ago = "%s days ago" % days

                #weeks
                elif days >= 24:
                    if weeks == 1:
                        time_ago = "%s week ago" % weeks
                    elif weeks > 1 and weeks < 4:
                        time_ago = "%s weeks ago" % weeks

                    #months
                    elif days >= 30:
                        if months == 1:
                            time_ago = "%s month ago" % months
                        elif months > 1 and months < 12:
                            time_ago = "%s day ago" % months

                        #years
                        elif days >= 365:
                            if years == 1:
                                time_ago = "%s year ago" % years
                            else:
                                time_ago = "%s years ago" % years

    return time_ago
