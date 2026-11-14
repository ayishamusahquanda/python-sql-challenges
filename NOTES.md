## Leap Year
**What was hard**: remembering and understanding century-year rules for 1900.
**What I tried first**: year % 4 == 0 which did not work for 1900 and 2100.
**What worked**: dividing by 400, 100, then 4.

**What was hard**: handling punctuations without fusing words ("end.start")
**What I tried**: sentence.replace(",", "") —— missed other punctuations and words were fused together
**What worked**: re.sub(r"[^\w\s]", " ", ...) then .split(), plus an explicit loof over words for correct tie-breaking.
**Decision**: first words to appear wins; empty or no string return 'None'