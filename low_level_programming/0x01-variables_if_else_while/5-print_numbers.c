#include <stdio.h>

/**
 * main - prints all single digit numbers of base
 * 10 starting from 0 and followed by a new line
 * Return: Always 0
 */
int main(void)
{
/* integer declaration */
	int n;
/* looping through the numers rangr */
	for (n = 0; n < 10; n++)
/* output block */
		printf("%d", n);
	printf("\n");
/* 0 to be returned if success */
	return (0);
}
