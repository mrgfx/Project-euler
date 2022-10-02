package main

import (
	"fmt"
	"math"
)

func arithmeticSeries(step, limit float64) float64 {
	first := step
	count := math.Floor((limit - 1) / step)
	last := step * count

	return count * (first + last) / 2
}

func main() {
	multiplesOf3 := arithmeticSeries(3, 1000)
	multiplesOf5 := arithmeticSeries(5, 1000)
	multiplesOf15 := arithmeticSeries(15, 1000)

	fmt.Println(multiplesOf3 + multiplesOf5 - multiplesOf15)
}
