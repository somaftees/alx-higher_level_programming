#include "lists.h"

/**
 * insert_node -  a function that inserts a number into
 * a sorted singly linked list.
 * @head: head of a list.
 * @number: index.
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n;
	listint_t *t;
	listint_t *h;

	t = *head;
	n = malloc(sizeof(listint_t));

	if (n == NULL)
		return (NULL);

	while (t != NULL)
	{
		if (t->n > number)
			break;
		h = t;
		t = t->next;
	}

	n->n = number;

	if (*head == NULL)
	{
		n->next = NULL;
		*head = n;
	}
	else
	{
		n->next = t;
		if (t == *head)
			*head = n;
		else
			h->next = n;
	}

	return (n);
}
