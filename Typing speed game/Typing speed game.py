from time import time  # to record the time


# Now to calculate the accuracy of input prompt
def tp_error(prompt):
    global inwords

    words = prompt.split()
    errors = 0
    for i in range(len(inwords)):
        if i in (0, len(inwords) - 1):
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors + 1
        else:
            if inwords[i] == words[i]:
                if inwords[i + 1] == words[i + 1] and inwords[i - 1] == words[i - 1]:
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors


# now to calculate the speed of typing words per minute
def speed(inprompt, stime, etime):
    global time
    global inwords
    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time

    return speed


# calculate the total elasped time
def elasped_time(stime, etime):
    time = etime - stime  # etime is the end time and stime is the start time
    return time


if __name__ == '__main__':
    prompt = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. " \
             "Its high-level built in data structures, combined with dynamic typing and dynamic binding, " \
             "make it very attractive for Rapid Application Development, as well as for use as a scripting or " \
             "glue language to connect existing components together."
# this was the paragraph which you have to type to check your speed
    print("Type This :-", prompt)

    # checking to input Enter basically it will see
    input("Press Enter when you are ready to check your speed !!!")

    # recording time for input
    stime = time()
    inprompt = input()
    etime = time()

    # collect all the information returned
    time = round(elasped_time(stime, etime), 2)  # round off the time
    speed = speed(inprompt, stime, etime)
    errors = tp_error(prompt)

    # printing all the required data to see result
    print("########################################################################")
    print("Total time elapsed : ", time, "seconds")
    print("Your Average typing speed was ", speed, "words per minute (w/m)")
    print("With the total of ", errors, "errors")
    print("#######################################################################")
