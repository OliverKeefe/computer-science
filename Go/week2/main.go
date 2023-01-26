package main

import (
	"fmt"
	"strconv"
)

func exOne() {
	fmt.Println("Hello, world!")
	fmt.Print("How are you?")
}

func exTwo() {
	var name string
	fmt.Println("Enter your name: ")
	fmt.Scanln(&name)
	fmt.Println("Hello", name+"!", "How are you?")
}

func exThree() {
	// A program for numbers
	var a int
	var b int
	var c float32
	var d int
	var userInput string
	var number int
	var r int

	a = 3 - 4 + 10
	b = 5 * 6
	c = 7.0 / 8.0

	fmt.Println("Theses are the values:", a, b, c)
	fmt.Println("Increment", a, "by one: ")
	a += 1
	fmt.Println(a)
	fmt.Println("The sum of", a, "and", b, "is")
	d = a + b
	fmt.Println(d)
	fmt.Scanln(&userInput)
	number, err := strconv.Atoi(userInput)

	if err != nil {
		fmt.Println("Error, string conversion failed.")
		return
	}

	fmt.Println(number)
	r = number * 2
	fmt.Println("Your number times 2 is", r)
}

func main() {
	exOne()
	exTwo()
	exThree()
}
