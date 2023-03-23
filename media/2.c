#include <stdio.h>
/*Print Fahrenheit-Celsius table for fahr values 0 20 40     300*/
main( )
{
int Fahr, Celsius;
int lower, higher, step;
 lower=0;
 higher=300;
 step=20;
 Fahr= lower;
 while ( Fahr <= higher)
 {  
     Celsius = 5 * ( Fahr-32 )/9;
    printf ("%d\t%d\n", Fahr, Celsius);
     Fahr=Fahr+step;
 }
}
