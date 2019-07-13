#include <stdio.h>
 
void main()
{
    int i, num1, sum1 = 0;
    scanf ("%d", &num1);
    for (i = 1; i <= num1; i++)
    {
        sum1 = sum1 + i;
    }
    printf ("%d",sum1);
}
