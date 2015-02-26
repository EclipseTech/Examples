#!/bin/bash -e

readonly PROGNAME=$(basename $0)
readonly PROGDIR=$(readlink -m $(dirname $0))
readonly ARGS="$@"

usage() {
    cat <<-EOF
    Usage: $PROGNAME options

    Example cmd line args

    OPTIONS:
        -a	Option a
        -b	Option b
        -h	show this help

    EXAMPLE:
        $PROGNAME -b other -a something more commmand line args
        Output:
            OPTION_A: something
            OPTION_B: other
            Extra Arguments: more command line args
EOF
}

cmdline() {
    local OPTIND=1
    while getopts "ha:b:" OPTION
    do
        case $OPTION in
            h)
                usage
                exit 0
                ;;
            a)
                OPTION_A=${OPTARG}
                ;;
            b)
                OPTION_B=${OPTARG}
                ;;
        esac
    done
    shift $((OPTIND-1))
    extras="$@"
}

main() {
    local OPTION_A OPTION_B extras
    cmdline $ARGS
    if [[ -n $OPTION_A ]]; then
        echo 'OPTION_A: '$OPTION_A
    fi
    if [[ -n $OPTION_B ]]; then
        echo 'OPTION_B: '$OPTION_B
    fi
    echo 'Extra Arguments: '$extras
}

main
