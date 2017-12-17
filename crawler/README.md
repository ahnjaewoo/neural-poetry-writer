# simple crawler for poetry site

Caution
 this crawler can potentially harm server performance, if wait time is not properly selected.
 we want to follow guideline of robots.txt, on https://www.poetryfoundation.org/robots.txt
 so, do not set each wait delay less than 5 seconds.
 see https://www.poetryfoundation.org/robots.txt for more guideline that this crawler need to follow.

usage : crawl(page-number, list_wait, poem_wait)
	page_number	- crawling poem list index
	list_wait	- wait seconds per list move
	poem_wait	- wait seconds per poem move