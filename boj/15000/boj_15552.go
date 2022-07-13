package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	var testCaseLength int
	fmt.Fscanln(reader, &testCaseLength)

	var num1 int
	var num2 int

	for idx := 0; idx < testCaseLength; idx++ {
		fmt.Fscanln(reader, &num1, &num2)
		fmt.Fprintln(writer, num1+num2)
	}
	writer.Flush()
}
