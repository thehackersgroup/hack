def timestampToDateTime(t):
    import datetime
    return datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S.%f')