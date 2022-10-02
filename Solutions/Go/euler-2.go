package main

import (
	"fmt"
	"math"
)

func main() {
	var (
		a      float64 = 2
		result float64 = a
	)

	for (a * math.Pow(math.Phi, 3)) < 4000000 {
		a = math.Round(a * math.Pow(math.Phi, 3))
		result += a
	}

	fmt.Printf("%.0f\n", result)
}
