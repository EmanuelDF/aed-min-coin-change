## Minimum coin change algorithm

Given in a sale you must return change with the fewest coins as possible.

__Input__:

- An integer value N is the amount of currency values in the monetary system of a fictional country.
- N real values corresponding to the currencies of the monetary system, already sorted in descending order,
  in a single line separated by blanks.
- Two numbers float bill entry amount and purchase amount, separated by whitespace.

__Output__:

- The coins used per line, starting with the coin with the highest value.

Example 1:

- __Input__:
  ```
  4
  0.25 0.10 0.05 0.01
  1.00 0.37
  ```
- __Output__
  ```
  0.25
  0.25
  0.10
  0.01
  0.01
  0.01
  ```

Example 2:

- __Input__:
  ```
  5
  0.25 0.21 0.10 0.05 0.01
  1.00 0.37
  ```
- __Output__
  ```
  0.21
  0.21
  0.21
  ```