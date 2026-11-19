## Leap Year

**What was hard**: remembering and understanding century-year rules for 1900.
**What I tried first**: year % 4 == 0 which did not work for 1900 and 2100.
**What worked**: dividing by 400, 100, then 4.

## Most Common Year

**What was hard**: handling punctuations without fusing words ("end.start")
**What I tried**: sentence.replace(",", "") —— missed other punctuations and words were fused together
**What worked**: re.sub(r"\[^\\w\\s]", " ", ...) then .split(), plus an explicit loop over words for correct tie-breaking.
**Decision**: first words to appear wins; empty or no string return 'None'

## Palindrome

**What was hard**: making sure punctuation between letters ("canal:" -> "canal", not fused or split weirdly) did not distort the string
**What I tried**: phrase.replace(" ", "").lower() —— missed punctuation ("Panama" trailing colon left in) and did not handle other whitespace
**What worked**: for ch in phrase.lower(): if ch.isalnum(): cleaned = cleaned + ch, then cleaned ==cleaned\[::-1]; which was easier for me to understand what the code is doing.
**Decision**: empty / punctuation-only -> True; digits count as characters; non-string -> TypeError

## Second Largest
**What was hard**: the "demote old maximum" case——[10, 8, 12] must give 10 and not 8. Also uniqueness—[5, 5, 3] must give 3 and not 5.
**What I tried**: a two-pass idea (find largest, then largest < largest) but that needed max(), which is forbidden. Also, I tried removing duplicates but it needed set(), but the constraints pushed me to a single pass without helper functions.
**What worked**: one pass with largest/second trackers, None to "unset" sentinel, explicit guard so an old maximum only demotes to second when it beats the current second, and v == largest duplicates ignored.
**Decision**: None for anything fewer than two unique values.

