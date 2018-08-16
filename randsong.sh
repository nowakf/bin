#!/bin/sh

mpc listall | shuf -n 1 | mpc add; mpc play


