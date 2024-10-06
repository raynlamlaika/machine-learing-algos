#include <stdarg.h>
#include <stdio.h>
#include <math.h>

double euclideanDistance(int sum, ...)
{
	va_list args;
	va_start(args, sum);
	int i = 0;
	double s= 0.0;
	while (i<sum)
	{
		double a = va_arg(args,double);
		double b = va_arg(args,double);
		s += pow(a-b,2);
		i++;
	}
	va_end(args);
	return sqrt(s);
}
/*
int main()
{
	double dist2D = euclideanDistance(2, 1.0, 2.0, 4.0, 6.0);
	printf("2D Euclidean Distance: %f\n", dist2D);
	double dist3D = euclideanDistance(3, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0);
	printf("3D Euclidean Distance: %f\n", dist3D);
}
*/
