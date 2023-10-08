#include "lists.h"

/**
 * reverse_listint - a function
 * @head: ptr.
 * Return: a pointer.
 */

void reverse_listint(listint_t **head)
{
	listint_t *pre = NULL;
	listint_t *cur = *head;
	listint_t *next = NULL;

	while (cur)
	{
		next = cur->next;
		cur->next = pre;
		pre = cur;
		cur = next;
	}

	*head = pre;
}

/**
 * is_palindrome - a function
 * @head: ptr.
 * Return: 1 or 0.
 */

int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		f = f->next->next;
		if (!f)
		{
			dup = s->next;
			break;
		}
		if (!f->next)
		{
			dup = s->next->next;
			break;
		}
		s = s->next;
	}

	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
