package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n < 2 {
		return false
	}

	if n == 2 || n == 3 {
		return true
	}

	if n%2 == 0 || n%3 == 0 {
		return false
	}

	limit := math.Floor(math.Sqrt(float64(n))) + 2

	for i := 6; i <= int(limit); i += 6 {
		if n%(i-1) == 0 || n%(i+1) == 0 {
			return false
		}
	}

	return true
}

func main() {
	seen := 0
	n := 1

	for seen < 10001 {
		n += 1
		if isPrime(n) {
			seen += 1
		}
	}

	fmt.Println(n)
}
