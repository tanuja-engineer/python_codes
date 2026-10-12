def analyze_marks(*args):
    if len(args)==0:
        print("no mrks supplied")
        return
    total=0
    highest=args[0]
    passing=0
    for marks in args:
        total=total+marks
        if marks>highest:
            highest=marks
        if marks>=40:
            passing=passing+1
    average=total/len(args)
    print("total marks:",total)
    print("average marks:",average)
    print("highest marks:",highest)
    print("passing marks:",passing)
analyze_marks(75,35,80,45,30)

    