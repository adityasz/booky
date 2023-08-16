This is a fork of [booky](https://github.com/SiddharthPant/booky) with additional functionality.
<hr>

# booky

This script creates bookmarks in a pdf from a simple text file using `pdftk`.

## Dependencies
- python3
- pdftk
- GNU sed (OSX may have BSD sed; install `gsed` instead)

## Bookmark format
- A level starts with a `{` and ends with a `}`, on lines of their own.
- Bookmark title and page numbers must be on the same line, separted by a
  comma.
- The following lines are equivalent (the script is whitespace-agnostic):
  ```
  title1, 1
  title1  ,     1
  ```
- If the page numbers of the pdf are offset from the page numbers in the table
  of contents by an amount $n$, add `!n` on a new line. Multiple offsets can
  be specified since it is checked on each line. Negative offsets can also be
  specified.

## Example
```
{
	Contents, 4
	!15
	Chapter 1, 7
	Chapter 2, 10
	{
		Section 2.1, 11
		Section 2.2, 12
		{
			!14
			Subsection 2.2.1, 13
			...
		}
	}
}
```

## Usage
- `./booky.sh doc.pdf bookmarks.txt` creates a new pdf file
  `doc_bookmarked.pdf` with bookmarks from `bookmarks.txt`.

- To run it from any directory, add the `booky` directory to the environment PATH

  ```
  export PATH=/path_to_booky:$PATH
  ```

### Windows
On a Windows machine, use the `booky.py` file in the repo to convert
`bookmarks.txt` to `pdftk` compatible format:

```
python3 booky.py < bookmarks.txt > output.txt
```

Use the export command to generate a dumped data file:

```
pdftk doc.pdf dump_data output doc_data.txt
```

Replace the old bookmarks in `doc_data.txt` with the contents of `output.txt`
and then import that data back:

```
pdftk doc.pdf update_info doc_data.txt output updated.pdf
```
