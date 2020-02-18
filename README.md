# notable-take-home

## Description

This is a Python project that parses an input string and transforms certain key phrases
into an ordered list format. This project is designed to purely be functional and stateless.

## Usage

In the root of the project, simply run the following command in the command line.

```
python3 TranscriptTransformer.py
```

Currently, a sample string that is to be transformed is hardcoded into the program. However,
this should be changed.

## Assumptions

Due to the vagueness of the spec, a few assumptions were made.

1. If there is no starting phrase 'Number n' where 'n' is 'one' through 'nine',
then the program will assume improper input and error.
2. It is assumed that the last item in the ordered list will contain the remaining
of the input string.
3. The first instance of 'Number n' is assumed to be the start of the ordered list.
Subsequent occurrences of 'Number n' will be assumed to be content for the ordered
list items.
4. In general, the program assumes proper input from the client. 
