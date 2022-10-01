package main

import (
	"fmt"
	"math"
	"sort"
)

func isPrime(n float64) bool {
	for i := float64(2); i <= math.Floor(math.Sqrt(n))+1; i++ {
		if math.Mod(n, i) == 0 {
			return false
		}
	}

	return true
}

func largestPrimeNumber(n float64) float64 {
	factors := []float64{}

	sort.Slice(factors, func(i, j int) bool {
		return factors[i] < factors[j]
	})

	for i := float64(2); i <= math.Floor(math.Sqrt(n))+1; i++ {
		if isPrime(i) {
			if math.Mod(n, i) == 0 {
				pair := n / i
				factors = append(factors, i)
				if isPrime(pair) {
					factors = append(factors, pair)
				}
			}
		}
	}

	if len(factors) == 0 {
		return 0
	}

	return factors[len(factors)-1]
}

func main() {
	fmt.Println(largestPrimeNumber(600851475143))
}
