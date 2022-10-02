package main

import (
	"fmt"
	"math"
)

func main() {
	var limit float64 = 100
	sumOfSquares := math.Pow(limit*(1+limit)/2, 2)
	squareOfSum := math.Pow(limit, 3)/3 + math.Pow(limit, 2)/2 + limit/6

	fmt.Printf("%.0f\n", sumOfSquares-squareOfSum)
}
