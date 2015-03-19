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
        -c	Option c
        -h	show this help

    EXAMPLE:
        $PROGNAME -b other -a something more commmand line args
        Output:
            OPTION_A: something
            OPTION_B: other
            OPTION_C: repeatable args
            Extra Arguments: more command line args
EOF
}

cmdline() {
    local OPTIND=1
    while getopts "ha:b:c:" OPTION
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
            c)
                OPTION_C+=("$OPTARG")
                ;;
        esac
    done
    shift $((OPTIND-1))
    extras="$@"
}

main() {
    local OPTION_A OPTION_B OPTION_C extras
    cmdline $ARGS
    if [[ -n $OPTION_A ]]; then
        echo 'OPTION_A: '$OPTION_A
    fi
    if [[ -n $OPTION_B ]]; then
        echo 'OPTION_B: '$OPTION_B
    fi
    local OPTION_C_apend
    for val in "${OPTION_C[@]}"; do
        OPTION_C_append+=("-c $val")
    done
    if [[ -n $OPTION_C ]]; then
        echo 'OPTION_C: '${OPTION_C[@]}
        echo 'OPTION_C_append: '${OPTION_C_append[@]}
    fi
    echo 'Extra Arguments: '${extras[@]}
}

main
