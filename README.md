# Week 6 Assignment: Times Tables, Skip Counting & Loop Hospital

This repository contains my Week 6 Python assignment focusing on `range()`, loops, skip counting, and debugging common loop errors.

## Files

* `times_table.py` — asks the user for a number and prints its multiplication table from 1 to 10.
* `skip_counter.py` — uses `range()` with positive and negative steps to print even numbers and a countdown.
* `loop_hospital.py` — fixes three faulty loops involving an off-by-one error, an infinite loop, and a misplaced accumulator.
* `screenshots/` — contains screenshots showing the programs running successfully.

## What Is an Off-by-One Error?

An off-by-one error happens when a loop repeats one time too many or one time too few. This commonly happens because Python's `range()` excludes the stop value.

A useful habit is to remember that the `range()` stop value is not included and to check the first and last values produced by the loop before running the program.
