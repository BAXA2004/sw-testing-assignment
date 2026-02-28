# Testing Strategy

## Overview

This project applies structured testing techniques to validate the correctness of a simple calculator application.

Both unit testing and integration testing were implemented using pytest.

---

## Unit Testing

Unit tests were written to verify each calculator function independently:

- add()
- sub()
- mul()
- div()
- clear()

Edge cases tested:
- Division by zero
- Negative numbers
- Decimal values

All unit tests pass successfully.

---

## Integration Testing

Integration tests verify that multiple functions work correctly together.

Examples:

1. Addition followed by multiplication
2. Division followed by clear operation

These tests ensure correct interaction between calculator operations.

---

## Black-box Testing

Black-box testing was applied by focusing on input-output behavior without considering internal implementation details.

Example:
- div(5, 0) should raise an exception

---

## White-box Testing

White-box testing ensured that internal logic paths were executed:

- Zero-division conditional branch
- Arithmetic operations flow

---

## Regression Testing

After adding integration tests and configuration updates, the full pytest suite was executed to confirm that previous functionality remained stable.

---

## Test Results Summary

All tests pass successfully:

- 8 unit tests
- 2 integration tests

Total: 10 tests passed