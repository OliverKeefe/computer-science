package main

import (
	"fmt"
	"math"
)

func exOne() {
	var firstEquation int8
	var secondEquation int8

	firstEquation = 6 + 4*10
	secondEquation = (6 + 4) * 10
	thirdEquation := math.Pow(23.0, 5)

	fmt.Println(firstEquation, secondEquation, thirdEquation)
}

func main() {
	exOne()
}
