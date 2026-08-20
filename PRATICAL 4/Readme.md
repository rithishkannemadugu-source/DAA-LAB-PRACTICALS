| Case         | Complexity | Explanation                                             |
| ------------ | ---------- | ------------------------------------------------------- |
| Best Case    | **O(1)**   | When `num = 0`, the loop does not execute.              |
| Average Case | **O(n)**   | For a general positive number, the loop runs `n` times. |
| Worst Case   | **O(n)**   | The loop runs `n` times.                                |

| Type            | Complexity | Explanation                                                               |
| --------------- | ---------- | ------------------------------------------------------------------------- |
| Auxiliary Space | **O(1)**   | Only a fixed number of variables (`num`, `fact`, `i`, `result`) are used. |
| Input Space     | **O(1)**   | Only one integer input is stored.                                         |
| Total Space     | **O(1)**   | No additional data structure is created.                                  |
Final: Time = O(n), Space = O(1).

Conclusion

The program successfully calculates the factorial of a given non-negative number using a function and an iterative loop. It handles the special case of 0! = 1 and returns the calculated factorial to the calling statement. The algorithm requires O(n) time complexity and O(1) space complexity.