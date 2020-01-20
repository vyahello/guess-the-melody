#!/usr/bin/env bash

PACKAGE="quiz"


check-black() {
    printf "Start black analysis ...\n" && ( black --check ${PACKAGE} )
}


check-unittests() {
    printf "Start unittests analysis ...\n" && pytest
}


main() {
    check-black && check-unittests
}


main