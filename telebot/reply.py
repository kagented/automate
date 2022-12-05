import task

def sample(input_text):
    usermsg = str(input_text).lower()

    if usermsg == '말씀':
        return task.show_scripture()