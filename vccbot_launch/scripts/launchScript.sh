#!/usr/bin/env bash
sudo -u ubuntu parallel -j0 bash :::: <(ls script{1..2}.sh)
