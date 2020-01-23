#!/usr/bin/env bash

PACKAGE="quiz"


--check-box() {
    printf "Start ${1} analysis ...\n"
}


check-black() {
    --check-box "black" && ( black --check ${PACKAGE} )
}


check-flake8() {
    --check-box "flake" && ( flake8 ${PACKAGE} )
}


check-unittests() {
    --check-box "unittest" && pytest
}


main() {
    check-black && check-flake8 && check-unittests
}


main