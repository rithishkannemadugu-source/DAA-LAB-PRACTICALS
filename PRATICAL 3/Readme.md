## Time Complexity

| Case | Time Complexity |
|---|---:|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

### Overall Time Complexity: O(n log n)

## Space Complexity

| Type | Space Complexity |
|---|---:|
| Auxiliary Space | O(log n) |
| In-place | Yes |

### Overall Space Complexity: O(log n)

## Conclusion

Heap Sort is an efficient comparison-based sorting algorithm that uses a Max Heap to sort the elements in ascending order. It first builds a Max Heap and then repeatedly moves the largest element to the end of the array.

The algorithm has a time complexity of **O(n log n)** in the best, average, and worst cases. It sorts the array in-place without requiring an additional array. However, because the `max_heap()` function is implemented recursively, the auxiliary space complexity is **O(log n)** due to the recursion stack.

Overall, Heap Sort is useful when predictable **O(n log n)** performance and in-place sorting are required.