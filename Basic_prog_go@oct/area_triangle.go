// Write a program to area of triangle

package main
import "fmt"

func tri_area(b,h float32){
	fmt.Println(b,h)
	var area float32
	area =0.5*(b*h)
	fmt.Println("Area of triangle:",area)
}
func main(){
	var base,height float32
	fmt.Println("Enter the base value:")
	fmt.Scan(&base)
	fmt.Println("Enter the height value:")
	fmt.Scan(&height)
	tri_area(base,height)
}