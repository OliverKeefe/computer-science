package main

import (
	"fmt"
	"reflect"
	"strconv"
)

func variadicFunction(s ...string) {
	fmt.Println(s[0])
	fmt.Println(s[3])
}

func main() {
	var stringVariable string
	var integerVariable int

	stringVariable = "100"
	integerVariable, err := strconv.Atoi(stringVariable)

	fmt.Println(integerVariable, err, reflect.TypeOf(integerVariable))

	variadicFunction("red", "blue", "green", "yellow")

}
