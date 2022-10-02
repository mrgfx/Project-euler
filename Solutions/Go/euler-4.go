package main

import (
	"fmt"
)

func isPalindrome(n int) bool {
	remainder := 0
	reverse := 0
	nTemp := n

	for nTemp != 0 {
		remainder = nTemp % 10
		reverse = reverse*10 + remainder
		nTemp /= 10
	}

	if n != reverse {
		return false
	}

	return true
}

func main() {
	largest := 0

	for i := 1000; i >= 100; i-- {
		for j := 1000; j >= 100; j-- {
			n := i * j
			if largest < n {
				if isPalindrome(n) {
					largest = n
				}
			}
		}
	}

	fmt.Println(largest)
}
