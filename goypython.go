package main

import (
	"fmt"
	"github.com/tliron/py4go"
)

func main() {
	py := py4go.New()
	script := "def suma(a, b):\n    return a + b\n"
	py.Exec(script)
	result := py.Call("suma", 5, 3)
	fmt.Println(result)
	py.Close()
}