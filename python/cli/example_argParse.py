import argparse

#python example_argParse.py -a 16543 -b True -c 3 "Positional" --multiple "m1" -m "m2" -b2
def str2bool(stringArg):
    if stringArg.lower() in ['yes', 'y', 'true', 't', '1']:
        return True
    elif stringArg.lower() in ['no', 'n', 'false', 'f', '0']:
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def parseArguments():
    parser = argparse.ArgumentParser(description="")
    # positional args
    parser.add_argument('positional1', action='store', type=str, help="")
    parser.add_argument('positional2', type=str, help="")
    # non-positional args
    parser.add_argument('-a', dest="number", type=int, help="")
    parser.add_argument('-b', dest="boolean", required=False, default=False, type=str2bool, help="")
    parser.add_argument('-b2', dest="boolean2", required=False, default=True, action='store_false', help="")
    parser.add_argument('-c', '--command', type=str, required=True, help="")
    parser.add_argument('-m', '--multiple', type=str, action='append', help="")

    # parser.add_subparsers()

    return parser


if __name__ == '__main__':
    parser = parseArguments()
    # unknown args and positional args don't mix well
    # options, unknown = parser.parse_known_args()
    # if unknown:
        # print "unknown:", unknown
    options = parser.parse_args()
    print "Required positional example 1:", options.positional1
    print "Required positional example 2:", options.positional2
    if "number" in options:
        print "Number example:", options.number
    if "boolean" in options:
        print "Boolean example:", options.boolean
    if "boolean2" in options:
        print "Boolean example 2:", options.boolean2
    if "multiple" in options:
        print options.multiple
    print "Print all example:", options
