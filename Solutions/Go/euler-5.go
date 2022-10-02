package main

import (
	"fmt"
	"math"
)

func generatePrimes(upperLimit int) []int {
	primes := []int{}
	isPrime := false
	j := 0

	primes = append(primes, 2)
	for i := 3; i <= upperLimit; i += 2 {
		j = 0
		isPrime = true
		for primes[j]*primes[j] <= i {
			if i%primes[j] == 0 {
				isPrime = false
				break
			}
			j++
		}
		if isPrime {
			primes = append(primes, i)
		}
	}
	return primes
}

func main() {
	var (
		divisorMax int   = 20
		result     int   = 1
		p          []int = generatePrimes(divisorMax)
	)

	for i := 0; i < len(p); i++ {
		a := int(math.Floor(math.Log(float64(divisorMax)) / math.Log(float64(p[i]))))
		result = result * int(math.Pow(float64(p[i]), float64(a)))
	}
	fmt.Println(result)
	return
}
