# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
import sys


def main():
    # prepare list of exact square numbers less than 10000
    squares = []
    for i in range(1, 100):
        squares.append(i * i)

    # group numbers by digits
    s1, s2, s3, s4 = 0, 0, 0, 0

    for i in range(len(squares)):
        if s2 == 0 and squares[i] >= 10:
            s2 = i
        if s3 == 0 and squares[i] >= 100:
            s3 = i
        if s4 == 0 and squares[i] >= 1000:
            s4 = i

    #print "index of square numbers grouping by digits:"
    #print "[%d, %d, %d, %d]\n" % (s1, s2, s3, s4)

    print "\n# exact square numbers:\n"
    print "1: %s" % squares[s1:s2]
    print "2: %s" % squares[s2:s3]
    print "3: %s" % squares[s3:s4]
    print "4: %s\n" % squares[s4:]

    # construct the candidate and validate
    answers = []
    for i in range(s1, s2):
        for j in range(s2, s3):
            for k in range(s3, s4):
                for l in range(s4, len(squares)):
                    candidate = "%d%d%d%d" % (squares[i], squares[j], squares[k], squares[l])

                    # validate
                    digits = []
                    for c in candidate:
                        if c in digits:
                            # digit is used more than once
                            break
                        digits.append(c)

                    if len(digits) == 10:
                        # every digit is used exact once
                        answers.append(candidate)
                        #print candidate

    print "# answers:\n"
    for i in answers:
        print "%s %s %s %s" % (i[0], i[1:3], i[3:6], i[6:])
    print


if __name__ == '__main__':
    import traceback

    try:
        main()

    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
