#include "lists.h"
/**
 * check_cycle - a function that checks if a singly
 * linked list has a cycle in it
 * @list: ptr
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *p, *k;

	if (list == NULL || list->next == NULL)
		return (0);
	p = list;
	k = p->next;

	while (p != NULL && k->next != NULL
		&& k->next->next != NULL)
	{
		if (p == k)
			return (1);
		p = p->next;
		k = k->next->next;
	}
	return (0);
}
